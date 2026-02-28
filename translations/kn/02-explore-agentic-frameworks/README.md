[![AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳ ಅನ್ವೇಷಣೆ](../../../translated_images/kn/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ಈ ಪಾಠದ ವಿಡಿಯೋವನ್ನು ವೀಕ್ಷಿಸಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸಿ

AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು AI ಏಜೆಂಟ್‌ಗಳ ಸೃಷ್ಟಿ, ನಿಯೋಜನೆ ಮತ್ತು ನಿರ್ವಹಣೆಯನ್ನು ಸರಳಗೊಳಿಸಲು ರೂಪುಗೊಂಡ ಸಾಫ್ಟ್‌ವೇರ್ ವೇದಿಕೆಗಳು. ಇವು ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಪೂರ್ವನಿರ್ಮಿತ ಘಟಕಗಳು, ಅವುಗಳ ಮೇಲ್ತಳಗಳು ಮತ್ತು ಸಂಕಲನಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ, ಹಾಗೆಯೇ ಸಂಕೀರ್ಣ AI ವ್ಯವಸ್ಥೆಗಳ ಅಭಿವೃದ್ಧಿಯನ್ನು ಸುಲಭಗೊಳಿಸಲು ಉಪಕರಣಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.

ಈ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ಸಾಮಾನ್ಯ AI ಏಜೆಂಟ್ ಅಭಿವೃದ್ಧಿಯ ಸವಾಲುಗಳಿಗೆ ಮಾನಕೃತ ದೃಷ್ಠಿಕೋಣಗಳನ್ನು ಒದಗಿಸುವ ಮೂಲಕ ಅಭಿವೃದ್ಧಿದಾರರನ್ನು ಅವರ ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ವಿಶಿಷ್ಟ ಅಂಶಗಳ ಮೇಲೆ ಗಮನಹರಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ. ಇವು AI ವ್ಯವಸ್ಥೆಗಳ ನಿರ್ಮಾಣದಲ್ಲಿ ವ್ಯಾಪ್ತಿಯನ್ನು, ಪ್ರವೇಶಯುತತೆಯನ್ನು ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸುಧಾರಿಸುತ್ತವೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ಈ ವಿಷಯಗಳನ್ನು ವ್ಯಾಪಕವಾಗಿ ಚರ್ಚಿಸಲಾಗುವುದು:

- AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳೇನು ಮತ್ತು ಅವು ಅಭಿವೃದ್ಧಿದಾರರಿಗೆ ಏನು ಸಾಧಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ?
- ತಂಡಗಳು ಅವರ ಏಜೆಂಟ್‌ಗಳ ಸಾಮರ್ಥ್ಯವನ್ನು ಶೀಘ್ರವಾಗಿ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡುವುದು, ಪುನರಾವರ್ತನೆ ಮಾಡುವುದು ಮತ್ತು ಸುಧಾರಿಸುವುದಾಗಿ ಹೇಗೆ ಬಳಸಬಹುದು?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI ಏಜೆಂಟ್ ಸೇವೆ</a> ಮತ್ತು the <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್</a>) ರಚಿಸಿದ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳ ಮತ್ತು ಸಾಧನಗಳ ನಡುವೆ有什么 ವ್ಯತ್ಯಾಸಗಳಿವೆ?
- ನಾನು ನನ್ನ ಈಗಿನ Azure ಪರಿಸರದ ಸಾಧನಗಳನ್ನು ನೇರವಾಗಿ ಸಂಯೋಜಿಸಬಹುದೇ, ಅಥವಾ ಸ್ವತಂತ್ರ ಪರಿಹಾರಗಳ ಅವಶ್ಯಕತೆ ಇದೆಯೇ?
- Azure AI ಏಜೆಂಟ್ ಸೇವೆ ಎಂದರೆ ಏನು ಮತ್ತು ಇದು ನನಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡುತ್ತಿದೆ?

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠದ ಗುರಿಗಳು ನಿಮಗೆ ಅರ್ಥಮಾಡಿಸಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುವುದು:

- AI ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳ ಪಾತ್ರ.
- ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳನ್ನು ಹೇಗೆ ಉಪಯೋಗಿಸುವುದು.
- AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳಿಂದ ಸಕ್ರಿಯಗೊಳ್ಳುವ ಪ್ರಮುಖ ಸಾಮರ್ಥ్యಗಳು.
- Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಮತ್ತು Azure AI ಏಜೆಂಟ್ ಸೇವೆಯ ನಡುವಿನ ವ್ಯತ್ಯಾಸಗಳು.

## AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ಎಂದರೆ ಏನು ಮತ್ತು ಅವು ಅಭಿವೃದ್ಧಿದಾರರಿಗೆ ಏನು ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ?

ಚಾರಿತ್ರಿಕ AI ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೂ AI ಸಂಯೋಜಿಸಲು ಹಾಗೂ ಈ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಕೆಳಗಿನ ರೀತಿಯಲ್ಲಿ ಉತ್ತಮಗೊಳಿಸಲು ಸಹಾಯ ಮಾಡಬಹುದು:

- **ವ್ಯಕ್ತಿಗತೀಕರಣ**: AI ಬಳಕೆದಾರರ ವರ್ತನೆ ಮತ್ತು ಮೆಚ್ಚುಗೆಯನ್ನು ವಿಶ್ಲೇಷಿಸಿ ವೈಯಕ್ತಿಕ荐 ಶಿಫಾರಸು, ವಿಷಯ ಮತ್ತು ಅನುಭವಗಳನ್ನು ಒದಗಿಸಬಹುದು.
ಉದಾಹರಣೆ: Netflixಂಥ ಸ್ಟ್ರೀಮಿಂಗ್ ಸೇವೆಗಳು ವೀಕ್ಷಣಾ ಇತಿಹಾಸದ ಆಧಾರದ ಮೇಲೆ ಚಲನಚಿತ್ರಗಳು ಮತ್ತು ಶೋಗಳನ್ನು ಸೂಚಿಸಲು AI ಬಳಸುತ್ತವೆ, ಬಳಕೆದಾರರ ತೊಡಗಿಸಿಕೊಡು ಮತ್ತು ತೃಪ್ತಿಯನ್ನು ಹೆಚ್ಚಿಸಿ.
- **ದಿನನಿತ್ಯ automatisation ಮತ್ತು ದಕ್ಷತೆ**: AI ಪುನರಾವರ್ತಿತ ಕಾರ್ಯಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಿ, ಕೆಲಸದ ಪ್ರವಾಹಗಳನ್ನು ಸರಳಗೊಳಿಸಿ ಮತ್ತು ಕಾರ್ಯಾಚರಣಾತ್ಮಕ ದಕ್ಷತೆಯನ್ನು ಸುಧಾರಿಸಬಹುದು.
ಉದಾಹರಣೆ: ಗ್ರಾಹಕ ಸೇವಾ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಸಾಮಾನ್ಯ ವಿಚಾರಣೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು AI ಚಾಲಿತ ಚಾಟ್‌ಬಾಟ್‌ಗಳನ್ನು ಬಳಸುತ್ತವೆ, ಪ್ರತಿಕ್ರಿಯಾ ಕಾಲವನ್ನು ಕಡಿಮೆ ಮಾಡಿ ಮಾನವ ಏಜೆಂಟ್‌ಗಳನ್ನು ಜಟಿಲ ಸಮಸ್ಯೆಗಳಿಗಾಗಿ ಮುಕ್ತಗೊಳಿಸುತ್ತವೆ.
- **ಉತ್ತರದಾಯಕ ಬಳಕೆದಾರ ಅನುಭವ**: ಧ್ವನಿ ಗುರುತಿಸುವಿಕೆ, ನೈಸರ್ಗಿಕ ಭಾಷಾ ಪ್ರಕ್ರಿಯೆ ಮತ್ತು ಕ್ರಮ ನಿರ್ಧಾರವನ್ನು ಮುನ್ನೋಟಿಸುವ ಪಠ್ಯದಂತಹ ಬುದ್ದಿವಂತ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಒದಗಿಸುವ ಮೂಲಕ AI ಒಟ್ಟು ಬಳಕೆದಾರ ಅನುಭವವನ್ನು ಸುಧಾರಿಸಬಹುದು.
ಉದಾಹರಣೆ: Siri ಮತ್ತು Google Assistant ಮೊದಲಾದ ವರ್ಚುಯಲ್ ಸಹಾಯಕರಲ್ಲಿ AI ಬಳಸಿ ಧ್ವನಿ ಆದೇಶಗಳನ್ನು ಅರ್ಥಮಾಡಿ ಪ್ರತಿಕ್ರಿಯಿಸುವುದು, ಬಳಕೆದಾರರಿಗೆ ಸಾಧನಗಳೊಂದಿಗೆ ಸಂವಹನವನ್ನು ಸುಲಭಗೊಳಿಸುತ್ತದೆ.

### ಎಲ್ಲವೂ ಚೆನ್ನಾಗಿಯೇ ಇದೆಯೆಂದು ತೋರುತ್ತದೆ, ಆದರೂ AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ಬೇಕಾದುದೇಕೆ?

AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ಸಾಮಾನ್ಯ AI ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳಿಗಿಂತ ಹೆಚ್ಚಿನುದನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತವೆ. ಇವು ಬಳಕೆದಾರರು, ಇತರ ಏಜೆಂಟ್‌ಗಳು ಮತ್ತು ಪರಿಸರದೊಂದಿಗೆ ಸಂವಹನ ನಡೆಸಿ ನಿರ್ದಿಷ್ಟ ಗತಿ ಪ್ರಾಪ್ತಿಗೊಳಿಸಲು ಬಲ್ಲ ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ. ಈ ಏಜೆಂಟ್‌ಗಳು ಸ್ವಾಯತ್ತ ನಡೆದುಕೊಳ್ಳಬಲ್ಲವು, ನಿರ್ಧಾರಗಳನ್ನು ಕೈಗೊಳ್ಳಬಹುದು ಮತ್ತು ಬದಲಾಗುತ್ತಿರುವ ಪರಿಸ್ಥಿತಿಗೆ ಹೊಂದಿಕೊಳ್ಳಬಹುದು. AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ಸಕ್ರಿಯಗೊಳಿಸುವ ಪ್ರಮುಖ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನೋಡುವುದಕ್ಕೆ ಬನ್ನಿ:

- **ಏಜೆಂಟ್ ಸಹಯೋಗ ಮತ್ತು ಸಂಯೋಜನೆ**: ಜಟಿಲ ಕಾರ್ಯಗಳನ್ನು ಪರಿಹರಿಸಲು ಪರಸ್ಪರ ಕೆಲಸ ಮಾಡಬಹುದಾದ, ಸಂವಹನ ನಡೆಸಬಹುದಾದ ಮತ್ತು ಸಂಯೋಜಿಸಬಹುದಾದ ಹಲವು AI ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.
- **ಕಾರ್ಯ ಸ್ವಯಂಚಾಲನೆ ಮತ್ತು ನಿರ್ವಹಣೆ**: ಬಹು ಹಂತದ ಕಾರ್ಯಪ್ರವಾಹಗಳು, ಕಾರ್ಯ ವಹಿಸಲು ಹಂಚಿಕೆ ಮತ್ತು ಏಜೆಂಟ್‌ಗಳ ಮಧ್ಯೆ ಡೈನಾಮಿಕ್ ಕಾರ್ಯ ನಿರ್ವಹಣೆಯಿಗಾಗಿ ಯಂತ್ರಗತ ವ್ಯವಸ್ಥೆಗಳ ಒದಗಿಸು.
- **ಸಂದರ್ಭಾಧಾರಿತ ಅರ್ಥಮಾಡಿಕೆ ಮತ್ತು ಹೊಂದಿಕೆ**: ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸಂದರ್ಭವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ, ಬದಲಾಗುತ್ತಿರುವ ಪರಿಸರಕ್ಕೆ ಹೊಂದಿಕೊಳ್ಳುವ ಮತ್ತು ನೈರುತ್ಯ ಮಾಹಿತಿ ಆಧಾರದ ಮೇಲೆ ನಿರ್ಧಾರಗಳನ್ನು ಕೈಗೊಳ್ಳುವ ಸಾಮರ್ಥ್ಯವನ್ನು ಒದಗಿಸುತ್ತದೆ.

ಸಾರಾಂಶವಾಗಿ, ಏಜೆಂಟ್‌ಗಳು ಸ್ವಯಂಚಾಲನೆಯನ್ನು ಮುಂದಿನ ಹಂತಕ್ಕೆ ತೆಗೆದುಕೊಂಡು ಹೋಗಲು, ಪಾರಂಪರಿಕautomation ಗಿಂತ ಹೆಚ್ಚು ಮಾಡಲು, ಪರಿಸರದಿಂದ ಕಲಿಯಲು ಮತ್ತು ಹೊಂದಿಕೊಳ್ಳುವ ಹೆಚ್ಚು ಬುದ್ಧಿವಂತ ವ್ಯವಸ್ಥೆಗಳನ್ನು ರಚಿಸಲು ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತವೆ.

## ಏಜೆಂಟ್‌ನ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಶೀಘ್ರವಾಗಿ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡುವುದು, ಪುನರಾವರ್ತನೆ ಮಾಡುವುದು ಮತ್ತು ಸುಧಾರಿಸುವುದು ಹೇಗೆ?

ಇದು ವೇಗವಾಗಿ ಬದಲಾಗುವ ವಲಯ, ಆದರೆ ಬಹುತೇಕ AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳಲ್ಲಿ ಶೀಘ್ರ ಪ್ರೋಟೋಟೈಪಿಂಗ್ ಮತ್ತು ಪುನರಾವರ್ತನೆಗೆ ಸಹಾಯಮಾಡುವ ಕೆಲವು ಸಾಮಾನ್ಯ ಅಂಶಗಳಿವೆ: ಘಟಕ-ಆಧಾರಿತ ಕಂಪೋನೆಂಟ್‌ಗಳು, ಸಹಕಾರ ಸಾಧನಗಳು ಮತ್ತು ರಿಯಲ್-ಟೈಮ್ ಲರ್ನಿಂಗ್. ಮುಂದೆ ಇದು ಹೇಗೆ ಎಂದು ನೋಡೋಣ:

- **ಘಟಕ-ಆಧಾರಿತ ಕಂಪೋನೆಂಟ್‌ಗಳನ್ನು ಬಳಸಿ**: AI SDKಗಳು AI ಮತ್ತು ಮೆಮೊರಿ ಸಂಪರ್ಕಕರು, ಕಾರ್ಯ ಕರೆಗಳನ್ನು ನೈಸರ್ಗಿಕ ಭಾಷೆ ಅಥವಾ ಕೋಡ್ ಪ್ಲಗಿನ್‌ಗಳ ಮೂಲಕ ನಡೆಸುವಿಕೆ, ಪ್ರಾಂಪ್ಟ್ ಟೆಂಪ್ಲೇಟ್ಗಳು ಮತ್ತು ಇನ್ನಿತರ ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.
- **ಸಹಕಾರ ಸಾಧನಗಳನ್ನು ಪ್ರಯೋಜನದುಂಟುಮಾಡಿ**: ನಿರ್ದಿಷ್ಟ ಪಾತ್ರಗಳು ಮತ್ತು ಕಾರ್ಯಗಳನ್ನು ಹೊಂದಿರುವ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ, ಅವುಗಳು ಸಹಯೋಗ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ಸುಧಾರಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.
- **ರಿಯಲ್-ಟೈಮ್‌ನಲ್ಲಿ ಕಲಿತುಕೊಳ್ಳಿ**: ಏಜೆಂಟ್‌ಗಳು ಸಂವಾದದಿಂದ ಕಲಿಯುವ ಮತ್ತು ಅವರ ವರ್ತನೆಯನ್ನು ಡೈನಾಮಿಕ್ ಆಗಿ ಹೊಂದಿಸುವ ಫೀಡ್‌ಬಾಕ್ ಲೂಪ್‌ಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ.

### ಘಟಕ-ಆಧಾರಿತ ಕಂಪೋನೆಂಟ್‌ಗಳನ್ನು ಬಳಸಿ

Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಮಾದರಿಯ SDKಗಳು AI ಸಂಪರ್ಕಕರು, ಸಾಧನ ಪರಿನಿರ್ಧಾರಗಳು ಮತ್ತು ಏಜೆಂಟ್ ನಿರ್ವಹಣೆಯಂತಹ ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು ನೀಡುತ್ತವೆ.

**ತಂಡಗಳು ಇವುಗಳನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು**: ತಂಡಗಳು ಈ ಘಟಕಗಳನ್ನು ಮುಂಬಯದಿಂದಲೇ ಸಂಯೋಜಿಸಿ ಮೂಲಭೂತ ಕಾರ್ಯಾಚರಣಾತ್ಮಕ ಪ್ರೋಟೋಟೈಪ್ ಅನ್ನು ಶೀಘ್ರವಾಗಿ ರಚಿಸಬಹುದು, ಇದರಿಂದ ಪ್ರಯೋಗ ಮತ್ತು ಪುನರಾವರ್ತನೆ ವೇಗವಾಗಿ ಸಾಧ್ಯವಾಗುತ್ತದೆ.

**ಅಭ್ಯಾಸದಲ್ಲಿ ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆಯೆಂದು**: ಬಳಕೆದಾರ ಇನ್‌ಪುಟ್‌ನಿಂದ ಮಾಹಿತಿ ತೆಗೆದುಹಿಡಿಯಲು ಪೂರ್ವ-ನಿರ್ಮಿತ ಪಾರ್ಸರ್ ಅನ್ನು ಬಳಸಬಹುದು, ಡೇಟಾ ಸಂಗ್ರಹಿಸಲು ಮತ್ತು ಪಡೆಯಲು ಮೆಮೊರಿ ಮೋಡ್ಯೂಲ್ ಉಪಯೋಗಿಸಬಹುದು ಮತ್ತು ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಹನಕ್ಕೆ ಪ್ರಾಂಪ್ಟ್ ಜನರೇಟರ್ ಅನ್ನು ಬಳಸಬಹುದು — ಇವೆಲ್ಲವೂ ಸೊಟ್ಟಿಯಿಂದ ನಿರ್ಮಿಸಲಾಗುವುದಿಲ್ಲದೇ.

**ಉದಾಹರಣೆಯ ಕೋಡ್**. Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಅನ್ನು `AzureAIProjectAgentProvider` ಬಳಸಿ ಯೂಸರ್ ಇನ್‍ಪುಟ್‌ಗೆ ಟೂಲ್ ಕರೆ ಮಾಡುವ ಮೂಲಕ ಮಾದರಿಯನ್ನು ಪ್ರತಿಕ್ರಿಯಿಸಲು ಹೇಗೆ ಬಳಸಲು ಸಾಧ್ಯವೆಂದು ಕೆಳಗಿನ ಉದಾಹರಣೆಯನ್ನು ನೋಡೋಣ:

``` python
# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಪೈಥಾನ್ ಉದಾಹರಣೆ

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# ಪ್ರಯಾಣ ಬುಕ್ ಮಾಡಲು ನಮೂನೆಯಾ ಟೂಲ್ ಫಂಕ್ಷನ್ ಅನ್ನು ನಿರ್ವಚಿಸಿ
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # ಉದಾಹರಣೆ ಔಟ್‌ಪುಟ್: ಜನವರಿ 1, 2025ರಂದು ನ್ಯೂಯಾರ್ಕ್‌ಗೆ ನಿಮ್ಮ ವಿಮಾನ ಯಶಸ್ವಿಯಾಗಿ ಬುಕ್ ಮಾಡಲಾಗಿದೆ. ಸುರಕ್ಷಿತ ಪ್ರಯಾಣ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ಈ ಉದಾಹರಣೆಯಿಂದ ನಿಮಗೆ ಕಾಣಿಸುವುದು, ಬಳಕೆದಾರ ಇನ್‌ಪುಟ್‌ನಿಂದ ಉದ್ಗಮ, ಗಮ್ಯ ಮತ್ತು ದಿನಾಂಕದಂತಹ ಪ್ರಮುಖ ಮಾಹಿತಿಯನ್ನು ತೆಗೆದುಹಿಡಿಯಲು ಪೂರ್ವ-ನಿರ್ಮಿತ ಪಾರ್ಸರ್ ಅನ್ನು ಹೇಗೆ ಉಪಯೋಗಿಸಬಹುದು ಎಂಬುದಾಗಿದೆ. ಈ ಘಟಕೀಕೃತ ಕ್ರಮವು ನಿಮಗೆ ಉನ್ನತ-ಮಟ್ಟದ ತರ್ಕದ ಮೇಲೆ ಗಮನ ಕೇಂದ್ರಗೊಳಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ.

### ಸಹಕಾರ ಸಾಧನಗಳನ್ನು ಪ್ರಯೋಜನದುಂಟುಮಾಡಿ

Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಮುಂತಾದ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ಪಾರಸ್ಪರ ಸಹಯೋಗಕ್ಕೆ ಯೋಗ್ಯವಾದ ಹಲವೊಂದು ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ಅನುಕೂಲವಾಗುವಂತೆ ಮಾಡುತ್ತವೆ.

**ತಂಡಗಳು ಇವುಗಳನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು**: ತಂಡಗಳು ನಿರ್ದಿಷ್ಟ ಪಾತ್ರಗಳು ಮತ್ತು ಕಾರ್ಯಗಳನ್ನು ಹೊಂದುವಂತೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ, ಸಹಕಾರ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ಸುಧಾರಿಸಲು ಮತ್ತು ಒಟ್ಟಾರೆ ವ್ಯವಸ್ಥೆಯ ದಕ್ಷತೆಯನ್ನು ಉತ್ತೇಜಿಸಲು ಸಹಾಯ ಮಾಡಬಹುದು.

**ಅಭ್ಯಾಸದಲ್ಲಿ ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ಪ್ರತಿ ಏಜೆಂಟ್ ವಿಶೇಷ ಕಾರ್ಯವನ್ನು ನಡೆಸುವಂತೆ (ಮಾಹಿತಿ ಹಿಂಪಡೆಯುವುದು, ವಿಶ್ಲೇಷಣೆ, ಅಥವಾ ನಿರ್ಧಾರ-ಗೊಳ್ಳುವಿಕೆ) ತಂಡವೊಂದು ರಚಿಸಬಹುದು. ಈ ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನ ನಡೆಸಿ ಮಾಹಿತಿ ಹಂಚಿಕೊಳ್ಳಿ ಸಾಮಾನ್ಯ ಗುರಿಯನ್ನು ಸಾಧಿಸಬಹುದು, ಉದಾಹರಣೆಗೆ ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗೆ ಉತ್ತರವಿಸ್ತಾರ ನೀಡುವುದು ಅಥವಾ ಕಾರ್ಯವನ್ನು ಪೂರ್ಣಗೊಳಿಸುವುದು.

**ಉದಾಹರಣೆಯ ಕೋಡ್ (Microsoft Agent Framework)**:

```python
# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ ಒಂದಾಗಿ ಕೆಲಸಮಾಡುವ ಹಲವಾರು ಏಜೆಂಟ್ಗಳನ್ನು ರಚಿಸುವುದು

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ಡೇಟಾ ಸಂಗ್ರಹಣಾ ಏಜೆಂಟ್
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ ಏಜೆಂಟ್
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ಕಾರ್ಯದಲ್ಲಿ ಏಜೆಂಟ್ಗಳನ್ನು ಕ್ರಮವಾಗಿ ಚಲಿಸು
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನೀವು ನೋಡಿರುವುದಾಗಿದ್ದು, ಡೇಟಾವನ್ನು ವಿಶ್ಲೇಷಿಸಲು ಸಹಕರಿಸುವ ಬಹು ಏಜೆಂಟ್‌ಗಳನ್ನು ಒಳಗೊಂಡ ಕಾರ್ಯವನ್ನು ನೀವು ಹೇಗೆ ರಚಿಸಬಹುದು ಎಂಬುದಾಗಿದೆ. ಪ್ರತಿ ಏಜೆಂಟ್ ಒಂದು ವಿಶಿಷ್ಟ ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಮತ್ತು ನಿರೀಕ್ಷಿತ ಫಲಿತಾಂಶವನ್ನು ಸಾಧಿಸಲು ಏಜೆಂಟ್‌ಗಳ ಸಂಯೋಜನೆಯ ಮೂಲಕ ಕಾರ್ಯ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ. ವಿಶೇಷ ಪಾತ್ರಗಳೊಂದಿಗೆ ಸಮರ್ಪಿತ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವ ಮೂಲಕ, ನೀವು ಕಾರ್ಯ ದಕ್ಷತೆ ಮತ್ತು ಸಾಮರ್ಥ್ಯವನ್ನು ಸುಧಾರಿಸಬಹುದಾಗಿದೆ.

### ರಿಯಲ್-ಟೈಮ್‌ನಲ್ಲಿ ಕಲಿಯಿರಿ

ಅಧುನಿಕ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳು ರಿಯಲ್-ಟೈಮ್ ಸಂದರ್ಭ ಅರ್ಥಮಾಡಿಕೆ ಮತ್ತು ಹೊಂದಿಕೆಗೆ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.

**ತಂಡಗಳು ಇವುಗಳನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು**: ತಂಡಗಳು ಫೀಡ್‌ಬ್ಯಾಕ್ ಲೂಪ್‌ಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ, ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನಗಳಿಂದ ಕಲಿಯುತ್ತಾ ಅವರ ವರ್ತನೆಯನ್ನು ಡೈನಾಮಿಕ್‌ ಆಗಿ ಹೊಂದಿಸಿಕೊಳ್ಳುತ್ತಾರೆ, ಇದರಿಂದ ಒಂದರ ಹತ್ತಿರ ನಿರಂತರ ಸುಧಾರಣೆ ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳ ಕ್ಷೇಮ ಸಂಭವಿಸುತ್ತದೆ.

**ಅಭ್ಯಾಸದಲ್ಲಿ ಇದು ಹೇಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ**: ಏಜೆಂಟ್‌ಗಳು ಬಳಕೆದಾರ ಫೀಡ್‌ಬ್ಯಾಕ್, ಪರಿಸರ ಡೇಟಾ ಮತ್ತು ಕಾರ್ಯ ಫಲಿತಾಂಶಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ ಅವರ ಜ್ಞಾನ ಆಧಾರವನ್ನು ನವೀಕರಿಸಬಹುದು, ನಿರ್ಧಾರ-ಮಾಡುವ ಆಲ್ಗೋರಿಥಮ್‌ಗಳನ್ನು ಹೊಂದಿಸಬಹುದು ಮತ್ತು ಸಮಯದೊಂದಿಗೆ ಪ್ರದರ್ಶನವನ್ನು ಸುಧಾರಿಸಬಹುದು. ಈ ಪುನರಾವರ್ತಿತ ಕಲಿಕಾ ಪ್ರಕ್ರಿಯೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ಬದಲಾಗುತ್ತಿರುವ ಪರಿಸ್ಥಿತಿಗಳಿಗೆ ಮತ್ತು ಬಳಕೆದಾರರ ಮೆಚ್ಚುಗೆಗಳಿಗೆ ಹೊಂದಿಕೊಳ್ಳಲು ಸಾಧ್ಯವಾಗಿಸುತ್ತದೆ, ಒಟ್ಟು ವ್ಯವಸ್ಥೆಯ ಪರಿಣಾಮಕಾರಿತೆಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.

## Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಮತ್ತು Azure AI ಏಜೆಂಟ್ ಸೇವೆಯ ನಡುವೆ有什么 ವ್ಯತ್ಯಾಸಗಳಿವೆ?

ಈ ವೈಚಾರಿಕ ವಿಧಾನಗಳನ್ನು ಹೋಲಿಸುವ ಹಲವು ಮಾರ್ಗಗಳಿವೆ, ಆದರೆ ಅವುಗಳ ವಿನ್ಯಾಸ, ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಗುರಿ ಬಳಸುವ ಗೋಚನೆಯಲ್ಲಿ ಕೆಲವು ಮುಖ್ಯ ವ್ಯತ್ಯಾಸಗಳನ್ನು ನೋಡೋಣ:

## Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ (MAF)

Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ `AzureAIProjectAgentProvider` ಉಪಯೋಗಿಸಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸ್ಟ್ರೀಮ್‌ಲೈನ್ಡ್ SDK ಅನ್ನು ಒದಗಿಸುತ್ತದೆ. ಇದು ಅಭಿವೃದ್ಧಿದಾರರಿಗೆ ಆಜ್ಯೂರ್ OpenAI ಮಾದರಿಗಳನ್ನು ಉಪಯೋಗಿಸಿ ಟೂಲ್ ಕರೆಗಳು, ಸಂವಾದ ವ್ಯವಸ್ಥಾಪನೆ ಮತ್ತು Azure ಗುರುತಿನ ಮೂಲಕ ಎಂಟರ್‌ಪ್ರೈಸ್-ಮಟ್ಟದ ಭದ್ರತೆಯನ್ನು ಹೊಂದಿರುವ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

**ಬಳಕೆ ಪ್ರಕರಣಗಳು**: ಟೂಲ್ ಬಳಸುವಿಕೆ, ಬಹು ಹಂತದ ಕಾರ್ಯಪ್ರವಾಹಗಳು ಮತ್ತು ಎಂಟರ್‌ಪ್ರೈಸ್ ಒಂದುಗೂಡಿಸುವ ಸಂದರ್ಭದಲ್ಲಿ ಉತ್ಪಾದನೆಗೆ ಸಿದ್ಧವಾದ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು.

Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ ಕೆಲವು ಪ್ರಮುಖ ಮೂಲ ಕಲ್ಪನೆಗಳು ಇಂತಿವೆ:

- **ಏಜೆಂಟ್‌ಗಳು**. ಏಜೆಂಟ್ ಅನ್ನು `AzureAIProjectAgentProvider` ಮೂಲಕ ರಚಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ಹೆಸರಿನೊಂದಿಗೆ, ಸೂಚನೆಗಳೊಂದಿಗೆ ಮತ್ತು ಸಾಧನಗಳೊಂದಿಗೆ ಸಂರಚಿಸಲಾಗುತ್ತದೆ. ಏಜೆಂಟ್:
  - **ಬಳಕೆದಾರ ಸಂದೇಶಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಬಹುದು** ಮತ್ತು Azure OpenAI ಮಾದರಿಗಳನ್ನು ಬಳಸಿ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ಉತ್ಪಾದಿಸಬಹುದು.
  - **ಸಂದರ್ಶನದ ಸಂದರ್ಭದ ಆಧಾರದ ಮೇಲೆ** ಸ್ವಯಂಚಾಲಿತವಾಗಿ **ಟೂಲ್‌ಗಳನ್ನು ಕರೆಮಾಡಬಹುದು**.
  - **ಅನೇಕ ಸಂವಹನಗಳ ಸಂಧರ್ಭದಲ್ಲಿ ಸಂವಾದ ಸ್ಥಿತಿಯನ್ನು ಕಾಪಾಡಬಹುದು**.

  ಇಲ್ಲಿದೆ ಏಜೆಂಟ್ ರಚಿಸುವುದನ್ನು ತೋರಿಸುವ ಕೋಡ್ ತುಣುಕು:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **ಟೂಲ್‌ಗಳು**. ಫ್ರೇಮ್‌ವರ್ಕ್ ಏಜೆಂಟ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕರೆಮಾಡಬಹುದಾದ Python ಫಂಕ್ಷನ್‌ಗಳಾಗಿ ಟೂಲ್‌ಗಳನ್ನು ನಿರ್ವಚಿಸಲು ಬೆಂಬಲ ನೀಡುತ್ತದೆ. ಏಜೆಂಟ್ ರಚಿಸುವಾಗ ಟೂಲ್‌ಗಳನ್ನು ನೋಂದಾಯಿಸಲಾಗುತ್ತದೆ:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **ಬಹು-ಏಜೆಂಟ್ ಸಂಯೋಜನೆ**. ವಿಭಿನ್ನ ವಿಶೇಷತೆಯೊಂದಿಗೆ ಹಲವಾರು ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಬಹುದು ಮತ್ತು ಅವುಗಳ ಕಾರ್ಯವನ್ನು ಸಂಯೋಜಿಸಬಹುದು:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure ಗುರುತು ಏಕೀಕರಣ**. ಫ್ರೇಮ್‌ವರ್ಕ್ ಸುರಕ್ಷಿತ, ಕೀ ರಹಿತ ಪ್ರಮಾಣೀಕರಣಕ್ಕಾಗಿ `AzureCliCredential` (ಅಥವಾ `DefaultAzureCredential`) ಬಳಸಿ, ನೇರವಾಗಿ API ಕೀಲಿಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಅಗತ್ಯವನ್ನು ತೆಗೆದುಹಾಕುತ್ತದೆ.

## Azure AI ಏಜೆಂಟ್ ಸೇವೆ

Azure AI ಏಜೆಂಟ್ ಸೇವೆ Microsoft Ignite 2024 ನಲ್ಲಿ ಪರಿಚಯಿಸಿದ ಇತ್ತೀಚಿನ ಸೇರ್ಪಡೆಗಳಲ್ಲಿಯೊಂದು. ಇದು Llama 3, Mistral ಮತ್ತು Cohere ಮುಂತಾದ ತೆರೆಯಲ್ಪಟ್ಟ ಮೂಲದ LLMಗಳನ್ನು ನೇರವಾಗಿ ಕರೆಮಾಡುವಂತೆ ಹೆಚ್ಚು ಲವಚಿಕ ಮಾದರಿಗಳೊಂದಿಗೆ AI ಏಜೆಂಟ್‌ಗಳ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ನಿಯೋಜನೆಯನ್ನು ಅನುವು ಮಾಡಿಸುತ್ತದೆ.

Azure AI ಏಜೆಂಟ್ ಸೇವೆ ಹೆಚ್ಚಿನ ಎಂಟರ್‌ಪ್ರೈಸ್ ಭದ್ರತಾ ಯಂತ್ರಗಳು ಮತ್ತು ಡೇಟಾ ಸಂಗ್ರಹಣಾ ವಿಧಾನಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ, ಏಕೆಂದರೆ ಇದು ಎಂಟರ್‌ಪ್ರೈಸ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಅನುಕೂಲಕರವಾಗಿದೆ.

ಇದು ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವ ಮತ್ತು ನಿಯೋಜಿಸುವMicrosoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಜೊತೆಗೆ immediateವಾಗಿ ಕೆಲಸಮಾಡುತ್ತದೆ.

ಈ ಸೇವೆ ಪ್ರಸ್ತುತ Public Preview ನಲ್ಲಿ ಇದೆ ಮತ್ತು ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವುದಕ್ಕೆ Python ಮತ್ತು C# ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.

Azure AI ಏಜೆಂಟ್ ಸೇವೆಯ Python SDK ಅನ್ನು ಬಳಸುವ ಮೂಲಕ, ನಾವು ಬಳಕೆದಾರ-ನಿರ್ವಚಿತ ಟೂಲ್ೊಂದಿಗೆ ಏಜೆಂಟ್ ರಚಿಸಬಹುದು:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ಉಪಕರಣ ಫังก್ಷನ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### ಮೂಲ ಕಲ್ಪನೆಗಳು

Azure AI ಏಜೆಂಟ್ ಸೇವೆ ಕೆಳಗಿನ ಮೂಲ ಕಲ್ಪನೆಗಳನ್ನು ಹೊಂದಿದೆ:

- **ಏಜೆಂಟ್**. Azure AI ಏಜೆಂಟ್ ಸೇವೆ Microsoft Foundry ಜತೆ ಏಕೀಕರಿಸುತ್ತದೆ. AI Foundry ಒಳಗೆ, AI ಏಜೆಂಟ್ ಒಂದು "ಸ್ಮಾರ್ಟ್" ಮೈಕ್ರೋಸರ್ವಿಸ್ ಆಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ಇದನ್ನು ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಲು (RAG), ಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಅಥವಾ ಸಂಪೂರ್ಣವಾಗಿ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಸ್ವಯಂ ಚಲಿತಗೊಳಿಸಲು ಬಳಸಬಹುದು. ಇದು ಜನರೇಟಿವ್ AI ಮಾದರಿಗಳ ಶಕ್ತಿಯನ್ನು ಅವುಗಳನ್ನು ನೈಜ-ವಿಶ್ವದ ಡೇಟಾ ಮೂಲಗಳಿಗೆ ಪ್ರವೇಶಿಸಲು ಮತ್ತು ಸಂವಹನ ನಡೆಸಲು ಅನುಮತಿಸುವ ಉಪಕರಣಗಳೊಂದಿಗೆ ಸಂಯೋಜಿಸುವ ಮೂಲಕ ಸಾಧಿಸುತ್ತದೆ. ಈ ಕೆಳಗಿನ ಉದಾಹರಣೆಯಲ್ಲಿ ಏಜೆಂಟ್ ಅನ್ನು ತೋರಿಸಲಾಗಿದೆ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, `gpt-4o-mini` ಮಾದರಿಯನ್ನು ಬಳಸಿ, `my-agent` ಎಂಬ ಹೆಸರಿನೊಂದಿಗೆ ಮತ್ತು `You are helpful agent` ಎಂಬ ಸೂಚನೆಗಳೊಂದಿಗೆ ಏಜೆಂಟ್ ರಚಿಸಲಾಗಿದೆ. ಏಜೆಂಟ್ ಕೋಡ್ ವ್ಯಾಖ್ಯಾನ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಟೂಲ್‌ಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳೊಂದಿಗೆ ಸಜ್ಜಾಗಿದೆ.

- **ಥ್ರೆಡ್ ಮತ್ತು ಸಂದೇಶಗಳು**. ಥ್ರೆಡ್ ಮತ್ತೊಂದು ಪ್ರಮುಖ ಕಲ್ಪನೆ. ಇದು ಏಜೆಂಟ್ ಮತ್ತು ಬಳಕೆದಾರ ನಡುವಿನ ಸಂವಾದ ಅಥವಾ ಪರಸ್ಪರ ಕ್ರಿಯೆಯನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತದೆ. ಥ್ರೆಡ್‌ಗಳನ್ನು ಸಂವಾದದ ಪ್ರಗತಿಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಲು, ಸಂದರ್ಭ ಮಾಹಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸಲು ಮತ್ತು ಸಂವಹನ ಸ್ಥಿತಿಯನ್ನು ನಿರ್ವಹಿಸಲು ಬಳಸಬಹುದು. ಇಲ್ಲಿ ಥ್ರೆಡ್ ಉದಾಹರಣೆ ಇದೆ:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ, ಒಂದು ಥ್ರೆಡ್ ರಚಿಸಲಾಗಿದೆ. ಅದರ ನಂತರ, ಥ್ರೆಡ್‌ಗೆ ಸಂದೇಶವನ್ನು ಕಳುಹಿಸಲಾಗಿದೆ. `create_and_process_run` ಅನ್ನು ಕರೆಯುವ ಮೂಲಕ, ಥ್ರೆಡ್ ಮೇಲಿನ ಕೆಲಸವನ್ನು ಏಜೆಂಟ್‌ಗಾಗಿ ಕೇಳಲಾಗಿದೆ. ಕೊನೆಗೆ, ಏಜೆಂಟ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೋಡಲು ಸಂದೇಶಗಳನ್ನು ಪಡೆಯಲಾಗುತ್ತದೆ ಮತ್ತು ಲಾಗ್ ಮಾಡಲಾಗುತ್ತದೆ. ಸಂದೇಶಗಳು ಬಳಕೆದಾರ ಮತ್ತು ಏಜೆಂಟ್ ನಡುವಿನ ಸಂವಾದದ ಪ್ರಗತಿಯನ್ನು ಸೂಚಿಸುತ್ತವೆ. ಸಂದೇಶಗಳು ಪಠ್ಯ, ಚಿತ್ರ ಅಥವಾ ಫೈಲ್ ಎಂಬ ಬಗೆಬಗೆಯ ಪ್ರಕಾರಗಳಾಗಿರಬಲ್ಲವೆಯೇ ಎಂಬುದನ್ನು ಮತ್ತು ಉದಾಹರಣೆಗೆ ಏಜೆಂಟ್‌ಗಳ ಕೆಲಸದ ಪರಿಣಾಮವಾಗಿ ಚಿತ್ರ ಅಥವಾ ಪಠ್ಯ ಪ್ರತಿಕ್ರಿಯೆ ಬಂದಿದೆ ಎಂಬುದನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು ಮುಖ್ಯ. ಅಭಿವೃದ್ಧಿದಾರನಾಗಿ, ನೀವು ಈ ಮಾಹಿತಿಯನ್ನು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಮುಂದುವರಿಸಿ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಅಥವಾ ಅದನ್ನು ಬಳಕೆದಾರರಿಗೆ ಪ್ರದರ್ಶಿಸಲು ಬಳಸಬಹುದು.

- **Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಜತೆಗೆ ಏಕೀಕರಣ**. Azure AI ಏಜೆಂಟ್ ಸೇವೆ Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಜೊತೆ ಸೌಮ್ಯವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ಅಂದರೆ ನೀವು `AzureAIProjectAgentProvider` ಬಳಸಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿ ಅವುಗಳನ್ನು ಪ್ರೊಡಕ್ಷನ್ ಸನ್ನಿವೇಶಗಳಿಗಾಗಿ ಏಜೆಂಟ್ ಸೇವೆ ಮೂಲಕ ನಿಯೋಜಿಸಬಹುದು.

**ಬಳಕೆ ಪ್ರಕರಣಗಳು**: Azure AI ಏಜೆಂಟ್ ಸೇವೆ ಸುರಕ್ಷಿತ, ವ್ಯಾಪಕವಾಗಿ ಹಾರುವ ಮತ್ತು ಲವಚಿಕ AI ಏಜೆಂಟ್ ನಿಯೋಜನೆ ಅಗತ್ಯವಿರುವ ಎಂಟರ್‌ಪ್ರೈಸ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗಾಗಿ ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ.

## ಈ ವಿಧಾನಗಳ ನಡುವೆ有什么 ವ್ಯತ್ಯಾಸ?

ಆವರಣಗಳಿದ್ದರೂ ಸಹ, ಅವುಗಳ ವಿನ್ಯಾಸ, ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಗುರಿ ಬಳಕೆ ಪ್ರಕರಣಗಳ ದೃಷ್ಟಿಯಿಂದ ಕೆಲವು ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳಿವೆ:

- **Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ (MAF)**: AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಉತ್ಪಾದನೆಗೆ ಸಿದ್ಧವಾದ SDK. ಇದು ಟೂಲ್ ಕರೆಗಳು, ಸಂವಾದ ನಿರ್ವಹಣೆ ಮತ್ತು Azure ಗುರುತಿನ ಏಕೀಕರಣದೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ಸರಳ API ಒದಗಿಸುತ್ತದೆ.
- **Azure AI ಏಜೆಂಟ್ ಸೇವೆ**: ಏಜೆಂಟ್‌ಗಳಿಗೆ Foundryಯಲ್ಲಿ ವೇದಿಕೆ ಮತ್ತು ನಿಯೋಜನೆ ಸೇವೆ. ಇದು Azure OpenAI, Azure AI Search, Bing Search ಮತ್ತು ಕೋಡ್ ಕಾರ್ಯಾಚರಣೆಯಂತಹ ಸೇವೆಗಳbuilt-in ಸಂಪರ್ಕವನ್ನು ಒದಗಿಸುತ್ತದೆ.

ಇದೇನು ಆಯ್ಕೆಮಾಡಬೇಕೆಂದು ಇನ್ನೂ ಅನುಮಾನವಿದೆಯೇ?

### ಬಳಕೆ ಪ್ರಕರಣಗಳು

ಕೆಲವು ಸಾಮಾನ್ಯ ಬಳಕೆ ಪ್ರಕರಣಗಳ ಮೂಲಕ ನಿಮಗೆ ಸಹಾಯವಾಗುವುದೇನೋ ನೋಡೋಣ:

> Q: I'm building production AI agent applications and want to get started quickly
>

>A: The Microsoft Agent Framework is a great choice. It provides a simple, Pythonic API via `AzureAIProjectAgentProvider` that lets you define agents with tools and instructions in just a few lines of code.

>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service is the best fit. It's a platform service that provides built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
 
> Q: I'm still confused, just give me one option
>
> A: Start with the Microsoft Agent Framework to build your agents, and then use Azure AI Agent Service when you need to deploy and scale them in production. This approach lets you iterate quickly on your agent logic while having a clear path to enterprise deployment.
 
ಎಲ್ಲವನ್ನೂ ಸಾರಾಂಶ ಮಾಡುವಲ್ಲಿ ಮುಖ್ಯ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಕೆಳಗಿನ ಪಟ್ಟಿಯಲ್ಲಿ ನೋಡಿ:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ಟೂಲ್ ಕರೆಗಳನ್ನು ಹೊಂದಿರುವ ಸ್ಟ್ರೀಮ್‌ಲೈನ್ಡ್ ಏಜೆಂಟ್ SDK | ಏಜೆಂಟ್‌ಗಳು, ಟೂಲ್‌ಗಳು, Azure ಗುರುತು | AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು, ಟೂಲ್ ಬಳಕೆ, ಬಹು-ಹಂತದ ಕಾರ್ಯಪ್ರವಾಹಗಳು |
| Azure AI Agent Service | ಲವಚಿಕ ಮಾದರಿಗಳು, ಎಂಟರ್‌ಪ್ರೈಸ್ ಭದ್ರತೆ, ಕೋಡ್ ಜನರೇಷನ್, ಟೂಲ್ ಕರೆಗಳು | ಘಟಕೀಕರಣ, ಸಹಕಾರ, ಪ್ರಕ್ರಿಯೆಯ ಸಂಯೋಜನೆ | ಸುರಕ್ಷಿತ, ವ್ಯಾಪಕ ಮತ್ತು ಲವಚಿಕ AI ಏಜೆಂಟ್ ನಿಯೋಜನೆ |

## ನಾನು ನನ್ನ ಈಗಿನ Azure ಪರಿಸರದ ಸಾಧನಗಳನ್ನು ನೇರವಾಗಿ ಸಂಯೋಜಿಸಬಹುದೇ, ಅಥವಾ ಸ್ವತಂತ್ರ ಪರಿಹಾರಗಳ ಅವಶ್ಯಕತೆ ಇನ್ನೂ ಇದೆಯೇ?
ಉತ್ತರ: ಹೌದು — ನೀವು ಈಗಾಗಲೆ ಹೊಂದಿದ್ದ Azure ಪರಿಸರದ ಉಪಕರಣಗಳನ್ನು, ವಿಶೇಷವಾಗಿ Azure AI Agent Service ಜೊತೆಗೆ ನೇರವಾಗಿ ಏಕೀಕರಿಸಬಹುದು, ಏಕೆಂದರೆ ಇದನ್ನು ಇತರ Azure ಸೇವೆಗಳೊಂದಿಗೆ ಸುಗಮವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವಂತೆ ನಿರ್ಮಿಸಲಾಗಿದೆ. ಉದಾಹರಣೆಗೆ ನೀವು Bing, Azure AI Search ಮತ್ತು Azure Functions ಅನ್ನು ಏಕೀಕರಿಸಬಹುದು. Microsoft Foundry ಜೊತೆಗೆ ಕೂಡ ಗಾಢವಾದ ಏಕೀಕರಣ ಇದೆ.

Microsoft Agent Framework ಕೂಡ `AzureAIProjectAgentProvider` ಮತ್ತು Azure identity ಮೂಲಕ Azure ಸೇವೆಗಳೊಂದಿಗೆ ಅಥವಾ Azure ಸೇವೆಗಳೊಂದಿಗೆ ಏಕೀಕರಿಸುತ್ತದೆ, ಇದು ನಿಮ್ಮ ಏಜೆಂಟ್ ಉಪಕರಣಗಳಿಂದ ನೇರವಾಗಿ Azure ಸೇವೆಗಳನ್ನು ಕರೆಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ.

## ಉದಾಹರಣೆ ಕೋಡ್‌ಗಳು

- Python: [ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್](./code_samples/02-python-agent-framework.ipynb)
- .NET: [ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್](./code_samples/02-dotnet-agent-framework.md)

## AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳ ಬಗ್ಗೆ ಇನ್ನೂ ಪ್ರಶ್ನೆಗಳಿವೆಯೇ?

ಇತರ ಅಧ್ಯಯನಾರ್ಥಿಗಳೊಂದಿಗೆ ಭೇಟಿಯಾಗಲು, ಕಾರ್ಯಾಗಾರ ಸಮಯಗಳಲ್ಲಿ ಭಾಗವಹಿಸಲು ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಗಳನ್ನು ಪಡೆಯಲು [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ನಲ್ಲಿ ಸೇರಿ.

## ಉಲ್ಲೇಖಗಳು

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure ಏಜೆಂಟ್ ಸೇವೆ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ - Azure OpenAI ಪ್ರತಿಕ್ರಿಯೆಗಳು</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI ಏಜೆಂಟ್ ಸೇವೆ</a>

## ಹಿಂದಿನ ಪಾಠ

[AI ಏಜೆಂಟ್‌ಗಳು ಮತ್ತು ಅವುಗಳ ಬಳಕೆ ಪ್ರಕರಣಗಳ ಪರಿಚಯ](../01-intro-to-ai-agents/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಏಜೆಂಟಿಕ್ ವಿನ್ಯಾಸ ಮಾದರಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:

ಈ ದಾಖಲೆಗಳನ್ನು AI ಭಾಷಾಂತರ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯತ್ತ ಪ್ರಯತ್ನಿಸಿದರೂ ಸಹ, ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಶುದ್ಧತೆಗಳು ಇರುವ ಸಾಧ್ಯತೆ ಇದೆ ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗೊಳ್ಳಿಕೆಗಳು ಅಥವಾ ತಪ್ಪು ವಿವಕ್ಳನೆಗಳಿಗಾಗಿ ನಾವು ಜವಾಬ್ದಾರಿಗಳಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->