package com.example.faceswap

import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Matrix
import android.graphics.Paint
import android.graphics.Path
import android.graphics.PointF
import android.graphics.PorterDuff
import android.graphics.PorterDuffXfermode
import android.graphics.RadialGradient
import android.graphics.Rect
import android.graphics.RectF
import android.graphics.Shader
import com.google.mlkit.vision.face.Face
import com.google.mlkit.vision.face.FaceContour
import com.google.mlkit.vision.face.FaceLandmark
import kotlin.math.atan2
import kotlin.math.hypot

/**
 * Core face swap engine.
 *
 * Algorithm:
 * 1. Compute a similarity transform (scale + rotate + translate) that maps
 *    the source eye positions onto the target eye positions.
 * 2. Warp the entire source bitmap into target-image space using that transform.
 * 3. Build a feathered elliptical / contour-based mask over the target face.
 * 4. Composite the warped source face onto the target image using the mask as alpha.
 */
object FaceSwapEngine {

    /**
     * Swap the primary face from [sourceBitmap] into [targetBitmap].
     *
     * @param sourceBitmap  The image that supplies the face to paste.
     * @param targetBitmap  The image that receives the swapped face.
     * @param sourceFace    ML Kit [Face] detected in [sourceBitmap].
     * @param targetFace    ML Kit [Face] detected in [targetBitmap].
     * @return A new [Bitmap] with the same dimensions as [targetBitmap].
     */
    fun swapFaces(
        sourceBitmap: Bitmap,
        targetBitmap: Bitmap,
        sourceFace: Face,
        targetFace: Face,
    ): Bitmap {
        // ── 1. Compute alignment transform ────────────────────────────────────
        val matrix = buildAlignmentMatrix(sourceFace, targetFace)

        // ── 2. Warp source image into target coordinate space ─────────────────
        val warpedSource = Bitmap.createBitmap(
            targetBitmap.width, targetBitmap.height, Bitmap.Config.ARGB_8888
        )
        Canvas(warpedSource).drawBitmap(
            sourceBitmap, matrix,
            Paint(Paint.ANTI_ALIAS_FLAG or Paint.FILTER_BITMAP_FLAG)
        )

        // ── 3. Build smooth face mask ─────────────────────────────────────────
        val mask = buildFaceMask(targetBitmap.width, targetBitmap.height, targetFace)

        // ── 4. Blend warped source onto target ────────────────────────────────
        val result = targetBitmap.copy(Bitmap.Config.ARGB_8888, true)
        blendWithMask(result, warpedSource, mask)

        warpedSource.recycle()
        mask.recycle()

        return result
    }

    // ── Transform helpers ──────────────────────────────────────────────────────

    private fun buildAlignmentMatrix(source: Face, target: Face): Matrix {
        val srcLeft  = source.getLandmark(FaceLandmark.LEFT_EYE)?.position
        val srcRight = source.getLandmark(FaceLandmark.RIGHT_EYE)?.position
        val tgtLeft  = target.getLandmark(FaceLandmark.LEFT_EYE)?.position
        val tgtRight = target.getLandmark(FaceLandmark.RIGHT_EYE)?.position

        return if (srcLeft != null && srcRight != null && tgtLeft != null && tgtRight != null) {
            similarityTransform(srcLeft, srcRight, tgtLeft, tgtRight)
        } else {
            boundingBoxTransform(source.boundingBox, target.boundingBox)
        }
    }

    /**
     * Returns the unique similarity transform (scale + rotation + translation)
     * that maps [srcL]/[srcR] to [tgtL]/[tgtR].
     */
    private fun similarityTransform(
        srcL: PointF, srcR: PointF,
        tgtL: PointF, tgtR: PointF,
    ): Matrix {
        val srcAngle = atan2((srcR.y - srcL.y).toDouble(), (srcR.x - srcL.x).toDouble())
        val tgtAngle = atan2((tgtR.y - tgtL.y).toDouble(), (tgtR.x - tgtL.x).toDouble())

        val srcDist = hypot((srcR.x - srcL.x).toDouble(), (srcR.y - srcL.y).toDouble()).toFloat()
        val tgtDist = hypot((tgtR.x - tgtL.x).toDouble(), (tgtR.y - tgtL.y).toDouble()).toFloat()

        val scale  = if (srcDist > 0f) tgtDist / srcDist else 1f
        val rotate = Math.toDegrees(tgtAngle - srcAngle).toFloat()

        val srcCx = (srcL.x + srcR.x) / 2f
        val srcCy = (srcL.y + srcR.y) / 2f
        val tgtCx = (tgtL.x + tgtR.x) / 2f
        val tgtCy = (tgtL.y + tgtR.y) / 2f

        return Matrix().apply {
            postTranslate(-srcCx, -srcCy)  // move source centre to origin
            postScale(scale, scale)         // scale to match face size
            postRotate(rotate)              // align eye-line angle
            postTranslate(tgtCx, tgtCy)    // move to target centre
        }
    }

