[![ಚೆನ್ನಾಗಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸುವುದು ಹೇಗೆ](../../../translated_images/kn/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ಈ ಪಾಠದ ವೀಡಿಯೊವನ್ನು ವೀಕ್ಷಿಸಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ

ಉಪಕರಣಗಳು ಆಸಕ್ತಿದಾಯಕವಾಗಿವೆ ಯಾಕಂದರೆ ಅವು AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ವ್ಯಾಪಕವಾದ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ. ಏಜೆಂಟ್ ಬಳಿ ಮಾಡಬಹುದಾದ ಕೆಲವೊಂದು ನಿಷ್ಕೃಷ್ಟ ಕ್ರಿಯೆಗಳ ಸಮುದಾಯವಿರದೆ, ಉಪಕರಣವನ್ನು ಸೇರಿಸುವ ಮೂಲಕ ಏಜೆಂಟ್ ಈಗ ವಿಶೇಷ ಕ್ರಿಯೆಗಳು ತುಂಬಾ ವ್ಯಾಪಕವಾಗಿ ಮಾಡಬಹುದು. ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ನಾವು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ನೋಡುತ್ತೇವೆ, ಇದು AI ಏಜೆಂಟ್‌ಗಳು ತಮ್ಮ ಗುರಿಯನ್ನು ಸಾಧಿಸಲು ನಿಶ್ಚಿತ ಉಪಕರಣಗಳನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು ಎಂದು ವರ್ಣಿಸುತ್ತದೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ, ಕೆಳಗಿನ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಹುಡುಕುತ್ತಿದ್ದೇವೆ:

- ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಎಂದರೆ ಏನು?
- ಅದನ್ನು ಅನ್ವಯಿಸಬಹುದಾದ ಉಪಯೋಗ ಪ್ರಕರಣಗಳೇನು?
- ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಅಗತ್ಯವಿರುವ ಅಂಶಗಳು/ನಿರ್ಮಾಣ ಘಟಕಗಳೇನು?
- ವಿಶ್ವಸನೀಯ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಬಳಸುವಾಗ ವಿಶೇಷ ಪರಿಗಣನೆಗಳೇನು?

## ಅಭ್ಯಾಸ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಹೀಗಾಗಲಾಗಿ:

- ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಮತ್ತು ಅದರ ಉದ್ದೇಶವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲು.
- ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಅನ್ವಯಿಸಬಹುದಾದ ಉಪಯೋಗ ಪ್ರಕರಣಗಳನ್ನು ಗುರುತಿಸಲು.
- ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಅಗತ್ಯವಿರುವ ಮುಖ್ಯ ಅಂಶಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು.
- ಈ ವಿನ್ಯಾಸ ಮಾದರಿ ಬಳಸುವ AI ಏಜೆಂಟ್‌ಗಳಲ್ಲಿ ವಿಶ್ವಾಸಾರ್ಹತೆಯನ್ನು ಖಚಿತಗೊಳಿಸುವ ಪರಿಗಣನೆಗಳನ್ನು ಗುರುತಿಸಲು.

## ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಎಂದರೆ ಏನು?

**ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ** ಆಫ್‌ಲೈನ್ ಅಂಗಾಂಗಗಳಿಗೆ ಸಂಪರ್ಕ ಹೊಂದುವುದಕ್ಕೆ LLMಗಳಿಗೆ ಸಾಮರ್ಥ್ಯವನ್ನು ನೀಡುತ್ತದೆ ಮತ್ತು ನಿಶ್ಚಿತ ಗುರಿಗಳನ್ನು ಸಾಧಿಸುವ ಸಂಧಾನವಾಗಿದೆ. ಉಪಕರಣಗಳು ಎಂದರೆ ಏಜೆಂಟ್ ಕಾರ್ಯನಿರ್ವಹಣೆಗೆ ತಿಳಿಸಲ್ಪಡುವ ಸಂಹಿತಾಗಳು (ಕೋಡ್). ಉಪಕರಣವು ಸರಳವಾದ ಫಂಕ್ಷನ್ ಆಗಿರಬಹುದು, ಉದಾಹರಣೆಗೆ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಅಥವಾ ಸ್ಟಾಕ್ ಬೆಲೆ ಪರಿಶೀಲನೆ ಅಥವಾ ಹವಾಮಾನ ಭವಿಷ್ಯವಾರ್ತೆಯಂತಹ ತೃತೀಯ ಪಕ್ಷ ಸೇವೆಗೆ API ಕರೆಗೆ ಬರುವುದಾಗಿ. AI ಏಜೆಂಟ್‌ಗಳ ಸಂದರ್ಭದಲ್ಲಿ, ಉಪಕರಣಗಳನ್ನು **ಮಾದರಿ-ನಿರ್ಮಿತ ಫಂಕ್ಷನ್ ಕರೆಗೆ** ಉತ್ತರವಾಗಿ ಏಜೆಂಟ್‌ಗಳು ಕಾರ್ಯಗತಗೊಳಿಸುತ್ತವೆ.

## ಅದನ್ನು ಅನ್ವಯಿಸಬಹುದಾದ ಉಪಯೋಗ ಪ್ರಕರಣಗಳೇನು?

AI ಏಜೆಂಟ್‌ಗಳು ಸಂಕೀರ್ಣ ಕೆಲಸಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಲು, ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಲು ಅಥವಾ ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು ಉಪಕರಣಗಳನ್ನು ಬಳಸಬಹುದು. ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಹೆಚ್ಚು ಬಾಹ್ಯ ವ್ಯವಸ್ಥೆಗಳ ಜೊತೆ ಸಡನ್ ಸಂವಹನವನ್ನು ಬೇಡಿಕೊಳ್ಳುವ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ, ಉದಾ. ಡೇಟಾಬೇಸ್‌ಗಳು, ವೆಬ್ ಸೇವೆಗಳು ಅಥವಾ ಕೋಡ್ ವ್ಯಾಖ್ಯಾನಕರಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿ ಬಳಸಲಾಗುತ್ತದೆ. ಇದನ್ನು ಬಳಸಬಹುದಾದ ವಿವಿಧ ಉಪಯೋಗ ಪ್ರಕರಣಗಳೆಂದರೆ:

- **ಗತಿಅನುಸಾರ ಮಾಹಿತಿಯ ಪತ್ತೆಮಾಡುವುದು:** ಏಜೆಂಟ್‌ಗಳು ಬಾಹ್ಯ APIಗಳು ಅಥವಾ ಡೇಟಾಬೇಸ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಇತ್ತೀಚಿನ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಬಹುದು (ಉದಾ: ಡೇಟಾ ವಿಶ್ಲೇಷಣೆಗೆ SQLite ಡೇಟಾಬೇಸ್ ಹಾಡಿಸುವುದು, ಸ್ಟಾಕ್ ಬೆಲೆಗಳು ಅಥವಾ ಹವಾಮಾನದ ಮಾಹಿತಿ ಪಡೆಯುವುದು).
- **ಕೋಡ್ ನಿರ್ವಹಣೆ ಮತ್ತು ವ್ಯಾಖ್ಯಾನ:** ಏಜೆಂಟ್‌ಗಳು ಗಣಿತ ಸಮಸ್ಯೆಗಳನ್ನು ಬಗೆಹರಿಸಲು, ವರದಿಗಳನ್ನು ರಚಿಸಲು ಅಥವಾ ಸಿಮ್ಯುಲೇಶನ್‌ಗಳನ್ನು ನಡೆಸಲು ಕೋಡ್ ಅಥವಾ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ಚಾಲನೆ ಮಾಡಬಹುದು.
- **ಕೆಲಸ ಕ್ರಿಯೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವುದು:** ಟಾಸ್ಕ್ ಶೆಡ್ಯೂಲರ್‌ಗಳು, ಇಮೇಲ್ ಸೇವೆಗಳು ಅಥವಾ ಡೇಟಾ ಪೈಪ್‌ಲೈನ್‌ಗಳಂತಹ ಉಪಕರಣಗಳನ್ನು ಸಂಯೋಜಿಸಿ ಪುನರಾವರ್ತಿತ ಅಥವಾ ಬಹು-ಹಂತ workflows ಅನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವುದು.
- **ಗ್ರಾಹಕ ಬೆಂಬಲ:** CRM ವ್ಯವಸ್ಥೆಗಳು, ಟಿಕೆಟ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್‌ಗಳು ಅಥವಾ ಜ್ಞಾನಾಧಾರಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡುವುದರಿಂದ ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಲು ಏಜೆಂಟ್‌ಗಳು.
- **ವಿಷಯ ರಚನೆ ಮತ್ತು ಸಂಪಾದನೆ:** ವ್ಯಾಕರಣ ಪರಿಶೋಧನೆ, ಪಠ್ಯ ಸಾರಾಂಶಕಗಳು ಅಥವಾ ವಿಷಯ ಭದ್ರತೆ ಮೌಲ್ಯಮಾಪಕಗಳನ್ನು ಉಪಯೋಗಿಸಿ ವಿಷಯ ರಚನೆ ಕಾರ್ಯಗಳಲ್ಲಿ ಸಹಾಯ ಮಾಡುವುದಕ್ಕೆ.

## ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಅಗತ್ಯವಿರುವ ಅಂಶಗಳು/ನಿರ್ಮಾಣ ಘಟಕಗಳೇನು?

ಈ ನಿರ್ಮಾಣ ಘಟಕಗಳು AI ಏಜೆಂಟ್ ಗೆ ವ್ಯಾಪಕ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಸಹಾಯಮಾಡುತ್ತವೆ. ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಅಗತ್ಯವಿರುವ ಪ್ರಮುಖ ಅಂಶಗಳನ್ನು ನೋಡೋಣ:

- **ಫಂಕ್ಷನ್/ಉಪಕರಣ ವಿನ್ಯಾಸಗಳು:** ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳ ವಿವರವಾದ ವ್ಯಾಖ್ಯಾನಗಳು, ಫಂಕ್ಷನ್ ಹೆಸರು, ಉದ್ದೇಶ, ಬೇಕಾದ ಪ್ಯಾರಾಮೀಟರ್ಗಳು ಮತ್ತು ನಿರೀಕ್ಷಿತ ಫಲಿತಾಂಶಗಳು ಸೇರಿದಂತೆ. ಈ ವಿನ್ಯಾಸಗಳು LLMಗೆ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ತಿಳಿಯಲು ಮತ್ತು ಮಾನ್ಯ ವಿನಂತಿಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.

- **ಫಂಕ್ಷನ್ ಕಾರ್ಯಗತಗೊಳ್ಳುವ ಲಾಜಿಕ್:** ಬಳಕೆದಾರರ ಉದ್ದೇಶ ಮತ್ತು ಸಂವಾದ ಪರಿಪ್ರೆಕ್ಷ್ಯ ಆಧಾರದ ಮೇಲೆ ಉಪಕರಣಗಳನ್ನು ಯಾವಾಗ ಮತ್ತು ಹೇಗೆ ಕರೆಮಾಡಬೇಕೋ ನಿಯಂತ್ರಿಸುತ್ತದೆ. ಇದು ಯೋಜನೆ ಮಾಡುವ ಘಟಕಗಳು, ರೂಟಿಂಗ್ ತಂತ್ರಗಳು ಅಥವಾ ಶರದಾರೂಢ ಹರಿವುಗಳನ್ನು ಹೊಂದಿರಬಹುದು, ಅವುಗಳು ಉಪಕರಣ ಬಳಕೆಯನ್ನು ಸಡನ್ ನಿರ್ಧರಿಸುತ್ತವೆ.

- **ಸಂದೇಶ ನಿರ್ವಹಣಾ ವ್ಯವಸ್ಥೆ:** ಬಳಕೆದಾರ ಇನ್ಪುಟ್, LLM ಪ್ರತಿಕ್ರಿಯೆಗಳು, ಉಪಕರಣ ಕರೆಗೆ ಮತ್ತು ಫಲಿತಾಂಶಗಳಿಗೆ ನಡುವಿನ ಸಂವಾದ ಹರಿವನ್ನು ನಿರ್ವಹಿಸುವ ಘಟಕಗಳು.

- **ಉಪಕರಣ ಇಂಟಿಗ್ರೇಷನ್ ಫ್ರೇಮ್ವರ್ಕ್:** ಏಜೆಂಟ್ ಮತ್ತು ವಿಭಿನ್ನ ಉಪಕರಣಗಳನ್ನು ಸಂಪರ್ಕಿಸುವ ಮೂಲಸೌಕರ್ಯ, ಅವು ಸರಳ ಫಂಕ್ಷನ್ ಆಗಿರಬಹುದು ಅಥವಾ ಸಂಕೀರ್ಣ ಬಾಹ್ಯ ಸೇವೆಗಳಾದರೂ.

- **ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಮಾನ್ಯತೆ:** ಉಪಕರಣ ಕಾರ್ಯಗತಗೊಳಿಕೆಲ್ಲಾಗದು, ಪ್ಯಾರಾಮೀಟರ್ಗಳ ಮಾನ್ಯತೆ ಮತ್ತು ಅಪ್ರತ್ಯಾಶಿತ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಉಪಾಯಗಳು.

- **ಸ್ಥಿತಿ ನಿರ್ವಹಣೆ:** ಸಂವಾದದ ಪರಿಪ್ರೆಕ್ಷ್ಯ, ಹಿಂದಿನ ಉಪಕರಣ ಸಂವಹನ ಮತ್ತು ಸ್ಥಿರ ಡೇಟಾವನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ ಬಹು-ಪಟ್ಟು ಸಂವಹನಗಳಲ್ಲಿ ಸಮ್ಮತತೆಯನ್ನು ಖಚಿತಪಡಿಸುವುದು.

ಮುಂದೆ ನೋಡೋಣ ಫಂಕ್ಷನ್/ಉಪಕರಣ ಕರೆ ಬಗ್ಗೆ ವಿಶದವಾಗಿ.

### ಫಂಕ್ಷನ್/ಉಪಕರಣ ಕರೆ

ಫಂಕ್ಷನ್ ಕರೆ LLMಗಳಿಗೆ ಉಪಕರಣಗಳ ಜೊತೆ ಸಂವಹನ ಮಾಡಲು ಪ್ರಾಥಮಿಕ ವಿಧಾನವಾಗಿದೆ. ನೀವು ಶ್ರೇಯಸ್ಸಾಗಿ 'ಫಂಕ್ಷನ್' ಮತ್ತು 'ಉಪಕರಣ' ಎಂಬ ಪದಗಳನ್ನು ಪರಸ್ಪರ ಬದಲಾಯಿಸಿ ಬಳಸುವುದನ್ನು ಕಾಣಬಹುದು ಏಕೆಂದರೆ 'ಫಂಕ್ಷನ್‌ಗಳು' (ಮರುಬಳಕೆ ಮಾಡಲು ಸಾಧ್ಯವಾಗುವ ಕೋಡ್ ಬ್ಲಾಕ್ಗಳು) ಎಂದರೆ ಏಜೆಂಟ್‌ಗಳು ಕೆಲಸ ಮಾಡಲು ಉಪಯೋಗಿಸುವ 'ಉಪಕರಣಗಳು'. ಫಂಕ್ಷನ್‌ಗಳ ಕೋಡ್ ಅನ್ನು ಕರೆಮಾಡಲು, LLM ಬಳಕೆದಾರರ ವಿನಂತಿಯನ್ನು ಫಂಕ್ಷನ್ ವಿವರಣೆಯೊಂದಿಗೆ ಹೋಲಿಸಬೇಕು. ಇದಕ್ಕಾಗಿ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಫಂಕ್ಷನ್‌ಗಳ ವಿವರಣೆಗಳುಳ್ಳ ಒಂದು ವಿನ್ಯಾಸ LLMಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ. LLM ಆ ಕೆಲಸಕ್ಕೆ ಸೂಕ್ತವಾದ ಫಂಕ್ಷನ್ ಅನ್ನು ಆರಿಸಿ ಅದರ ಹೆಸರು ಮತ್ತು ತರ್ಕಗಳನ್ನು ಟಪ್ಪಿಸುತ್ತದೆ. ಆರಿಸಲಾದ ಫಂಕ್ಷನ್ ಕರೆಮಾಡಲಾಗುತ್ತದೆ ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯು LLMಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ, ಅದು ಮಾಹಿತಿ ಬಳಸಿಕೊಂಡು ಬಳಕೆದಾರರ ವಿನಂತಿಗೆ ಉತ್ತರ ಕೊಡುತ್ತದೆ.

ಡಿವೆಲಪರ್‌ಗೆ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಫಂಕ್ಷನ್ ಕರೆ ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಬೇಕಾಗಿರುವುದು:

1. ಫಂಕ್ಷನ್ ಕರೆ ಬೆಂಬಲಿಸುವ LLM ಮಾದರಿ
2. ಫಂಕ್ಷನ್ ವಿವರಣೆಗಳನ್ನು ಒಳಗೊಂಡ ವಿನ್ಯಾಸ
3. ಪ್ರತಿ ವಿವರಣೆಗೊಂಡ ಫಂಕ್ಷನ್‌ಗೆ ಕೋಡ್

ಈ ಉದಾಹರಣೆಗಾಗಿ, ನಗರದಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯ ಪಡೆಯುವುದನ್ನು ನೋಡಿ:

1. **ಫಂಕ್ಷನ್ ಕರೆ ಬೆಂಬಲಿಸುವ LLM ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ:**

   ಎಲ್ಲಾ ಮಾದರಿಗಳು ಫಂಕ್ಷನ್ ಕರೆ ಬೆಂಬಲಿಸುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ ಬಳಸುತ್ತಿರುವ LLM ಬೆಂಬಲಿಸುವುದೇ ಇಲ್ಲವೇ ಎಂದು ಪರಿಶೀಲಿಸಬೇಕು.  
   <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ಫಂಕ್ಷನ್ ಕರೆ ಬೆಂಬಲಿಸುತ್ತದೆ. ನಾವು Azure OpenAI ಕ್ಲೈಯೆಂಟ್ ಪ್ರಾರಂಭಿಸಬಹುದು.

    ```python
    # ಅಜೂರ್ ಓಪನ್‌ಎಐ ಕ್ಲೈಂಟ್ ಅನ್ನು ಆರಂಭಿಸಿ
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ಫಂಕ್ಷನ್ ವಿನ್ಯಾಸ ಸೃಷ್ಟಿಸಿ**:

   ಈಗ ನಾವು ಫಂಕ್ಷನ್ ಹೆಸರು, ಫಂಕ್ಷನ್ ಮಾಡುವ ಕೆಲಸದ ವರ್ಣನೆ, ಮತ್ತು ಫಂಕ್ಷನ್ ಪ್ಯಾರಾಮೀಟರ್ ಹೆಸರುಗಳು ಮತ್ತು ವಿವರಣೆಗಳ JSON ವಿನ್ಯಾಸವನ್ನು ನಿರೂಪಿಸುವುದು.  
   ಇದನ್ನು ಹಿಂದಿನ ಕ್ಲೈಯೆಂಟ್‌ಗೆ ಮತ್ತು ಬಳಕೆದಾರನು ಸೋಲಿರುವ ಸಮಯದ ಸ್ಥಳಕ್ಕಾಗಿ ವಿನಂತಿಯನ್ನು ಹಾಕಿ ಕಳುಹಿಸೋಣ. ಮುಖ್ಯವಾಗಿ ಗಮನಿಸಬೇಕಾದುದು, **ಉಪಕರಣ ಕರೆ** ಫಲಿತಾಂಶವಾಗಿ ಬರುತ್ತದೆ, ಪ್ರಶ್ನೆಗೆ ಅಂತಿಮ ಉತ್ತರವಲ್ಲ. ಮೊದಲೇ ಹೇಳಿದಂತೆ, LLM ಕಾರ್ಯಕ್ಕೆ ಆಯ್ಕೆಮಾಡಿದ ಫಂಕ್ಷನ್ ಹೆಸರು ಮತ್ತು ತರ್ಕಗಳನ್ನು ತರುತ್ತದೆ.

    ```python
    # ಮಾದರಿಗಾಗಿ ಓದುವ ಕಾರ್ಯ ವಿವರಣೆ
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
  
    # ಮೊದಲ API ಕರೆ: ಮಾದರಿಗೆ ಕಾರ್ಯವನ್ನು ಬಳಸಲು ಕೇಳಿ
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # ಮಾದರಿಯ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **ಕಾರ್ಯ ಚಟುವಟಿಕೆಯ ಫಂಕ್ಷನ್ ಕೋಡ್**:

   ಈಗ LLM ಆಯ್ಕೆಮಾಡಿದ ಫಂಕ್ಷನ್ ನಡೆಯಬೇಕಾಗಿದೆ, ಅದರ ಕೋಡ್ ಅನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಬೇಕು.  
   ನಾವು Python ನಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯವನ್ನು ಪಡೆಯಲು ಕೋಡ್ ಅನ್ನು ಬರೆಯಬಹುದು. ಉತ್ತರ ಸಂದೇಶದಿಂದ ಫಂಕ್ಷನ್ ಹೆಸರು ಮತ್ತು ತರ್ಕಗಳನ್ನು ತೆಗೆಯಲು ಕೋಡ್ ಕೂಡ ಬರೆಯಬೇಕು.

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
     # ಫಂಕ್ಷನ್ ಕರೆಗಳನ್ನು ನಿರ್ವಹಿಸಿ
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
  
      # ಎರಡನೇ API ಕರೆ: ಮಾದರಿಯಿಂದ ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯಿರಿ
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

ಫಂಕ್ಷನ್ ಕರೆ ಬಹುತೇಕ ಏಜೆಂಟ್ ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ನಿಧಾನದಲ್ಲಿ ಹೃದಯವಾಗಿದೆ, ಆದರೂ ಸದ್ದುಮಾಡುವುದು ಕೆಲವೊಮ್ಮೆ ಕಷ್ಟಕರವಾಗಬಹುದು.  
[ಪಾಠ 2](../../../02-explore-agentic-frameworks) ನಲ್ಲಿ ತಿಳಿದಂತಿದ್ದಂತೆ, ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಉಪಕರಣ ಬಳಕೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಪೂರ್ವನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.

## ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಉಪಕರಣ ಬಳಕೆ ಉದಾಹರಣೆಗಳು

ವಿಭಿನ್ನ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳನ್ನು ಉಪಯೋಗಿಸಿ ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಯನ್ನು ಹೇಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸಬಹುದು ಎಂಬ ಕೆಲವು ಉದಾಹರಣೆಗಳು ಇಲ್ಲಿವೆ:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> ನಮ್ಮ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಒಂದು ಮುಕ್ತ ಮೂಲ AI ಫ್ರೇಮ್ವರ್ಕ್. ಇದು ಫಂಕ್ಷನ್ ಕರೆ ಮಾಡುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಸರಳಗೊಳಿಸುತ್ತವೆ, ಉಪಕರಣಗಳನ್ನು Python ಫಂಕ್ಷನ್‌ಗಳಾಗಿ `@tool` ಅಲಂಕಾರವನ್ನು ಉಪಯೋಗಿಸಿ ನಿರೂಪಿಸಲು ಅನುಮತಿಸುತ್ತದೆ. ಫ್ರೇಮ್ವರ್ಕ್ ಮಾದರಿ ಮತ್ತು ನಿಮ್ಮ ಕೋಡ್ ನಡುವಿನ ಸಂವಹನವನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುತ್ತವೆ. ఇది `AzureAIProjectAgentProvider` ಮೂಲಕ ಫೈಲ್ ಸರ್ಚ್ ಮತ್ತು ಕೋಡ್ ಇಂಟರ್ಪ್ರೆಟರ್ ಮುಂತಾದ ಪೂರ್ವನಿರ್ಮಿತ ಉಪಕರಣಗಳಿಗೆ ಪ್ರವೇಶವನ್ನು ಒದಗಿಸುತ್ತದೆ.

ಕೆಳಗಿನ ಚಿತ್ರ Microsoft Agent Framework ಮೂಲಕ ಫಂಕ್ಷನ್ ಕರೆ ಮಾಡುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಚಿತ್ರಿಸುತ್ತದೆ:

![function calling](../../../translated_images/kn/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework ನಲ್ಲಿ, ಉಪಕರಣಗಳನ್ನು ಅಲಂಕಾರಿಸಿದ ಫಂಕ್ಷನ್‌ಗಳಾಗಿ ಘೋಷಿಸಲಾಗುತ್ತದೆ. ನಾವು ಮೊದಲು ನೋಡಿ ವೈಶಿಷ್ಟ್ಯ ಪಡೆದ `get_current_time` ಫಂಕ್ಷನ್ ಅನ್ನು `@tool` ಅಲಂಕಾರವನ್ನು ಉಪಯೋಗಿಸಿ ಉಪಕರಣವಾಗಿ ಪರಿವರ್ತಿಸಬಹುದು. ಫ್ರೇಮ್ವರ್ಕ್ ಫಂಕ್ಷನ್ ಮತ್ತು ಅದರ ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸರಣೀಕರಿಸಿ LLM ಗೆ ಕಳುಹಿಸುವ ವಿನ್ಯಾಸ ರಚಿಸುತ್ತದೆ.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ಗ್ರಾಹಕನನ್ನು ರಚಿಸಿ
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ಏಜೆಂಟ್ ಅನ್ನು ರಚಿಸಿ ಮತ್ತು ಸಾಧನದೊಂದಿಗೆ ಚಾಲನೆಮಾಡಿ
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ಹೊಸ ಏಜೆಂಟಿಕ್ ಫ್ರೇಮ್ವರ್ಕ್ ಆಗಿದ್ದು, ಡೆವಲಪರ್‌ಗಳಿಗಾಗಿ ಹೈ-ಕ್ವಾಲಿಟಿ, ವಿಸ್ತಾರಗೊಳ್ಳಬಹುದಾದ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಸುರಕ್ಷಿತವಾಗಿ ನಿರ್ಮಿಸಲು, ನಿಯೋಜಿಸಲು ಮತ್ತು ಮಾಪಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ, ಅಡಿಗಡಿ ಗಣನೆ ಮತ್ತು ಸಂಗ್ರಹಣಾ ಸಂಪನ್ಮೂಲಗಳನ್ನು ನಿರ್ವಹಿಸಬೇಕಾಗಿಲ್ಲ. ಇದು ವಿಶೇಷವಾಗಿ ಉದ್ಯಮ ಅನ್ವಯಿಕತೆಗಳಿಗೆ ಉಪಯುಕ್ತವಾಗಿದ್ದು, ಪೂರ್ಣವಾಗಿ ನಿರ್ವಹಿಸಲ್ಪಟ್ಟ ಸೇವೆ ಮತ್ತು ಉದ್ಯಮ ಗುಣಮಟ್ಟದ ಭದ್ರತೆಯನ್ನು ಒದಗಿಸುತ್ತದೆ.

ನೇರವಾಗಿ LLM API ಮೂಲಕ ಅಭಿವೃದ್ಧಿಗೊಳಿಸುವುದರೊಂದಿಗೆ ಹೋಲಿಸಿದಾಗ, Azure AI Agent Service ಕೆಲವು ಪ್ರಯೋಜನಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ, ಅವುಗಳಾಗಿವೆ:

- ಸ್ವಯಂಚಾಲಿತ ಉಪಕರಣ ಕರೆ – ಉಪಕರಣ ಕರೆಯಲು, ಅವುಗಳನ್ನು ಚಾಲನೆ ಮಾಡಲು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಿರ್ವಹಿಸಲು ಅಗತ್ಯವಿಲ್ಲ; ಎಲ್ಲವೂ ಸರ್ವರ್-ಮಟ್ಟದಲ್ಲಿ ನಡೆಯುತ್ತದೆ
- ಭದ್ರವಾಗಿ ನಿರ್ವಹಿಸಲಾದ ಡೇಟಾ – ನಿಮ್ಮ ಸ್ವಂತ ಸಂವಾದ ಸ್ಥಿತಿಯನ್ನು ನಿರ್ವಹಿಸಬೇಕಾಗಿಲ್ಲ, ನೀವು ಎಲ್ಲಾ ಮಾಹಿತಿಯನ್ನು ಸ್ಟೋರ್ ಮಾಡಲು ಥ್ರೆಡ್‌ಗಳ ಮೇಲೆ ಅವಲಂಬಿಸಬಹುದು
- ಪೂರ್ವನಿರ್ಮಿತ ಉಪಕರಣಗಳು – Bing, Azure AI Search ಮತ್ತು Azure Functions ಮುಂತಾದ ಡೇಟಾ ಮೂಲಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಉಪಕರಣಗಳನ್ನು ಬಳಸಬಹುದು.

Azure AI Agent Serviceನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳನ್ನು ಎರಡು ವರ್ಗಗಳಿಗೆ ವಿಂಗಡಿಸಬಹುದು:

1. ಜ್ಞಾನ ಉಪಕರಣಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ಮೂಲಕ ಗ್ರೌಂಡಿಂಗ್</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ಫೈಲ್ ಸರ್ಚ್</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. ಕಾರ್ಯ ಉಪಕರಣಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ಫಂಕ್ಷನ್ ಕರೆ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">ಕೋಡ್ ಇಂಟರ್ಪ್ರೆಟರ್</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI ವ್ಯಾಖ್ಯಾನಿತ ಉಪಕರಣಗಳು</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ಏಜೆಂಟ್ ಸೇವೆ ಈ ಉಪಕರಣಗಳನ್ನು `toolset` ಆಗಿ ಬಳಕೆ ಮಾಡಬಹುದು. ಇದು 또한 ಸಂವಾದದ ನಿರ್ದಿಷ್ಟ ಚರಿತ್ರೆಯನ್ನು ಸಂಗ್ರಹಿಸುವ `threads` ಅನ್ನು ಉಪಯೋಗಿಸುತ್ತದೆ.

ನೀವು Contoso ಎನ್ನುವ ಕಂಪನಿಯಲ್ಲಿ ಮಾರಾಟ ಏಜೆಂಟ್‌ ಎಂದು ಕಲ್ಪಿಸಿ. ನಿಮ್ಮ ಮಾರಾಟ ಡೇಟಾ ಕುರಿತು ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ನೀಡಬಲ್ಲ ಸಂವಹನ ಏಜೆಂಟ್ ಅನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸಲು ಬಯಸುತ್ತೀರಿ.

ಕೆಳಗಿನ ಚಿತ್ರವು Azure AI Agent Service ಬಳಸಿ ನಿಮ್ಮ ಮಾರಾಟ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ ಮಾಡುವುದನ್ನು ಚಿತ್ರಿಸುತ್ತದೆ:

![Agentic Service In Action](../../../translated_images/kn/agent-service-in-action.34fb465c9a84659e.webp)

ಈ ಸೇವೆಯೊಂದಿಗೆ ಯಾವುದೇ ಉಪಕರಣಗಳನ್ನು ಬಳಸಲು, ನಾವು ಕ್ಲೈಯೆಂಟ್ ಅನ್ನು ರಚಿಸಿ ಉಪಕರಣ ಅಥವಾ ಉಪಕರಣಸಂಕಲಪವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಬಹುದು. ಪ್ರಾಯೋಗಿಕ ಅನುಷ್ಠಾನಕ್ಕಾಗಿ ಕೆಳಗಿನ Python ಕೋಡ್ ಬಳಸಬಹುದು. LLM ಉಪಕರಣಸಂಕಲ್ಪವನ್ನು ನೋಡಿ ಬಳಕೆದಾರ ನಿರ್ಮಿಸಿದ `fetch_sales_data_using_sqlite_query` ಫಂಕ್ಷನ್ ಅಥವಾ ಪೂರ್ವನಿರ್ಮಿತ ಕೋಡ್ ಇಂಟರ್ಪ್ರೆಟರ್ ಅನ್ನು ಬಳಸಿ ನಿರ್ಧರಿಸುತ್ತದೆ.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ಫังก್ಷನ್ ಅನ್ನು fetch_sales_data_functions.py ಫೈಲ್‌ನಲ್ಲಿ ಕಂಡುಬರುತ್ತದೆ.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ಸಾಧನ ಸೆಟ್ ಆಗರೀಕರಿಸಿ
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ಫังก್ಷನ್ ಜೊತೆಗೆ ಫังก್ಷನ್ ಕರೆಯುವ ಏಜೆಂಟ್ ಅನ್ನು ಆಗರೀಕರಿಸಿ ಮತ್ತು ಅದನ್ನು ಸಾಧನ ಸೆಟ್‌ಗೆ ಸೇರಿಸಿ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# ಕೋಡ್ ವ್ಯಾಖ್ಯಾನಕರ ಸಾಧನವನ್ನು ಆಗರೀಕರಿಸಿ ಮತ್ತು ಅದನ್ನು ಸಾಧನ ಸೆಟ್‌ಗೆ ಸೇರಿಸಿ.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ವಿಶ್ವಾಸಾರ್ಹ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿ ಬಳಕೆಯ ವಿಶೇಷ ಪರಿಗಣನೆಗಳೇನು?

LLMಗಳಿಂದ ಗತಿಸುಡುಗೊಳಿಸಲಾದ SQLನ ಸಾದಾರಣ ದೂರು ಭದ್ರತೆ ಸಂಬಂಧಿತವಾಗಿದ್ದು, ವಿಶೇಷವಾಗಿ SQL ಇಂಜೆಕ್ಷನ್ ಅಥವಾ ದುಷ್ಟ ಕ್ರಿಯೆಗಳ ಅಪಾಯ, ಉದಾಹರಣೆಗೆ ಡೇಟಾಬೇಸ್ ಕುಸಿತ ಅಥವಾ ಅವನತಿ ಮಾಡುವಂತಹ ಅಪಾಯಗಳ ಕುರಿತು. ಈ ಆತಂಕಗಳು ಸತ್ಯವಾದರೂ, ಡೇಟಾಬೇಸ್ ಪ್ರವೇಶ ಅನುಮತಿಗಳನ್ನು ಸರಿ ರೀತಿಯಲ್ಲಿ ಸಂರಚಿಸುವ ಮೂಲಕ ಅವುಗಳನ್ನು ಪರಿಣಾಮಕಾರಿಯಾಗಿ ತಡೆಯಬಹುದು. ಹೆಚ್ಚಿನ ಡೇಟಾಬೇಸ್‌ಗಳಿಗೆ ಇದು ಓದುವ ಮೇಲೆ ಮಾತ್ರ ಪ್ರವೇಶ (read-only) ಸಿದ್ಧಪಡಿಸುವುದಾಗಿದೆ. PostgreSQL ಅಥವಾ Azure SQLಂತಹ ಡೇಟಾಬೇಸ್ ಸೇವೆಗಳಿಗೆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಓದುವ (SELECT) ಹಕ್ಕು ನೀಡಬೇಕು.

ಆಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಸುರಕ್ಷಿತ ಪರಿಸರದಲ್ಲಿ ಚಲಾಯಿಸುವುದರಿಂದ ರಕ್ಷಣೆ ಹೆಚ್ಚಾಗುತ್ತದೆ. ಉದ್ಯಮ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ, ಡೇಟಾ ಸಹಜವಾಗಿ ಕಾರ್ಯಾಚರಣಾ ವ್ಯವಸ್ಥೆಗಳಿಂದ ತೆಗೆದು ಓದುವ ಮಾತ್ರ ಡೇಟಾಬೇಸ್ಗೆ ಅಥವಾ ಡೇಟಾ ವರಹೌಸ್‌ಗೆ ಪರಿವರ್ತಿತಗೊಳ್ಳುತ್ತದೆ, ಮತ್ತು ಬಳಕೆದಾರ ಸ್ನೇಹಿ ವಿನ್ಯಾಸದಡಿ ಇರುತ್ತದೆ. ಈ ವಿಧಾನವು ಡೇಟಾವನ್ನು ಭದ್ರವಾಗಿದ್ದು, ಕಾರ್ಯಕ್ಷಮತೆ ಮತ್ತು ಪ್ರವೇಶದೃಷ್ಟಿಯಿಂದ ಸ್ವಲ್ಪವೆಂದು ಮಾಡುತ್ತದೆ ಮತ್ತು ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ನಿರ್ಬಂಧಿತ ಓದುವಲ್ಲದ ಪ್ರವೇಶವನ್ನು ನೀಡುತ್ತದೆ.

## ಮಾದರಿ ಕೋಡ್‌ಗಳು

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಮಾದರಿಗಳ ಬಗ್ಗೆ ಹೆಚ್ಚು ಪ್ರಶ್ನೆಗಳಿವೆಯೆ?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ಸೇರಿ ಇತರ ಕಲಿಯುವವರನ್ನು ಭೇಟಿಯಾಗಿರಿ, ಆಫೀಸ್ ժամдарға ಹಾಜರಾಗಿರಿ ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಗಳ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಪಡೆಯಿರಿ.

## ಹೆಚ್ಚು ಸಂಪನ್ಮೂಲಗಳು

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service ವರ್ಕ್‌ಶಾಪ್</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso ಸೃಜನಾತ್ಮಕ ಲೇಖಕರ ಬಹು ಏಜೆಂಟ್ ವರ್ಕ್‌ಶಾಪ್</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework ಅವಲೋಕನ</a>

## ಹಿಂದಿನ ಪಾಠ

[ಎಜೆಂಟಿಕ್ ವಿನ್ಯಾಸ ಮಾದರಿಗಳ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](../03-agentic-design-patterns/README.md)

## ಮುಂದಿನ ಪಾಠ
[ಎಜೆಂಟಿಕ್ RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಪವರ್ತನೆ**:
ಈ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುವರೂ, ಸ್ವಯಂಕ್ರಿಯ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ನೀರಾಷ್ಟ್ರಿತ ದಾಖಲೆವನ್ನು ಪ್ರಾಮಾಣಿಕ ಮೂಲ ಎಂದು ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಸಮಜುತಿ ಅಥವಾ ತಪ್ಪು ಅರ್ಥಕಲ್ಪನೆಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->