[![ಚೆನ್ನಾಗಿ ವಿನ್ಯಾಸಗೊಳಿಸಿರುವ AI ಏಜೆಂಟ್ಸ್ ಹೇಗೆ](../../../translated_images/kn/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ಈ ಪಾಠದ ವೀಡಿಯೋವನ್ನು ನೋಡಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# ಉಪಕರಣ ಬಳಕೆಯ ವಿನ್ಯಾಸ ಮಾದರಿ

ಉಪಕರಣಗಳು ಆಕರ್ಷಕವಾಗಿವೆ ಏಕೆಂದರೆ ಅವು AI ಏಜೆಂಟ್ಗಳಿಗೆ ವ್ಯಾಪಕ ಶ್ರೇಣಿಯ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಹೊಂದಲು ಅನುಮತಿಸುತ್ತವೆ. ಏಜೆಂಟ್ ನಡೆಸಬಹುದಾದ ಕ್ರಿಯೆಗಳ ಸೀಮಿತ ಸಂಗ್ರಹವಿದ್ದ ಬದಲು, ಉಪಕರಣವನ್ನು ಸೇರಿಸುವ ಮೂಲಕ, ಏಜೆಂಟ್ ಈಗ ವ್ಯಾಪಕ ಶ್ರೇಣಿಯ ಕ್ರಿಯೆಗಳನ್ನು ನಡೆಸಬಹುದು. ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ನಾವು ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ನೋಡುತ್ತೇವೆ, ಇದು AI ಏಜೆಂಟ್ಗಳು ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ಹೇಗೆ ವಿಶೇಷ ಉಪಕರಣಗಳನ್ನು ಬಳಸಬಹುದು ಎಂದು ವಿವರಿಸುತ್ತದೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಕೆಳಗಿನ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ನೀಡಲು ಉದ್ದೇಶಿಸುತ್ತೇವೆ:

- ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿ ಎಂದರೆ ಏನು?
- ಇದನ್ನು ಯಾವ ಉಪಯೋಗಗಳಿಗೆ ಅನ್ವಯಿಸಬಹುದು?
- ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಜಾರಿಗೊಳಿಸಲು ಬೇಕಾಗುವ ಅಂಶಗಳು/ನಿರ್ಮಾಣ ಬ್ಲಾಕ್ಗಳು ಯಾವುವು?
- ನಂಬಿಕೆಯಸರು AI ಏಜೆಂಟ್ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಬಳಸುವಾಗ ವಿಶೇಷ ಪರಿಗಣನೆಗಳು ಯಾವುವು?

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಮತ್ತು ಅದರ ಉದ್ದೇಶವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದು.
- ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿ ಅನ್ವಯಿಸುವ ಉಪಯೋಗ ಸಂದರ್ಭಗಳನ್ನು ಗುರುತಿಸುವುದು.
- ವಿನ್ಯಾಸ ಮಾದರಿ ಜಾರಿಗೆ ಬೇಕಾದ ಪ್ರಮುಖ ಅಂಶಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು.
- ಈ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಬಳಸಿಕೊಂಡು AI ಏಜೆಂಟ್ಗಳಲ್ಲಿ ನಂಬಿಕೆಯಶೀಲತೆಯನ್ನು ಖಚಿತಪಡಿಸಲು ಪರಿಗಣನೆಗಳನ್ನು ಗುರುತಿಸುವುದು.

## ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿ ಎಂದರೆ ಏನು?

**ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿ** ವಿಸ್ತಾರವಾಗಿ LLMಗಳು ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ಹೊರಗಿನ ಉಪಕರಣಗಳೊಂದಿಗೆ ಸಂವಹನ ಸಾಧಿಸುವ ಸಾಮರ್ಥ್ಯವನ್ನು ನೀಡುವಲ್ಲಿ ಗುರಿಯಾಗಿರುತ್ತದೆ. ಉಪಕರಣಗಳು ಏಜೆಂಟ್ ಮೂಲಕ ಕಾರ್ಯಗತಗೊಳಿಸಬಹುದಾದ ಕೋಡ್ ಆಗಿರುತ್ತವೆ. ಉಪಕರಣವು ಸರಳ ಕಾರ್ಯವಾಗಬಹುದು, ಉದಾಹರಣೆಗೆ ಕ್ಯಾಲ್ಕುಲೇಟರ್, ಅಥವಾ ಥರ್ಡ್-пಾರ್ಟಿ ಸೇವೆಗೆ ವಿನಂತಿ ಕಲ್ಳಣೆಯಾದರು, ಉದಾಹರಣೆಗೆ ಸ್ಟಾಕ್ ಬೆಲೆ ಪರಿಶೀಲನೆ ಅಥವಾ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ. AI ಏಜೆಂಟ್ ಗಳ ಸಾಂದರ್ಭದಲ್ಲಿ, ಉಪಕರಣಗಳನ್ನು ಮಾದರಿ-ರಚಿತ ಕಾರ್ಯಗಳ ಕರೆಗಳಿಗೆ ಪ್ರತಿಕ್ರಿಯೆವಾಗಿ ಏಜೆಂಟ್‍ಗಳು ಕಾರ್ಯಗತಗೊಳಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ.

## ಇದನ್ನು ಯಾವ ಉಪಯೋಗಗಳಿಗೆ ಅನ್ವಯಿಸಬಹುದು?

AI ಏಜೆಂಟ್ಗಳು ಸಂಕೀರ್ಣ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು, ಮಾಹಿತಿ ಪಡೆದುಕೊಳ್ಳಲು ಅಥವಾ ತೀರ್ಮಾನಗಳನ್ನು ಮಾಡಲು ಉಪಕರಣಗಳನ್ನು ಉಪಯೋಗಿಸಬಹುದು. ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಹೊರಗಿನ ವ್ಯವಸ್ಥೆಗಳೊಂದಿಗೆ ಗತಿಶೀಲ ಸಂವಹನ ಅಗತ್ಯವಿರುವ ಸಂದರ್ಭದಲ್ಲಿ ಬಳಸಲಾಗುತ್ತದೆ, ಉದಾಹರಣೆಗೆ ಡೇಟಾಬೇಸ್ ಗಳ, ವೆಬ್ ಸೇವೆಗಳ ಅಥವಾ ಕೋಡ್ ವಿವರಣೆಕಾಯಕರಲ್ಲಿ. ಈ ಸಾಮರ್ಥ್ಯವು ಹಲವಾರು ಉಪಯೋಗ ಸಂದರ್ಭಗಳಿಗೆ ಉಪಯುಕ್ತವಾಗಿದೆ, ಉದಾಹರಣೆಗೆ:

- **ಗಿನಮಯ ಮಾಹಿತಿ ಪಡೆಯುವುದು:** ಏಜೆಂಟ್ಗಳು ಹೊಸದಾಗಿ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಲು ಹೊರಗಿನ ಏಪಿಐ ಅಥವಾ ಡೇಟಾಬೇಸ್‍ಗಳಿಗೆ ಕೇಳಿಸಬಹುದು (ಉದಾ: SQLite ಡೇಟಾಬೇಸ್‌ಗೆ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆಗೆ ಕೇಳುವುದು, ಸ್ಟಾಕ್ ಬೆಲೆಗಳು ಅಥವಾ ಹವಾಮಾನ ಮಾಹಿತಿ ಪಡೆಯುವುದು).
- **ಕೋಡ್ ನಿರ್ವಹಣೆ ಮತ್ತು ವಿವರಣೆ:** ಏಜೆಂಟ್ ಗಳು ಗಣಿತ ಸಮಸ್ಯೆಗಳನ್ನು ಪರಿಹರಿಸಲು, ವರದಿಗಳನ್ನು ಸೃಷ್ಟಿಸಲು ಅಥವಾ ಸಿಮ್ಯುಲೇಷನ್ ನಡಿಸಲು ಕೋಡ್ ಅಥವಾ ಸ್ಕ್ರಿಪ್ಟ್ ಗಳನ್ನು ನಿರ್ವಹಿಸಬಹುದು.
- **ಕೆಲಸ ಪ್ರಕ್ರಿಯೆ ಸ್ವಯಂಚಾಲನೆ:** ಕಾರ್ಯ ನಿರ್ವಹಣಾ ವ್ಯವಸ್ಥೆಗಳಂತಹ ಉಪಕರಣಗಳೊಂದಿಗೆ ಒಟ್ಟಾಗಿ ಪುನರಾವರ್ತಿತ ಅಥವಾ ಬಹುಹಂತ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವುದು.
- **ಗ್ರಾಹಕೀಯ ಸಹಾಯ:** ಏಜೆಂಟ್ಗಳು CRM ವ್ಯವಸ್ಥೆಗಳು, ಟಿಕೆಟ್ ವ್ಯವಸ್ಥೆಗಳು ಅಥವಾ ಜ್ಞಾನಾಧಾರಗಳೊಂದಿಗೆ ಸಂವಹನ ನಡೆಸಿ ಬಳಕೆದಾರರ ಕೇಳಿಗೆ ಉತ್ತರ ನೀಡಬಹುದು.
- **ವಿಷಯ ಸೃಜನೆ ಮತ್ತು ಸಂಪಾದನೆ:** ವ್ಯಾಕರಣ ಪರಿಶೀಲಕಗಳು, ಪಠ್ಯ ಸಂಕ್ಷೇಪಕಗಳು ಅಥವಾ ವಿಷಯ ಸುರಕ್ಷತಾ ಮೌಲ್ಯಮಾಪಕಗಳು ಮೇಲಿನಂತಹ ಉಪಕರಣಗಳನ್ನು ಬಳಸಿ ವಿಷಯ ಸೃಜನೆಯಲ್ಲಿ ಸಹಾಯ ಮಾಡಬಹುದು.

## ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿ ಜಾರಿಗೆ ಬೇಕಾದ ಅಂಶಗಳು/ನಿರ್ಮಾಣ ಬ್ಲಾಕ್ಗಳು ಯಾವುವು?

ಈ ನಿರ್ಮಾಣ ಬ್ಲಾಕ್ಗಳಲ್ಲಿ AI ಏಜೆಂಟ್ ಬೃಹತ್ಪದರ ಕಾರ್ಯವಾಷ್ಟಗಳನ್ನು ನಿರ್ವಹಿಸಬಹುದು. ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಜಾರಿಗೆ ಬೇಕಾದ ಪ್ರಮುಖ ಅಂಶಗಳನ್ನು ನೋಡೋಣ:

- **ಕಾರ್ಯ/ಟೂಲೊ ಸ್ಕೀಮಾಗಳು:** ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳ ವಿವರವಾದ ವ್ಯಾಖ್ಯಾನಗಳು, ಕಾರ್ಯದ ಹೆಸರು, ಉದ್ದೇಶ, ಅಗತ್ಯ ಪ್ಯಾರಾಮೀಟರ್ಗಳು ಮತ್ತು ನಿರೀಕ್ಷಿತ ಉತ್ಪಾದನೆಗಳು. ಈ ಸ್ಕೀಮಾಗಳು LLMಗೆ ಯಾವ ಉಪಕರಣಗಳು ಲಭ್ಯವಿವೆ ಮತ್ತು ಮಾನ್ಯವಾದ ಅರ್ಜಿಗಳನ್ನು ಹೇಗೆ ರಚಿಸಬೇಕು ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

- **ಕಾರ್ಯಗತಗೊಳಿಸುವ ಲಾಜಿಕ್:** ಬಳಕೆದಾರನ ಉದ್ದೇಶ ಮತ್ತು ಸಂಭಾಷಣೆಯ ಸಾಂದರ್ಭಿಕತೆಯ ಆಧಾರದ ಮೇಲೆ ಉಪಕರಣಗಳನ್ನು ಯಾವಾಗ ಮತ್ತು ಹೇಗೆ ಕರೆ ಮಾಡಬೇಕು ಎಂಬುದನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ. ಇದರಲ್ಲಿ ಯೋಜನೆ ಮಾಡೋಣಾ ಭಾಗಗಳು, ಮಾರ್ಗ ನಿರ್ದೇಶಕಗಳು ಅಥವಾ ಶರತಿತ ಪಥಗಳು ಇರಬಹುದು.

- **ಸಂದೇಶ ನಿರ್ವಹಣಾ ವ್ಯವಸ್ಥೆ:** ಬಳಕೆದಾರರ ಇನ್ಪುಟ್ಗಳು, LLM ಪ್ರತಿಕ್ರಿಯೆಗಳು, ಉಪಕರಣಗಳ ಕರೆ ಮತ್ತು ಅದರ ಉತ್ಪತ್ತಿಗಳ ನಡುವೆ ಸಂಭಾಷಣೆಯ ಹರಿವನ್ನು ನಿರ್ವಹಿಸುವ ಘಟಕಗಳು.

- **ಉಪಕರಣ ಸಮಗ್ರತೆ ನೆಲೆಕಂಡ ವ್ಯವಸ್ಥೆ:** ಸರಳ ಕಾರ್ಯಗಳಾಗಿರಲಿ ಅಥವಾ ಸಂಕೀರ್ಣ ಹೊರಗಿನ ಸೇವೆಗಳಾಗಿರಲಿ ಏಜೆಂಟ್ ಅನ್ನು ವಿವಿಧ ಉಪಕರಣಗಳಿಗೆ ಸಂಪರ್ಕಿಸುವ ಮೂಲಸೌಕರ್ಯ.

- **ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಮಾನ್ಯತೆ:** ಉಪಕರಣ ಕಾರ್ಯಗತಗೊಳಿಸುವ ಸಂದರ್ಭದಲ್ಲಿ ಆಗುವ ವೈಫಲ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು, ಪ್ಯಾರಾಮೀಟರ್ಗಳ ಮಾನ್ಯತೆ ಮಾಡುವುದು ಮತ್ತು ಅಪ್ರত্যಾಶಿತ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ವಿಧಾನಗಳು.

- **ಸ್ಥಿತಿ ನಿರ್ವಹಣೆ:** ಸಂಭಾಷಣೆಯ ಸಾಂದರ್ಭಿಕತೆ, ಹಳೆಯ ಉಪಕರಣಗಳ ಸಂವಹನಗಳು ಮತ್ತು ನಿರಂತರ ಡೇಟಾವನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ ಬಹು-ತಿರುವು ಸಂವಹನಗಳಲ್ಲಿ ಸಮ್ಮತತೆಯನ್ನು ಖಚಿತಪಡಿಸುವುದು.

ಮುಂದಾಗಿ, ಕಾರ್ಯ/ಟೂಲೊ ಕರೆ ಬಗ್ಗೆ ಹೆಚ್ಚು ವಿವರವಾಗಿ ನೋಡೋಣ.
 
### ಕಾರ್ಯ/ಟೂಲೊ ಕರೆ

ಕಾರ್ಯ ಕರೆ LLMಗಳು ಉಪಕರಣಗಳೊಂದಿಗೆ ಸಂವಹನ ಸಾಧಿಸಲು ಮುಖ್ಯ ವಿಧಾನ. 'ಕಾರ್ಯ' ಮತ್ತು 'ಟೂಲೊ' ಪದಗಳನ್ನು ವಿನಿಮಯವಾಗಿ ಬಳಸಲಾಗುತ್ತದೆ ಏಕೆಂದರೆ 'ಕಾರ್ಯಗಳು' (ಮರುಬಳಕೆ ಮಾಡಬಹುದಾದ ಕೋಡ್ ಬ್ಲಾಕ್ಗಳು)ವು ಏಜೆಂಟ್ ಮಾಡಬೇಕಾದ ಕಾರ್ಯಗಳನ್ನು ನಡಿಸುವ ಉಪಕರಣಗಳು ಆಗಿವೆ. ಕಾರ್ಯದ ಕೋಡ್ ನಿರ್ವಹಣೆಗೆ, LLM ಬಳಕೆದಾರರ ವಿನಂತಿಯನ್ನು ಕಾರ್ಯ ವಿವರಣೆಯೊಂದಿಗೆ ಹೋಲಿಕೆಯಾಗಬೇಕು. ಇದಕ್ಕಾಗಿ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಕಾರ್ಯಗಳ ವಿವರಣೆಯಿರುವ ಸ್ಕೀಮಾ LLMಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ. LLM ಬಳಿಕ ಕಾರ್ಯಕ್ಕಾಗಿ ಸೂಕ್ತವಾದದ್ದು ಆಯ್ಕೆಮಾಡಿ ಅದರ ಹೆಸರು ಮತ್ತು ಅರ್ಗ್ಯೂಮೆಂಟ್‍ಗಳನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. ಆಯ್ಕೆಯಾದ ಕಾರ್ಯವನ್ನು ಕರೆಮಾಡಲಾಗುತ್ತದೆ, ಅದರ ಪ್ರತಿಕ್ರಿಯೆ LLMಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ, ಇದನ್ನು ಬಳಸಿ ಬಳಕೆದಾರರ ವಿನಂತಿಗೆ ಉತ್ತರ ನೀಡಲಾಗುತ್ತದೆ.

ಏಜೆಂಟ್ ಗಾಗಿ ಕಾರ್ಯ ಕರೆ ಜಾರಿಗೆ ಡೆವಲಪರ್ಗಳು ಬೇಕಾಗುವುದು:

1. ಕಾರ್ಯ ಕರೆಗಾಗಿ ಬೆಂಬಲಿಸುವ LLM ಮಾದರಿ
2. ಕಾರ್ಯ ವಿವರಣೆಗಳಿರುವ ಸ್ಕೀಮಾ
3. ಪ್ರತಿ ಕಾರ್ಯದ ಜಾರಿಗೆ ಬೇಕಾಗುವ ಕೋಡ್

ನಗರದಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯ ಪಡೆಯುವ ಉದಾಹರಣೆಯನ್ನು ನೋಡೋಣ:

1. **ಕಾರ್ಯ ಕರೆಗೆ ಬೆಂಬಲಿಸುವ LLM ಆರಂಭಿಸು:**

    ಎಲ್ಲಾ ಮಾದರಿಗಳು ಕಾರ್ಯ ಕರೆ ಬೆಂಬಲಿಸುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ ನೀವು ಬಳಸುತ್ತಿರುವ LLM ಆ ಬೆಂಬಲವನ್ನು ಒದಗಿಸುತ್ತಿದೆಯೇ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸುವುದು ಮಹತ್ವದ್ದು.  <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">ಏಜೂರ್ ಓಪನ್‌ಎಐ</a> ಕಾರ್ಯ ಕರೆ ಬೆಂಬಲನೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ. ನಾವು ಏಜೂರ್ ಓಪನ್‌ಎಐ **ಪ್ರತಿಕ್ರಿಯೆಗಳು API** ಗೆ ವಿರುದ್ಧ OpenAI ಕ್ಲೈಯೆಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸುವುದು (ಸ್ಥಿರ `/openai/v1/` ಎಂಡ್‌ಪಾಯಿಂಟ್ — `api_version` ಅವಶ್ಯಕವಿಲ್ಲ).

    ```python
    # Azure OpenAI (Responses API, v1 ಎಂಡ್ಪಾಯಿಂಟ್)ಗಾಗಿ OpenAI ಕ್ಲಯಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **ಕಾರ್ಯ ಸ್ಕೀಮಾ ರಚನೆ ಮಾಡಿ:**

    ಮುಂದಾಗಿ ನಾವು JSON ಸ್ಕೀಮಾದಲ್ಲಿ ಕಾರ್ಯದ ಹೆಸರು, ಕಾರ್ಯವೇನು ಮಾಡುತ್ತದೆ ಎಂಬ ವಿವರಣೆ, ಮತ್ತು ಕಾರ್ಯ ಪ್ಯಾರಾಮೀಟರ್ ಗಳ ಹೆಸರುಗಳ ಹಾಗೂ ವಿವರಣೆಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದು.  
    ನಂತರ ಈ ಸ್ಕೀಮಾ ಹಾಲಿ ಬಳಕೆದಾರನ ವಿನಂತಿಯನ್ನು ಸೇರಿಸಿ ಕೋಡ್ ಮಾಡುತ್ತೇವೆ, ಉದಾಹರಣೆಗೆ ಸಾನ್ ಫ್ರಾನ್ಸಿಸ್ಕೋನ ಸಮಯವನ್ನು ಕಂಡುಹಿಡಿಯಲು. ಗಮನಸೇರಿಸಬೇಕಾದುದು `ಟೂಲೊ ಕರೆ` ಹಿಂತಿರುಗಿಸುವದು, ಪ್ರಶ್ನೆಯ ಅಂತಿಮ ಉತ್ತರವಲ್ಲ. LLM ಕರ್ತವ್ಯದ ಕಾರ್ಯದ ಹೆಸರು ಮತ್ತು ಅದಕ್ಕೆ ಪಾಸಾಗುವ ಅರ್ಗೂಮೆಂಟ್ ಗಳನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.

    ```python
    # ಮಾದರಿಗಾಗಿ ಕಾರ್ಯ ವಿವರಣೆ ಓದಲು (ಪ್ರತಿಕ್ರಿಯೆಗಳು API ಫ್ಲಾಟ್ ಸಾಧನ ಸ್ವರೂಪ)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # ಪ್ರಾರಂಭಿಕ ಬಳಕೆದಾರ ಸಂದೇಶ
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # ಮೊದಲ API ಕರೆ: ಮಾದರಿಯನ್ನು ಕಾರ್ಯವನ್ನು ಬಳಸಲು ಕೇಳಿ
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API ಕಾರ್ಯಕರೆಗಳ್ಮು function_call ಐಟಂಗಳಾಗಿ response.output ನಲ್ಲಿ ನೀಡುತ್ತದೆ.
    # ಮಾದರಿಗೆ ಮುಂದಿನ ಬಾರಿಗೆ ಸಂಪೂರ್ಣ సందర్భವನ್ನು ನೀಡಲು ಅವುಗಳನ್ನು ಸಂಭಾಷಣೆಗೆ ಸೇರಿಸಿ.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **ಕಾರ್ಯ ನಿರ್ವಹಣೆಗೆ ಬೇಕಾದ ಕೋಡ್:**

    LLM ಆಯ್ಕೆಮಾಡಿದ ಕಾರ್ಯ ಕಾರ್ಯಗತಗೊಳಿಸಲು, ಆ ಕಾರ್ಯದ ಕೋಡ್ ನಿಜಕ್ಕೂ ಜಾರಿಗೆ ತರುವುದನ್ನು ಬರೆಯಬೇಕು.
    Python ನಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯ ಪಡೆಯುವ ಕೋಡ್ ನಮೂದಿಸಬಹುದು. ಪ್ರತಿಕ್ರಿಯೆ ಸಂದೇಶದಿಂದ ಹೆಸರು ಮತ್ತು ಅರ್ಗೂಮೆಂಟ್ ಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು ಕೋಡ್ ಬರೆಯಬೇಕು.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # ಫಂಕ್ಷನ್ کال್ಗಳನ್ನು ನಿರ್ವಹಿಸಿ
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # ಫಂಕ್ಷನ್_ಕಾಲ್_ಔಟ್ಪುಟ್ ಐಟಂವಂತೆ ಸಾಧನ ಫಲಿತಾಂಶವನ್ನು ಹಿಂತಿರುಗಿಸಿ
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # ಎರಡನೇ ஏಪಿಐ ಕರೆ: ಮಾದರಿಯಿಂದ ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯಿರಿ
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ಕಾರ್ಯ ಕರೆ ಹೆಚ್ಚಿನ ಭಾಗದಲ್ಲಿ, ಇಲ್ಲವೆ ಎಲ್ಲಾ ಏಜೆಂಟ್ ಟೂಲ ಉಪಯೋಗ ವಿನ್ಯಾಸದ ಹೃದಯಭಾಗವಾಗಿದೆ, ಆದರೆ ಇದನ್ನು ನಿಂತರಿತವಾಗಿ ಜಾರಿಗೊಳಿಸುವುದು ಕೆಲವೊಮ್ಮೆ ಸವಾಲಾಗಬಹುದು.
[ಪಾಠ 2](../../../02-explore-agentic-frameworks)ನಲ್ಲಿ ನಾವು ಕಲಿತಂತೆ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಗಳು ಪೂರ್ವನಿರ್ಮಿತ ಕಟ್ಟಡ ಬ್ಲಾಕ್ಗಳನ್ನು ಟೂಲ ಉಪಯೋಗಕ್ಕೆ ಒದಗಿಸುತ್ತವೆ.
 
## ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಗಳೊಂದಿಗೆ ಟೂಲ ಉಪಯೋಗದ ಉದಾಹರಣೆಗಳು

ವಿವಿಧ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಗಳ ಮೂಲಕ ಟೂಲೊ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಹೇಗೆ ಜಾರಿಗೆ ತರಬಹುದೆಂಬುದರ ಕೆಲವು ಉದಾಹರಣೆಗಳು:

### Microsoft ಏಜಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft ಏಜಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್</a> ಎಂಬುದು AI ಏಜೆಂಟ್ಗಳ ನಿರ್ಮಾಣಕ್ಕಾಗಿ ಒಪನ್-ಸೋರ್ಸ್ AI ಫ್ರೇಮ್‌ವರ್ಕ್ ಆಗಿದ್ದು, ಕಾರ್ಯ ಕರೆ ಉಪಕರಣಗಳನ್ನು Python ಕಾರ್ಯಗಳಾಗಿ `@tool` ಡೆಕೊರೇಟರ್ನೊಂದಿಗೆ ವ್ಯಾಖ್ಯಾನಿಸಲು ಸಾದ್ಯವಾಗಿಸುತ್ತದೆ. ಫ್ರೇಮ್‌ವರ್ಕ್ ಮಾದರಿ ಮತ್ತು ನಿಮ್ಮ ಕೋಡ್ ನಡುವಿನ ಸಂವಹನ ನಿರ್ವಹಣೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತ ಮಾಡುತ್ತದೆ. ಇದು `FoundryChatClient` ಮೂಲಕ ಫೈಲ್ ಸರ್ಚ್ ಮತ್ತು ಕೋಡ್ ಇಂಟರ್‌ಪ್ರಿಟರ್ ಮುಂತಾದ ಪೂರ್ವನಿರ್ಮಿತ ಸಾಧನಗಳಿಗೆ ಪ್ರವೇಶವನ್ನು ಒದಗಿಸುತ್ತದೆ.

Microsoft ಏಜಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ನಲ್ಲಿ ಕಾರ್ಯ ಕರೆ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಅಳವಡಿಸುವ ಡಯಾಗ್ರಾಮ್ ಕೆಳಕಂಡಂತೆ ಇದೆ:

![ಕಾರ್ಯ ಕರೆ](../../../translated_images/kn/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft ಏಜಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ನಲ್ಲಿ, ಉಪಕರಣಗಳು ಅಲಂಕರಿತ ಕಾರ್ಯಗಳಾಗಿ ವ್ಯಾಖ್ಯಾನಿಸಲಾಗುತ್ತವೆ. ಅತಿಗೆ ನಾವು ಮುಂಚಿತವಾಗಿ ನೋಡಿದ `get_current_time` ಕಾರ್ಯವನ್ನು `@tool` ಡೆಕೊರೇಟರ್‍ನೊಂದಿಗೆ ಉಪಕರಣವಾಗಿ ಪರಿವರ್ತಿಸಬಹುದು. ಫ್ರೇಮ್‌ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಾರ್ಯ ಮತ್ತು ಅದರ ಪ್ಯಾರಾಮೀಟರ್ ಗಳ ಸರಣೀಕರಣವನ್ನು ನಡೆಸುತ್ತದೆ, LLMಗೆ ಕಳುಹಿಸಲು ಸ್ಕೀಮಾ ರಚಿಸುತ್ತದೆ.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ಕ್ಲೈಂಟ್ ರಚಿಸಿ
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ಏಜೆಂಟ್ ರಚಿಸಿ ಮತ್ತು ಟೂಲ್‌ನೊಂದಿಗೆ ಚಾಲನೆ ಮಾಡಿ
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry ಏಜಂಟ್ ಸೇವೆ

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry ಏಜಂಟ್ ಸೇವೆ</a> ಎಂಬುದು ಹೊಸ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಆಗಿದ್ದು ಡೆವಲಪರ್‌ಗಳಿಗೆ ಅಡಿಯಲ್ಲಿ ಕಂಪ್ಯೂಟ್ ಮತ್ತು ಸ್ಟೋರೆಜ್ ಸಂಪನ್ಮೂಲಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಅಗತ್ಯವಿಲ್ಲದೆ ಭದ್ರವಾಗಿ, deploy ಹಾಗೂ ವಿಸ್ತರಿಸಬಹುದಾದ ಉನ್ನತ ಗುಣಮಟ್ಟದ AI ಏಜೆಂಟ್ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಅನುಕರಿಸುವುದು. ಇದು ವಿಶೇಷವಾಗಿ ಎಂಟರ್‌ಪ್ರೈಸ್ ಆಪ್ಲಿಕೇಶನ್ಗಳಿಗೆ ಆಗಿದೆ ಏಕೆಂದರೆ ಇದು ಸಂಪೂರ್ಣ ಸಂಚಾಲಿತ ಸೇವೆಯಾಗಿದ್ದು ಎಂಟರ್‌ಪ್ರೈಸ್ ಶ್ರೇಣಿಯ ಭದ್ರತೆ ಒದಗಿಸುತ್ತದೆ.

ನೇರವಾಗಿ LLM API ಬಳಸಿ ಅಭಿವೃದ್ಧಿ ಮಾಡೋದೊಂದಿಗೆ ಹೋಲಿಸಿದಾಗ, Microsoft Foundry ಏಜಂಟ್ ಸೇವೆ ಕೆಲವು ಪ್ರಯೋಜನಗಳು ಒದಗಿಸುತ್ತದೆ, ಅಂದರೆ:

- ಸ್ವಯಂಚಾಲಿತ ಟೂಲ ಹcalling – ಟೂಲೊ ಕರೆವನ್ನು ವಿಶ್ಲೇಷಿಸುವುದು, ಉಪಕರಣವನ್ನು ಕರೆಸು, ಮತ್ತು ಉತ್ತರ ನಿರ್ವಹಿಸುವ ಅವಶ್ಯಕತೆ ಇಲ್ಲ; ಇದು ಎಲ್ಲವೂ ಸರ್ವರ್-ಪಾರ್ಶ್ವದಲ್ಲಿ ನಡೆಯುತ್ತದೆ
- ಭದ್ರತೆಯಾದ ಡೇಟಾ ನಿರ್ವಹಣೆ – ನಿಮ್ಮ ಸ್ವಂತ ಸಂಭಾಷಣ ಸ್ಥಿತಿಯನ್ನು ನಿರ್ವಹಿಸುವ ಬದಲು, ಸಂಪೂರ್ಣ ಮಾಹಿತಿ ಸಂಗ್ರಹಿಸಲು ಥ್ರೆಡ್ಗಳನ್ನು ನಂಬಬಹುದು
- ಅರ್ಜಿ ತಯಾರಿಕೆಗೆ ಸಿದ್ಧವಾದ ಟೂಲಗಳು – Bing, Azure AI Search, ಮತ್ತು Azure Functions ಮುಂತಾದ ಡೇಟಾ ಮೂಲಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಉಪಯುಕ್ತವಾಗುವ ಟೂಲಗಳು

Microsoft Foundry ಏಜಂಟ್ ಸೇವೆಯ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ಎರಡು ವರ್ಗಗಳಾಗಿ ವಿಭಜಿಸಬಹುದು:

1. ಜ್ಞಾನ ಟೂಲಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ಮೂಲಕ ಅಡಿಕೆ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ಫೈಲ್ ಹುಡುಕಾಟ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI ಹುಡುಕಾಟ</a>

2. ಕಾರ್ಯ ಟೂಲಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ಕಾರ್ಯ ಕರೆ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">ಕೋಡ್ ಇಂಟರ್‌ಪ್ರಿಟರ್</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI ವ್ಯಾಖ್ಯಾನಿತ ಉಪಕರಣಗಳು</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure ಕಾರ್ಯಗಳು</a>

ಏಜೆಂಟ್ ಸೇವೆ ನಮಗೆ ಇವುಗಳನ್ನು `ಟೂಲ್ಸೆಟ್` ಎನಿಸಿಕೊಂಡು ಉಪಯೋಗಿಸಲು ಅವಕಾಶ ಮಾಡಿಕೊಡುತ್ತದೆ. ಇದು ಸಂಭಾಷಣೆಯ ಸಂದೇಶಗಳ ಇತಿಹಾಸವನ್ನು ಮುಡಿಪಾಗೊಳಿಸುವ `ಥ್ರೆಡ್ಗಳನ್ನು` ಸಹ ಬಳಸುತ್ತದೆ.

ನೀವು Contoso ಎಂಬ ಕಂಪನಿಯಲ್ಲಿ ಮಾರಾಟ ಏಜಂಟ್ ಆಗಿದ್ದೀರಿ ಎಂದು ಕಲ್ಪಿಸೋಣ. ನಿಮ್ಮ ಮಾರಾಟ ಡೇಟಾ ಬಗ್ಗೆ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ನೀಡುವ ಸಂಭಾಷಣ ಏಜೆಂಟ್ ಅನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸಲು ಬಯಸುತ್ತೀರಿ.

ಕೆಳಗಿನ ಚಿತ್ರವು Microsoft Foundry ಏಜಂಟ್ ಸೇವೆಯನ್ನು ಬಳಸಿಕೊಂಡು ನಿಮ್ಮ ಮಾರಾಟ ಡೇಟಾವನ್ನು ವಿಶ್ಲೇಷಿಸುವ ವಿಧಾನವನ್ನು ತೋರುತ್ತದೆ:

![ಎಜಂಟಿಕ್ ಸೇವೆಯ ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ](../../../translated_images/kn/agent-service-in-action.34fb465c9a84659e.webp)

ಈ ಸೇವೆಯೊಂದಿಗೆ ಯಾವುದೇ ಉಪಕರಣವನ್ನು ಬಳಸಲು ನಾವು ಕ್ಲೈಯೆಂಟ್ ರಚಿಸಿ ಟೂಲೊ ಅಥವಾ ಟೂಲ್ಸೆಟ್ ನಿಗದಿಮಾಡಬಹುದು. ಇದನ್ನು ಪ್ರಾಯೋಗಿಕವಾಗಿ ಜಾರಿಗೊಳಿಸಲು Python ಕೋಡ್ ಕೆಳಕಂಡಂತೆ ಇರಬಹುದು. LLM ಉಪಕರಣ ಸಂಗ್ರಹವನ್ನು ನೋಡಿ ಬಳಕೆದಾರರ ವಿನಂತಿಗೆ ತಕ್ಕಂತೆ ಬಳಕೆದಾರ ರಚಿಸಿದ `fetch_sales_data_using_sqlite_query` ಕಾರ್ಯ ಅಥವಾ ಪೂರ್ವನಿರ್ಮಿತ ಕೋಡ್ ಇಂಟರ್‌ಪ್ರಿಟರ್ ಅನ್ನು ಬಳಸುವುದು ನಿರ್ಧರಿಸುತ್ತದೆ.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ಕಾರ್ಯವು fetch_sales_data_functions.py ಕಡತದಲ್ಲಿ ಕಾಣುತ್ತದೆ.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ಉಪಕರಣ ಸೆಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ಕಾರ್ಯದೊಂದಿಗೆ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ ಏಜೆಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಅದನ್ನು ಉಪಕರಣ ಸೆಟ್‌ಗೆ ಸೇರ್ಸಿಕೊಳ್ಳಿ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# ಕೋಡ್ ಇಂಟರಪ್ರಿಟರ್ ಉಪಕರಣವನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಅದನ್ನು ಉಪಕರಣ ಸೆಟ್‌ಗೆ ಸೇರ್ಸಿಕೊಳ್ಳಿ.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ನಂಬಪಹೊಸ AI ಏಜೆಂಟ್ಗಳಿಗೆ ಟೂಲ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಬಳಸುವ ವಿಶೇಷ ಪರಿಗಣನೆಗಳು ಯಾವುವು?

LLMಗಳಿಂದ ಸೃಷ್ಟಿಸಲಾಗುವ ಡೈನಾಮಿಕ್ SQL ಗೆ ಸಾಮಾನ್ಯವಾದ ವ್ಯತ್ಯಾಸ ಎನ್ನುವುದು ಭದ್ರತೆ, ವಿಶೇಷವಾಗಿ SQL ಇಂಜೆಕ್ಷನ್ ಅಥವಾ ದುರುದ್ದೇಶಿ ಕಾರ್ಯಗಳ ಅಪಾಯ (ಡೇಟಾಬೇಸ್ ಡ್ರಾಪ್ ಅಥವಾ ಹಾನಿ). ಈ ವೈಫಲ್ಯಗಳನ್ನು ಸಮರ್ಥವಾಗಿ ತಡೆಗಟ್ಟಲು ಸರಿಯಾಗಿ ಡೇಟಾಬೇಸ್ ಪ್ರವೇಶ ಹಕ್ಕುಗಳನ್ನು ಜಾರಿಗೆ ತರಬೇಕು. ಬಹಳ ಡೇಟಾಬೇಸ್‌ಗಳಿಗೆ ರೀಡ್-ಒನ್‌ಲಿ ಆಗಿ ಕಾನ್ಫಿಗರ್ ಮಾಡುವುದು ಸಂಬಂಧಪಟ್ಟದ್ದಾಗಿದೆ. PostgreSQL ಅಥವಾ Azure SQL ಮುಂತಾದ ಸೇವೆಗಳಿಗೂ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ SELECT (ಪಠ್ಯ-ಮಾತ್ರ) ಹಕ್ಕು ನೀಡಬೇಕು.

ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಭದ್ರ ಪರಿಸರದಲ್ಲಿ ನಡಿಸುವುದು ರಕ್ಷಣೆ ಹೆಚ್ಚಿಸುತ್ತದೆ. ಎಂಟರ್‌ಪ್ರೈಸ್ ಸಂದರ್ಭಗಳಲ್ಲಿ, ಡೇಟಾ ಕಾರ್ಯಾಚರಣಾ ವ್ಯವಸ್ಥೆಯುತದಿಂದ ತೆಗೆದು, ರೀಡ್-ಒನ್‌ಲಿ ಡೇಟಾಬೇಸ್ ಅಥವಾ ಡೇಟಾ ವೇರ್‌ಹೌಸ್‌ಗೆ ಪರಿವಾರ್ತಿತಗೊಳಿಸಲಾಗುತ್ತದೆ, ಇದು ಸುಲಭವಾಗಿ ಬಳಸಬಹುದಾದ ಸ್ಕೀಮಾಕ್ಕೆ ಹೊಂದಿಕೆಯಾಗಿರುತ್ತದೆ. ಇದು ಡೇಟಾ ಭದ್ರತೆಯನ್ನು, ಕಾರ್ಯಕ್ಷಮತೆ ಮತ್ತು ಉಪಲಭ್ಯತೆಯನ್ನು ಸುಧಾರಿಸುತ್ತದೆ ಹಾಗೂ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ವಿಧಿಯುತ ರೀಡ್-ಒನ್‌ಲಿ ಪ್ರವೇಶ ನೀಡುತ್ತದೆ.

## ಮಾದರಿ ಕೋಡ್ಗಳು

- Python: [ಎಜಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್](./code_samples/04-python-agent-framework.ipynb)
- .NET: [ಎಜಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್](./code_samples/04-dotnet-agent-framework.md)

## ಟೂಲ ಉಪಯೋಗ ವಿನ್ಯಾಸ ಮಾದರಿಗಳ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿದೆಯೇ?

[Microsoft Foundry ಡಿಸ್ಕರ್ಡ್](https://discord.com/invite/ATgtXmAS5D) ನಲ್ಲಿ ಸೇರಿ ಇತರೆ ಕಲಿಯುತ್ತಿರುವವರನ್ನೊಬ್ಬರಿಗೆ ಭೇಟಿ ಮಾಡಿ, ಕಾರ್ಯಾಲಯ ಸಮಯಗಳಲ್ಲಿ ಭಾಗವಹಿಸಿ ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ಸ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಪಡೆಯಿರಿ.

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI ಏಜೆಂಟ್ ಸೇವೆ ಕಾರ್ಯಾಗಾರ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso ಸೃಜನಾತ್ಮಕ ಬರಹಗಾರ ಬಹು-ಏಜೆಂಟ್ ಕಾರ್ಯಾಗಾರ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft ಏಜಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಅವಲೋಕನ</a>


## ಈ ಏಜೆಂಟ್ ಅನ್ನು ಸ್ಮೋಕ್-ಟೆಸ್ಟ್ ಮಾಡುವುದು (ಐಚ್ಛಿಕ)

ನೀವು [ಪಾಠ 16](../16-deploying-scalable-agents/README.md) ನಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿಯೋಜಿಸಲು ಕಲಿತ ನಂತರ, ಈ ಪಾಠದ `TravelToolAgent` ಅನ್ನು ಸ್ಮೋಕ್-ಟೆಸ್ಟ್ ಮಾಡಬಹುದು (ಇದು ಇನ್ನೂ ತನ್ನ ಟೂಲ್‌ಗಳನ್ನು ಕರೆಗೊಳ್ಳುತ್ತದೆಯಾ ಮತ್ತು ಉತ್ತರಿಸುತ್ತದೆಯಾ?) [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) ಬಳಸಿ. ಅದನ್ನು ಹೇಗೆ ಚಾಲನೆ ಮಾಡುವುದು ಎನ್ನುವುದಕ್ಕೆ [`tests/README.md`](../tests/README.md) ನೋಡಿ.

## ಹಿಂದಿನ ಪಾಠ

[ಏಜೆಂಟಿಕ್ ಡಿಸೈನ್ ಪ್ಯಾಟರ್ನ್‌ಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](../03-agentic-design-patterns/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಏಜೆಂಟಿಕ್ RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->