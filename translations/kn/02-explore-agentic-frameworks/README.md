[![AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು](../../../translated_images/kn/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ ಈ ಪಾಠದ ವಿಡಿಯೋವನ್ನು ವೀಕ್ಷಿಸಿ)_

# AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸಿ

AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳು AI ಏಜೆಂಟ್‌ಗಳ ರಚನೆ, ನಿಯೋಜನೆ ಮತ್ತು ನಿರ್ವಹಣೆಯನ್ನು ಸರಳಗೊಳಿಸಲು ವಿನ್ಯಾಸಗೊಳ್ಳಲಾದ ಸಾಫ್ಟ್‌ವೇರ್ ವೇದಿಕೆಗಳಾಗಿವೆ. ಈ ಫ್ರೇಮುವರ್ಕ್‌ಗಳು ಅಭಿವೃದ್ಧಿಪಡಕರು ಕೀಲಿ ಭಾಗಗಳು, ಅಬ್ಸ್ಟ್ರಾಕ್ಷನ್‌ಗಳು ಮತ್ತು ಸಂಕೀರ್ಣ AI ವ್ಯವಸ್ಥೆಗಳ ಅಭಿವೃದ್ಧಿಯನ್ನು ಸುಗಮಗೊಳಿಸುವ ಸಾಧನಗಳನ್ನು ಪೂರ್ವ-ಬಿಲ್ಟ್ ರೂಪದಲ್ಲಿ ಒದಗಿಸುತ್ತವೆ.

ಈ ಫ್ರೇಮುವರ್ಕ್‌ಗಳು ಅಭಿವೃದ್ಧಿಪಡಕರಿಗೆ ಸಾಮಾನ್ಯ ಸವಾಲುಗಳಿಗೆ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಮಾಡಲಾದ സമീപನೆಯನ್ನು ಒದಗಿಸುವ ಮೂಲಕ ಅವರ ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ವಿಶೇಷ ಅಂಶಗಳ ಮೇಲೆ ಗಮನಹರಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ. ಅವು ಮಾರಾಟನೀಯತೆ, ಲಭ್ಯತೆ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ವೃದ್ಧಿಸುತ್ತವೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ಕುಕ್ರಮಾಗಿರುವುದು:

- AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳು 무엇이며 դրանք ಅಭಿವೃದ್ಧಿಪಡಕರಿಗೆ ಏನು ಸಾಧಿಸಲು ಅನುಮತಿಸುತ್ತವೆ?
- ತಂಡಗಳು ಅವರ ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತ್ವರಿತವಾಗಿ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡಿ, ಪುನರಾವರ್ತಿಸು ಮತ್ತು ಸುಧಾರಿಸಲು ಈಗಳನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> ಮತ್ತು <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) ರಚಿಸಿರುವ ಫ್ರೇಮು ವರ್ಕ್‌ಗಳು ಮತ್ತು ಸಾಧನಗಳ ಮಧ್ಯೆ ಏನು ವ್ಯತ್ಯಾಸಗಳಿವೆ?
- ನಾನು ನನ್ನ ಇದ್ದಿರುವ Azure ಪರಿಸರ ಸಾಧನಗಳನ್ನು ನೇರವಾಗಿ ಏಕೀಕರಿಸಬಹುದೇ, ಅಥವಾ ಸ್ವತಂತ್ರ ಪರಿಹಾರಗಳ ಅಗತ್ಯವಿದೆಯೇ?
- Azure AI Agents ಸೇವೆ ಏನು ಮತ್ತು ಇದು ನನ್ನಿಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡುತ್ತಿದೆ?

## ಕಲಿಕೆಯ ಗುರಿಗಳು

ಈ ಪಾಠದ ಉದ್ದೇಶಗಳು ನಿಮಗೆ ಸಹಾಯ ಮಾಡುವುದು:

- AI ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳ ಪಾತ್ರವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು.
- ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳನ್ನು ಹೇಗೆ ಉಪಯೋಗಿಸಬೇಕು ಎಂಬುದನ್ನು ಕಲಿಯುವುದು.
- AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳಿಂದ ಸಾಧ್ಯವಾಗುವ ಪ್ರಮುಖ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತಿಳಿಯುವುದು.
- Microsoft Agent Framework ಮತ್ತು Azure AI Agent Service ನಡುವೆ ಇರುವ ಭೇದಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು.

## AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳು ಎಂದರೆ 무엇 ಮತ್ತು ಅವು ಅಭಿವೃದ್ಧಿಪಡಕರಿಗೆ ಏನು ಮಾಡಲು ಅನುಮತಿಸುತ್ತವೆ?

ಸಾಂಪ್ರದಾಯಿಕ AI ಫ್ರೇಮುವರ್ಕ್‌ಗಳು ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ AI ಅನ್ನು ಸಂಯೋಜಿಸಲು ಮತ್ತು ಕೆಳಗಿನ ರೀತಿಯಲ್ಲಿ ಆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಉತ್ತಮಗೊಳಿಸಲು ಸಹಾಯ ಮಾಡಬಹುದು:

