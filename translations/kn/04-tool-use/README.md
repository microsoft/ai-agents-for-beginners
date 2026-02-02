[![ಒಳ್ಳೆಯ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಹೇಗೆ ವಿನ್ಯಾಸಗೊಳಿಸಬೇಕು](../../../translated_images/kn/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ಈ ಪಾಠದ ವೀಡಿಯೋ ನೋಡಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ

ಉಪಕರಣಗಳು ಆಸಕ್ತಿಕರವಾಗಿವೆ ಏಕೆಂದರೆ ಅವು AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ವ್ಯಾಪಕ ಶಕ್ತಿ ಶ್ರೇಣಿಯನ್ನು ಅನುಮತಿಸುತ್ತವೆ. ಏಜೆಂಟ್ ಒಂದು ನಿರ್ದಿಷ್ಟಕ್ರಮದ ಕ್ರಿಯೆಗಳನ್ನಷ್ಟೇ ಮಾಡಲು ಸಾಧ್ಯವಿದ್ದರೆ, ಉಪಕರಣವನ್ನು ಸೇರಿಸಿದರೆ, ಈಗ ಏಜೆಂಟ್ ವ್ಯಾಪಕ ಶ್ರೇಣಿಯ ಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸಬಹುದು. ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ನಾವು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ನೋಡುತ್ತೇವೆ, ಇದು AI ಏಜೆಂಟ್‌ಗಳು ತಮ್ಮ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ನಿರ್ದಿಷ್ಟ ಉಪಕರಣಗಳನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು ಎಂದು ವಿವರಿಸುತ್ತದೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಕೆಳಗಿನ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಹುಡುಕುವೆವು:

- ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಎಂದರೆ 무엇?
- ಅದನ್ನು ಬಳಕೆ ಮಾಡಬಹುದಾದ ಪ್ರಕರಣಗಳು ಯಾವುವು?
- ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳ್ಳಿಸಲು ಅಗತ್ಯವಿರುವ ಅಂಶಗಳು/ನಿರ್ಮಾಣ ಘಟಕಗಳು ಯಾವುವು?
- ವಿಶ್ವಾಸಾರ್ಹ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಬಳಸುವಾಗ ವಿಶೇಷ ಗಮನವಿರಬೇಕಾದ ಅಂಶಗಳು ಯಾವುವು?

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠ ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಮಾಡಬಲ್ಲಿರಾ:

- ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಮತ್ತು ಅದರ ಉದ್ದೇಶವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದು.
- ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಅನ್ವಯವಾಗಬಹುದಾದ ಬಳಕೆದ ಪ್ರಕರಣಗಳನ್ನು ಗುರುತಿಸುವುದು.
- ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳ್ಳಿಸಲು ಪ್ರಮುಖ ಅಂಶಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು.
- ಈ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಉಪಯೋಗಿಸುವ AI ಏಜೆಂಟ್‌ಗಳಲ್ಲಿ ವಿಶ್ವಾಸಾರ್ಹತೆ ಖಚಿತಪಡಿಸಲು ಕಾಳಜಿ ವಹಿಸುವುದು.

## ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಎಂದರೆ 무엇?

**ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ** LLMಗಳಿಗೆ (ಲಾರ್ಜ್ ಲ್ಯಾಂಗೆಜ್ ಮಾದಲ್‌ಗಳಿಗೆ) ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ಬಾಹ್ಯ ಉಪಕರಣಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಸಾಧ್ಯತೆ ನೀಡುತ್ತದೆ. ಉಪಕರಣಗಳು ಎಂದರೆ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಏಜೆಂಟ್ ಬಳಸಬಹುದಾದ ಕೋಡ್ ಆಗಿರುತ್ತವೆ. ಒಂದು ಉಪಕರಣ ಸರಳ ಕಾರ್ಯವಲ್ಲ, ಉದಾಹರಣೆಗೆ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್ ಅಥವಾ ಥರ್ಡ್-ಪಾರ್ಟಿ ಸೇವೆಗಳಂತಹ API ಕರೆದಂತೆ (ಹಣದ ಬೆಲೆ ಹೋಲಿಕೆ ಅಥವಾ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ). AI ಏಜೆಂಟ್‌ಗಳ ಹಿನ್ನೆಲೆಯಲ್ಲಿ, ಉಪಕರಣಗಳು **ಮಾದರಿ-ಉತ್ಪಾದಿತ ಕಾರ್ಯಕಾಲಿಂಗ್**ಗಾಗಿ ಏಜೆಂಟ್‌ಗಳ ಮೂಲಕ ಚಾಲನೆಗೆ ಒಳಪಡಿಸಲ್ಪಡುತ್ತವೆ.

## ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಯಾವ ಬಳಕೆದ ಪ್ರಕರಣಗಳಿಗೆ ಅನ್ವಯಿಸಬಹುದು?

AI ಏಜೆಂಟ್‌ಗಳು ಸങ്കೀರ್ಣ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು, ಮಾಹಿತಿ ಪಡೆಯಲು ಅಥವಾ ನಿರ್ಧಾರ ಕೈಗೊಳ್ಳಲು ಉಪಕರಣಗಳನ್ನು ಬಳಸಬಹುದು. ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಅನೇಕ ಸಂದರ್ಭಗಳಲ್ಲಿ ಬಳಸಲಾಗುತ್ತದೆ, ವಿಶೇಷವಾಗಿ ಬಾಹ್ಯ ವ್ಯವಸ್ಥೆಗಳೊಂದಿಗೆ ಗತಿಶೀಲ ಸಂವಹನ ಅಗತ್ಯವಿರುವಾಗ, ಉದಾ: ಡೇಟಾಬೇಸ್‌ಗಳು, ವೆಬ್ ಸೇವೆಗಳು ಅಥವಾ ಕೋಡ್ ವಿವೇಚಕರು. ಇದಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ಕೆಲವು ಬಳಕೆದ ಪ್ರಕರಣಗಳು:

- **ಗತಿಶೀಲ ಮಾಹಿತಿ ಪಡೆದಿಕೆ:** ಏಜೆಂಟ್‌ಗಳು ಬಾಹ್ಯ APIಗಳು ಅಥವಾ ಡೇಟಾಬೇಸ್‌ಗಳ ಮೂಲಕ ನವೀನ ಡೇಟಾಗಳನ್ನು ಪಡೆಯಬಹುದು (ಉದಾ: SQLite ಡೇಟಾಬೇಸ್ ಕೈಗೊಳ್ಳುವುದು, ಸ್ಟಾಕ್ ಬೆಲೆಗಳು ಅಥವಾ ಹವಾಮಾನ ಮಾಹಿತಿ ಪಡೆಯುವುದು).
- **ಕೋಡ್ ಕಾರ್ಯಗತೆ ಮತ್ತು ವಿವರಣೆ:** ಗಣಿತ ಸಮಸ್ಯೆಗಳನ್ನು ಬಗೆಹರಿಸಲು ಕೋಡ್ ಅಥವಾ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸುವುದು, ವರದಿಗಳನ್ನು ರಚಿಸುವುದು ಅಥವಾ ಅನುಕರಣಗಳನ್ನು ನಡೆಸುವುದು.
- **ವರ್ಕ್‌ಫ್ಲೋ ಸ್ವಯಂಕ್ರಿಯತೆ:** ಪುನರಾವರ್ತಿತ ಅಥವಾ ಬಹು ಹಂತದ ಕಾರ್ಯವಾಹಿಗಳನ್ನು ಟಾಸ್ಕ್ ಶೆಡ್ಯೂಲರ್‌ಗಳು, ಇಮೇಲ್ ಸೇವೆಗಳು ಅಥವಾ ಡೇಟಾ ಪೈಪ್ಲೈನ್ಗಳ ಮೂಲಕ ಒಂದಾಗಿ ಮಾಡಲು.
- **ಗ್ರಾಹಕ ಬೆಂಬಲ:** CRM ವ್ಯವಸ್ಥೆಗಳು, ಟಿಕೆಟ್ ವ್ಯವಸ್ಥೆಗಳು ಅಥವಾ ಜ್ಞಾನಾಧಾರವನ್ನು ಸಂಪರ್ಕಿಸಿ ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ನೀಡುವುದು.
- **ವಿಷಯ ರಚನೆ ಮತ್ತು ಸಂಪಾದನೆ:** ವ್ಯಾಕರಣ ಪರಿಶೋಧನೆ, ಪಠ್ಯ ಸಾರಾಂಶ ಅಥವಾ ವಿಷಯ ಸುರಕ್ಷತಾ ಮೌಲ್ಯಮಾಪನ ಉಪಕರಣಗಳನ್ನು ಉಪಯೋಗಿಸಿ ವಿಷಯ ಸೃಷ್ಟಿ ಕಾರ್ಯಗಳಲ್ಲಿ ಸಹಾಯ ಮಾಡುವುದು.

## ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳ್ಳಿಸಲು ಬೇಕಾಗುವ ಅಂಶಗಳು/ನಿರ್ಮಾಣ ಘಟಕಗಳು ಯಾವುವು?

ಈ ಘಟಕಗಳು AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ವ್ಯಾಪಕ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ. ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳ್ಳಿಸಲು ಅವಶ್ಯವಾಗಿರುವ ಪ್ರಮುಖ ಅಂಶಗಳನ್ನು ನೋಡೋಣ:

- **ಕಾರ್ಯವಿಧಾನ/ಉಪಕರಣ ಸ್ಕಿಮಾಗಳು**: ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳ ವಿಸ್ತೃತ ವಿವರಗಳು, ಕಾರ್ಯದ ಹೆಸರು, ಉದ್ದೇಶ, ಅಗತ್ಯವಿರುವ ಪರಿಮಾಣಗಳು ಮತ್ತು ನಿರೀಕ್ಷಿತ ಫಲಿತಾಂಶಗಳೊಂದಿಗೆ. ಈ ಸ್ಕಿಮಾಗಳು LLMಗೆ ಯಾವ ಉಪಕರಣಗಳು ಲಭ್ಯವಿದ್ದು ಹೇಗೆ ಮಾನ್ಯ ವಿನಂತಿಗಳನ್ನು ರಚಿಸಬಹುದು ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.

- **ಕಾರ್ಯ ನಿರ್ವಹಣಾ ತಂತ್ರಶಾಸ್ತ್ರ**: ಬಳಕೆದಾರರ ಉದ್ದೇಶ ಮತ್ತು ಸಂಭಾಷಣಾ ಸಂದರ್ಭ ಆಧರಿಸಿ ಉಪಕರಣಗಳನ್ನು ಯಾವಾಗ ಮತ್ತು ಹೇಗೆ ಹಂಬಲಿಸುವುದನ್ನು ನಿರ್ಧರಿಸುವುದು. ಇದರಲ್ಲಿ ಯೋಜಕ ಮಂಡಳಿಗಳು, ಮಾರ್ಗದರ್ಶನ ವ್ಯವಸ್ಥೆಗಳು ಅಥವಾ ಶರತ್ತು ಆಧಾರಿತ ಹರಿವುಗಳು ಇರಬಹುದಾಗಿದೆ.

- **ಸಂದೇಶ ನಿರ್ವಹಣಾ ವ್ಯವಸ್ಥೆ**: ಬಳಕೆದಾರರ ಇನ್‌ಪುಟ್‌ಗಳು, LLM ಪ್ರತಿಕ್ರಿಯೆಗಳು, ಉಪಕರಣ ಕರೆ ಮತ್ತು ಉಪಕರಣ ಫಲಿತಾಂಶಗಳ ನಡುವಿನ ಸಂಭಾಷಣಾ ಹರಿವು ನಿರ್ವಹಿಸುವ ಘಟಕಗಳು.

- **ಉಪಕರಣ ಸಂಯೋಜನೆ ರಾಜ್ಯಕೊಳವು**: ಏಜೆಂಟ್ ಅನ್ನು ಸರಳ ಕಾರ್ಯಗಳು ಅಥವಾ ಸಂಕೀರ್ಣ ಬಾಹ್ಯ ಸೇವೆಗಳಾದ ಅವುಗಳಿಗೆ ಸಂಪರ್ಕಿಸುವ ಮೂಲಸೌಕರ್ಯ.

- **ದೋಷ ನಿರ್ವಹಣಾ ಮತ್ತು ಪರಿಶೀಲನೆ**: ಉಪಕರಣ ಕಾರ್ಯಗತಗೊಳ್ಳುವಲ್ಲಿ ವೈಫಲ್ಯಗಳನ್ನು ಮುಚ್ಚಿಡಲು, ಪರಿಮಾಣಗಳನ್ನು ಪರಿಶೀಲಿಸಲು ಮತ್ತು ಅಪ್ರತೀಕ್ಷಿತ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು ವಿಧಾನಗಳು.

- **ಸ್ಥಿತಿ ನಿರ್ವಹಣೆ**: ಸಂಭಾಷಣೆಯ ಸಂದರ್ಭ, ಹಿಂದಿನ ಉಪಕರಣ ಸಂವಹನಗಳು ಮತ್ತು ಸದೃಢ ಅನೇಕ ಮಾಡಿದ ಸಂವಹನದ ಮೂಲಕ ಆಯಕಟ್ಟಿನ ಮಾಹಿತಿ ವಹಿಸುವಿಕೆ.

ಮುಂದೆ, ಕಾರ್ಯವಿಧಾನ/ಉಪಕರಣ ಕರೆ ಬಗ್ಗೆ ವಿವರವಾಗಿ ನೋಡೋಣ.

### ಕಾರ್ಯವಿಧಾನ/ಉಪಕರಣ ಕರೆ

ಕಾರ್ಯಕಾಲಿಂಗ್ (Function calling) ಅಂದರೆ LLMಗಳನ್ನು ಉಪಕರಣಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಕೇಂದ್ರವಾಗಿರುವ ವಿಧಾನ. 'ಕಾರ್ಯವಿಧಾನ' ಮತ್ತು 'ಉಪಕರಣ' ಎಂಬ ಪದಗಳು ಪರ್ಯಾಯವಾಗಿ ಬಳಸಲಾಗುತ್ತವೆ ಏಕೆಂದರೆ 'ಕಾರ್ಯವಿಧಾನಗಳು' (ಪುನರಾವರ್ತನೆಗೆ ಯೋಗ್ಯ ಕೋಡ್ ಬ್ಲಾಕಗಳು) ಏಜೆಂಟ್‌ಗಳು ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಬಳಸುವ 'ಉಪಕರಣಗಳು' ಆಗಿವೆ. ಕಾರ್ಯವಿಧಾನಕ್ಕೆ ಕಾನೂನು ಚಲಾಯಿಸಲು, LLM ಬಳಕೆದಾರರ ವಿನಂತಿಯನ್ನು ಕಾರ್ಯವಿವರಣೆಯ ವಿರುದ್ಧ ಹೋಲಿಸಬೇಕು. ಇದಕ್ಕಾಗಿ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಕಾರ್ಯವಿಧಾನಗಳ ವರ್ಣನೆಗಳಿರುವ ಸ್ಕಿಮಾವನ್ನು LLMಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ. ಬಳಿಕ LLM ಕಾರ್ಯಕ್ಕೆ ಅತಿನಬದ ಲಭ್ಯವಿರುವ ಕಾರ್ಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ ಅದರ ಹೆಸರು ಮತ್ತು ಆರ್ಗ್ಯುಮೆಂಟ್ಗಳನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. ಆಯ್ಕೆ ಮಾಡಿದ ಕಾರ್ಯ ಕಾರಭಾರನಿರ್ವಹಣೆಗಾಗಿ ಚಾಲನೆಗೊಂಡು ಅದರ ಪ್ರತಿಕ್ರಿಯೆ LLMಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ, ಅದು ಆ ಮಾಹಿತಿಯನ್ನು ಬಳಸಿ ಬಳಕೆದಾರರ ವಿನಂತಿಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುತ್ತದೆ.

ಕಾರ್ಯವಿಧಾನ ಕರೆಗಳು ಏಜೆಂಟ್‌ಗಳಿಗೆ ಅನುಷ್ಠಾನಗೊಳ್ಳಲು ನಿಮಗೆ ಬೇಕಾಗುವುದು:

1. ಕಾರ್ಯವಿಧಾನ ಕರೆಯನ್ನು ಬೆಂಬಲಿಸುವ LLM ಮಾದರಿ
2. ಕಾರ್ಯವಿವರಣೆ ಹೊಂದಿರುವ ಸ್ಕಿಮಾ
3. ಪ್ರತಿ ಕಾರ್ಯವಿಧಾನಕ್ಕಾಗಿ ಕೋಡ್ ವಿವರಗಳು

ನಗರದಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯ ಪಡೆಯುವ ಉದಾಹರಣೆ ನೋಡೋಣ:

1. **ಕಾರ್ಯವಿಧಾನ ಕರೆಯನ್ನು ಬೆಂಬಲಿಸುವ LLM ಅನ್ನು ಪ್ರಾರಂಭಿಸಿರಿ:**

   ಎಲ್ಲಾ ಮಾದರಿಗಳು ಕಾರ್ಯವಿಧಾನ ಕರೆಯನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ ನೀವು ಬಳಸುತ್ತಿರುವ LLM ಅದನ್ನು ಬೆಂಬಲಿಸುವುದನ್ನು ಪರಿಶೀಲಿಸುವುದು ಮುಖ್ಯ. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ಕಾರ್ಯವಿಧಾನ ಕರೆಯನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. ನಾವು Azure OpenAI ಕ್ಲೈಂಟ್ ಪ್ರಾರಂಭಿಸುವ ಮೂಲಕ ಪ್ರಾರಂಭಿಸಬಹುದು.

    ```python
    # ಆಜೂರ್ ಓಪನ್‌ಎಐ ಕ್ಲೈಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ಕಾರ್ಯವಿಧಾನ ಸ್ಕಿಮಾ ರಚನೆ:**

   ಮುಂದೆ, ಕಾರ್ಯವಿಧಾನದ ಹೆಸರು, ಅದರ ಕಾರ್ಯವಿವರಣೆ ಮತ್ತು ಕಾರ್ಯವಿಧಾನದ ಪರಿಮಾಣಗಳ ಹೆಸರು ಮತ್ತು ವರ್ಣನೆ ಒಳಗೊಂಡ JSON ಸ್ಕಿಮಾವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸೋಣ.
   ನಂತರ ಈ ಸ್ಕಿಮಾವನ್ನು ಹಿಂದಿನಂತಾಗುತ್ತಿರುವ ಕ್ಲೈಂಟ್‌ಗೆ ಕಳುಹಿಸಿ, ಬಳಕೆದಾರನು ಸ್ಯಾನ್ ಫ್ರಾನ್ಸಿಸ್ಕೋ ಸಮಯ ಕಂಡುಹಿಡಿಯಲು ಮಾಡಿದ ವಿನಂತಿಯನ್ನು ಸೇರಿಸಬೇಕು. ಗಮನಿಡಬೇಕಾದದ್ದು, **ಉಪಕರಣ ಕರೆ** ಮಾರ್ಪಟ್ಟಂತೆ, ಪ್ರಶ್ನೆಯ ಅಂತಿಮ ಉತ್ತರ ಅಲ್ಲ. ಮೊದಲನೆಯದಾಗಿ, LLM ಕರೆಯಲು ಆಯ್ಕೆ ಮಾಡಿದ ಕಾರ್ಯವಿಧಾನದ ಹೆಸರು ಮತ್ತು ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.

    ```python
    # ಮಾದರಿಗಾಗಿ ಕಾರ್ಯವಿವರಣೆ ಓದಲು
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಸಂದೇಶ
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # ಮೊದಲ API ಕರೆ: ಮಾದರಿಯ ಪ್ರಕಾರ ಕಾರ್ೕಯವಿಧಾನವನ್ನು ಬಳಸಲು ಕೇಳಿ
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # ಮಾದರಿಯ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಸಂಸ್ಕರಿಸಿ
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **ಕಾರ್ಯ ನಿರ್ವಹಿಸುವ ಕೋಡ್:**

   ಈಗ LLM ಕಾರ್ಯವಿಧಾನ ಆಯ್ಕೆಮಾಡಿಕೊಂಡಿದೆ, ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸುವ ಕೋಡ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ ಮತ್ತು ಕಾರ್ಯಗತಗೊಳಿಸಬೇಕಾಗುತ್ತದೆ.
   ಪೈಥಾನ್‌ನಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯ ಪಡೆಯುವ ಕೋಡ್ ನಾವು ರಚಿಸಬಹುದು. ಜೊತೆಗೆ response_message ನಿಂದ ಹೆಸರು ಮತ್ತು ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ತೆಗೆದು ಅಂತಿಮ ಫಲಿತಾಂಶವನ್ನು ಪಡೆಯಲು ಕೋಡ್ ಬರೆಯಬೇಕಾಗುತ್ತದೆ.

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
     # ಕಾರ್ಯಪಡೆ ಕಾಲ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸಿ
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # ಎರಡನೇ API ಕಾಲ್: ಮಾದರಿಯಿಂದ ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆ ಪಡೆಯಿರಿ
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ಕಾರ್ಯವಿಧಾನ ಕರೆ ಬಹುಮಾನವಾಗಿ ಅಥವಾ ಬಹುತಃ ಏಜೆಂಟ್ ಉಪಕರಣ ಬಳಕೆಯ ವಿನ್ಯಾಸದ ಹೃದಯವಾಗಿದೆ, ಆದರೆ ಅದನ್ನು ಶೂನ್ಯದಿಂದ ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು ಕಷ್ಟಕರವಾಗಬಹುದು.
ನಾವು [ಪಾಠ 2](../../../02-explore-agentic-frameworks) ನಲ್ಲಿ ಬರೆದಂತೆ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ಉಪಕರಣ ಬಳಕೆಗೆ ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.

## ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಉಪಕರಣ ಬಳಕೆ ಉದಾಹರಣೆಗಳು

ನೀವು ಹೇಗೆ ವಿಭಿನ್ನ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಬಹುದು ಎಂಬುದಕ್ಕೆ ಕೆಲವು ಉದಾಹರಣೆಗಳು ಇಲ್ಲಿವೆ:

### ಸಿಮೆಂಟಿಕ್ ಕರ್ಣೆಲ್

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">ಸಿಮೆಂಟಿಕ್ ಕರ್ಣೆಲ್</a> .NET, ಪೈಥಾನ್, ಜावा ಅಭಿವೃದ್ಧಿಪಡಿಸಲ್ಪಡುವವರಿಗೆ ಲಾರ್ಜ್ ಲ್ಯಾಂಗೆಜ್ ಮಾದಲ್‌ಗಳೊಂದಿಗೆ ಕೆಲಸ ಮಾಡಲು ತೆರೆದ ಮೂಲ AI ಫ್ರೇಮ್‌ವರ್ಕ್ ಆಗಿದೆ. ಇದು ಕಾರ್ಯವಿಧಾನಗಳ ವಿವರಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸೀರಿಯಲೈಸ್ ಮಾಡುವ ಮೂಲಕ ಕಾರ್ಯವಿಧಾನ ಕರೆಯನ್ನು ಸರಳಗೊಳಿಸುತ್ತದೆ. ಇದು ಮಾದರಿ ಮತ್ತು ನಿಮ್ಮ ಕೋಡ್ ನಡುವಿನ ಹಿಂದಿರುಗಿ ಸಂವಹನವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. Semantic Kernel ಎಂಬ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಬಳಸುವುದರಿಂದ ಮತ್ತೊಂದು ಲಾಭವೆಂದರೆ ಫೈಲ್ ಹುಡುಕು ಮತ್ತು ಕೋಡ್ ವಿವೇಚಕರಂತಹ ಪೂರ್ವನಿರ್ಮಿತ ಉಪಕರಣಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳಲು ಸಾಧ್ಯತೆ.

ಕೆಳಗಿನ ಆಕೃತಿ Semantic Kernel ನಲ್ಲಿ ಕಾರ್ಯವಿಧಾನ ಕರೆಯ ಪ್ರಕ್ರಿಯೆಯನ್ನು ವಿವರಿಸುತ್ತದೆ:

![function calling](../../../translated_images/kn/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernel ನಲ್ಲಿ ಕಾರ್ಯಗಳು/ಉಪಕರಣಗಳನ್ನು <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">ಪ್ಲಗಿನ್‌ಗಳು</a> ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ. ನಾವು ಮೊದಲು ಕಂಡ get_current_time ಕಾರ್ಯವನ್ನು ಪ್ಲಗಿನ್ ಆಗಿ ತರಲು ಅದನ್ನು ಕ್ಲಾಸ್ ಆಗಿ ಮಾರ್ಪಡಿಸಬಹುದು. kernel_function ಡೆಕೋರೇಟರ್ ಅನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಬಹುದು, ಇದು ಕಾರ್ಯದ ವಿವರಣೆಯನ್ನು ಹೊಂದಿದೆ. ನಂತರ GetCurrentTimePlugin ಜೊತೆ kernel ರಚಿಸಿದಾಗ, kernel ಕಾರ್ಯ ಮತ್ತು ಅದರ ಪರಿಮಾಣಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸೀರಿಯಲೈಸ್ ಮಾಡಿ LLMಗೆ ಕಳುಹಿಸಲು ಸ್ಕಿಮಾಗೆ ರೂಪ ನೀಡುತ್ತದೆ.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# ಕERNEL್ ರಚಿಸಿ
kernel = Kernel()

# ಪ್ಲಗಿನ್ ರಚಿಸಿ
get_current_time_plugin = GetCurrentTimePlugin(location)

# ಪ್ಲಗಿನ್ ಅನ್ನು ಕERNEL್‍ಗೆ ಸೇರಿಸಿ
kernel.add_plugin(get_current_time_plugin)
```
  
### ಅಜೂರ್ AI ಏಜೆಂಟ್ ಸರ್ವೀಸ್

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">ಅಜೂರ್ AI ಏಜೆಂಟ್ ಸರ್ವೀಸ್</a> ಹೊಸ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಆಗಿದ್ದು, ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಭದ್ರವಾಗಿ ಗುಣಮಟ್ಟದ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಅಡಿಕೆ, ನಿಯೋಜನೆ, ವಿಸ್ತರಣೆ ಮಾಡಲು ನೆರವಾಗುತ್ತದೆ, ಆಧಾರಿತ ಕಂಪ್ಯೂಟ್ ಮತ್ತು ಸಂಗ್ರಹಣಾ ಸಂಪನ್ಮೂಲಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಅಗತ್ಯವಿಲ್ಲದೆ. ಇದು ಎಂಟರ್ಪ್ರೈಸ್ ಅನ್ವಯಿಕೆಗಳಿಗೆ ಬಹಳ ಉಪಯುಕ್ತವಾಗಿದೆ ಏಕೆಂದರೆ ಇದು ಸಂಪೂರ್ಣ ನಿರ್ವಹಿತ ಸೇವೆಯಾಗಿದೆ ಮತ್ತು ಎಂಟರ್ಪ್ರೈಸ್-ಗ್ರೇಡ್ ಭದ್ರತೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ.

ನೇರವಾಗಿ LLM API ಬಳನೆಯೊಂದಿಗೆ ಹೋಲಿಸಿದಾಗ, ಅಜೂರ್ AI ಏಜೆಂಟ್ ಸರ್ವೀಸಿನ ಕೆಲವು ಹಿತಗಳು:

- ಸ್ವಯಂಚಾಲಿತ ಉಪಕರಣ ಕರೆ – ಉಪಕರಣ ಕರೆ ವಿಶ್ಲೇಷಿಸಿ, ಉಪಕರಣವನ್ನು ಹಂಬಲಿಸಿ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆ ನಿರ್ವಹಿಸುವ ಅಗತ್ಯವಿಲ್ಲ; ಎಲ್ಲವನ್ನೂ ಸರ್ವರ್‌ಮಾಡಲಾಗಿ ಮಾಡುತ್ತದೆ
- ಭದ್ರವಾಗಿ ನಿರ್ವಹಿಸಲಾದ ಡೇಟಾ – ನಿಮ್ಮ ಸಂಭಾಷಣಾ ಸ್ಥಿತಿಯನ್ನು ನೀವು ನಿರ್ವಹಿಸುವ ಬದಲು ಎಲ್ಲ ಮಾಹಿತಿಯನ್ನೂ threads ನಲ್ಲಿ ಸಂಗ್ರಹಿಸಬಹುದು
- ತಕ್ಷಣ ಬಳಸಬಹುದಾದ ಉಪಕರಣಗಳು – Bing, ಅಜೂರ್ AI ಸರ್ಚ್, ಅಜೂರ್ ಫಂಕ್ಷನ್ಸ್ ಮುಂತಾದ ಡೇಟಾ ಮೂಲಗಳೊಂದಿಗೆ ಸಂವಹನಕ್ಕೆ.

ಅಜೂರ್ AI ಏಜೆಂಟ್ ಸರ್ವೀಸಿನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ಎರಡು ವರ್ಗಗಳಲ್ಲಿ ವಿಭಾಗಿಸಬಹುದು:

1. ಜ್ಞಾನ ಉಪಕರಣಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ಸಹಿತ ಗ್ರೌಂಡಿಂಗ್</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ಫೈಲ್ ಹುಡುಕು</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">ಅಜೂರ್ AI ಸರ್ಚ್</a>

2. ಕಾರ್ಯ ಉಪಕರಣಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ಕಾರ್ಯವಿಧಾನ ಕರೆ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">ಕೋಡ್ ವಿವೇಚಕ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI ನಿರ್ಧಾರಿತ ಉಪಕರಣಗಳು</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">ಅಜೂರ್ ಫಂಕ್ಷನ್ಸ್</a>

ಈ ಏಜೆಂಟ್ ಸರ್ವೀಸ್ ನಾವು ಈ ಉಪಕರಣಗಳನ್ನು `toolset` ಆಗಿ ಪ್ರಯೋಜನ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. ಇದು `threads` ಎಂಬುದು ಬಳಸುತ್ತದೆ, ಅದು ನಿರ್ದಿಷ್ಟ ಸಂಭಾಷಣೆಯ ಸಂದೇಶಗಳ ಇತಿಹಾಸವನ್ನು ಸಂಗ್ರಹಿಸುತ್ತದೆ.

ನೀವು Contoso ಎಂಬ ಕಂಪನಿಯಲ್ಲಿ ಮಾರಾಟ ಏಜೆಂಟ್ ಎಂದು ಗಾಳಿಗೊಳ್ಳಿರಿ. ನಿಮ್ಮ ಮಾರಾಟ ಡೇಟಾ ಕುರಿತು ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ನೀಡಲು ಸಂಭಾಷಣಾತ್ಮಕ ಏಜೆಂಟ್ ರಚಿಸಲು ಇಚ್ಛಿಸುತ್ತಿದ್ದೀರಿ.

ಕೆಳಗಿನ ಚಿತ್ರದಲ್ಲಿ ನೀವು ಅಜೂರ್ AI ಏಜೆಂಟ್ ಸರ್ವೀಸ್ ಬಳಸಿ ನಿಮ್ಮ ಮಾರಾಟ ಡೇಟಾವನ್ನು ವಿಶ್ಲೇಷಿಸಲು ಹೇಗೆ ಉಪಯೋಗಿಸಬಹುದು ಎಂಬುದನ್ನು ತೋರಿಸಲಾಗಿದೆ:

![Agentic Service In Action](../../../translated_images/kn/agent-service-in-action.34fb465c9a84659e.webp)

ಸರ್ವೀಸ್ ಜೊತೆಗೆ ಇವುಗಳಲ್ಲಿ ಯಾವುದಾದರೂ ಉಪಕರಣಗಳನ್ನು ಬಳಸಲು ನಾವು ಕ್ಲೈಯಿಂಟ್ ರಚಿಸಿ ಉಪಕರಣ ಅಥವಾ ಉಪಕರಣ ಸಂಗ್ರಹವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಬಹುದು. ಇದನ್ನು ಪ್ರಾಯೋಗಿಕವಾಗಿ ಅನುಷ್ಠಾನಗೊಳ್ಳಿಸಲು ಕೆಳಗಿನ ಪೈಥಾನ್ ಕೋಡ್ ಬಳಸಬಹುದು. LLM ಉಪಕರಣ ಸಂಗ್ರಹವನ್ನು ನೋಡಿ ಬಳಸುವ ಮಾರ್ಗವನ್ನು ಆಯ್ಕೆಮಾಡುತ್ತದೆ: ಬಳಕೆದಾರ ರಚಿಸಿದ `fetch_sales_data_using_sqlite_query` ಕಾರ್ಯವಿಧಾನ ಅಥವಾ ಪೂರ್ವ ನಿರ್ಮಿತ ಕೋಡ್ ವಿವೇಚಕ.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ಫಂಕ್ಷನ್ ಅನ್ನು fetch_sales_data_functions.py ಫೈಲ್‌ನಲ್ಲಿ ಕಾಣಬಹುದು.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ಟೂಲ್ಸೆಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ಫಂಕ್ಷನ್ ಒಳಗೊಂಡ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ ಏಜೆಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಅದನ್ನು ಟೂಲ್ಸೆಟ್‌ಗೆ ಸೇರಿಸಿ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# ಕೋಡ್ ಇಂಟರ್‌ಪ್ರೇಟರ್ ಟೂಲ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಅದನ್ನು ಟೂಲ್ಸೆಟ್‌ಗೆ ಸೇರಿಸಿ.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ವಿಶ್ವಾಸಾರ್ಹ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಬಳಸುವ ವಿಶೇಷ ಗಮನಾರ್ಹ ಅಂಶಗಳು ಯಾವುವು?

LLMಗಳ ಮೂಲಕ ಡೈನಾಮಿಕ್ ಆದ SQL ಬಗ್ಗೆ ಸಾಮಾನ್ಯವಾದ ಚಿಂತೆ ಭದ್ರತೆ, ವಿಶೇಷವಾಗಿ SQL ಇಂಜೆಕ್ಷನ್ ಅಥವಾ ಆಕ್ರಮಣ, ಡೇಟಾಬೇಸ್ ಡ್ರೋಪ್ ಮಾಡುವ ಅಥವಾ ತೊಂದರೆ ಉಂಟುಮಾಡುವ ಅಪಾಯಗಳು. ಈ ಚಿಂತೆಗಳು ನ್ಯಾಯಯುತವಾಗಿವೆ, ಆದರೆ ಡೇಟಾಬೇಸ್ ಪ್ರವೇಶ ಅನುಮತಿಗಳನ್ನು ಸೂಕ್ತವಾಗಿ ಸಂರಚಿಸುವ ಮೂಲಕ ಪರಿಣಾಮಕಾರಿಯಾಗಿ ತಡೆಹಿಡಿಯಬಹುದು. ಬಹುಮಟ್ಟಿಗೆ, ದಾಖಲೆಗಳನ್ನು ಓದುವ ಮಾದರಿಗಾಗಿ ಡೇಟಾಬೇಸ್ ನಿಯೋಜಿಸುವುದು ಮುಖ್ಯ. PostgreSQL ಅಥವಾ ಅಜೂರ್ SQL ಮುಂತಾದ ಡೇಟಾಬೇಸ್ ಸೇವೆಗಳಿಗಾಗಿ ಅಪ್ಲಿಕೇಶನ್ಗೆ ಓದುವ ಹಕ್ಕು (SELECT) ನೀಡಬೇಕು.
ಸುರಕ್ಷಿತ ವಾತಾವರಣದಲ್ಲಿ ಆ್ಯಪ್ ಅನ್ನು ನಡೆಸುವುದರಿಂದ ಇನ್ನಷ್ಟು ರಕ್ಷಣೆಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ. ಉದ್ಯಮ ಸನ್ನಿವೇಶಗಳಲ್ಲಿ, ಡೇಟಾವನ್ನು ಸಾಮಾನ್ಯವಾಗಿ ಕಾರ್ಯಾಚರಣೆ ವ್ಯವಸ್ಥೆಗಳಿಂದ ಓದುವಷ್ಟು ಮಾತ್ರ ಇರುವ ಡೇಟಾಬೇಸ್ ಅಥವಾ ಡೇಟಾ ವೇರ್‌ಹೌಸ್‌ಗೆ ಹಿಂದಿರುಗಿಸಿ ರೂಪಾಂತರಿಸಲಾಗುತ್ತದೆ ಹಾಗೂ ಬಳಕೆದಾರ ಸ್ನೇಹಿ స్కೀಮಾ ಹೊಂದಿರುತ್ತದೆ. ಈ ರೀತಿ ಡೇಟಾ ಸುರಕ್ಷಿತವಾಗಿದ್ದು, ಪ್ರದರ್ಶನ ಮತ್ತು ಪ್ರವೇಶಿಕತೆಗೆ ಸೂಕ್ತವಾಗಿದೆ, ಮತ್ತು ಆ್ಯಪ್‌ಗೆ ನಿರ್ಬಂಧಿತ, ಓದುವಷ್ಟೇ ಆಗಿರುವ ಪ್ರವೇಶವಿದೆ ಎಂಬುದು ಖಚಿತಪಡಿಸುತ್ತದೆ.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ರದ್ದತಿ ತಿಳிப்பு**:  
ಈ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಆಠಟತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸುವಾಗ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುಗಳಿರಬಹುದು. ಮೂಲ ನಾಟಕದಲ್ಲಿ ಇರುವ ಮೂಲ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ಅಧಿಕಾರದ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುಬುರುಪುಗಳು ಅಥವಾ ತಪ್ಪು ಅನರ್ಥನೆಗಳಿಗಾಗಿ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->