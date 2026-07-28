[![ಉತ್ತಮ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ಹೇಗೆ ವಿನ್ಯಾಸಗೊಳಿಸಬೇಕು](../../../translated_images/kn/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ಈ ಪಾಠದ ವೀಡಿಯೊವನ್ನು ವೀಕ್ಷಿಸಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸವನ್ನು ಪ್ಯಾಟರ್ನ್

ಉಪಕರಣಗಳು ಆಸಕ್ತಿಕರವಾಗಿವೆ ಏಕೆಂದರೆ ಅವು AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ವ್ಯಾಪಕವಾದ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನೀಡುತ್ತವೆ. ಏಜೆಂಟ್ ಸೀಮಿತ ಘಟಕಗಳನ್ನು ನಡೆಸುವ ಬದಲು, ಉಪಕರಣ ಸೇರಿಸುವ ಮೂಲಕ ಏಜೆಂಟ್ ಈಗ ವ್ಯಾಪಕ ಕ್ರಿಯೆಗಳನ್ನು ನಡೆಸಬಹುದು. ಈ ಅಧ್ಯಾಯದಲ್ಲಿ, ನಾವು ಟೂಲ್ಗಳನ್ನು ಬಳಸಿ ಗುರಿಗಳನ್ನು ಸಾಧಿಸುವ ವಿಧಾನಗಳನ್ನು ವಿವರಿಸುವ ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ನೋಡಿಕೊಳ್ಳೋಣ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ, ನಾವು ಕೆಳಗಿನ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದೇವೆ:

- ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಎಂದರೇನು?
- ಇದನ್ನು ಯಾವ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಗೆ ಅನ್ವಯ ಮಾಡಬಹುದೆ?
- ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಜಾರಿಗೆ ಅಗತ್ಯವಿರುವ ಅಂಶಗಳು/ನಿರ್ಮಾಣ ಘಟಕಗಳು ಯಾವುವು?
- ನಂಬಿಕೆಯಾರ್ಹ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಉಪಯೋಗಿಸುವ ವಿಶೇಷ ಪರಿಗಣನೆಗಳು ಯಾವುವು?

## ಕಲಿಕಾ ಗುರಿಗಳು

ಈ ಪಾಠವನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಸಾಧ್ಯವಾಗುವುದು:

- ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಮತ್ತು ಅದರ ಉದ್ದೇಶವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದು.
- ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಅನ್ವಯಿಸುವ ಬಳಕೆ ಪ್ರಕರಣಗಳನ್ನು ಗುರುತು ಮಾಡುವುದು.
- ಪ್ಯಾಟರ್ನ್ ಜಾರಿಗೆ ಅಗತ್ಯವಿರುವ ಮುಖ್ಯ ಅಂಶಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು.
- ಈ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಬಳಸಿದಾಗ AI ಏಜೆಂಟ್‌ಗಳ ನಂಬಿಕೆಯನ್ನು ಖಚಿತಪಡಿಸುವ ಪರಿಗಣನೆಗಳನ್ನು ಗುರುತಿಸುವುದು.

## ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಎಂದರೇನು?

**ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್** LLMಗಳಿಗೆ ಹೊರಗಿನ ಉಪಕರಣಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಬಲ್ಲ ಸಾಮರ್ಥ್ಯವನ್ನು ನೀಡುವುದರ ಮೇಲೆ ಕೇಂದ್ರೀಕರಿಸುತ್ತದೆ. ಉಪಕರಣಗಳು ಏಜೆಂಟ್ ಕಾರ್ಯಾಚರಣೆ ಮಾಡಲು ಚಾಲಿತವಾಗಬಹುದಾದ ಕೋಡ್ ಆಗಿವೆ. ಒಂದು ಉಪಕರಣವು ಲಘು ಕಾರ್ಯವಾಗಿರಬಹುದು, ಹೀಗಾಗಿ ಕ್ಯಾಲ್ಕ್ಯುಲೇಟರ್ ಅಥವಾ ಥರ್ಡ್-ಪಾರ್ಟಿ ಸೇವೆಗಳಿಗೆ API ಕರೆಗಳು (ಸ್ಟಾಕ್ ಬೆಲೆ ಪರಿಶೀಲನೆ ಅಥವಾ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆಗಳಂತಹ). AI ಏಜೆಂಟ್ ಗಳ ಸಂದರ್ಭದಲ್ಲಿ, ಉಪಕರಣಗಳನ್ನು **ಮಾಡೆಲ್-ತಯಾರಿಸಿದ ಕಾರ್ಯ ಕಾಲ್‌ಗಳು** ಮೂಲಕ ಏಜೆಂಟ್‌ಗಳು ನಿರ್ವಹಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ.

## ಇದನ್ನು ಯಾವ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಗೆ ಅನ್ವಯಿಸಬಹುದು?

AI ಏಜೆಂಟ್‌ಗಳು ಉಪಕರಣಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಸಂಕೀರ್ಣ ಕಾರ್ಯಗಳನ್ನು ಪೂರ್ಣಗೊಳಿಸಬಹುದು, ಮಾಹಿತಿ ಪಡೆಯಬಹುದು, ಅಥವಾ ನಿರ್ಧಾರಗಳನ್ನು ಮಾಡಬಹುದು. ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಹೆಚ್ಚಿನ ಸಂದರ್ಭಗಳಲ್ಲಿ ಬಾಹ್ಯ ವ್ಯವಸ್ಥೆಗಳಾಗಿ ಡೈನಾಮಿಕ್ ಸಂವಹನ ಅಗತ್ಯವಿರುವ ಸಂದರ್ಭಗಳಲ್ಲಿ ಬಳಸಲಾಗುತ್ತದೆ, ಉದಾ: ಡೇಟಾಬೇಸ್, ವೆಬ್ ಸೇವೆಗಳು ಅಥವಾ ಕೋಡ್ ವಿಶ್ಲೇಷಕಗಳು. ಇದು ಕೆಳಗಿನ ಅನೇಕ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಗೆ ಪ್ರಯೋಜನಕಾರಿಯಾಗಿರುತ್ತದೆ:

- **ಡೈನಾಮಿಕ್ ಮಾಹಿತಿ ಪಡೆಯುವುದು:** ಏಜೆಂಟ್‌ಗಳು ಬಾಹ್ಯದ APIಗಳು ಅಥವಾ ಡೇಟಾಬೇಸ್‌ಗಳಿಂದ ನವೀಕರಿಸಲಾದ ಮಾಹಿತಿಯನ್ನು ಪಡೆದುಕೊಳ್ಳಬಹುದು (ಉದಾ: SQLite ಡೇಟಾಬೇಸ್‌ನಲ್ಲಿ ವಿನ್ಯಾಸ ವಿಮರ್ಶೆಗಾಗಿ ವಿಚಾರಣೆ, ಸ್ಟಾಕ್ ಬೆಲೆಗಳ ಅಥವಾ ಹವಾಮಾನ ಮಾಹಿತಿಯ ಪಡೆಯುವುದು).
- **ಕೋಡ್ ನಿರ್ವಹಣೆ ಮತ್ತು ಅರ್ಥಮಾಡಿಕೆ:** ಏಜೆಂಟ್‌ಗಳು ಗಣಿತ ಸಮಸ್ಯೆಗಳನ್ನು ಬಗೆಹರಿಸಲು, ವರದಿಗಳನ್ನು ರಚಿಸಲು, ಅಥವಾ ಅನುಕರಣಗಳನ್ನು ನಡೆಸಲು ಕೋಡ್ ಅಥವಾ ಸ್ಕ್ರಿಪ್ಟ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸಬಹುದು.
- **ಕಾರ್ಯಪ್ರವಾಹ ಸ್ವಯಂಚಾಲಿತ:** ಕಾರ್ಯಗಳನ್ನು ಪುನರಾವರ್ತಿಸಲು ಅಥವಾ ಬಹು ಹಂತದ ಕಾರ್ಯಪಥಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಲು ಟಾಸ್ಕ್ ಶೆಡ್ಯೂಲರ್‌ಗಳು, ಇಮೇಲ್ ಸೇವೆಗಳು ಅಥವಾ ಡೇಟಾ ಪೈಪ್ಲೈನ್ ಗಳಂತಹ ಉಪಕರಣಗಳನ್ನು ಸಂಯೋಜಿಸುವುದು.
- **ಗ್ರಾಹಕ ಬೆಂಬಲ:** ಏಜೆಂಟ್‌ಗಳು CRM ವ್ಯವಸ್ಥೆಗಳು, ಟಿಕೆಟ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್‌ಗಳು ಅಥವಾ ಜ್ಞಾನಕೋಶಗಳಿಂದ ಬಳಕೆದಾರ ಪ್ರಶ್ನೆಗಳನ್ನು ಪರಿಹರಿಸಲು ಸಂವಹನ ನಡೆಸಬಹುದು.
- **ವಿಷಯ ರಚನೆ ಮತ್ತು ಸಂಪಾದನೆ:** ಏಜೆಂಟ್‌ಗಳು ವ್ಯಾಕರಣ ಪರಿಶೀಲಕರು, ಪಠ್ಯ ಸಾರಾಂಶಕಾರರು, ಅಥವಾ ವಿಷಯ ಸುರಕ್ಷತಾ ಮೌಲ್ಯಮಾಪಕರಂತಹ ಉಪಕರಣಗಳನ್ನ ಬಳಸಿ ವಿಷಯ ಸೃಷ್ಟಿ ಕೆಲಸಗಳಿಗೆ ಸಹಾಯ ಮಾಡಬಹುದು.

## ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಜಾರಿಗೆ ಅಗತ್ಯವಿರುವ ಅಂಶಗಳು/ನಿರ್ಮಾಣ ಘಟಕಗಳು ಯಾವುವು?

ಈ ನಿರ್ಮಾಣ ಘಟಕಗಳು AI ಏಜೆಂಟ್‌ಗೆ ಅಗತ್ಯವಿರುವ ವಿಸ್ತೃತ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ. ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಜಾರಿಗೆ ಅಗತ್ಯವಿರುವ ಪ್ರಮುಖ ಅಂಶಗಳನ್ನು ನೋಡೋಣ:

- **ಕಾರ್ಯ/ಉಪಕರಣ schemas**: ಲಭ್ಯವಿರುವ ಉಪಕರಣಗಳ ವಿವರವಾದ ವ್ಯಾಖ್ಯಾನಗಳು, ಕಾರ್ಯದ ಹೆಸರು, ಉದ್ದೇಶ, ಅಗತ್ಯವಾದ ಪರಿಮಾಣಗಳು ಮತ್ತು ನಿರೀಕ್ಷಿತ ಫಲಿತಾಂಶಗಳನ್ನು ಒಳಗೊಂಡಿದೆ. ಈ schemas LLMಗೆ ಯಾವ ಉಪಕರಣಗಳು ಲಭ್ಯವಿವೆ ಮತ್ತು ಮಾನ್ಯವಾದ ವಿನಂತಿಗಳನ್ನು ಹೇಗೆ ರಚಿಸುವುದು ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ನೆರವಾಗುತ್ತದೆ.

- **ಕಾರ್ಯ ನಿರ್ವಹಣೆ ತಂತ್ರಜ್ಞಾನ**: ಬಳಕೆದಾರರ ಉದ್ದೇಶ ಮತ್ತು ಸಂಭಾಷಣಾ ಪ್ರಸ್ತ Context ಆಧಾರದ ಮೇಲೆ ಉಪಕರಣಗಳನ್ನು ಯಾವಾಗ ಮತ್ತು ಹೇಗೆ ಕರೆ ಮಾಡುವುದು ಎಂಬುದನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ. ಇದರಲ್ಲಿ ಯೋಜಕ ಘಟಕಗಳು, ಮಾರ್ಗದರ್ಶನ ಯಂತ್ರಿಕೆಗಳು ಅಥವಾ ಶರತ್ತು ಪ್ರವರ್ತಿತ ಹರಿವುಗಳು ಇದು ಉಪಕರಣ ಬಳಕೆಯನ್ನು ಡೈನಾಮಿಕ್ ಆಗಿ ನಿರ್ಧರಿಸುವುದನ್ನು ಒಳಗೊಂಡಿರಬಹುದು.

- **ಸಂದೇಶ ನಿರ್ವಹಣೆ ವ್ಯವಸ್ಥೆ**: ಬಳಕೆದಾರ ಇನ್‌ಪುಟ್‌ಗಳು, LLM ಪ್ರತಿಕ್ರಿಯೆಗಳು, ಉಪಕರಣ ಕರೆಗಳು ಮತ್ತು ಉಪಕರಣ ಫಲಿತಾಂಶಗಳ ನಡುವೆ ಸಂಭಾಷಣಾ ಪ್ರವಾಹವನ್ನು ನಿರ್ವಹಿಸುವ ಘಟಕಗಳು.

- **ಉಪಕರಣ ಸಂಯೋಜನೆ ಚಟುವಟಿಕೆ**: ಏಜೆಂಟ್‌ಗಳು ವಿವಿಧ ಉಪಕರಣಗಳಿಗೆ ಸಂಪರ್ಕ ಹೊಂದಲು ಅನುಕೂಲಪಡಿಸುವ ಮೂಲಸೌಕರ್ಯಗಳು, ಅವು ಸರಳ ಕಾರ್ಯಗಳಾಗಿದ್ದರೂ ಅಥವಾ ಸಂಕೀರ್ಣ ಬಾಹ್ಯ ಸೇವೆಗಳಾಗಿದ್ದರೂ ಸಹ.

- **ದೋಷ ನಿರ್ವಹಣೆ ಮತ್ತು ಮಾನ್ಯತೆ**: ಉಪಕರಣ ಕಾರ್ಯಾಚರಣೆಯಲ್ಲಿ ವಿಫಲತೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ವಿಧಾನಗಳು, ಪರಿಮಾಣಗಳನ್ನು ಪರಿಶೀಲಿಸುವುದು, ಮತ್ತು ಅಪ್ರತ್ಯಕ್ಷ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವ ವ್ಯವಸ್ಥೆ.

- **ಸ್ಥಿತಿ ನಿರ್ವಹಣೆ**: ಸಂಭಾಷಣಾ ಪ್ರಸ್ತ Context ಗಳನ್ನು, ಪೂರ್ವ ಉಪಕರಣ ಸಂವಹನಗಳನ್ನು, ಮತ್ತು ಬಹು-ತಿರುಗು ಸಂವಹನಗಳಲ್ಲಿ ಸತತತೆಯನ್ನು ಖಚಿತಪಡಿಸಲು ಸದಾಕಾಲ ಡೇಟಾವನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡುತ್ತದೆ.

ಮುಂದಿನ ಭಾಗದಲ್ಲಿ, ಕಾರ್ಯ/ಉಪಕರಣ ಕರೆ ಕುರಿತು ಹೆಚ್ಚಿನ ವಿವರ ನೋಡೋಣ.
 
### ಕಾರ್ಯ/ಉಪಕರಣ ಕರೆ

ಕಾರ್ಯ ಕರೆ ಲಾರ್ಜ್ ಲ್ಯಾಂಗ್ವೇಜ್ ಮಾದರಿಗಳ (LLM) ಉಪಕರಣಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಪ್ರಾಥಮಿಕ ವಿಧಾನವಾಗಿದೆ. ನೀವು 'ಕಾರ್ಯ' ಮತ್ತು 'ಉಪಕರಣ' ಪದಗಳನ್ನು ಪರಿವರ್ತಿಸುವುದನ್ನು ಕಂಡಿರಬಹುದು ಏಕೆಂದರೆ 'ಕಾರ್ಯಗಳು' (ಪುನಃಬಳಕೆ ಮಾಡಬಹುದಾದ ಕೋಡ್ ಬ್ಲಾಕ್‌ಗಳು) ಎಂಬವು ಏಜೆಂಟ್‌ಗಳು ಕಾರ್ಯಗಳನ್ನು ನಿಭಾಯಿಸಲು ಬಳಸುವ 'ಉಪಕರಣಗಳಾಗಿವೆ'. ಕಾರ್ಯ ಕೋಡ್ ಅನ್ನು ಕರೆ ಮಾಡಲು, LLM ಬಳಕೆದಾರರ ವಿನಂತಿಯನ್ನು ಕಾರ್ಯ ವಿವರಣೆಯ ವಿರುದ್ಧ ಹೋಲಿಸಬೇಕು. ಇದಕ್ಕಾಗಿ ಎಲ್ಲ ಲಭ್ಯವಿರುವ ಕಾರ್ಯಗಳ ವಿವರಣೆಗಳನ್ನು ಒಳಗೊಂಡ schema ಅನ್ನು LLMಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ. ನಂತರ LLM ಸೂಕ್ತ ಕಾರ್ಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ ಅದರ ಹೆಸರು ಮತ್ತು ಆರ್ಗ್ಯೂಮೆಂಟುಗಳನ್ನು ನೀಡುತ್ತದೆ. ಆಯ್ಕೆಯಾದ ಕಾರ್ಯವನ್ನು ಕರೆಮಾಡಲಾಗುತ್ತದೆ, ಅದರ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು LLMಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ಅದು ಅದನ್ನು ಬಳಕೆದಾರರ ವಿನಂತಿಗೆ ಉತ್ತರಿಸಲು ಉಪಯೋಗಿಸುತ್ತದೆ.

ಕಾರ್ಯ ಕರೆ ಜಾರಿಗೆ ಡೆವಲಪರ್‌ಗಳಿಗೆ ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಬೇಕಾಗುತ್ತದೆ:

1. ಕಾರ್ಯ ಕರೆ ಸಪೋರ್ಟ್ ಮಾಡುವ LLM ಮಾದರಿ
2. ಕಾರ್ಯ ವಿವರಣೆಗಳನ್ನು ಒಳಗೊಂಡ schema
3. ಪ್ರತಿ ಕಾರ್ಯಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ಕೋಡ್

ನಗರದಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯವನ್ನು ಪಡೆಯುವ ಉದಾಹರಣೆಯನ್ನು ವಿವರಿಸಲು ಬಳಸೋಣ:

1. **ಕಾರ್ಯ ಕರೆ ಬೆಂಬಲಿಸುವ LLM ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ:**

    ಎಲ್ಲಾ ಮಾದರಿಗಳು ಕಾರ್ಯ ಕರೆ ಬೆಂಬಲಿಸುವುದಿಲ್ಲ, ಆದ್ದರಿಂದ ನೀವು ಬಳಸುವ LLM ಬೆಂಬಲಿತವೋ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸುವುದು ಮುಖ್ಯ. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">ಅಜ್ಯೂರ್ ಓಪನ್ ಏಐ</a> ಕಾರ್ಯ ಕರೆ ಬೆಂಬಲಿಸುತ್ತದೆ. ನಾವು OpenAI ಕ್ಲೈಂಟ್ ಅನ್ನು ಅಜ್ಯೂರ್ ಓಪನ್ ಏಐ **ಪ್ರತಿಕ್ರಿಯೆಗಳ API** ವಿರುದ್ಧ (ಸ್ಥಿರ `/openai/v1/` ಎಂಡ್‌ಪಾಯಿಂಟ್ — ಯಾವುದೇ `api_version` ಅಗತ್ಯವಿಲ್ಲ) ಪ್ರಾರಂಭಿಸಬಹುದು.

    ```python
    # ಆಜುರ್ ಓಪನ್ಎಐ (Responses API, v1 ಎಂಡ್‌ಪಾಯಿಂಟ್) ಗೆ ಓಪನ್ಎಐ ಕ್ಲೈಂಟ್ ಅನ್ನು ಮೂರು.Initialize ಮಾಡಿ
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **ಕಾರ್ಯ schema ರಚಿಸಿ**:

    ನಂತರ ಕಾರ್ಯದ ಹೆಸರು, ಕಾರ್ಯ ಯಾವುದು ಮಾಡುತ್ತದೆ ಎಂಬ ವಿವರಣೆ, ಕಾರ್ಯ ಪರಿಮಾಣಗಳ ಹೆಸರು ಮತ್ತು ವಿವರಣೆಗಳನ್ನು ಒಳಗೊಂಡ JSON schema ವ್ಯಾಖ್ಯಾನ ಮಾಡೋಣ. ಈ schema ಅನ್ನು ಪೂರ್ವದಲ್ಲಿಯೂ ರಚಿಸಿದ ಕ್ಲೈಂಟ್‌ಗೆ, ಮತ್ತು ಬಳಕೆದಾರರ 'San Francisco' ನಲ್ಲಿ ಸಮಯ ಕಂಡುಹಿಡಿಯಲು ಮಾಡಿರುವ ವಿನಂತಿಯೊಂದಿಗೆ ಕಳುಹಿಸುವುದು.
    ಮುಖ್ಯವಾಗಿ ಗಮನಿಸಬೇಕಾದುದು, **ಟೂಲ್ ಕಾಲ್** ಅನ್ನು ಹಿಂತಿರುಗಿಸಲಾಗುತ್ತದೆ, ಪ್ರಶ್ನೆಗೆ ಅಂತಿಮ ಉತ್ತರವಲ್ಲ. ಮೇಲ್ಪಟ್ಟಂತೆ, LLM ಆಯ್ಕೆಮಾಡಿದ ಕಾರ್ಯದ ಹೆಸರು ಮತ್ತು ಆರ್ಗ್ಯೂಮೆಂಟುಗಳನ್ನು ಹಿಂದಿರುಗಿಸುತ್ತದೆ.

    ```python
    # ಮಾದರಿಯು ಓದುವುದಕ್ಕಾಗಿ ಕಾರ್ಯ ವಿವರಣೆ (ಪ್ರತಿಕ್ರಿಯೆಗಳ API ಫ್ಲಾಟ್ ಟೂಲ್ ಫಾರ್ಮ್ಯಾಟ್)
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
  
    # ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಸಂದೇಶ
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # ಮೊದಲ API ಕರೆ: ಮಾದರಿಯಿಂದ ಫಂಕ್ಷನ್ ಬಳಕೆಯನ್ನು ಕೇಳಿ
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API ಫಂಕ್ಷನ್_ಕಾಲ್ ಐಟಂಗಳಾಗಿ ಟೂಲ್ ಕಾಳ್‌ಗಳನ್ನು response.output ನಲ್ಲಿ ಹಿಂತಿರುಗಿಸುತ್ತದೆ.
    # ಮುಂದಿನ ತಿರುವಿನಲ್ಲಿ ಮಾದರಿಯು ಸಂಪೂರ್ಣ ಪ್ರಚ್ಛೇದವನ್ನು ಹೊಂದಲು ಅವುಗಳನ್ನು ಸಂಭಾಷಣೆಗೆ ಸೇರಿಸಿ.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **ಕಾರ್ಯ ಕೋಡ್ ಕಾರ್ಯಾಚರಣೆಗಾಗಿ:**

    ಈಗ LLM ಆಯ್ಕೆ ಮಾಡಿದ ಕಾರ್ಯ ಕಾರ್ಯಗತಗೊಳ್ಳಬೇಕಾಗಿದ್ದರಿಂದ, ಅದನ್ನು ಕ್ರಿಯಾತ್ಮಕಗೊಳಿಸಿ ಚಾಲನೆ ಮಾಡಬೇಕು.
    ನಾವು Pythonನಲ್ಲಿ ಪ್ರಸ್ತುತ ಸಮಯ ಪಡೆಯುವ ಕೋಡ್ ಜಾರಿಗೆ ತರಬಹುದು. ಅಂತಿಮ ಫಲಿತಾಂಶ ಪಡೆಯಲು ಪ್ರತಿಕ್ರಿಯೆ_ಸಂದೇಶದಿಂದ ಹೆಸರು ಮತ್ತು ಆರ್ಗ್ಯೂಮೆಂಟ್‌ಗಳನ್ನು ತೆಗೆದುಹಾಕುವ ಕೋಡ್ ಕೂಡ ಬರೆಯಬೇಕು.

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
    # ಫังก್ಷನ್ ಕರೆಗೆ ಹ್ಯಾಂಡಲ್ ಮಾಡಿ
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # ಟೂಲ್ ಫಲಿತಾಂಶವನ್ನು function_call_output ಐಟಮ್ ретінде ಹಿಂತಿರುಗಿಸಿ
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # ಎರಡನೇ API ಕರೆ: ಮಾದರಿಯಿಂದ ಅಂತಿಮ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಪಡೆಯಿರಿ
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

ಕಾರ್ಯ ಕರೆ ಬಹುತೇಕ ಏಜೆಂಟ್ ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸದ ಹೃದಯವಾಗಿದೆ, ಆದರೆ ಅದನ್ನು ಪ್ರಾರಂಭದಿಂದ ಜಾರಿಗೊಳಿಸುವುದು ಕೆಲವೊಮ್ಮೆ ಸವಾಲಾಗಬಹುದು.
ನಾವು [ಪಾಠ 2](../../../02-explore-agentic-frameworks) ನಲ್ಲಿ ಕಲಿತಂತೆ ಏಜೆಂಟ್ ಚಟುವಟಿಕೆ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ಉಪಕರಣ ಬಳಕೆಗೆ ಪೂರ್ವನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.
 
## ಏಜೆಂಟ್ ಚಟುವಟಿಕೆ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಉಪಕರಣ ಬಳಕೆ ಉದಾಹರಣೆಗಳು

ಬಾಹ್ಯ ಏಜೆಂಟ್ ಚಟುವಟಿಕೆ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಅನ್ನು ಜಾರಿಗೆ ತರಬಹುದಾದ ಕೆಲವು ಉದಾಹರಣೆಗಳು:

### Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್</a> AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ತೆರವುಮುಖ AI ಫ್ರೇಮ್‌ವರ್ಕ್ ಆಗಿದೆ. ಇದು ಕಾರ್ಯ ಕರೆದುವಿಕೆಯನ್ನು ಸರಳಗೊಳಿಸುತ್ತದೆ ಮತ್ತು Python ಕಾರ್ಯಗಳನ್ನಾಗಿ ಉಪಕರಣವನ್ನು @tool ಅಲಂಕಾರದಿಂದ ಪ್ರತಿಪಾದಿಸುತ್ತದೆ. ಫ್ರೇಮ್‌ವರ್ಕ್ ಮಾದರಿ ಮತ್ತು ನಿಮ್ಮ ಕೋಡ್ ನಡುವೆ ಸಂವಹನ ನಿರ್ವಹಿಸುವುದನ್ನು ಕೈಗೊಂಡಿದೆ. ಇದು File Search ಮತ್ತು Code Interpreter ರೀತಿ ಪೂರ್ವ ನಿರ್ಮಿತ ಉಪಕರಣಗಳಿಗೂ `FoundryChatClient` ಮೂಲಕ ಪ್ರವೇಶ ನೀಡುತ್ತದೆ.

ಕೆಳಗಿನ ಚಿತ್ರ Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಜೊತೆಗೆ ಕಾರ್ಯ ಕರೆ ಪ್ರಕ್ರಿಯೆಯನ್ನು ವಿವರಿಸುತ್ತದೆ:

![function calling](../../../translated_images/kn/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ನಲ್ಲಿ, ಉಪಕರಣಗಳನ್ನು ಅಲಂಕರಿತ ಕಾರ್ಯಗಳಾಗಿ ವ್ಯವಹರಿಸಲ್ಪಡುತ್ತವೆ. ನಾವು ಮುಂದು ಹೇಳಿದ `get_current_time` ಕಾರ್ಯವನ್ನು ಉಪಕರಣವಾಗಿಸಲು `@tool` ಅಲಂಕಾರವನ್ನು ಬಳಸಿ ಪರಿವರ್ತಿಸಬಹುದು. ಫ್ರೇಮ್‌ವರ್ಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಾರ್ಯ ಹಾಗೂ ಅದರ ಪರಿಮಾಣಗಳನ್ನು ಸರಣೀಕರಿಸಿ LLMಗೆ schema ರಚಿಸುತ್ತದೆ.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# ಕ್ಲೈಂಟ್ ಅನ್ನು ರಚಿಸಿ
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ಏಜೆಂಟ್ ಅನ್ನು ರಚಿಸಿ ಮತ್ತು ಟೂಲ್‌ನೊಂದಿಗೆ ಚಲಾಯಿಸಿ
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry ಏಜೆಂಟ್ ಸೇವೆ

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry ಏಜೆಂಟ್ ಸೇವೆ</a> ಅಭಿವೃದ್ಧಿಪಡಕರಿಗೆ ಸುರಕ್ಷಿತವಾಗಿ ಉನ್ನತ ಗುಣಮಟ್ಟದ, ವ್ಯಾಪಕ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ವಹಣೆ ಹಾಗೂ ವಿಸ್ತಾರಗೊಳಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಿದ ಹೊಸ ಏಜೆಂಟ್ ಚಟುವಟಿಕೆಯ ಫ್ರೇಮ್‌ವರ್ಕ್. ಇದು ಮೂಲ ಕಂಪ್ಯೂಟ್ ಮತ್ತು ಸಂಗ್ರಹಣಾ ಸಂಪನ್ಮೂಲಗಳನ್ನು ನಿರ್ವಹಿಸದೆ ಮಾಡಲಾಗುತ್ತದೆ. ಇದು ಉದ್ಯಮ ಅನ್ವಯಗಳಿಗೆ ವಿಶೇಷ ಉಪಯುಕ್ತ, ಸಂಪೂರ್ಣ ನಿರ್ವಹಿತ ಸೇವೆ ಮತ್ತು ಉದ್ಯಮ ಮಟ್ಟದ ಭದ್ರತೆ ಒದಗಿಸುತ್ತದೆ.

LLM API ನೇರವಾಗಿ ಅಭಿವೃದ್ಧಿಗೊಳಿಸುವಿಕೆಯಿಂದ ಹೋಲಿಸಿದರೆ, Microsoft Foundry ಏಜೆಂಟ್ ಸೇವೆ ಕೆಲವು ಪ್ರಯೋಜನಗಳನ್ನು ನೀಡುತ್ತದೆ, ಅವುಗಳೆಂದರೆ:

- ಸ್ವಯಂಚಾಲಿತ ಉಪಕರಣ ಕರೆಯುವಿಕೆ – ಉಪಕರಣವನ್ನು ವಿಶ್ಲೇಷಿಸಿ, ಕರೆ ಮಾಡು, ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನಿರ್ವಹಿಸುವ ಅಗತ್ಯವಿಲ್ಲ; ಇದು ಈಗ ಸರ್ವರ್-ಬದಿಯಲ್ಲಿ ಆಗುತ್ತದೆ
- ಸುರಕ್ಷಿತವಾಗಿ ನಿರ್ವಹಿಸಲಾದ ಡೇಟಾ – ನಿಮ್ಮದೇ ಸಂಭಾಷಣಾ ಸ್ಥಿತಿಯನ್ನು ನಿರ್ವಹಿಸುವ ಬದಲು, ಎಲ್ಲಾ ಮಾಹಿತಿ ಸಂಗ್ರಹಿಸಲು ಥ್ರೆಡ್‌ಗಳು ಬಳಸಬಹುದು
- ಬೇಸರ ಇಲ್ಲದ ಉಪಕರಣಗಳು – Bing, Azure AI Search ಮತ್ತು Azure Functions ಮೇಲಿನ ಡೇಟಾ ಮೂಲಗಳೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಉಪಕರಣಗಳಿವೆ.

Microsoft Foundry ಏಜೆಂಟ್ ಸೇವೆಯ ಉಪಕರಣಗಳನ್ನು ಎರಡು ವರ್ಗಗಳಿಗೆ ವಿಭಜಿಸಬಹುದು:

1. ಜ್ಞಾನ ಉಪಕರಣಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search ನೊಂದಿಗೆ ಭೂಮಾಹಿತಿ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ಫೈಲ್ ಹುಡುಕಾಟ</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. ಕಾರ್ಯ ಉಪಕರಣಗಳು:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ಕಾರ್ಯ ಕಾಲ್</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">ಕೋಡ್ ಇಂಟರ್ಪ್ರೆಟರ್</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI ವ್ಯಾಖ್ಯಾನಿತ ಉಪಕರಣಗಳು</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ಏಜೆಂಟ್ ಸೇವೆಯು ಈ ಉಪಕರಣಗಳನ್ನು `toolset` ಆಗಿ ಬಳಕೆ ಮಾಡಲು ಅನುಮತಿಸುತ್ತದೆ. ಇದು ಸಂಭಾಷಣೆಯ ಸಂದೇಶಗಳ ಇತಿಹಾಸವನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡುವ `threads` ಅನ್ನು ಸಹ ಉಪಯೋಗಿಸುತ್ತದೆ.

Contoso ಎಂಬ ಕಂಪನಿಯ ಸೆಲ್ಸ್ ಏಜೆಂಟ್ ನೀವು ಇರುತ್ತೀರಂತೆ ಕಲ್ಪಿಸಿ. ನೀವು ನಿಮ್ಮ ಮಾರಾಟ ಡೇಟಾ ಕುರಿತು ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸುವ ಸಂಭಾಷಣಾ ಏಜೆಂಟ್‌ಗಳನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸಲು ಬಯಸುತ್ತೀರಿ.

ಕೆಳಗಿನ ಚಿತ್ರ Microsoft Foundry ಏಜೆಂಟ್ ಸೇವೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಸೆಲ್ಸ್ ಡೇಟಾವನ್ನು ವಿಶ್ಲೇಷಿಸುವ ವಿಧಾನವನ್ನು ತೋರಿಸುತ್ತದೆ:

![Agentic Service In Action](../../../translated_images/kn/agent-service-in-action.34fb465c9a84659e.webp)

ಸೇವೆಯೊಂದಿಗೆ ಯಾವುದೇ ಉಪಕರಣವನ್ನು ಬಳಸಲು ನಾವು ಕ್ಲೈಂಟ್ ಸೃಷ್ಟಿಸಿ ಉಪಕರಣ ಅಥವಾ ಉಪಕರಣಸಂಪುಟವನ್ನು ನಿರ್ಧರಿಸಬಹುದು. ಇದನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸಲು ಕೆಳಗಿನ Python ಕೋಡ್ ಬಳಸಿ. LLM ಉಪಕರಣಸಂಪುಟವನ್ನು ನೋಡಿ ಬಳಕೆದಾರರ ವಿನಂತಿ ಆಧಾರವಾಗಿ ಬಳಕೆದಾರ ಸೃಷ್ಟಿಸಿದ ಕಾರ್ಯವನ್ನು `fetch_sales_data_using_sqlite_query` ಅಥವಾ ಪೂರ್ವ-ನಿರ್ಮಿತ ಕೋಡ್ ಇಂಟರ್ಪ್ರೆಟರ್ ಅನ್ನು ಆರಿಸುತ್ತದೆ.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ಫಂಕ್ಷನ್ ಅನ್ನು fetch_sales_data_functions.py ಫೈಲಿನಲ್ಲಿ ಕಂಡುಹಿಡಿಯಬಹುದು.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# ಸಾಧನ ಸેટ್ ಪ್ರಾರಂಭಿಸಿ
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ಫಂಕ್ಷನ್ ಅನ್ನು ಫಂಕ್ಷನ್ ಕರೆ ಏಜೆಂಟ್‌ನೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಅದನ್ನು ಸಾಧನ ಸೆಟ್ಗೆ ಸೇರಿಸಿ
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# ಕೋಡ್ ಪ್ರಕಟಕಾರ ಸಾಧನವನ್ನು ಪ್ರಾರಂಭಿಸಿ ಮತ್ತು ಅದನ್ನು ಸಾಧನ ಸೆಟ್ಗೆ ಸೇರಿಸಿ.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## ನಂಬಿಕೆಯಾರ್ಹ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್ ಬಳಕೆಯ ವಿಶೇಷ ಪರಿಗಣನೆಗಳು ಯಾವುವು?

LLMಗಳಿಂದ ಡೈನಾಮಿಕ್ ಆಗ ನಿರ್ಮಾಣವಾಗುವ SQL ಬದಲಾಗಿ ಸಾಮಾನ್ಯ ಚಿಂತನೆ ಭದ್ರತೆ, ವಿಶೇಷವಾಗಿ SQL ಇಂಜೆಕ್ಷನ್ ಅಥವಾ ದುಷ್ಟ ಕ್ರಿಯೆಗಳ ಅಪಾಯ, ಉದಾ: ಡೇಟಾಬೇಸ್ ನಾಶ ಮಾಡುವುದು ಅಥವಾ ತಿದ್ದುವಿಕೆ. ಈ ಚಿಂತನೆಗಳಿಗೆ ಸಮಾಧಾನ ನೀಡಲು ಡೇಟಾಬೇಸ್ ಪ್ರವೇಶ ಅನುಮತಿಗಳನ್ನು ಸರಿಯಾಗಿ ಕಾನ್ಫಿಗರ್ ಮಾಡುವುದು ಪರಿಣಾಮಕಾರಿಯಾಗಿದೆ. ಬಹುತೇಕ ಡೇಟಾಬೇಸ್‌ಗಳಿಗಾಗಿ ಇದು ಡೇಟಾಬೇಸ್ಗೆ ಓದಲು ಮಾತ್ರ ಅನುಮತಿಯನ್ನು ಹೊಂದಿಸುವುದಾಗಿದೆ. PostgreSQL ಅಥವಾ Azure SQL ಸೇವೆಗಳಂತಹ ಡೇಟಾಬೇಸ್‌ಗಳಿಗಾಗಿ ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ಓದಲು ಮಾತ್ರ ವಹಿವಾಟಿನ (SELECT) ಪಾತ್ರ ನೀಡಲಾಗುತ್ತದೆ.

ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ಸುರಕ್ಷಿತ ಪರಿಸರದಲ್ಲಿ ನಡೆಸುವುದರಿಂದ ರಕ್ಷಣೆ ಹೆಚ್ಚಾಗುತ್ತದೆ. ಉದ್ಯಮ ಖಚಿತತೆಗಳಲ್ಲಿ, ಡೇಟಾ ಸಾಮಾನ್ಯವಾಗಿ ಕಾರ್ಯಾಚರಣಾ ವ್ಯವಸ್ಥೆಗಳಿಂದ ಹೊರಹಾಕಿ ಓದಿ-ಮಾತ್ರ ಡೇಟಾಬೇಸ್ ಅಥವಾ ಡೇಟಾ ಗೋದಾಮಿಗೆ ಪರಿವರ್ತಿಸಲಾಗುತ್ತದೆ. ಈ ವಿಧಾನ ಡೇಟಾಗೆ ಭದ್ರತೆ, ಕಾರ್ಯಕ್ಷಮತೆ ಹಾಗೂ ಪ್ರವೇಶ ಸುಲಭತೆ ನಿಶ್ಚಿತಪಡಿಸುತ್ತದೆ ಮತ್ತು ಅಪ್ಲಿಕೇಶನ್‌ಗೆ ನಿಯಂತ್ರಿತ ಓದುವ ಪ್ರವೇಶವಿದೆ.

## ಉದಾಹರಣಾ ಕೋಡ್‌ಗಳು

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ಉಪಕರಣ ಬಳಕೆ ವಿನ್ಯಾಸ ಪ್ಯಾಟರ್ನ್‌ಗಳ ಕುರಿತು ಮತ್ತಷ್ಟು ಪ್ರಶ್ನೆಗಳಿದೆಯೇ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ಗೆ ಸೇರಿ, ಇತರ ಕಲಿಯುವವರನ್ನು ಭೇಟಿಯಾಗಿ, ಆಫೀಸ್ ಗಂಟೆಗಳಲ್ಲಿ ಪಾಲ್ಗೊಳ್ಳಿ ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಪ್ರಶ್ನೆಗಳು ಉತ್ತರ ಪಡೆಯಿರಿ.

## ಮತ್ತಷ್ಟು ಸಂಪನ್ಮೂಲಗಳು

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service ಕಾರ್ಯಾಗಾರ</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso ಕ್ರಿಯೇಟಿವ್ ರೈಟರ್ ಮಲ್ಟಿ-ಏಜೆಂಟ್ ಕಾರ್ಯಾಗಾರ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಪರಿಚಯ</a>


## ಈ ಏಜೆಂಟ್‌ನ ಸ್ಮೋಕ್ಟೆಸ್ಟಿಂಗ್ (ऐच्छಿಕ)

ನೀವು [ಪಾಠ 16](../16-deploying-scalable-agents/README.md) ರಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿಯೋಜಿಸಲು ಕಲಿತ ಮೇಲೆ, ನೀವು ಈ ಪಾಠದ `TravelToolAgent` ಅನ್ನು ಸ್ಮೋಕ್ಟೆಸ್ಟ್ ಮಾಡಬಹುದು (ಇದು ಇನ್ನೂ ತನ್ನ ಉಪಕರಣಗಳನ್ನು ಕರೆದದೆ ಮತ್ತು ಉತ್ತರ ನೀಡುತ್ತದೆಯೇ?) ಇದಕ್ಕಾಗಿ [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) ಅನ್ನು ಬಳಸಬಹುದು. ಇದನ್ನು ಹೇಗೆ ಚಾಲನೆ ಮಾಡುವುದು ಎಂಬುದನ್ನು ನೋಡಲು [`tests/README.md`](../tests/README.md) ನೋಡಿ.

## ಹಿಂದಿನ ಪಾಠ

[ಎಜೆಂಟಿಕ್ ವಿನ್ಯಾಸ ಮಾದರಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](../03-agentic-design-patterns/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಎಜೆಂಟಿಕ್ RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->