- **ವೈಯಕ್ತೀಕರಣ**: AI ಬಳಕೆದಾರರ ನಡೆ ಮತ್ತು ಇಷ್ಟಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ ವೈಯಕ್ತೀಕೃತ ಶಿಫಾರಸುಗಳು, ವಿಷಯ ಮತ್ತು ಅನುಭವಗಳನ್ನು ಒದಗಿಸಬಹುದು.
ಉದಾಹರಣೆ: Netflix ಮುಂತಾದ ಸ್ಟ್ರೀಮಿಂಗ್ ಸೇವೆಗಳು ವೀಕ್ಷಣಾ ಇತಿಹಾಸದ ಆಧಾರದಲ್ಲಿ ಸಿನೆಮಾಗಳು ಮತ್ತು ಶೋಗಳನ್ನು ಶಿಫಾರಸು ಮಾಡಲು AI ಅನ್ನು ಬಳಸುತ್ತವೆ, ಇದು ಬಳಕೆದಾರರ ತೊಡಗಿಸಿಕೊಳ್ಳುವಿಕೆಯನ್ನು ಮತ್ತು ತೃಪ್ತಿಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.
- **ಸ್ವಯಂಚಾಲನೆ ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆ**: AI ಪುನರಾವರ್ತಿಸಬಹುದಾದ ಕಾರ್ಯಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಿ, ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ಸರಳಗೊಳಿಸಿ ಮತ್ತು ಕಾರ್ಯಾಚರಣಾತ್ಮಕ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸುಧಾರಿಸಬಹುದು.
ಉದಾಹರಣೆ: ಗ್ರಾಹಕ ಸೇವಾ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಸಾಮಾನ್ಯ ವಿಚಾರಣೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು AI-ಶಕ್ತಿ ಪಡೆದ ಚಾಟ್‌ಬಾಟ್‌ಗಳನ್ನು ಬಳಸುತ್ತವೆ, ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯವನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತವೆ ಮತ್ತು ಮಾನವ ಏಜೆಂಟ್‌ಗಳನ್ನು ಮಿಕ್ಕಿ ಮಟ್ಟದ ಸಮಸ್ಯೆಗಳಿಗೆ ಮುಕ್ತಗೊಳಿಸುತ್ತವೆ.
- **ಬಲವಾದ ಬಳಕೆದಾರ ಅನುಭವ**: AI ಧ್ವನಿ ಗುರುತು, ಪ್ರಾಕೃತಿಕ ಭಾಷಾ ಪ್ರಕ್ರಿಯೆ ಮತ್ತು ಭವಿಷ್ಯ ಟೆಕ್ಸ್ಟ್ ಮುಂತಾದ ಬುದ್ಧಿವಂತ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಒದಗಿಸುವ ಮೂಲಕ ಒಟ್ಟು ಬಳಕೆದಾರ ಅನುಭವವನ್ನು ಸುಧಾರಿಸಬಹುದು.
ಉದಾಹರಣೆ: Siri ಮತ್ತು Google Assistant ಮುಂತಾದ ವರ್ಚುವಲ್ ಸಹಾಯಕರು ಧ್ವನಿ ಆಜ್ಞೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯಿಸಲು AI ಅನ್ನು ಬಳಸುತ್ತವೆ, ಇದು ಉಪಕರಣಗಳೊಂದಿಗೆ ಬಳಕೆದಾರರ ಸಂವಹನವನ್ನು ಸುಲಭವನ್ನಾಗಿಸುತ್ತದೆ.

### ಇವೆಲ್ಲಾ ಚೆನ್ನಲ್ಲವೇ, ಆದ್ರೆ ಏಕೆ AI Agent Framework ಬೇಕು?

AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳು ಕೇವಲ AI ಫ್ರೇಮುವರ್ಕ್‌ಗಿಂತ ಹೆಚ್ಚು ಕೆಲವು ವಿಷಯಗಳನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತವೆ. ಇವು ಬಳಕೆದಾರರು, ಇತರ ಏಜೆಂಟ್‌ಗಳು ಮತ್ತು ಪರಿಸರದೊಂದಿಗೆ ಸಂವಹನ ನಡೆಸಲುವಂತಹ, ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ಸ್ವಾಯತ್ತ ವ್ಯವಹಾರವನ್ನು ಪ್ರದರ್ಶಿಸುವ ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳ ರಚನೆಯನ್ನು ಸಾಧ್ಯಮಾಡಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ. ಈ ಏಜೆಂಟ್‌ಗಳು ಸ್ವಾಯತ್ತ ವರ್ತನೆಯನ್ನು ತೋರಿಸಬಹುದು, ನಿರ್ಣಯಗಳನ್ನು ಮಾಡಬಹುದು ಮತ್ತು ಬದಲಾಗುತ್ತಿರುವ ಪರಿಸ್ಥಿತಿಗಳಿಗೆ ಹೊಂದಿಕೊಳ್ಳಬಹುದು. AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳಿಂದ ಸಾದ್ಯವಾಗುವ ಕೆಲವು ಪ್ರಮುಖ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನೋಡೋಣ:

- **ಏಜೆಂಟ್ ಸಹಕಾರ ಮತ್ತು ಸಂಯೋಜನೆ**: ಜಟಿಲ ಕಾರ್ಯಗಳನ್ನು ಪ್ರಯೋಗಿಸುವ, ಸಂವಹನ ಮಾಡುವ ಮತ್ತು ಸಂಯೋಜನೆ ಮಾಡುವ ಬಹು ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.
- **ಕಾರ್ಯ ಸ್ವಯಂಚಾಲನೆ ಮತ್ತು ನಿರ್ವಹಣೆ**: ಬಹು ಹಂತದ ವರ್ಕ್ಫ್ಲೋಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವ, ಕಾರ್ಯ ಹಂಚಿಕೆಯನ್ನು ಮತ್ತು ಏಜೆಂಟ್‌ಗಳ ನಡುವೆ ಡೈನಾಮಿಕ್ ಕಾರ್ಯ ನಿರ್ವಹಣೆಯ ಕ್ರಮಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.
- **ಸಂದರ್ಭ ನಿರ್ಧಾರ ಮತ್ತು ಹೊಂದಿಕೊಳ್ಳುವಿಕೆ**: ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸಂದರ್ಭವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ, ಬದಲಾಗುತ್ತಿರುವ ಪರಿಸರಗಳಿಗೆ ಹೊಂದಿಕೊಳ್ಳುವ ಮತ್ತು ಯಥಾರ್ಥ ಸಮಯದ ಮಾಹಿತಿಯ ಆಧಾರದಲ್ಲಿ ನಿರ್ಣಯಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುವ ಸಾಮರ್ಥ್ಯವನ್ನು ಸಜ್ಜಾಗಿಸುತ್ತದೆ.

ಸಾರಾಂಶವಾಗಿ, ಏಜೆಂಟ್‌ಗಳು ನಿಮಗೆ ಹೆಚ್ಚು ಮಾಡಲು, ಸ್ವಯಂಚಾಲನೆಯನ್ನು ಮುಂದಿನ ಹಂತಕ್ಕೆ ಇಳಿಸುವುದು, ಪರಿಸರದಿಂದ ಅನುಗುಣವಾಗಿ ಕಲಿಯುವ ಮತ್ತು ಹೊಂದಿಕೊಳ್ಳುವ ಹೆಚ್ಚು ಬುದ್ಧಿವಂತ ವ್ಯವಸ್ಥೆಗಳನ್ನು ರಚಿಸುವುದು ಸಾಧ್ಯವಾಗಿಸುತ್ತದೆ.

## ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತ್ವರಿತವಾಗಿ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡಿ, ಪುನರಾವರ್ತಿಸಿ ಮತ್ತು ಸುಧಾರಿಸಲು ಹೇಗೆ?

ಇದು ವೇಗವಾಗಿ ಬದಲಾಗುವ ಕ್ಷೇತ್ರವಿದೆ, ಆದರೆ ಹೆಚ್ಚಿನ AI ಏಜೆಂಟ್ ಫ್ರೇಮುವರ್ಕ್‌ಗಳಲ್ಲಿಯೂ ಸಾಮಾನ್ಯವಾಗಿರುವ ಕೆಲವು ಅಂಶಗಳು ನಿಮಗೆ ತ್ವರಿತವಾಗಿ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡಿ ಪುನರಾವರ್ತಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ: ಬೆನ್ನುಘಟಕ ಕಂಪೋನಂಟ್‌ಗಳು (module components), ಸಹಕಾರದ ಸಾಧನಗಳು ಮತ್ತು ಯಥಾರ್ಥ ಕಾಲದ ಶಿಕ್ಷಣ (real-time learning). ಇವನ್ನು ವಿವರಿಸೋಣ:

- **ಮಾಡ್ಯೂಲರ್ ಕಂಪೋನಂಟ್‌ಗಳನ್ನು ಬಳಸಿ**: AI SDKಗಳು AI ಮತ್ತು ಮೆಮೊರಿ ಕನೆಕ್ಟರ್‌ಗಳು, ನೈಸರ್ಗಿಕ ಭಾಷೆಯ ಮೂಲಕ ಅಥವಾ ಕೋಡ್ ಪ್ಲಗಿನ್‌ಗಳನ್ನು ಬಳಸಿ ಫಂಕ್ಷನ್ ಕರೆಗಳು, ಪ್ರಾಂಪ್ ಟೆಂಪ್ಲೇಟ್‌ಗಳು ಮುಂತಾದ ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.
- **ಸಹಕಾರದ ಸಾಧನಗಳನ್ನು ಉಪಯೋಗಿಸಿ**: ನಿರ್ದಿಷ್ಟ ಪಾತ್ರಗಳು ಮತ್ತು ಕಾರ್ಯಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ, ಅವುಗಳು ಸಹಕರಿಸುವ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ಮತ್ತು ಸುಧಾರಿಸಬಹುದು.
- **ಯಥಾರ್ಥ ಕಾಲದಲ್ಲಿ ಕಲಿಯಿರಿ**: ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನಗಳಿಂದ ಕಲಿಯುವ ಪ್ರತಿಕ್ರಿಯೆ ಲೂಪ್‌ಗಳನ್ನು ಜಾರಿಗೊಳಿಸಿ ಮತ್ತು ಅವರ ವರ್ತನೆಯನ್ನು ಡೈನಾಮಿಕ್ ಆಗಿ ಹೊಂದಿಸಿಕೊಳ್ಳಿ.

### ಮಾಡ್ಯೂಲರ್ ಕಂಪೋನಂಟ್‌ಗಳನ್ನು ಬಳಸಿ

Microsoft Agent Framework ಮುಂತಾದ SDKಗಳು AI ಕನೆಕ್ಟರ್‌ಗಳು, ಸಾಧನ ನಿರ್ವಚನೆಗಳು ಮತ್ತು ಏಜೆಂಟ್ ನಿರ್ವಹಣೆ ಮುಂತಾದ ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.

**ತಂಡಗಳು ಇದನ್ನು ಹೇಗೆ ಉಪಯೋಗಿಸಬಹುದು**: ತಂಡಗಳು ಸ್ಕ್ರ್ಯಾಚ್‌ನಿಂದ ಪ್ರಾರಂಭಿಸದೆ ಈ ಘಟಕಗಳನ್ನು ತ್ವರಿತವಾಗಿ ಸಂಯೋಜಿಸಿ ಕಾರ್ಯನಿರ್ವಹಣಾ ಪ್ರೋಟೋಟೈಪ್ ನಿರ್ಮಿಸಬಹುದು, ಇದು ತ್ವರಿತ ಪ್ರಯೋಗ ಮತ್ತು ಪುನರಾವರ್ತನೆಗೆ ಅವಕಾಶ ಕೊಡುತ್ತದೆ.

**ಪ್ರಾಯೋಗಿಕವಾಗಿ ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ಬಳಕೆದಾರರ ಇನ್‌ಪುಟ್‌ನಿಂದ ಮಾಹಿತಿಯನ್ನು ಹೊರತೆಗೆಯಲು ಪೂರ್ವ-ನಿರ್ಮಿತ ಪಾರ್ಸರ್ ಅನ್ನು, ಡೇಟಾವನ್ನು ಸಂಗ್ರಹಿಸಲು ಮತ್ತು ಮರುಪ್ರಾಪ್ತಿಗೆ ಮೆಮೊರಿ ಘಟಕವನ್ನು, ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಪ್ರಾಂಪ್ ಜನರೇಟರ್ ಅನ್ನು ಬಳಸಬಹುದು, ಇವುಗಳನ್ನು ಸ್ಕ್ರ್ಯಾಚ್‌ನಿಂದ ನಿರ್ಮಿಸಬೇಕಾಗಿಲ್ಲ.

**ಉದಾಹರಣಾ ಕೋಡ್**. ಶೀಘ್ರವಾಗಿ Microsoft Agent Framework ಅನ್ನು `AzureAIProjectAgentProvider` ಜೊತೆಗೆ ಉಪಯೋಗಿಸಿ ಮಾದರಿ ಬಳಕೆದಾರ ಇನ್‌ಪುಟ್‌ಗೆ ಟೂಲ್ ಕರೆ ಮಾಡಿ ಪ್ರತಿಕ್ರಿಯಿಸುವುದರ ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ:

