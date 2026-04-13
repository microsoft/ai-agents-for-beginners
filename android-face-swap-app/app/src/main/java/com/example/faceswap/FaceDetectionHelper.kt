package com.example.faceswap

import android.graphics.Bitmap
import com.google.mlkit.vision.common.InputImage
import com.google.mlkit.vision.face.Face
import com.google.mlkit.vision.face.FaceDetection
import com.google.mlkit.vision.face.FaceDetectorOptions
import kotlinx.coroutines.tasks.await

/**
 * Wraps ML Kit Face Detection with coroutine support.
 * Uses ACCURATE mode with all landmarks and contours for best face swap results.
 */
class FaceDetectionHelper {

    private val detector by lazy {
        val options = FaceDetectorOptions.Builder()
            .setPerformanceMode(FaceDetectorOptions.PERFORMANCE_MODE_ACCURATE)
            .setLandmarkMode(FaceDetectorOptions.LANDMARK_MODE_ALL)
            .setContourMode(FaceDetectorOptions.CONTOUR_MODE_ALL)
            .setClassificationMode(FaceDetectorOptions.CLASSIFICATION_MODE_NONE)
            .setMinFaceSize(0.1f)
            .build()
        FaceDetection.getClient(options)
    }

    /**
     * Detects all faces in [bitmap] and returns them sorted by face size (largest first).
     */
    suspend fun detectFaces(bitmap: Bitmap): List<Face> {
        val image = InputImage.fromBitmap(bitmap, 0)
        val faces = detector.process(image).await()
        // Sort largest face first so the primary subject is always picked
        return faces.sortedByDescending { it.boundingBox.width() * it.boundingBox.height() }
    }

    fun close() {
        detector.close()
    }
}
