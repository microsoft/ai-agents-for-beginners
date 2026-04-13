package com.example.faceswap

import android.Manifest
import android.content.ContentValues
import android.content.pm.PackageManager
import android.graphics.Bitmap
import android.net.Uri
import android.os.Build
import android.os.Bundle
import android.os.Environment
import android.provider.MediaStore
import android.view.View
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import androidx.lifecycle.lifecycleScope
import com.example.faceswap.databinding.ActivityMainBinding
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    private val detector = FaceDetectionHelper()

    private var sourceBitmap: Bitmap? = null
    private var targetBitmap: Bitmap? = null
    private var resultBitmap: Bitmap? = null

    // Which slot is waiting for the user's image pick
    private var pickingSlot: Slot = Slot.SOURCE

    enum class Slot { SOURCE, TARGET }

    // ── Activity result launchers ──────────────────────────────────────────────

    private val imagePickerLauncher = registerForActivityResult(
        ActivityResultContracts.GetContent()
    ) { uri: Uri? ->
        uri?.let { handlePickedImage(it) }
    }

    private val storagePermissionLauncher = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { granted ->
        if (granted) saveResultToGallery()
        else showToast("Storage permission required to save images")
    }

    // ── Lifecycle ──────────────────────────────────────────────────────────────

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        setupUi()
    }

    override fun onDestroy() {
        super.onDestroy()
        detector.close()
        sourceBitmap?.recycle()
        targetBitmap?.recycle()
        resultBitmap?.recycle()
    }

    // ── UI setup ───────────────────────────────────────────────────────────────

    private fun setupUi() {
        binding.btnPickSource.setOnClickListener {
            pickingSlot = Slot.SOURCE
            imagePickerLauncher.launch("image/*")
        }
        binding.btnPickTarget.setOnClickListener {
            pickingSlot = Slot.TARGET
            imagePickerLauncher.launch("image/*")
        }
        binding.btnSwap.setOnClickListener { performFaceSwap() }
        binding.btnSave.setOnClickListener { requestSavePermissionOrSave() }
        binding.btnReset.setOnClickListener { resetAll() }

        updateSwapButton()
    }

    // ── Image loading ──────────────────────────────────────────────────────────

    private fun handlePickedImage(uri: Uri) {
        lifecycleScope.launch {
            val bitmap = withContext(Dispatchers.IO) {
                ImageUtils.loadAndCorrectBitmap(this@MainActivity, uri)
            } ?: run {
                showToast("Could not load image")
                return@launch
            }

            when (pickingSlot) {
                Slot.SOURCE -> {
                    sourceBitmap?.recycle()
                    sourceBitmap = bitmap
                    binding.imgSource.setImageBitmap(bitmap)
                    binding.tvSourceHint.visibility = View.GONE
                    binding.labelSourceStatus.text = getString(R.string.label_ready)
                }
                Slot.TARGET -> {
                    targetBitmap?.recycle()
                    targetBitmap = bitmap
                    binding.imgTarget.setImageBitmap(bitmap)
                    binding.tvTargetHint.visibility = View.GONE
                    binding.labelTargetStatus.text = getString(R.string.label_ready)
                }
            }
            updateSwapButton()
        }
    }

    // ── Face swap ──────────────────────────────────────────────────────────────

    private fun performFaceSwap() {
        val src = sourceBitmap ?: return
        val tgt = targetBitmap ?: return

        setLoadingState(true, getString(R.string.status_detecting))

        lifecycleScope.launch {
            try {
                // Fetch strings on Main before jumping to Default
                val errSource  = getString(R.string.error_no_face_source)
                val errTarget  = getString(R.string.error_no_face_target)
                val txtSwapping = getString(R.string.status_swapping)

                val swapped = withContext(Dispatchers.Default) {
                    val srcFaces = detector.detectFaces(src)
                    val tgtFaces = detector.detectFaces(tgt)

                    when {
                        srcFaces.isEmpty() -> error(errSource)
                        tgtFaces.isEmpty() -> error(errTarget)
                        else -> {
                            withContext(Dispatchers.Main) {
                                binding.tvStatus.text = txtSwapping
                            }
                            FaceSwapEngine.swapFaces(src, tgt, srcFaces[0], tgtFaces[0])
                        }
                    }
                }

                resultBitmap?.recycle()
                resultBitmap = swapped
                binding.imgResult.setImageBitmap(swapped)
                binding.cardResult.visibility = View.VISIBLE
                binding.tvStatus.text = getString(R.string.status_done)

            } catch (e: IllegalStateException) {
                binding.tvStatus.text = e.message
                showToast(e.message ?: getString(R.string.error_generic))
            } catch (e: Exception) {
                binding.tvStatus.text = getString(R.string.error_generic)
                showToast("${getString(R.string.error_generic)}: ${e.message}")
            } finally {
                setLoadingState(false)
            }
        }
    }

    // ── Save ───────────────────────────────────────────────────────────────────

    private fun requestSavePermissionOrSave() {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.Q &&
            ContextCompat.checkSelfPermission(
                this, Manifest.permission.WRITE_EXTERNAL_STORAGE
            ) != PackageManager.PERMISSION_GRANTED
        ) {
            storagePermissionLauncher.launch(Manifest.permission.WRITE_EXTERNAL_STORAGE)
        } else {
            saveResultToGallery()
        }
    }

    private fun saveResultToGallery() {
        val bitmap = resultBitmap ?: run {
            showToast(getString(R.string.error_no_result))
            return
        }

        lifecycleScope.launch(Dispatchers.IO) {
            try {
                val fileName = "face_swap_${System.currentTimeMillis()}.jpg"
                val values = ContentValues().apply {
                    put(MediaStore.Images.Media.DISPLAY_NAME, fileName)
                    put(MediaStore.Images.Media.MIME_TYPE, "image/jpeg")
                    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                        put(MediaStore.Images.Media.RELATIVE_PATH, Environment.DIRECTORY_PICTURES)
                        put(MediaStore.Images.Media.IS_PENDING, 1)
                    }
                }

                val resolver = contentResolver
                val uri      = resolver.insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values)
                    ?: error("MediaStore insert returned null")

                resolver.openOutputStream(uri)?.use { out ->
                    bitmap.compress(Bitmap.CompressFormat.JPEG, 95, out)
                }

                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
                    values.clear()
                    values.put(MediaStore.Images.Media.IS_PENDING, 0)
                    resolver.update(uri, values, null, null)
                }

                withContext(Dispatchers.Main) {
                    showToast(getString(R.string.saved_to_gallery))
                }
            } catch (e: Exception) {
                withContext(Dispatchers.Main) {
                    showToast("${getString(R.string.error_save)}: ${e.message}")
                }
            }
        }
    }

    // ── Reset ──────────────────────────────────────────────────────────────────

    private fun resetAll() {
        sourceBitmap?.recycle(); sourceBitmap = null
        targetBitmap?.recycle(); targetBitmap = null
        resultBitmap?.recycle(); resultBitmap = null

        binding.imgSource.setImageDrawable(null)
        binding.imgTarget.setImageDrawable(null)
        binding.tvSourceHint.visibility = View.VISIBLE
        binding.tvTargetHint.visibility = View.VISIBLE
        binding.labelSourceStatus.text = ""
        binding.labelTargetStatus.text = ""
        binding.cardResult.visibility = View.GONE
        binding.tvStatus.text = ""

        updateSwapButton()
    }

    // ── State helpers ──────────────────────────────────────────────────────────

    private fun updateSwapButton() {
        binding.btnSwap.isEnabled = sourceBitmap != null && targetBitmap != null
    }

    private fun setLoadingState(loading: Boolean, statusText: String = "") {
        binding.progressBar.visibility = if (loading) View.VISIBLE else View.GONE
        binding.btnSwap.isEnabled      = !loading && sourceBitmap != null && targetBitmap != null
        binding.btnPickSource.isEnabled = !loading
        binding.btnPickTarget.isEnabled = !loading
        if (statusText.isNotEmpty()) binding.tvStatus.text = statusText
    }

    private fun showToast(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_LONG).show()
    }
}