``` python
# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಪೈಥಾನ್ ಉದಾಹರಣೆ

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# ಪ್ರಯಾಣವನ್ನು ಬುಕ್ ಮಾಡಲು ಒಂದು ಮಾದರಿ ಉಪಕರಣ ಫಂಕ್ಷನ್ ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
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
    # ಉದಾಹರಣೆಯ output: ಜನವರಿ 1, 2025 ರಂದು ನ್ಯೂಯಾರ್ಕ್ ಗೆ ನಿಮ್ಮ ವಿಮಾನ ಯಶಸ್ವಿಯಾಗಿ ಬುಕ್ ಮಾಡಲಾಗಿದೆ. ಸುರಕ್ಷಿತ ಪ್ರಯಾಣ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ಈ ಉದಾಹರಣೆಯಿಂದ ನೀವು ನೋಡಬಹುದಾದುದು ಬಳಕೆದಾರರ ಇನ್‌ಪುಟ್‌ನಿಂದ ಮೂಲ ಮಾಹಿತಿ (ಉದಾ: ಪ್ರಯಾಣ ರಿಜರ್ವೇಶನ್‌ನ ಮೂಲ, ಗಮ್ಯಸ್ಥಾನ ಮತ್ತು ದಿನಾಂಕ) ಅನ್ನು ಹೊರತೆಗೆಯಲು ಪೂರ್ವ-ನಿರ್ಮಿತ ಪಾರ್ಸರ್ ಅನ್ನು ಹೇಗೆ ಉಪಯೋಗಿಸಬಹುದು ಎಂಬುದಾಗಿದೆ. ಈ ಮಾಡ್ಯೂಲರ್ ದೃಷ್ಠಿಕೋಣವು ನಿಮಗೆ ಹೈ-ಲೆವೆಲ್ ಲಾಜಿಕ್ ಮೇಲೆ ದೃಷ್ಠಿ ಹರಿಸಲು ಅವಕಾಶ ಮಾಡುತ್ತದೆ.

### ಸಹಕಾರದ ಸಾಧನಗಳನ್ನು ಉಪಯೋಗಿಸಿ

Microsoft Agent Framework ಮುಂತಾದ ಫ್ರೇಮುವರ್ಕ್‌ಗಳು ಸಹಕರಿಸುವ ಬಹು ಏಜೆಂಟ್‌ಗಳ ರಚನೆಯನ್ನು ಸರಳಗೊಳಿಸುತ್ತವೆ.

**ತಂಡಗಳು ಇದನ್ನು ಹೇಗೆ ಉಪಯೋಗಿಸಬಹುದು**: ತಂಡಗಳು ನಿರ್ದಿಷ್ಟ ಪಾತ್ರಗಳು ಮತ್ತು ಕಾರ್ಯಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ, ಸಹಕಾರದ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ಮತ್ತು ಸುಧಾರಿಸಬಹುದು.

**ಪ್ರಾಯೋಗಿಕವಾಗಿ ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ಪ್ರತಿ ಏಜೆಂಟ್‌ಗೆ ಡೇಟಾ ಪಡೆದುಕೊಳ್ಳುವುದು, ವಿಶ್ಲೇಷಣೆ ಅಥವಾ ನಿರ್ಣಯ ಕೈಗೊಳ್ಳುವುದು ಮುಂತಾದ ವಿಶೇಷ ಕಾರ್ಯಗಳನ್ನು ನೀಡುವ ಏಜೆಂಟ್‌ಗಳ ತಂಡವನ್ನು ರಚಿಸಬಹುದು. ಈ ಏಜೆಂಟ್‌ಗಳು ಸಾಮಾನ್ಯ ಗುರಿಯನ್ನು ಸಾಧಿಸಲು ಪರಸ್ಪರ ಸಂವಹನ ಮತ್ತು ಮಾಹಿತಿ ಹಂಚಿಕೊಳ್ಳಬಹುದು, ಉದಾಹರಣೆಗೆ ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗೆ ಉತ್ತರಿಸುವುದು ಅಥವಾ ಕಾರ್ಯವನ್ನು ಮುಗಿಸುವುದು.

**ಉದಾಹರಣಾ ಕೋಡ್ (Microsoft Agent Framework)**:

```python
# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಎಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಬಳಸಿಕೊಂಡು ಒಟ್ಟಾಗಿ ಕೆಲಸಮಾಡುವ ಹಲವಾರು ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲಾಗುತ್ತಿದೆ

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ಡೇಟಾανάಗೆೃಕಾಷೆ ಏಜೆಂಟ್
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ಡೇಟಾ ವಿಶ್ಲೇಷಣಾ ಏಜೆಂಟ್
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ಒಂದು ಕಾರ್ಯದ ಮೇಲೆ ಕ್ರಮವಾಗಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸಿ
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ಮುಂಬರುವ ಕೋಡ್‌ನಲ್ಲಿ ನೀವು ನೋಡೋದು ಬಹು ಏಜೆಂಟ್‌ಗಳು ಡೇಟಾವನ್ನು ವಿಶ್ಲೇಷಿಸಲು ಒಟ್ಟಾಗಿ ಕೆಲಸ ಮಾಡುವ ಕಾರ್ಯವನ್ನು ಹೇಗೆ ರಚಿಸಬಹುದು ಎಂಬುದಾಗಿದೆ. ಪ್ರತಿ ಏಜೆಂಟ್ ವಿಶೇಷ ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಮತ್ತು ಬಯಸಿದ ಫಲಿತಾಂಶವನ್ನು ಸಾಧಿಸಲು ಏಜೆಂಟ್‌ಗಳನ್ನು ಸಂಯೋಜಿಸುವ ಮೂಲಕ ಕಾರ್ಯ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ. ವಿಶಿಷ್ಟ ಪಾತ್ರಗಳೊಂದಿಗೆ ನಿಯೋಜಿತ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವ ಮೂಲಕ ನೀವು ಕಾರ್ಯದ ಕಾರ್ಯಕ್ಷಮತೆ ಮತ್ತು ಪ್ರದರ್ಶನವನ್ನು ಸುಧಾರಿಸಬಹುದು.

### ಯಥಾರ್ಥ ಕಾಲದಲ್ಲಿ ಕಲಿಯಿರಿ

ಅಧುನಾತನ ಫ್ರೇಮುವರ್ಕ್‌ಗಳು ಯಥಾರ್ಥ ಕಾಲದ ಕಾಂಟೆಕ್ಸ್ಟ್ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು ಮತ್ತು ಹೊಂದಿಕೊಳ್ಳುವಿಕೆಯ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.

