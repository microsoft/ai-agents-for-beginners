[![ಯಂತ್ರಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸುವ ವಿಧಾನ](../../../translated_images/kn/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ಈ ಪಾಠದ ವೀಡಿಯೋವನ್ನು ವೀಕ್ಷಿಸಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ

ಟೂಲ್ಗಳು ಆಸಕ್ತಿದಾಯಕವಾಗಿವೆ ಏಕೆಂದರೆ ಅವು AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ವಿಶಾಲ ಶ್ರೇಣಿಯ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನೀಡುತ್ತವೆ. ಏಜೆಂಟ್‌ಗೆ ಕೇವಲ ನಿರ್ದಿಷ್ಟ ಕ್ರಿಯೆಗಳ ಸೆಟ್ ಇದ್ದರೆ, ಟೂಲ್ ಸೇರಿಸುವ ಮೂಲಕ ಏಜೆಂಟ್ ಈಗ ವಿಭಿನ್ನ ಕ್ರಿಯೆಗಳ ವಿಶಾಲ ಶ್ರೇಣಿಯನ್ನು ನಿರ್ವಹಿಸಬಹುದು. ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ನಾವು ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ನೋಡೋಣ, ಇದು AI ಏಜೆಂಟ್‌ಗಳು ತಮ್ಮ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ನಿರ್ದಿಷ್ಟ ಟೂಲ್ಗಳನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು ಎನ್ನುವುದನ್ನು ವಿವರಿಸುತ್ತದೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಕೆಳಗಿನ ಪ್ರಶ್ನೆಗಳ উত্তর ಹುಡುಕಲಿದ್ದೇವೆ:

- ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಎಂದರೇನು?
- ಇದನ್ನು ಬಳಸಬಹುದಾದ ಉಪಯೋಗ ಪ್ರಕರಣಗಳು ಯಾವುವು?
- ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ನಡಿಸಲು ಅಗತ್ಯವಿರುವ ಅಂಶಗಳು/ಆಧಾರಗಳು ಯಾವುವು?
- ನಂಬಿಕೆಯುತ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯ ವಿಶೇಷ ಪರಿಗಣನೆಗಳು ಯಾವುವು?

## ಅಧ್ಯಯನ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಸಾಧ್ಯವಾಗುವುದು:

- ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯ ಪರಿಗಣನೆ ಮತ್ತು ಅದರ ಉದ್ದೇಶವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲಾಗುವುದು.
- ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಅನ್ವಯಿಸಲು ಸಾಧ್ಯವಾಗುವ ಉಪಯೋಗ ಪ್ರಕರಣಗಳನ್ನು ಗುರುತಿಸಲಾಗುವುದು.
- ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ನಡಿಸಲು ಅಗತ್ಯವಿರುವ ಪ್ರಮುಖ ಅಂಶಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲಾಗುವುದು.
- ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಬಳಸುವಾಗ AI ಏಜೆಂಟ್‌ಗಳಲ್ಲಿ ನಂಬಿಕೆ ಕುರಿತು ಪರಿಗಣನೆಗಳನ್ನು ಗುರುತಿಸಲಾಗುವುದು.

## ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಎಂದರೇನು?

**ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ** LLM ಗಳು ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ಹೊರಗಿನ ಟೂಲ್ಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಸಾದ್ಯವಾಗುವಂತೆ ಮಾಡುವುದರ ಮೇಲೆ ಕೇಂದ್ರೀಕೃತವಾಗಿದೆ. ಟೂಲ್ಗಳು ಒಬ್ಬ ಏಜೆಂಟ್ ಸಂಘಟಿಸಿದ ಕೋಡ್ ಆಗಿದ್ದು ಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು ನಿರ್ವಹಿಸಬಹುದು. ಟೂಲ್ ಸರಳ ಕಾರ್ಯವಾಗಿರಬಹುದು ಅಂದರೆ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್, ಅಥವಾ ತೃತೀಯ-ಪಕ್ಷ ಸೇವೆಯ API ಕರೆ ಆಗಬಹುದು ಉದಾಹರಣೆಗೆ ಷೇರು ಬೆಲೆ ಪರಿಶೀಲನೆ ಅಥವಾ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ. AI ಏಜೆಂಟ್‌ಗಳ ಸನ್ನಿವೇಶದಲ್ಲಿ, ಟೂಲ್ಗಳು **ಮಾದರಿ-ಸೃಷ್ಟಿಸಿದ ಕಾರ್ಯಕಾಲ್ಸ್** ಗೆ ಪ್ರತಿಕ್ರಿಯಿಸುವಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳ ಮೂಲಕ ನಿರ್ವಹಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿವೆ.

## ಯಾವ ಉಪಯೋಗ ಪ್ರಕರಣಗಳಲ್ಲಿ ಅನ್ವಯಿಸಬಹುದು?

AI ಏಜೆಂಟ್‌ಗಳು ಜಟಿಲ ಕೆಲಸಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು, ಮಾಹಿತಿಯನ್ನು ಪಡೆದುಕೊಳ್ಳಲು ಅಥವಾ ನಿರ್ಣಯಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು ಟೂಲ್ಗಳನ್ನು ಬಳಸಬಹುದು. ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಬಹುಪಟಿ ಕೆಲಸಗಳಿಗೆ ಹೊರಗಿನ ವ್ಯವಸ್ಥೆಗಳೊಂದಿಗೆ ಗತಿ ಹೊಂದುವ ಸಂವಹನ ಅಗತ್ಯವಿರುವ ಸನ್ನಿವೇಶಗಳಲ್ಲಿ ಬಳಸಲಾಗುತ್ತದೆ, ಉದಾ: ಡೇಟಾಬೇಸ್‌ಗಳು, ವೆಬ್ ಸೇವೆಗಳು ಅಥವಾ ಕೋಡ್ ವಿವೇಚಕರು. ಇದನ್ನು ಹಲವು ಉಪಯೋಗಗಳಿಗೆ ಬಳಸಬಹುದು:

- **ಗತ್ಯಮಯ ಮಾಹಿತಿ ಪಡೆಯುವುದು:** ಏಜೆಂಟ್‌ಗಳು ನವೀಕೃತ ಡೇಟಾವನ್ನು ಪಡೆಯಲು ಹೊರಗಿನ API ಗಳು ಅಥವಾ ಡೇಟಾಬೇಸ್‌ಗೆ ಕೇಳಬಹುದು (ಉದಾ:SQLite ಡೇಟಾಬೇಸ್‌ಗೆ ಪ್ರಶ್ನೆ, ಷೇರು ಬೆಲೆ ಅಥವಾ ಹವಾಮಾನ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯುವುದು).
- **ಕೋಡ್ ಕಾರ್ಯಗತಿಪಡಿಸುವುದು ಮತ್ತು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು:** ಏಜೆಂಟ್‌ಗಳು ಗಣಿತ ಸಮಸ್ಯೆಗಳನ್ನು ಪರಿಹರಿಸಲು, ವರದಿಗಳನ್ನು ರಚಿಸಲು ಅಥವಾ ಸಿಮ್ಯುಲೇಶನ್‌ಗಳನ್ನು ನಡೆಸಲು ಕೋಡ್ ಅಥವಾ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಕಾರ್ಯಗತಿಪಡಿಸಬಹುದು.
- **ಕಾರ್ಯಪದ್ಧತಿ ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವುದು:** ಕಾರ್ಯಗಳ ಶಾಲುಗೆ, ಇಮೇಲ್ ಸೇವೆಗಳು ಅಥವಾ ಡೇಟಾ ಪೈಪ್ಲೈನ್ಗಳಂತಹ ಸಾಧನಗಳನ್ನು ಏಕೀಕೃತಗೊಳಿಸಿ ಪುನರಾವರ್ತಿತ ಅಥವಾ ಬಹು ಹಂತದ ಕಾರ್ಯಪದ್ಧತಿಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವುದು.
- **ಗ್ರಾಹಕ ಬೆಂಬಲ:** ಏಜೆಂಟ್‌ಗಳು CRM ವ್ಯವಸ್ಥೆಗಳು, ಟಿಕೆಟ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್‌ಗಳು ಅಥವಾ ಜ್ಞಾನ ಮೂಲಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡುತ್ತಾ ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗಳನ್ನು ಪರಿಹರಿಸಬಹುದು.
- **ವಿಷಯ ರಚನೆ ಮತ್ತು ಸಂಪಾದನೆ:** ವ್ಯಾಕರಣ ಪರಿಶೋಧಕರು, ಪಠ್ಯ ಸಾರಾಂಶಕಾರರು ಅಥವಾ ವಿಷಯ ಭದ್ರತಾ ವಿಮರ್ಶಕರುಗಳಂತಹ ಟೂಲ್ಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳುತ್ತಾ ವಿಷಯವನ್ನು ರಚಿಸುವ ಕಾರ್ಯಗಳಿಗೆ ಸಹಾಯ ಮಾಡಬಹುದು.

## ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ನಡಿಸಲು ಬೇಕಾದ ಅಂಶಗಳು/ಆಧಾರಗಳು ಯಾವುವು?

ಈ ಸಿದ್ಧಾಂತಗಳು AI ಏಜೆಂಟ್‌ಗೆ ವಿವಿಧ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ. ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ನಡಿಸಲು ಬೇಕಾದ ಪ್ರಮುಖ ಅಂಶಗಳು ಇವು:

- **ಕೋಡ್/ಟುಲ್ ಸ್ಕೆಮಾಗಳು**: ಲಭ್ಯವಿರುವ ಟೂಲ್ಗಳ ವಿವರವಾದ ವಿವರಣೆಗಳು, ಕಾರ್ಯದ ಹೆಸರು, ಉದ್ದೇಶ, ಅಗತ್ಯವಾದ ಪರಿಮಿತಿಗಳನ್ನು ಒಳಗೊಂಡಂತೆ ನಿರೀಕ್ಷಿತ ನಿರ್ಗಮನಗಳೊಂದಿಗೆ. ಈ ಸ್ಕೆಮಾಗಳು LLM ಗಾಗಿ ಲಭ್ಯವಿರುವ ಟೂಲ್‌ಗಳನ್ನು ಹಾಗೂ ಮಾನ್ಯ ವಿನಂತಿಗಳನ್ನು ರಚಿಸುವ ವಿಧಾನವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.

- **ಕಾರ್ಯನಿರ್ವಹಣಾ ತರ್ಕ**: ಬಳಸುತ್ತಿರುವವರ ಉದ್ದೇಶ ಮತ್ತು ಸಂಭಾಷಣೆಯ ಪ್ರಾಸಂಗಿಕತೆಯ ಆಧಾರವಾಗಿ ಟೂಲ್ಗಳನ್ನು ಯಾವಾಗ ಮತ್ತು ಹೇಗೆ ಕರೆಸುವುದು ಎಂಬುದನ್ನು ನಿರ್ಧರಿಸುವುದು. ಇದರಲ್ಲಿ ಯೋಜನಾ ಘಟಕಗಳು, ಮಾರ್ಗದರ್ಶನ ವ್ಯವಸ್ಥೆಗಳು ಅಥವಾ ಸ್ಥಿತಿಗತਿਹೊಂದಿಗಿನ ಪ್ರವಾಹಗಳು ಇರಬಹುದು.

- **ಸಂದೇಶ ನಿರ್ವಹಣಾ ವ್ಯವಸ್ಥೆ**: ಬಳಕೆದಾರರ ಇನ್ಪುಟ್ಗಳಿಂದ, LLM ಪ್ರತಿಕ್ರಿಯೆಗಳ, ಟೂಲ್ ಕರೆಗಳ ಮತ್ತು ಟೂಲ್ ನಿರ್ಗಮನಗಳ ನಡುವಣ ಸಂಭಾಷಣಾತ್ಮಕ ಪ್ರವಾಹವನ್ನು ನಿರ್ವಹಿಸುವ ಘಟಕಗಳು.

- **ಟೂಲ್ ಇಂಟಿಗ್ರೇಷನ್ ಫ್ರೇಮ್ವರ್ಕ್**: ಏಜೆಂಟ್‌ನ್ನು ವಿವಿಧ ಟೂಲ್ಗಳೊಂದಿಗೆ ಸಂಪರ್ಕಿಸುವ ಮೂಲಸೌಕರ್ಯಗಳು, ಸರಳ ಕಾರ್ಯಗಳಾಗಿದ್ದರೂ ಅಥವಾ ಸಂಯುಕ್ತ ತೃತೀಯ-ಪಕ್ಷ ಸೇವೆಗಳಾಗಿದ್ದರೂ.

- **ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಮಾನ್ಯತೆ**: ಟೂಲ್ನ ಕಾರ್ಯಗತಿಪಡಿಸುವಿಕೆಯಲ್ಲಿ ವೈಫಲ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುವ, ಪರಿಮಿತಿಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸುವ ಮತ್ತು ನಿರೀಕ್ಷಿತವಲ್ಲದ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಯಂತ್ರಗಳು.

- **ಸ್ಥಿತಿ ನಿರ್ವಹಣೆ**: ಸಂಭಾಷಣೆ ಪ್ರಾಸಂಗಿಕತೆ, ಹಿಂದಿನ ಟೂಲ್ ಸಂವಹನಗಳು ಮತ್ತು ಬಹು-ಸುತ್ತು ಸಂವಹನಗಳಲ್ಲಿ ಸಮ್ಮಿಲನವನ್ನು ಖಚಿತಪಡಿಸುವ ನಿರಂತರ ಡೇಟಾವನ್ನು ಅನುಸರಿಸುವುದು.

ಇನ್ನೂ ಮುಂದೆ, ಕಾರ್ಯ/ಟೂಲ್ ಕರೆ ಮಾಡುವಿಕೆ ಬಗ್ಗೆ ವಿವರವಾಗಿ ನೋಡೋಣ.

### ಕಾರ್ಯ/ಟೂಲ್ ಕರೆಯುವುದು

ಕಾರ್ಯ ಕರೆ ಮಾಡುವುದು LLM ಗಳಿಗೆ ಟೂಲ್ಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಮುಖ್ಯ ವಿಧಾನವಾಗಿದೆ. ನೀವು ಹೆಚ್ಚಾಗಿ 'ಕಾರ್ಯ' ಮತ್ತು 'ಟೂಲ್' ಪದಗಳನ್ನು ಪರ್ಯಾಯವಾಗಿ ಬಳಸುವುದನ್ನು ಕಾಣಬಹುದು ಏಕೆಂದರೆ 'ಕಾರ್ಯಗಳು' (ಪುನಃಬಳಕೆಗೊಳ್ಳಬಹುದಾದ ಕೋಡ್ ಘಟಕಗಳು) ಎಂಬುವವು ಮೌಲ್ಯವಂತ ಟೂಲ್ಗಳಾಗಿವೆ ಏಜೆಂಟ್‌ಗಳು ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಬಳಸುವವು. ಕಾರ್ಯದ ಕೋಡ್ ಅನ್ನು ಕರೆಸಲು, LLM ಗೆ ಬಳಕೆದಾರರ ವಿನಂತಿಯನ್ನು ಕಾರ್ಯ ವಿವರಣೆಯೊಂದಿಗೆ ಹೋಲಿಸಲು ಸಾಧ್ಯವಾಗಬೇಕು. ಇದಕ್ಕಾಗಿ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಕಾರ್ಯಗಳ ವಿವರಣೆಗಳ ಸ್ಕೆಮಾ LLM ಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ. ನಂತರ LLM ಬಹುಮಾನ ಹೊಂದಿದ ಕಾರ್ಯವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ ಅದರ ಹೆಸರು ಮತ್ತು ವಾದಗಳನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ. ಆಯ್ದ ಕಾರ್ಯವನ್ನು ಕರೆಸಲಾಗುತ್ತದೆ, ಅದರ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLM ಗೆ ತಲುಪಿಸಲಾಗುತ್ತದೆ, ಅದು ಆ ಮಾಹಿತಿಯನ್ನು ಬಳಸಿ ಬಳಕೆದಾರರ ವಿನಂತಿಗೆ ಉತ್ತರ ನೀಡುತ್ತದೆ.

ಕಾರ್ಯ ಕರೆ ಮಾಡಿಕೋಳ್ಳಲು ಡೆವಲಪರ್‌ಗಳು ಬೇಕಾಗುವವು:

1. ಕಾರ್ಯ ಕರೆಕೆ ಹೊಣೆಗಾರ LLM ಮಾದರಿ
2. ಕಾರ್ಯ ವಿವರಣೆ ಹೊಂದಿರುವ ಸ್ಕೆಮಾ
3. ಪ್ರತಿಯೊಬ್ಬ ಕಾರ್ಯಕ್ಕೆ ಸಂಬಂಧಪಟ್ಟ ಕೋಡ್

ನಾವು ನಗರದಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯವನ್ನು ಪಡೆಯುವ ಉದಾಹರಣೆಯನ್ನು ತೆಗೆದುಕೊಳ್ಳೋಣ:

1. **ಕಾರ್ಯ ಕರೆ ಮಾಡಬಲ್ಲ LLM ಆರಂಭಿಸು:**

    ಎಲ್ಲಾ ಮಾದರಿಗಳಲ್ಲ ಕೆಲಸ ಮಾಡುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ ನೀವು ಬಳಸುತ್ತಿರುವ ಮಾದರಿ ಕಾರ್ಯ ಕರೆ ಮಾಡಲು ಸಧ್ಯ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ಕಾರ್ಯ ಕರೆ ಆಧರಿತವಾಗಿದೆ. ನಾವು ಅಧಿಕೃತವಾಗಿ Azure OpenAI ಕ್ಲೈಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಬಹುದು.

    ```python
    # Azure OpenAI ಕ್ಲೈಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ಕಾರ್ಯ ಸ್ಕೆಮಾ ರಚನೆ ಮಾಡಿ:**

    ನಂತರ ಕಾರ್ಯದ ಹೆಸರು, ಕಾರ್ಯದ ಕೆಲಸದ ವಿವರಣೆ ಮತ್ತು ಕಾರ್ಯ ಪರಿಮಿತಿಗಳ ಹೆಸರು ಮತ್ತು ವಿವರಣೆಗಳನ್ನು ಹೊಂದಿರುವ JSON ಸ್ಕೆಮಾ ನಿರ್ಧರಿಸುವೆವು.
    ನಂತರ ಈ ಸ್ಕೆಮಾವನ್ನು ಮೊದಲಿಗೆ ನಿರ್ಮಿಸಿದ ಕ್ಲೈಂಟ್‌ಗೆ ಕಳುಹಿಸುವೆವು, ಬಳಕೆದಾರನ ವಿನಂತಿಯನ್ನು ಸಹ ಸೇರಿಸುವೆವು, ಉದಾಹರಣೆಗೆ ಸಾನ್ ಫ್ರಾನ್ಸಿಸ್ಕೋದಲ್ಲಿ ಸಮಯ ಪಡೆಯಲು. ಗಮನಿಸಬೇಕಾದ ಪ್ರಮುಖ ಅಂಶ, **ಟೂಲ್ ಕರೆ** ಹಿಂತಿರುಗುತ್ತದೆ, **ವಿಚಾರ ಪ್ರಶ್ನೆಗೆ ಅಂತಿಮ ಉತ್ತರವಲ್ಲ**. ಮೊದಲು ಹೇಳಿದಂತೆ, LLM ಅದಕ್ಕಾಗಿ ಆಯ್ದ ಕಾರ್ಯದ ಹೆಸರು ಮತ್ತು ಆ ಕಾರ್ಯಕ್ಕೆ ಬರುವ ವಾದಗಳನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.

    ```python
    # ಮಾದರಿಯನ್ನು ಓದಲು ಫಂಕ್ಷನ್ ವಿವರಣೆ
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
  
    # ಮೊದಲ API ಕರೆ: ಮಾದರಿಯನ್ನು ಫಂಕ್ಷನ್ ಬಳಸಲು ಕೇಳಿ
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # ಮಾದರಿಯ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪ್ರಕ್ರಿಯೆಮಾಡಿ
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **ಕಾರ್ಯ ನಿರ್ವಹಿಸಲು ಬೇಕಾದ ಕೋಡ್:**

    LLM ಆಯ್ದ ಕಾರ್ಯವನ್ನು ನಡಿಸಲು, ಕಾರ್ಯದ ಕೋಡನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸುವುದು ಮತ್ತು ನಿರ್ವಹಿಸುವುದು ಅಗತ್ಯ.
    Python ನಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯವನ್ನು ಪಡೆಯಲು ಕೋಡ್ ನಡಿಸಲು ನಾವು ಬರೆಯಬಹುದು. ಪ್ರತಿಕ್ರಿಯೆ ಸಂದೇಶದಿಂದ ಕಾರ್ಯದ ಹೆಸರು ಮತ್ತು ವಾದಗಳನ್ನು ಪಡೆದ ಮೇಲೆ ಅಂತಿಮ ಫಲಿತಾಂಶ ಪಡೆಯಲು ಕೋಡ್ ಬರೆಯುವುದೂ ಅಗತ್ಯ.

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
     # ಫಂಕ್ಷನ್ ಕಾಲ್‌ಗಳನ್ನು ಹ್ಯಾಂಡಲ್ ಮಾಡಿ
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
  
      # ಎರಡನೇ API ಕಾಲ್: ಮಾದರಿಯಿಂದ ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯಿರಿ
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

ಕಾರ್ಯ ಕರೆ ಮಾಡುವುದು ಬಹು ಮೀಟಿಂಗ್ ಟೂಲ್ ಬಳಕೆ ವಿನ್ಯಾಸದ ಹೃದಯभाग ಇದ್ದರೂ, ಅದನ್ನು ಶೂನ್ಯದಿಂದ ಅನುಷ್ಠಾನಗೊಳಿಸುವುದು ಕೆಲವೊಮ್ಮೆ ಸವಾಲು ಆಗಿರಬಹುದು.
ನಾವು [ಪಾಠ 2](../../../02-explore-agentic-frameworks) ನಲ್ಲಿ ಕಲಿತಂತೆ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್ಗಳು ನಮಗೆ ಪೂರ್ವನಿರ್ಮಿತ ಕಟ್ಟಡ ಘಟಕಗಳನ್ನು ನೀಡಿ ಟೂಲ್ ಬಳಕೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುತ್ತವೆ.

## ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಟುಲ್ ಬಳಕೆ ಉದಾಹರಣೆಗಳು

ಕೆಳಗಿನ ಕೆಲವು ಉದಾಹರಣೆಗಳಿವೆ ನೀವು ವಿಭಿನ್ನ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಹೇಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸಬಹುದು ಎಂಬುದರ:

### Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್</a> AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ತೆರೆದ ಮೂಲ ಫ್ರೇಮ್ವರ್ಕ್. ಇದು ಕಾರ್ಯ ಕರೆ ನಡೆಸುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಸರಳಗೊಳಿಸುತ್ತದೆ ಇದರಲ್ಲಿ ನೀವು Python ಕಾರ್ಯಗಳನ್ನು `@tool` ಅಲಂಕಾರದೊಂದಿಗೆ ಟೂಲ್ಗಾಗಿ ವ್ಯಾಖ್ಯಾನ ಮಾಡಬಹುದು. ಈ ಫ್ರೇಮ್ವರ್ಕ್ ಮಾದರಿ ಮತ್ತು ಕೋಡ್ ನಡುವಣ ಪಾಶ್ಚಾತ್ಯ ಸಂವಹನವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. ಇದರಲ್ಲಿ `AzureAIProjectAgentProvider` ಮೂಲಕ ಪೂರ್ವನಿರ್ಮಿತ ಟೂಲ್ಗಳಾದ ಫೈಲ್ ಹುಡುಕು ಮತ್ತು ಕೋಡ್ ವಿವೇಚಕ ಸೇರಿವೆ.

ಕೆಳಗಿನ ಚಿತ್ರ Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ನೊಂದಿಗೆ ಕಾರ್ಯ ಕರೆ ಪ್ರಕ್ರಿಯೆಯನ್ನು ವಿವರಿಸುತ್ತದೆ:

![function calling](../../../translated_images/kn/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ನಲ್ಲಿ, ಟೂಲ್ಗಳನ್ನು ಅಲಂಕೃತ ಕಾರ್ಯಗಳಾಗಿ ವ್ಯಾಖ್ಯಾನಿಸಲಾಗುತ್ತದೆ. ನಾವು ಮೊದಲು ನೋಡಿದ `get_current_time` ಕಾರ್ಯವನ್ನು `@tool` ಅಲಂಕಾರ ಬಳಸಿ ಟೂಲ್ಗಾಗಿ ಪರಿವರ್ತಿಸಬಹುದು. ಫ್ರೇಮ್ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಾರ್ಯ ಮತ್ತು ಅದರ ಪರಿಮಿತಿಗಳನ್ನು ಸೀರಿಯಲ್ ಮಾಡಿದಂತೆ ರೂಪಾಂತರಿಸುತ್ತದೆ, LLM ಗೆ ಕಳುಹಿಸಲು ಸ್ಕೆಮಾವನ್ನು ರಚಿಸುತ್ತದೆ.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ಗ್ರಾಹಕನನ್ನು ಸೃಷ್ಟಿಸಿ
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ಏಜೆಂಟನ್ನು ಸೃಷ್ಟಿಸಿ ಮತ್ತು ಸಾಧನದೊಡನೆ ಚಾಲನೆಮಾಡಿ
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI ಏಜೆಂಟ್ ಸೇವೆ

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI ಏಜೆಂಟ್ ಸೇವೆ</a> ಡೆವಲಪರ್‌ಗಳು ಸುರಕ್ಷಿತವಾಗಿ, ದಕ್ಷವಾಗಿ, ಮತ್ತು ವಿಸ್ತಾರಗೊಳ್ಳುವ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಿದ ಹೊಸ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್ ಆಗಿದೆ. ಇದು ಮೂಲ ಗಣನೆ ಮತ್ತು ಸಂಗ್ರಹಣೆ ವನರಹಿತವಾಗಿ ನಿರ್ವಹಿಸಿದೆ ಮತ್ತು ಸಂಸ್ಥೆಗಳ ಮಟ್ಟದಲ್ಲಿ ಭದ್ರತೆ ಒದಗಿಸುತ್ತದೆ.

ನೇರವಾಗಿ LLM API ಜತೆ ಅಭಿವೃದ್ಧಿಪಡಿಸುವುದಕ್ಕೆ ಹೋಲಿಸಿದರೆ, Azure AI ಏಜೆಂಟ್ ಸೇವೆ ಕೆಲವು ಪ್ರಯೋಜನಗಳನ್ನು ನೀಡುತ್ತದೆ:

- ಸ್ವಯಂಚಾಲಿತ ಟೂಲ್ ಕರೆ – ಟೂಲ್ ಕರೆ ವಿಭಜಿಸಲು, ಕಾರ್ಯಚರಿಸು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಬೇಡ; ಇವು ಎಲ್ಲವನ್ನೂ ಸರ್ವರ್‌ ಪಕ್ಕದಲ್ಲಿ ನಡೀತವೆ
- ಸುರಕ್ಷಿತವಾಗಿ ನಿರ್ವಹಿತ ಡೇಟಾ – ನಿಮ್ಮವರ ಸಂಭಾಷಣಾ ಸ್ಥಿತಿಯನ್ನು ನಿರ್ವಹಿಸುವುದಿಲ್ಲ, ಕಾರ್ಯಗಳಲ್ಲಿ ಎಲ್ಲ ಮಾಹಿತಿ ಹೊಂಡವನ್ನು ಹಂಚುತ್ತದೆ
- ದಯವಿಟ್ಟುಬಂದ ಟೂಲ್ಗಳು – ನೀವು ಬಳಕೆಮಾಡಬಹುದಾದ ಟೂಲ್ಗಳು, ಉದಾ: Bing, Azure AI Search ಮತ್ತು Azure Functions.

Azure AI ಏಜೆಂಟ್ ಸೇವೆಯಲ್ಲಿ ಲಭ್ಯವಿರುವ ಟೂಲ್ಗಳನ್ನು ಎರಡು ವರ್ಗಗಳಾಗಿ ವಿಭಜಿಸಲಾಗಿದೆ:

1. ಜ್ಞಾನ ಟೂಲ್ಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ಮೂಲಕ ನೆಲೆಮಾಡಿಕೊಳ್ಳುವುದು</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ಫೈಲ್ ಹುಡುಕುವುದು</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. ಕಾರ್ಯ ಟೂಲ್ಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ಫಂಕ್ಷನ್ ಕರೆ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">ಕೋಡ್ ವಿವೇಚಕ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI ವ್ಯಾಖ್ಯಾನಿತ ಟೂಲ್ಗಳು</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ಏಜೆಂಟ್ ಸೇವೆ ಈ ಟೂಲ್‌ ಮುಂತಾದವುಗಳನ್ನು `toolset` ಆಗಿ ನಿರ್ವಹಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ. ಇದು `threads` ಗಳನ್ನು ಬಳಸಿ ಮಾಧ್ಯಮದಿಂದ ಸಂದೇಶಗಳ ಇತಿಹಾಸವನ್ನು ಅನುಸರಿಸುತ್ತದೆ.

ನೀವು Contoso ಎಂಬ ಕಂಪನಿಯ ಮಾರಾಟ ಏಜೆಂಟ್ ಎಂದು ಊಹಿಸೋಣ. ನಿಮ್ಮ ಮಾರಾಟ ಡೇಟಾಬೇಟಿನ ಬಗ್ಗೆ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸುವ ಸಂಭಾಷಣಾತ್ಮಕ ಏಜೆಂಟ್‌ ಅನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸಲು ಬಯಸುತ್ತೀರಿ.

ಕೆಳಗಿನ ಚಿತ್ರ Azure AI ಏಜೆಂಟ್ ಸೇವೆಯನ್ನು ಬಳಸಿ ನಿಮ್ಮ ಮಾರಾಟ ಡೇಟಾವನ್ನು ವಿಶ्लेषಿಸುವ ರೀತಿ ವಿವರಿಸುತ್ತದೆ:

![Agentic Service In Action](../../../translated_images/kn/agent-service-in-action.34fb465c9a84659e.webp)

ಈ ಟೂಲ್ಗಳಲ್ಲಿಂದ ಯಾವುದೇ ಒಂದು ಬಳಸಲು ನಾವು ಕ್ಲೈಂಟ್ ರಚಿಸಿ ಟೂಲ್ ಅಥವಾ ಟೂಲ್ ಸೆಟ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಬಹುದು. ಪ್ರಯೋಗಾತ್ಮಕವಾಗಿ ಇದನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಲು Python ಕೋಡ್ ಕೆಳಗಿನಂತಿದೆ. LLM ಟೂಲ್ಸೆಟ್ ನೋಡಿ ಬಳಕೆದಾರ ರಚಿಸಿದ ಕಾರ್ಯ `fetch_sales_data_using_sqlite_query` ಅಥವಾ ಪೂರ್ವನಿರ್ಮಿತ ಕೋಡ್ ವಿವೇಚಕವನ್ನು ಬಳಕೆದಾರನ ವಿನಂತಿ ಆಧಾರವಾಗಿ ಆಯ್ಕೆ ಮಾಡಬಹುದು.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ಫಂಕ್ಷನ್ ಅನ್ನು fetch_sales_data_functions.py ಫೈಲ್ ನಲ್ಲಿ ಕಾಣಬಹುದು.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ಉಪಕರಣ ಸೆಟ್ ಪ್ರಾರಂಭಿಸಿ
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ಫಂಕ್ಷನ್‌ನೊಂದಿಗೆ ಫಂಕ್ಷನ್ ಕರೆಯುವ ಏಜೆಂಟ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಅದನ್ನು ಉಪಕರಣ ಸೆಟ್‌ಗೆ ಸೇರ್ಪಡೆಮಾಡಿ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# ಕೋಡ್ ವಿವೇಚಕ ಉಪಕರಣವನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಅದನ್ನು ಉಪಕರಣ ಸೆಟ್‌ಗೆ ಸೇರಿಸಿ.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ನಂಬಿಕೆಯುತ AI ಏಜೆಂಟ್ ಆರಂಭಿಸಲು ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಬಳಕೆ ಮಾಡುವಾಗ ವಿಶೇಷ ಪರಿಗಣನೆಗಳು ಯಾವುವು?

LLM ಗಳಿಂದ ಡೈನಾಮಿಕ್ ಆಗಿ ಸೃಷ್ಟಿಸಲಾದ SQL ಬಗ್ಗೆ ಸಾಮಾನ್ಯ ಚಿಂತೆ ಭದ್ರತೆ, ವಿಶೇಷವಾಗಿ SQL ಇಂಜೆಕ್ಷನ್ ಅಥವಾ ದುಷ್ಟ ಕ್ರಿಯೆಗಳ ಆತಂಕ, ಉದಾ: ಡೇಟಾಬೇಸ್ ವಿಲೋಪಣೆ ಅಥವಾ ತಿದ್ದುಪಡಿ. ಈ ಆತಂಕಗಳು ತಮ್ಮ ಸ್ಥಾನ ಬಾಳುತ್ತವೆಯಾದರೂ, ಡೇಟಾಬೇಸ್ ಪ್ರವೇಶ ಅನುಮತಿಗಳನ್ನು ಸರಿಯಾಗಿ ಸಂರಚಿಸುವ ಮೂಲಕ ಪರಿಣಾಮಕಾರಿಯಾಗಿ ತಡೆಯಬಹುದು. ಹೆಚ್ಚಿನ ಡೇಟಾಬೇಸ್‌ಗಳಲ್ಲಿ ಇದರಲ್ಲಿ ಡೇಟಾಬೇಸ್ ಅನ್ನು ಓದಲು ಮಾತ್ರ ಅನುಮತಿಸಿದ್ದಂತೆ ಸಂರಚನೆ ಮಾಡುವುದು ಒಳಗೊಂಡಿದೆ. PostgreSQL ಅಥವಾ Azure SQLsಾರख्या ಡೇಟಾಬೇಸ್ ಸೇವೆಗಳಲ್ಲಿ, ಆಪ್ ಓದಲು ಮಾತ್ರ (SELECT) ಹಕ್ಕು ಹೊಂದಿರಬೇಕು.

ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಸುರಕ್ಷಿತ ಪರಿಸರದಲ್ಲಿ ಚಾಲನೆ ಮಾಡುವುದು ರಕ್ಷಣೆಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ. ಸಂಸ್ಥೆಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ಸನ್ನಿವೇಶಗಳಲ್ಲಿ, ಡೇಟಾ ಸಾಮಾನ್ಯವಾಗಿ ಕಾರ್ಯ ಪದ್ಧತಿಯ ವ್ಯವಸ್ಥೆಗಳಿಂದ ಓದಲು ಮಾತ್ರ ಇರುವ ಡೇಟಾಬೇಸ್ ಅಥವಾ ಡೇಟಾ ವೇರ್‌ಹೌಸ್‌ಗೆ ಹೊರತೆಗೆಯಲ್ಪಡುವುದು ಮತ್ತು ಪರಿವರ್ತಿಸಲಾಗುವುದು. ಈ ವಿಧಾನ ಡೇಟಾಗೆ ಭದ್ರತೆ, ಕಾರ್ಯಕ್ಷಮತೆ ಮತ್ತು ಅಧಿಕೃತತೆಗೆ ಅನುಕೂಲಕರವಾಗಿದ್ದು ಆಪ್‌ಗಳಿಗೆ ಓದಲು ಮಾತ್ರ ಹಕ್ಕುಗಳನ್ನು ನೀಡುತ್ತದೆ.

## ಮಾದರಿ ಕೋಡ್‌ಗಳು

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ಟುಲ್ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಗಳ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿದ್ದರೆ?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ನಲ್ಲಿ ಸೇರಿ ಇತರ ಕಲಿತವರನ್ನು ಭೇಟಿಯಾಗಿರಿ, ಕಚೇರಿ ಸಮಯದಲ್ಲಿ ಭಾಗವಹಿಸಿ ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿ.

## ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI ಏಜೆಂಟ್ ಸೇವೆ ಕಾರ್ಯಾಗಾರ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso ಕ್ರಿಯೇಟಿವ್ ರೈಟರ್ ಮಲ್ಟಿ-ಏಜೆಂಟ್ ಕಾರ್ಯಾಗಾರ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಅವಲೋಕನ</a>

## ಹಿಂದಿನ ಪಾಠ

[ಏಜೆಂಟಿಕ್ ವಿನ್ಯಾಸ ಮಾದರಿಗಳ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](../03-agentic-design-patterns/README.md)

## ಮುಂದಿನ ಪಾಠ
[ಏಜೆಂಟಿಕ್ RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->