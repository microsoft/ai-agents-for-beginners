# AI Face Swap — Android App

An on-device Android application that swaps faces between two photos using **Google ML Kit Face Detection** and custom bitmap compositing — no cloud calls, no API keys required.

---

## Features

- **On-device AI** — uses ML Kit's accurate face detector (landmarks + contours) entirely on the device
- **Smart alignment** — computes a similarity transform from eye positions so the swapped face matches scale, rotation, and position
- **Smooth blending** — feathered contour-based mask produces a seamless edge; falls back to an ellipse if contours aren't available
- **EXIF-aware loading** — images from any camera orientation are auto-rotated before processing
- **Save to Gallery** — writes the result as a JPEG via MediaStore (works on Android 9 – 14+)
- **Material 3 UI** — side-by-side pickers, progress indicator, result card with save/reset

---

## Screenshots

| Pick photos | Swap in progress | Result |
|---|---|---|
| *(source + target pickers)* | *(progress bar + status text)* | *(result card with save button)* |

---

## Requirements

| Item | Version |
|---|---|
| Android Studio | Hedgehog (2023.1.1) or newer |
| Android Gradle Plugin | 8.2.2 |
| Kotlin | 1.9.22 |
| Min SDK | 24 (Android 7.0) |
| Target SDK | 34 (Android 14) |

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/cliffhop23/ai-agents-for-beginners.git
cd ai-agents-for-beginners/android-face-swap-app
```

### 2. Open in Android Studio

`File → Open` → select the `android-face-swap-app` folder.

Android Studio will sync Gradle and download all dependencies automatically (ML Kit is pulled from Maven Central — no additional setup needed).

### 3. Run

Connect a physical device or start an emulator, then click **Run ▶**.

> **Tip:** ML Kit face detection works best on a real device. Emulators may be slower due to missing hardware acceleration.

---

## Project Structure

```
android-face-swap-app/
├── app/
│   └── src/main/
│       ├── java/com/example/faceswap/
│       │   ├── MainActivity.kt          # UI, gallery picker, save logic
│       │   ├── FaceDetectionHelper.kt   # ML Kit wrapper (coroutine-based)
│       │   ├── FaceSwapEngine.kt        # Core swap algorithm
│       │   └── ImageUtils.kt            # EXIF-correcting bitmap loader
│       ├── res/
│       │   ├── layout/activity_main.xml # Material 3 scroll layout
│       │   └── drawable/                # Icons + launcher adaptive icon
│       └── AndroidManifest.xml
├── build.gradle.kts
└── settings.gradle.kts
```

---

## How the Swap Works

```
Source image  ──► FaceDetectionHelper ──► sourceFace (landmarks + contours)
Target image  ──► FaceDetectionHelper ──► targetFace (landmarks + contours)
                                               │
                         FaceSwapEngine ◄──────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        Similarity        Warp source      Feathered
        transform         into target      face mask
        (eye-aligned)     coordinates      (contour/ellipse)
              │                │                │
              └────────────────┴────────────────┘
                                │
                         DST_IN blend
                                │
                          Result bitmap
```

1. **Align** — a similarity transform (scale + rotate + translate) is computed from the left/right eye landmarks of both faces so the swapped face lands at exactly the right size and angle.
2. **Warp** — the full source bitmap is painted into target-image space using that matrix with bilinear filtering.
3. **Mask** — a smooth alpha mask is built from the ML Kit face contour path, then softened with a radial gradient so edges dissolve into the background.
4. **Blend** — the masked warped face is composited onto the target using `PorterDuff.Mode.DST_IN` alpha blending.

---

## Dependencies

| Library | Purpose |
|---|---|
| `com.google.mlkit:face-detection:16.1.5` | On-device face detection |
| `androidx.core:core-ktx` | Kotlin Android extensions |
| `org.jetbrains.kotlinx:kotlinx-coroutines-android` | Async processing |
| `org.jetbrains.kotlinx:kotlinx-coroutines-play-services` | `Tasks.await()` for ML Kit |
| `androidx.exifinterface:exifinterface` | EXIF rotation correction |
| `com.google.android.material:material` | Material 3 UI components |

---

## Tips for Best Results

- Use **front-facing**, well-lit photos where the face is clearly visible
- Avoid heavy occlusions (sunglasses, masks, extreme angles)
- Faces of similar size in both photos produce the most natural blends
- The largest detected face in each image is always used for the swap