**ತಂಡಗಳು ಇದನ್ನು ಹೇಗೆ ಉಪಯೋಗಿಸಬಹುದು**: ತಂಡಗಳು ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನಗಳಿಂದ ಕಲಿಯುವ ಪ್ರತಿಕ್ರಿಯೆ ಲೂಪ್‌ಗಳನ್ನು ಜಾರಿಗೊಳಿಸಿ ಮತ್ತು ಅವರ ವರ್ತನೆಯನ್ನು ಡೈನಾಮಿಕ್ ಆಗಿ ಹೊಂದಿಸಿಕೊಳ್ಳಲು ಅನುಷ್ಠಾನಗೊಳಿಸಬಹುದು, ಇದರಿಂದ ನಿರಂತರ ಸುಧಾರಣೆ ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳ ಸುಧಾರಣೆ ಸಾಧ್ಯವಾಗುತ್ತದೆ.

**ಪ್ರಾಯೋಗಿಕವಾಗಿ ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ಏಜೆಂಟ್‌ಗಳು ಬಳಕೆದಾರ ಪ್ರತಿಕ್ರಿಯೆ, ಪರಿಸರ ಡೇಟಾ ಮತ್ತು ಕಾರ್ಯ ಫಲಿತಾಂಶಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ ಅವರ ಜ್ಞಾನ ಭಂಡಾರವನ್ನು ನವೀಕರಿಸಬಹುದು, ನಿರ್ಣಯ алгоритಮ್‌ಗಳನ್ನು ಹೊಂದಿಸಬಹುದು ಮತ್ತು ಸಮಯದೊಂದಿಗೆ ಪ್ರದರ್ಶನವನ್ನು ಸುಧಾರಿಸಬಹುದು. ಈ ಪುನರಾವರ್ತಿತ ಕಲಿಕೆ ಪ್ರಕ್ರಿಯೆ ಏಜೆಂಟ್‌ಗಳು ಬದಲಾಗುತ್ತಿರುವ нөхರೆಗಾಣಿಕೆ ಮತ್ತು ಬಳಕೆದಾರ ಇಚ್ಛೆಗಳೊಂದಿಗೆ ಹೊಂದಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ, ಒಟ್ಟಾರೆ ವ್ಯವಸ್ಥೆಯ ಪರಿಣಾಮಕಾರಿತ್ವವನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.

## Microsoft Agent Framework ಮತ್ತು Azure AI Agent Service ನಡುವಿನ ವ್ಯತ್ಯಾಸಗಳು ಯಾವುವು?

ಈ ಪರಿಕಲ್ಪನೆಯನ್ನು ಹೋಲಿಸಲು ಅನೇಕ ಮಾರ್ಗಗಳಿವೆ, ಆದರೆ ಅವರ ವಿನ್ಯಾಸ, ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಗುರಿ ಬಳಕೆ ಪ್ರಕರಣಗಳ ದೃಷ್ಟಿಯಿಂದ ಕೆಲವು ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳನ್ನು ನೋಡೋಣ:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `AzureAIProjectAgentProvider` ಉಪಯೋಗಿಸಿ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸರಳಗೊಳಿಸಲಾದ SDK ಅನ್ನು ಒದಗಿಸುತ್ತದೆ. ಇದು ಅಭಿವೃದ್ಧಿಪಡಕರಿಗೆ ನಿರ್ಮಿಸಿರುವ ಟೂಲ್ ಕಾalling, ಸಂಭಾಷಣೆ ನಿರ್ವಹಣೆ ಮತ್ತು Azure ಗುರುತಿನ ಮೂಲಕ ಎಂಟರ್‌ಪ್ರೈಸ್-ಮಟ್ಟದ ಭದ್ರತೆಯೊಂದಿಗೆ Azure OpenAI ಮಾದರಿಗಳನ್ನು ಅನ್ವಯಿಸಲು ಸಾಧ್ಯವನ್ನిస్తుంది.

**ಬಳಕೆ ಪ್ರಕರಣಗಳು**: ಟೂಲ್ ಬಳಕೆ, ಬಹು ಹಂತದ ವರ್ಕ್ಫ್ಲೋಗಳು ಮತ್ತು ಎಂಟರ್‌ಪ್ರೈಸ್ ಸಮ್ಮಿಲನ ದೃಶ್ಯಗಳನ್ನು ಹೊಂದಿರುವ ಉತ್ಪಾದನೆ-ಸಿದ್ಧ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು.

ಇಲ್ಲಿವೆ Microsoft Agent Framework ನ ಕೆಲವು ಪ್ರಮುಖ ಮೂಲ ಕಲ್ಪನೆಗಳು:

- **ಏಜೆಂಟ್‌ಗಳು**. ಏಜೆಂಟ್ ಅನ್ನು `AzureAIProjectAgentProvider` ಮೂಲಕ ರಚಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ಹೆಸರು, ನಿರ್ದೇಶನಗಳು ಮತ್ತು ಸಾಧನಗಳೊಂದಿಗೆ ಸಂರಚಿಸಲಾಗುತ್ತದೆ. ಏಜೆಂಟ್ ಅನ್ನು:
  - **ಬಳಕೆದಾರ ಸಂದೇಶಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಬಹುದು** ಮತ್ತು Azure OpenAI ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ರಚಿಸಬಹುದು.
  - **ಟೂಲ್‌ಗಳನ್ನು ಕರೆ ಮಾಡಬಹುದು** ಸಂಭಾಷಣಾ ಸಾಮರಸ್ಯದ ಆಧಾರದ ಮೇಲೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ.
  - **ಬಹು ಸಂವಹನಗಳಾದರೂ ಸಂಭಾಷಣಾ ಸ್ಥಿತಿಯನ್ನು বজಾಯಿಸಬಹುದು**.

  ಈ ಕೆಳಗಿನ ಕೋಡ್ ಸ್ನಿಪೆಟ್‌ನಲ್ಲಿ ಏಜೆಂಟ್ ಅನ್ನು ಹೇಗೆ ರಚಿಸಬೇಕೆಂದು ತೋರಿಸಲಾಗಿದೆ:

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

- **ಟೂಲ್‌ಗಳು**. ಫ್ರೇಮುವರ್ಕ್ ಏಜೆಂಟ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕರೆ ಮಾಡಬಹುದಾದ Python ಫಂಕ್ಷನ್‌ಗಳಾಗಿ ಟೂಲ್‌ಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಬೆಂಬಲಿಸುತ್ತದೆ. ಏಜೆಂಟ್ ರಚಿಸುವಾಗ ಟೂಲ್‌ಗಳು ದಾಖಲಾಗುತ್ತವೆ:

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