    /** Fallback: uniform scale + translate from bounding box centres. */
    private fun boundingBoxTransform(src: Rect, tgt: Rect): Matrix {
        val scale = if (src.width() > 0) tgt.width().toFloat() / src.width() else 1f
        return Matrix().apply {
            postTranslate(-src.exactCenterX(), -src.exactCenterY())
            postScale(scale, scale)
            postTranslate(tgt.exactCenterX(), tgt.exactCenterY())
        }
    }

    // ── Mask helpers ───────────────────────────────────────────────────────────

    /**
     * Creates a grayscale alpha mask the size of [width] × [height].
     * White/opaque = face region; transparent = background.
     * Edges are feathered for seamless blending.
     */
    private fun buildFaceMask(width: Int, height: Int, face: Face): Bitmap {
        val mask   = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888)
        val canvas = Canvas(mask)

        val contourPoints = face.getContour(FaceContour.FACE)?.points
        if (!contourPoints.isNullOrEmpty()) {
            drawContourMask(canvas, contourPoints, face.boundingBox)
        } else {
            drawEllipseMask(canvas, face.boundingBox)
        }
        return mask
    }

    /** Precise mask using ML Kit face contour points + feathered radial gradient. */
    private fun drawContourMask(
        canvas: Canvas,
        points: List<PointF>,
        box: Rect,
    ) {
        // Build the face outline path
        val path = Path().apply {
            moveTo(points.first().x, points.first().y)
            for (i in 1 until points.size) lineTo(points[i].x, points[i].y)
            close()
        }

        // First pass: solid fill so the whole face area is opaque
        canvas.drawPath(path, Paint(Paint.ANTI_ALIAS_FLAG).apply { color = Color.WHITE })

        // Second pass: clip to path, then overdraw a radial gradient that fades
        // toward the edges, softening the hard outline into a smooth blend.
        val cx = box.exactCenterX()
        val cy = box.exactCenterY()
        val r  = maxOf(box.width(), box.height()) / 2f * 1.1f

        val gradient = RadialGradient(
            cx, cy, r,
            intArrayOf(Color.WHITE, Color.WHITE, Color.TRANSPARENT),
            floatArrayOf(0f, 0.65f, 1f),
            Shader.TileMode.CLAMP
        )
        canvas.save()
        canvas.clipPath(path)
        canvas.drawRect(
            (box.left  - r).toInt().toFloat(), (box.top  - r).toInt().toFloat(),
            (box.right + r).toInt().toFloat(), (box.bottom + r).toInt().toFloat(),
            Paint(Paint.ANTI_ALIAS_FLAG).apply {
                shader = gradient
                xfermode = PorterDuffXfermode(PorterDuff.Mode.SRC_ATOP)
            }
        )
        canvas.restore()
    }

    /** Fallback: feathered ellipse centred on the bounding box. */
    private fun drawEllipseMask(canvas: Canvas, box: Rect) {
        val cx = box.exactCenterX()
        val cy = box.exactCenterY()
        val rx = box.width()  / 2f * 1.05f
        val ry = box.height() / 2f * 1.05f
        val r  = maxOf(rx, ry)

        val gradient = RadialGradient(
            cx, cy, r,
            intArrayOf(Color.WHITE, Color.WHITE, Color.TRANSPARENT),
            floatArrayOf(0f, 0.70f, 1f),
            Shader.TileMode.CLAMP
        )
        canvas.drawOval(
            RectF(cx - rx, cy - ry, cx + rx, cy + ry),
            Paint(Paint.ANTI_ALIAS_FLAG).apply { shader = gradient }
        )
    }

    // ── Compositing ────────────────────────────────────────────────────────────

    /**
     * Composites [overlay] onto [base] using [mask] as the alpha channel of the overlay.
     * Pixels where the mask is white are fully replaced; transparent mask edges blend smoothly.
     */
    private fun blendWithMask(base: Bitmap, overlay: Bitmap, mask: Bitmap) {
        // Step 1: Apply the mask as the alpha of a copy of the overlay.
        val maskedOverlay = Bitmap.createBitmap(base.width, base.height, Bitmap.Config.ARGB_8888)
        val mc = Canvas(maskedOverlay)
        mc.drawBitmap(overlay, 0f, 0f, Paint())
        mc.drawBitmap(
            mask, 0f, 0f,
            Paint().apply { xfermode = PorterDuffXfermode(PorterDuff.Mode.DST_IN) }
        )

        // Step 2: Draw the masked overlay on top of the base (SRC_OVER = default alpha blend).
        Canvas(base).drawBitmap(maskedOverlay, 0f, 0f, Paint())
        maskedOverlay.recycle()
    }
}