- **ಬಹು-ಏಜೆಂಟ್ ಸಂಯೋಜನೆ**. ವಿಭಿನ್ನ ವಿಶೇಷೀಕರಣಗಳೊಂದಿಗೆ ನೀವು ಹಲವು ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಿ ಅವುಗಳ ಕೆಲಸವನ್ನು ಸಂಯೋಜಿಸಬಹುದು:

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

- **Azure ಗುರುತಿನ ಏಕೀಕರಣ**. ಫ್ರೇಮುವರ್ಕ್ `AzureCliCredential` (ಅಥವಾ `DefaultAzureCredential`) ಅನ್ನು ಕೀಲು ರಹಿತ ಭದ್ರತೆಗಾಗಿ ಉಪಯೋಗಿಸುತ್ತದೆ, ಇದು ಕಾಗದೋಪಾಯಗಳನ್ನು ನೇರವಾಗಿ ನಿರ್ವಹಿಸುವ ಅಗತ್ಯವನ್ನು ತೆಗೆದುಹಾಕುತ್ತದೆ.

## Azure AI Agent Service

Azure AI Agent Service ಅನ್ನು Microsoft Ignite 2024 ನಲ್ಲಿ ಪರಿಚಯಿಸಲಾಯಿತು. ಇದು Llama 3, Mistral, Cohere ಮುಂತಾದ ಓಪನ್-ಸೋರ್ಸ್ LLMಗಳನ್ನು ನೇರವಾಗಿ ಕರೆ ಮಾಡುವಂತಹ ಹೆಚ್ಚು ಬದಲಾಯಿಸಬಹುದಾದ ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು AI ಏಜೆಂಟ್‌ಗಳ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ನಿಯೋಜನೆಯನ್ನು ಅನುಮತಿಸುತ್ತದೆ.

Azure AI Agent Service ಉತ್ತಮ ಎಂಟರ್‌ಪ್ರೈಸ್ ಭದ್ರತಾ ವ್ಯವಸ್ಥೆಗಳು ಮತ್ತು ಡೇಟಾ ಸಂಗ್ರಹಣಾ ವಿಧಾನಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ, ಇದು ಅದನ್ನು ಎಂಟರ್‌ಪ್ರೈಸ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಸೂಕ್ತವಾಗಿಸುತ್ತದೆ.

ಇದು ನಿರ್ಮಾಣ-ಮೇಲೆ ಸೂಚಿಗಳೊಂದಿಗೆ Microsoft Agent Framework ಜೊತೆಗೆ ನೇರವಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಮತ್ತು ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿ ನಿಯೋಜಿಸಲು ಅನುಕೂಲವಾಗಿದೆ.

ಈ ಸೇವೆ ಪ್ರಸ್ತುತ Public Preview ನಲ್ಲಿ ಇದೆ ಮತ್ತು ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು Python ಮತ್ತು C# ಅನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.

Azure AI Agent Service Python SDK ಬಳಸಿ ನಾವು ಬಳಕೆದಾರ-ನಿರ್ಧರಿತ ಟೂಲ್‌ೊಂದಿಗೆ ಏಜೆಂಟ್ ಅನ್ನು ರಚಿಸಬಹುದು:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ಸಲಕರಣೆ ಕಾರ್ಯಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
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

Azure AI Agent Service ನಗೆ ಕೆಳಗಿನ ಮೂಲ ಕಲ್ಪನೆಗಳಿವೆ:

- **ಏಜೆಂಟ್**. Azure AI Agent Service Microsoft Foundry ಜೊತೆ ಏಕೀಕರಿಸುತ್ತದೆ. AI Foundry ಒಳಗೆ, AI ಏಜೆಂಟ್ "ಸ್ಮಾರ್ಟ್" ಮೈಕ್ರೋಸೇವೆಯಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ಇದು ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸುವುದು (RAG), ಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು ಅಥವಾ ಸಂಪೂರ್ಣವಾಗಿ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವುದಕ್ಕಾಗಿ ಉಪಯೋಗಿಸಬಹುದು. ಇದು ಜನರೇಟಿವ್ AI ಮಾದರಿಗಳ ಶಕ್ತಿ ಮತ್ತು ವಾಸ್ತವಿಕ-ವಲಯದ ಡೇಟಾ ಮೂಲಗಳಿಗೆ ಪ್ರಾಪ್ತಿಯಾಗಲು ಮತ್ತು ಸಂವಹನ ಮಾಡಲು ಅನುಮತಿಸುವ ಟೂಲ್‌ಗಳ ಸಂಯೋಜನೆಯಿಂದ ಇದು ಸಾಧಿಸುತ್ತದೆ. ಕೆಳಗಿನ ಉದಾಹರಣೆಯೊಂದು ಏಜೆಂಟ್‌ನ ಚೌಕಟ್ಟನ್ನು ತೋರಿಸುತ್ತದೆ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, `gpt-4o-mini` ಮಾದರಿಯನ್ನು ಬಳಸಿಕೊಂಡು, `my-agent` ಎಂಬ ಹೆಸರು ಮತ್ತು `You are helpful agent` ಎಂಬ ನಿರ್ದೇಶನಗಳೊಂದಿಗೆ ಏಜೆಂಟ್ ರಚಿಸಲಾಗಿದೆ. ಏಜೆಂಟ್ ಕೋಡ್ ವ್ಯಾಖ್ಯಾನ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಟೂಲ್‌ಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳೊಂದಿಗೆ ಲಸಗಿಸಲಾಗಿದೆ.

- **ಥ್ರೆಡ್ ಮತ್ತು ಸಂದೇಶಗಳು**. ಥ್ರೆಡ್ ಮತ್ತೊಂದು ಪ್ರಮುಖ ಕಲ್ಪನೆ. ಅದು ಏಜೆಂಟ್ ಮತ್ತು ಬಳಕೆದಾರರ ನಡುವಣ ಸಂಭಾಷಣೆ ಅಥವಾ ಸಂವಹನವನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತದೆ. ಥ್ರೆಡ್‌ಗಳ ಮೂಲಕ ಸಂಭಾಷಣೆಯ ಪ್ರಗತಿಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡುವುದು, ಕಾಂಟೆಕ್ಸ್ಟ್ ಮಾಹಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸುವುದು ಮತ್ತು ಸಂವಹನ ಸ್ಥಿತಿಯನ್ನು ನಿರ್ವಹಿಸುವುದು ಸಾಧ್ಯ. ಥ್ರೆಡ್ ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ:

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

    ಮೇಲಿನ ಕೋಡ್‌ನಲ್ಲಿ, ಒಂದು ಥ್ರೆಡ್ ರಚಿಸಲಾಗಿದೆ. ನಂತರ, ಥ್ರೆಡ್‌ಗೆ ಸಂದೇಶವನ್ನು ಕಳುಹಿಸಲಾಗಿದೆ. `create_and_process_run` ಅನ್ನು ಕರೆ ಮಾಡುವ ಮೂಲಕ, ಥ್ರೆಡ್‌ನಲ್ಲಿ ಏಜೆಂಟ್ ಕಾರ್ಯನಿರ್ವಹಿಸಲು ಕೇಳಲಾಗುತ್ತದೆ. ಕೊನೆಗೆ, ಏಜೆಂಟ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ನೋಡಲು ಸಂದೇಶಗಳನ್ನು ಪಡೆದು ಲಾಗ್ ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಸಂದೇಶಗಳು ಬಳಕೆದಾರ ಮತ್ತು ಏಜೆಂಟ್ ನಡುವಿನ ಸಂಭಾಷಣೆಯ ಪ್ರಗತಿಯನ್ನು ಸೂಚಿಸುತ್ತವೆ. ಸಂದೇಶಗಳು ಪಠ್ಯ, ಚಿತ್ರ ಅಥವಾ ಫೈಲ್ ಮುಂತಾದ ವಿವಿಧ ಪ್ರಕಾರಗಳಾಗಿರಬಹುದು; ಉದಾಹರಣೆಗೆ ಏಜೆಂಟ್ ಕಾರ್ಯವು ಚಿತ್ರ ಅಥವಾ ಪಠ್ಯ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಫಲಿತಾಂಶವಾಗಿ ನೀಡಬಹುದು. ಅಭಿವೃದ್ಧಿಪಡಕರಾಗಿ, ನೀವು ನಂತರ ಈ ಮಾಹಿತಿಯನ್ನು ತದನಂತರ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಅಥವಾ ಬಳಕೆದಾರನಿಗೆ ಪ್ರದರ್ಶಿಸಲು ಬಳಸಿ ತೀರ್ಮಾನಿಸಬಹುದು.

- **Microsoft Agent Framework ಜೊತೆ ಏಕೀಕರಿಸುತ್ತದೆ**. Azure AI Agent Service Microsoft Agent Framework ಜೊತೆ ಸೌಕರ್ಯವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ಅಂದರೆ ನೀವು `AzureAIProjectAgentProvider` ಬಳಸಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿ ಅವುಗಳನ್ನು ಏಜೆಂಟ್ ಸೇವೆಯ ಮೂಲಕ ಉತ್ಪಾದನಪ್ರಯೋಗಗಳಿಗೆ ನಿಯೋಜಿಸಬಹುದು.

**ಬಳಕೆ ಪ್ರಕರಣಗಳು**: Azure AI Agent Service ಎಂಟರ್‌ಪ್ರೈಸ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಉದ್ದೇಶಿತವಾಗಿದ್ದು, ಭದ್ರ, ಪ್ರಮಾಣೋತ್ತರ ಮತ್ತು ಲವಚಿಕ್ ಏಜೆಂಟ್ ನಿಯೋಜನೆಯನ್ನು ಅಗತ್ಯವಿರುವ ಪರಿಸ್ಥಿತಿಗಳಿಗೆ ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ.

## ಈ մոտವಾಡುಗಳ ನಡುವೆ ಏನು ವ್ಯತ್ಯಾಸ?

ಓವರ್ ಲ್ಯಾಪ್ ಇರುವಂತೆ ತೋರುತ್ತದೆ, ಆದರೆ ಅವರ ವಿನ್ಯಾಸ, ಸಾಮರ್ಥ್ಯ ಮತ್ತು ಗುರಿ ಬಳಕೆ ಪ್ರಕರಣಗಳ ದೃಷ್ಟಿಯಿಂದ ಕೆಲವು ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳಿವೆ:

- **Microsoft Agent Framework (MAF)**: ಇದು ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಉತ್ಪಾದನೆಗೆ ಸಿದ್ಧವಾದ SDK. ಇದು ಟೂಲ್ ಕರೆ, ಸಂಭಾಷಣೆ ನಿರ್ವಹಣೆ ಮತ್ತು Azure ಗುರುತಿನ ಏಕೀಕರಣದೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ಸರಳಗೋಲಾದ API ಅನ್ನು ಒದಗಿಸುತ್ತದೆ.
- **Azure AI Agent Service**: ಇದು ಏಜೆಂಟ್‌ಗಳಿಗೆ ವೇದಿಕೆ ಮತ್ತು ನಿಯೋಜನೆ ಸೇವೆ, Foundry ಒಳಗೊಂದು. ಇದು Azure OpenAI, Azure AI Search, Bing Search ಮತ್ತು ಕೋಡ್ ಕಾರ್ಯನಿರ್ವಹಣೆ ಮುಂತಾದ ಸೇವೆಗಳಿಗೆ ಒಳಗೋಲಾದ ಸಂಪರ್ಕವನ್ನು ಒದಗಿಸುತ್ತದೆ.

ಇರಲಾದರೂ ಯಾವದನ್ನು ಆಯ್ಕೆಮಾಡಬೇಕೆಂದು ಇನ್ನೂ ಕಂಕಣದಲ್ಲಿ ಇದ್ದೀರಾ?

### ಬಳಕೆ ಪ್ರಕರಣಗಳು

ಕೆಲವು ಸಾಮಾನ್ಯ ಬಳಕೆ ಪ್ರಕರಣಗಳ ಮೂಲಕ ನಾವು ನಿಮಗೆ ಸಹಾಯ ಮಾಡಬಹುದೇ ನೋಡೋಣ:

> Q: ನಾನು ಉತ್ಪಾದನಾ AI ಏಜೆಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುತ್ತಿದ್ದೇನೆ ಮತ್ತು ತ್ವರಿತವಾಗಿ ಪ್ರಾರಂಭಿಸಲು ಇಚ್ಛಿಸುತ್ತೇನೆ
>

>A: Microsoft Agent Framework ಉತ್ತಮ ಆಯ್ಕೆ. ಇದು `AzureAIProjectAgentProvider` ಮೂಲಕ ಸರಳ, Pythonಪ್ರಕಾರದ API ಅನ್ನು ಒದಗಿಸುತ್ತದೆ, ಇದು ನಿಮಗೆ ಕೇವಲ ಕೆಲವು ಸಾಲಿನ ಕೋಡ್‌ನಲ್ಲಿ ಟೂಲ್‌ಗಳು ಮತ್ತು ನಿರ್ದೇಶನಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ವಚಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ.

>Q: ನನಗೆ Azure ನಂತಹ Search ಮತ್ತು ಕೋಡ್ ಕಾರ್ಯನಿರ್ವಹಣೆ ಸೇರಿದಂತೆ ಎಂಟರ್‌ಪ್ರೈಸ್-ಮಟ್ಟದ ನಿಯೋಜನೆ ಬೇಕು
>
> A: Azure AI Agent Service ಅತ್ಯುತ್ತಮ votos. ಇದು ಬಹು ಮಾದರಿಗಳು, Azure AI Search, Bing Search ಮತ್ತು Azure Functions ಮುಂತಾದ forbuilt ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒದಗಿಸುವ ವೇದಿಕೆ ಸೇವೆ. Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಏಜೆಂಟ್‌ಗಳನ್ನು ಸುಲಭವಾಗಿ ನಿರ್ಮಿಸಿ ಮತ್ತು ತೂಕಮಟ್ಟಕ್ಕೆ ನಿಯೋಜಿಸಲು ಇದು ಸಹಾಯಮಾಡುತ್ತದೆ.
 
> Q: ನಾನು ಇನ್ನೂ ಗೊಂದಲದಲ್ಲಿದ್ದೇನೆ, ಒಂದು ಆಯ್ಕೆಯನ್ನು ಕೊಡಿ
>
> A: ನಿಮ್ಮ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು Microsoft Agent Framework ನಿಂದ ಪ್ರಾರಂಭಿಸಿ, ಮತ್ತು ಉತ್ಪಾದನದಲ್ಲಿ ನಿಯೋಜಿಸಲು ಮತ್ತು ಹದಗೊಳಿಸಲು Azure AI Agent Service ಅನ್ನು ಬಳಸಿ. ಈ ದೃಷ್ಠಿಕೋಣವು ನಿಮ್ಮ ಏಜೆಂಟ್ ಲಾಜಿಕ್ ನಲ್ಲಿ ತ್ವರಿತವಾಗಿ ಪುನರಾವರ್ತನೆ ಮಾಡಲು ಅನುಮತಿಸಿ ಎಂಟರ್‌ಪ್ರೈಸ್ ನಿಯೋಜನೆಗೆ ಸ್ಪಷ್ಟ ಮಾರ್ಗವನ್ನು ಒದಗಿಸುತ್ತದೆ.
 
ಕೀ ಭೇದಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ सारಾಂಶ ಮಾಡೋಣ:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## ನಾನು ನನ್ನ ಇದ್ದಿರುವ Azure ಪರಿಸರವಂಜಯ ಸಾಧನಗಳನ್ನು ನೇರವಾಗಿ ಏಕೀಕರಿಸಬಹುದೇ, ಅಥವಾ ಸ್ವತಂತ್ರ ಪರಿಹಾರಗಳ ಅಗತ್ಯವಿದೆಯೇ?
ಉತ್ತರ ಹೌದು — ನೀವು ನಿಮ್ಮ ಇರುವ Azure ಪಾರಿಸರಿಕ ಸಾಧನಗಳನ್ನು ವಿಶೇಷವಾಗಿ Azure AI Agent Service ಜೊತೆಗೆ ನೇರವಾಗಿ ಏಕರೂಪಗೊಳಿಸಬಹುದು, ಏಕೆಂದರೆ ಇದನ್ನು ಇತರ Azure ಸೇವೆಗಳೊಂದಿಗೆ ಸಹಜವಾಗಿ ಕೆಲಸ ಮಾಡಲು ನಿರ್ಮಿಸಲಾಗಿದ್ದುದು. ಉದಾಹರಣೆಗೆ ನೀವು Bing, Azure AI Search ಮತ್ತು Azure Functions ಅನ್ನು ಸಂಯೋಜಿಸಬಹುದು. Microsoft Foundry ಜೊತೆಗೆ ಕೂಡ ಗಂಭೀರ ಏಕರೂಪವಿದೆ.

The Microsoft Agent Framework ಕೂಡ `AzureAIProjectAgentProvider` ಮತ್ತು `Azure identity` ಮೂಲಕ Azure ಸೇವೆಗಳೊಂದಿಗೆ ಏಕರೂಪಗೊಳ್ಳುತ್ತದೆ, ಇದು ನಿಮ್ಮ ಏಜೆಂಟ್ ಸಾಧನಗಳಿಂದ ನೇರವಾಗಿ Azure ಸೇವೆಗಳನ್ನು ಕರೆಯಲು ಅನುಮತಿಸುತ್ತದೆ.

## ಸ್ಯಾಂಪಲ್ ಕೋಡ್

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳ ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿದೆಯಾ?

ಇತರ ಕಲಿಕಾರ್ತಿಗಳೊಂದಿಗೆ ಭೇಟಿಯಾಗಲು, office hours‌ಗಳಿಗೆ ಹಾಜರಾಗಲು ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಪಡೆಯಲು [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ಸೇರಿ.

## ಉಲ್ಲೇಖಗಳು

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure ಏಜೆಂಟ್ ಸೇವೆ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI ಪ್ರತಿಕ್ರಿಯೆಗಳು</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI ಏಜೆಂಟ್ ಸೇವೆ</a>

## ಹಿಂದಿನ ಪಾಠ

[AI ಏಜೆಂಟ್‌ಗಳಿಗೆ ಪರಿಚಯ ಮತ್ತು ಏಜೆಂಟ್ ಬಳಕೆ ಪ್ರಕರಣಗಳು](../01-intro-to-ai-agents/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಏಜೆಂಟಿಕ್ ವಿನ್ಯಾಸ ಮಾದರಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ:
ಈ ದಾಖಲೆಯನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಪ್ರಯತ್ನಿಸಿದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸೂಕ್ತತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗೊತ್ತಿರಲಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆಯನ್ನು ಪ್ರಾಮಾಣಿಕ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೆಗಳು ಅಥವಾ ತಪ್ಪಾಗಿ ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->