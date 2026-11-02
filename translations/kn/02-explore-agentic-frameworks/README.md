[![AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದು](../../../translated_images/kn/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ಈ ಪಾಠದ ವೀಡಿಯೋವನ್ನು ವೀಕ್ಷಿಸಲು ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸಿ

AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು AI ಏಜೆಂಟ್‌ಗಳ ಸೃಷ್ಟಿ, ನಿಯೋಜನೆ ಮತ್ತು ನಿರ್ವಹಣೆಯನ್ನು ಸರಳಗೊಳಿಸುವುದಕ್ಕಾಗಿ ವಿನಂತಿಸಲಾದ ಸಾಫ್ಟ್‌ವೇರ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್‌ಗಳಾಗಿವೆ. ಈ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳು, ಅವಲೋಕನಗಳು ಮತ್ತು ಸಾಧನಗಳನ್ನು ಒದಗಿಸುವ ಮೂಲಕ ಸಂಕೀರ್ಣ AI ವ್ಯವಸ್ಥೆಗಳ ಅಭಿವೃದ್ಧಿಯನ್ನು ಸರಳಗೊಳಿಸುತ್ತವೆ.

ಈ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಅವರ ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ವಿಶಿಷ್ಟ ಅಂಶಗಳ ಮೇಲೆ ಕೆಂದ್ರಿಕೃತವಾಗಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ ಮತ್ತು AI ಏಜೆಂಟ್ ಅಭಿವೃದ್ಧಿಯ ಸಾಮಾನ್ಯ ಸವಾಲುಗಳಿಗೆ ಪ್ರಮಾಣೀಕೃತ ವಿಧಾನಗಳನ್ನು ನೀಡುತ್ತವೆ. ಇವು AI ವ್ಯವಸ್ಥೆಗಳ ನಿರ್ಮಾಣದಲ್ಲಿ ವಿಸ್ತರಣೆ, ಪ್ರವೇಶಾರ್ಹತೆ ಮತ್ತು ಪರಿಣಾಮಕಾರಿತ್ವವನ್ನು ಹೆಚ್ಚಿಸುವವು.

## ಪರಿಚಯ

ಈ ಪಾಠವು ಈ ವಿಷಯಗಳ ಬಗ್ಗೆ ವಿವರಿಸುತ್ತದೆ:

- AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಏನು ಮತ್ತು ಅವುಗಳ ಮೂಲಕ ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರು ಏನು ಸಾಧಿಸಬಹುದು?
- ತಂಡಗಳು ಇದೇನ್ಸ್ ಅನ್ನು ಬಳಸಿ ಏನು ವೇಗವಾಗಿ ಪ್ರೊಟೋಟೈಪ್, ಪುನರಾವರ್ತನೆ ಮತ್ತು ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸುಧಾರಿಸಬಹುದು?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ಮತ್ತು <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) ರಚಿಸಿದ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳ ಮತ್ತು ಸಾಧನಗಳ ನಡುವೆ有什么 ವ್ಯತ್ಯಾಸಗಳಿವೆ?
- ನನ್ನ ಇತ್ತೀಚಿನ Azure ಪರಿಸರದ ಸಾಧನಗಳನ್ನು ನೇರವಾಗಿ ಇನ್‌ಟಿಗ್ರೇಟ್ ಮಾಡಬಹುದೇ ಅಥವಾ ಸ್ವತಂತ್ರ ಪರಿಹಾರಗಳ ಅವಶ್ಯಕತೆ ಇದೆಯೇ?
- Microsoft Foundry Agent Service ಎಂದರೆ ಏನು ಮತ್ತು ಇದು ನನಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡುತ್ತಿದೆ?

## ಅಧ್ಯಯನ ಗುರಿಗಳು

ಈ ಪಾಠದ ಗುರಿಗಳು ನಿಮಗೆ ಕೆಳಗಿನ ವಿಚಾರಗಳನ್ನು ತಿಳಿದುಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುವುದು:

- AI ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳ ಪಾತ್ರ.
- ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳನ್ನು ಹೇಗೆ ಉಪಯೋಗಿಸುವುದು.
- AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳಿಂದ ಸಕ್ರಿಯಗೊಂಡ ಪ್ರಮುಖ ಸಾಮರ್ಥ್ಯಗಳು.
- Microsoft Agent Framework ಮತ್ತು Microsoft Foundry Agent Service ನಡುವಿನ ವೈಶಿಷ್ಟ್ಯಗಳ ಕುರಿತು.

## AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಏನು ಮತ್ತು ಅವು ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಏನು ಸಾಧ್ಯಮಾಡುತ್ತವೆ?

ರೂಪಾಂತರದಲ್ಲಿರುವ AI ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ AI ಅನ್ನು ಏನ್ಮೀಚಲು ಸಹಾಯ ಮಾಡಬಹುದು ಮತ್ತು ಈ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಕೆಳಗಿನ ರೀತಿಗಳಲ್ಲಿ ಉತ್ತಮಗೊಳಿಸಬಹುದು:

- **ವ್ಯಕ್ತಿಗತೀಕರಣ**: AI ಬಳಕೆದಾರನ ವರ್ತನ ಮತ್ತು ಇচ্ছೆಗಳ ವಿಶ್ಲೇಷಣೆಯನ್ನು ಮಾಡಿ ವೈಯಕ್ತಿಕ ಸೂಚನೆಗಳು, ವಿಷಯಗಳು ಮತ್ತು ಅನುಭವಗಳನ್ನು ಒದಗಿಸಬಹುದು.
ಉದಾಹರಣೆ: ನೆಟ್‌ಫ್ಲಿಕ್ಸ್‌ವೇರ್ ಮುಂತಾದ ಸ್ಟ್ರೀಮಿಂಗ್ ಸೇವೆಗಳು AI ಬಳಸಿ ವೀಕ್ಷಣಾ ಇತಿಹಾಸದ ಆಧಾರದಲ್ಲಿ ಚಲನಚಿತ್ರಗಳು ಮತ್ತು ಶೋಗಳನ್ನು ಸೂಚಿಸುತ್ತವೆ, ಬಳಕೆದಾರರ ತೊಡಗು ಮತ್ತು ತೃಪ್ತಿಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತವೆ.
- **ಸ್ವಯಂಚಾಲನೆ ಮತ್ತು ಕಾರ್ಯದಕ್ಷತೆ**: AI ಪುನರಾವರ್ತಿತ ಕಾರ್ಯಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಬಹುದು, ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಸರಳಗೊಳಿಸಬಹುದು ಹಾಗೂ ಕಾರ್ಯಾಚರಣಾ ಕಾರ್ಯದಕ್ಷತೆಯನ್ನು ಸುಧಾರಿಸಬಹುದು.
ಉದಾಹರಣೆ: ಗ್ರಾಹಕ ಸೇವೆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು AI ಚಾಲಿತ ಚಾಟ್‌ಬಾಟ್‌ಗಳನ್ನು ಉಪಯೋಗಿಸಿ ಸಾಮಾನ್ಯ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ನೀಡುತ್ತವೆ, ಪ್ರತಿಕ್ರಿಯೆಯ ಸಮಯವನ್ನು ಕಡಿಮೆಮಾಡಿ ಗಂಡುಜನರ ಏಜಂಟ್‌ಗಳನ್ನು ಹೆಚ್ಚು ಸಂಕೀರ್ಣ ವಿಷಯಗಳಿಗೆ ಮುಕ್ತಗೊಳಿಸುತ್ತವೆ.
- **ಸುಧಾರಿತ ಬಳಕೆದಾರ ಅನುಭವ**: AI ಧ್ವನಿ ಗುರುತಿಸುವಿಕೆ, ಸಹಜ ಭಾಷಾ ಪ್ರಕ್ರಿಯೆ ಅಥವಾ ಭವಿಷ್ಯವಾಣಿ ಒಳಗೊಂಡ ಬುದ್ಧಿವಂತ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.
ಉದಾಹರಣೆ: ಸಿರಿ ಮತ್ತು ಗೂಗಲ್ ಅಸಿಸ್ಟೆಂಟ್ ಮುಂತಾದ ವರ್ಚುವಲ್ ಸಹಾಯಕರು ಧ್ವನಿ ಆಜ್ಞೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯಿಸಲು AI ಉಪಯೋಗಿಸ್ತಾರೆ, ಬಳಕೆದಾರರಿಗೆ ಸಾಧನಗಳೊಂದಿಗೆ ಸುಲಭವಾಗಿ ಸಂವಹನ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.

### ಈ ಎಲ್ಲವೂ ಚೆನ್ನಾಗಿದೆಯೆ, ಆದರೆ AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ನಮಗೆ ಬೇಕಾದ ಕಾರಣವೇನು?

AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಕೇವಲ AI ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳಿಗಿಂತ ಹೆಚ್ಚಾಗಿದೆ. ಇವು ಬುದ್ಧಿವಂತ ಏಜೆಂಟ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲ್ಪಟ್ಟಿದ್ದು, ಉಪಯೋಗಿಸುವವರೊಂದಿಗೆ, ಇತರ ಏಜೆಂಟ್‌ಗಳೊಂದಿಗೆ ಮತ್ತು ಪರಿಸರದೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಿ ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸುತ್ತವೆ. ಇವು ಸ್ವಾಯತ್ತ ನಿರ್ವಹಣೆ ಕಾಣಿಸಿದ್ದರು, ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಂಡು ಬದಲಾಗುತ್ತಿರುವ ಪರಿಸ್ಥಿತಿಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತವೆ. AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳಿಂದ ಸಕ್ರಿಯಗೊಳ್ಳುವ ಕೆಲವು ಪ್ರಮುಖ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನೋಡೋಣ:

- **ಏಜೆಂಟ್ ಸಹಕಾರ ಮತ್ತು ಸಮನ್ವಯ**: ಸಹಕಾರದಿಂದ ಕಾರ್ಯನಿರ್ವಹಿಸುವ, ಸಂವಹನ ಮಾಡಬಲ್ಲ, ಮತ್ತು ಸಂಕೀರ್ಣ ಕಾರ್ಯಗಳನ್ನು ಬಗೆಹರಿಸುವ ಗುಣವಿರುವ ಬಹು ಏಜೆಂಟ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.
- **ಕಾರ್ಯ ಸ್ವಯಂಚಾಲನೆ ಮತ್ತು ನಿರ್ವಹಣೆ**: ಬಹು ಹಂತದ ಕಾರ್ಯಪ್ರವಾಹಗಳ ಸ್ವಯಂಚಾಲನೆ, ಕಾರ್ಯ ನಿಯೋಜನೆ, ಮತ್ತು ಏಜೆಂಟ್‌ಗಳ ನಡುವೆ ಚಾಲನಾ ಕಾರ್ಯ ನಿರ್ವಹಣೆಗಾಗಿ ಉಪಕರಣಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.
- **ಸಂದರ್ಭಜ್ಞಾನ ಮತ್ತು ಹೊಂದಾಣಿಕೆ**: ಏಜೆಂಟ್‌ಗಳು ಸನ್ನಿವೇಶವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು, ಬದಲಾಗುತ್ತಿರುವ ಪರಿಸರಕ್ಕೆ ಹೊಂದಿಕೊಳ್ಳುವುದು, ಮತ್ತು ದೈನಂದಿನ ಮಾಹಿತಿ ಆಧಾರಿತ ನಿರ್ಧಾರಗಳನ್ನು ಕೈಗೊಳ್ಳುವುದು ಸಾಧ್ಯವಾಗಿಸುತ್ತದೆ.

ಸಾರಾಂಶವಾಗಿ, ಏಜೆಂಟ್‌ಗಳು ನಿಮಗೆ ಹೆಚ್ಚಿನ ಸ್ವಾಯಂತ್ಯ ಮತ್ತು ಬುದ್ಧಿವಂತ ವ್ಯವಸ್ಥೆಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ, ಇವು ಪರಿಸರದಿಂದ ಕಲಿಯುತ್ತಾ ಸರಿಹೊಂದಿಕೊಳ್ಳುತ್ತವೆ.

## ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ತ್ವರಿತವಾಗಿ ಪ್ರೊಟೋಟೈಪ್ ಮಾಡುವುದು, ಪುನರಾವರ್ತನೆ ಮಾಡುವುದು ಮತ್ತು ಸುಧಾರಿಸುವುದು ಹೇಗೆ?

ಇದು ವೇಗವಾಗಿ ಬದಲಾಗುವ ಕ್ಷೇತ್ರವಾಗಿದೆ, ಆದರೆ ಹೆಚ್ಚು AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳಲ್ಲಿ ಸಾಮಾನ್ಯವಾಗಿರುವ ಕೆಲವು ಅಂಶಗಳಿವೆ: ಘಟಕಗಳು, ಸಹಕಾರಿ ಸಾಧನಗಳು, ಮತ್ತು ನೇರ ಕಾಲ ಅಧ್ಯಯನ. ಅವುಗಳ ಬಗ್ಗೆ ವಿವರಿಸೋಣ:

- **ಘಟಕಗಳನ್ನು ಬಳಸಿ**: AI SDKಗಳು ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು (AI ಮತ್ತು ಮೆಮೊರಿ ಸಂಯೋಚಕರು, ಸಹಜ ಭಾಷೆಯ ಅಥವಾ ಕೋಡ್ ಪ್ಲಗಿನ್‌ಗಳ ಮೂಲಕ ಕಾರ್ಯ ಕರೆ, ಪ್ರಾಂಪ್ಟ್ ಟೆಂಪ್ಲೇಟುಗಳು ಮುಂತಾದವು) ಒದಗಿಸುತ್ತವೆ.
- **ಸಹಕಾರಿ ಉಪಕರಣಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳಿ**: ನಿರ್ದಿಷ್ಟ ಪಾತ್ರ ಮತ್ತು ಕಾರ್ಯಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ, ಸಹಕಾರಿ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ಮತ್ತು ಸುಧಾರಿಸಬಹುದು.
- **ನೇರವೇಳೆ ಕಲಿಯಿರಿ**: ಪ್ರತಿಕ್ರಿಯಾ ಲೂಪ್‌ಗಳನ್ನು ನಿರ್ವಾಹಿಸಿ, ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನಗಳಿಂದ ಕಲಿತು ತಮ್ಮ ವರ್ತನೆಯನ್ನು ಬದಲಾಯಿಸಬಹುದು.

### ಘಟಕಗಳನ್ನು ಬಳಸಿ

Microsoft Agent Framework ಲాంటి SDKಗಳು AI ಸಂಯೋಚಕರು, ಸಾಧನ ವ್ಯಾಖ್ಯಾನಗಳು, ಮತ್ತು ಏಜೆಂಟ್ ನಿರ್ವಹಣಾ ಘಟಕಗಳನ್ನು ಪೂರ್ವನಿರ್ಮಿತವಾಗಿ ಒದಗಿಸುತ್ತವೆ.

**ತಂಡಗಳು ಹೇಗೆ ಬಳಸಬಹುದು**: ತಂಡಗಳು ಬೇರೆಬೇರೆ ಘಟಕಗಳನ್ನು ಒಟ್ಟುಗೂಡಿಸಿ, ಮರುಪ್ರಯೋಗ ಮತ್ತು ಪ್ರಯೋಗಗಳಿಗಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಪ್ರೋಟೋಟೈಪ್ ಅನ್ನು ತ್ವರಿತವಾಗಿ ರಚಿಸಬಹುದು.

**ವಾಸ್ತವಿಕ ಅನುಭವದಲ್ಲಿ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ಬಳಕೆದಾರ ಇನ್‌ಪುಟ್‌ನಿಂದ ಮಾಹಿತಿ ತೆಗೆದುಕೊಳ್ಳಲು ಪೂರ್ವನಿರ್ಮಿತ ಪಾಸರ್, ಡೇಟಾ ಸಂಗ್ರಹಿಸಲು ಮತ್ತು ಪುನಃ ಪಡೆಯಲು ಮೆಮೊರಿ ಘಟಕ, ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಹನಕ್ಕೆ ಪ್ರಾಂಪ್ಟ್ ಜನರೇಟರ್ ಅನ್ನು ಬಳಸಬಹುದು, ಎಲ್ಲವೂ ಶೂನ್ಯದಿಂದ ನಿರ್ಮಿಸದೆಯೇ.

**ಉದಾಹರಣಾ ಕೋಡ್**. Microsoft Agent Framework ಅನ್ನು `FoundryChatClient` ಜೊತೆಗೆ ಹೇಗೆ ಬಳಸಬಹುದು ಎಂಬುದಾಗಿ ನೋಡೋಣ, ಬಳಕೆದಾರ ಇನ್‌ಪುಟ್‌ಗೆ ಉಪಕರಣ ಕರೆಸುವ ಮೂಲಕ ಮಾದರಿಯನ್ನು ಪ್ರತಿಕ್ರಿಯಿಸುವುದಕ್ಕಾಗಿ:

``` python
# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮನಾರ್ಕ್ ಪೈಥಾನ್ ಉದಾಹರಣೆ

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# ಪ್ರಯಾಣ ಬುಕ್ ಮಾಡಲು ಒಂದು ಮಾದರಿ ಉಪಕರಣ ಕಾರ್ಯವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # ಉದಾಹರಣೆಯ ಔಟ್‌ಪುಟ್: ಜನವರಿ 1, 2025 ರಂದು ನಿಮ್ಮ ನ್ಯೂಯಾರ್ಕ್ ವಿಮಾನ ಯಶಸ್ವಿಯಾಗಿ ಬುಕ್ ಮಾಡಲಾಗಿದೆ. ಸುರಕ್ಷಿತ ಪ್ರಯಾಣ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ಈ ಉದಾಹರಣೆಯಿಂದ ನೀವು ನೋಡಬಹುದು, ಬಳಕೆದಾರ ಇನ್‌ಪುಟ್‌ನಿಂದ ಪ್ರಮುಖ ಮಾಹಿತಿ (ಮೊದಲಿನ ಸ್ಥಾನ, ಗಮ್ಯಸ್ಥಾನ ಮತ್ತು ವಿಮಾನ ಟಿಕೆಟ್ ಅನುರೋಧದ ತಾರೀಖು) ಹೊರತೆಗೆದುಕೊಳ್ಳುವುದಕ್ಕಾಗಿ ಪೂರ್ವ-ನಿರ್ಮಿತ ಪಾಸರ್ ಅನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು ಎಂಬುದು. ಈ ಘಟಕ ಆಧಾರಿತ ಕ್ರಮವು ನಿಮಗೆ ಉನ್ನತ-ಮಟ್ಟದ ತರ್ಕದ ಮೇಲೆ ಗಮನಸೇರಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ.

### ಸಹಕಾರಿ ಸಾಧನಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳಿ

Microsoft Agent Framework ಮುಂತಾದ ಹೀಗೆ ಇರುವ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಒಟ್ಟಾಗಿ ಕೆಲಸ ಮಾಡುವ ಬಹು ಏಜೆಂಟ್‌ಗಳ ಸೃಷ್ಟಿಯನ್ನು ಸುಲಭಗೊಳಿಸುತ್ತವೆ.

**ತಂಡಗಳು ಹೇಗೆ ಬಳಸಬಹುದು**: ತಂಡಗಳು ನಿರ್ದಿಷ್ಟ ಪಾತ್ರ ಮತ್ತು ಕಾರ್ಯಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ, ಸಹಕಾರಿ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಪರೀಕ್ಷಿಸುವುದು ಮತ್ತು ಸುಧಾರಿಸುವುದಕ್ಕಾಗಿ ಸಹಾಯ ಮಾಡಬಹುದು.

**ವಾಸ್ತವಿಕ ಅನುಭವದಲ್ಲಿ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ಪ್ರತಿ ಏಜೆಂಟ್‌ಗೂ ವಿಶಿಷ್ಟ ಕಾರ್ಯವಿದೆ (ತথ್ಯ ಸಂಗ್ರಹಣೆ, ವಿಶ್ಲೇಷಣೆ ಅಥವಾ ನಿರ್ಧಾರ ತೆಗೆದುಕೊಳ್ಳುವುದು). ಈ ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನ ಮಾಡಿ, ಮಾಹಿತಿ ಹಂಚಿಕೊಂಡು ಸಾಮಾನ್ಯ ಗುರಿಯನ್ನು ಸಾಧಿಸುತ್ತವೆ, ಉದಾ: ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗೆ ಉತ್ತರಿಸುವುದು ಅಥವಾ ಕಾರ್ಯವನ್ನು ಪೂರ್ಣಗೊಳಿಸುವುದು.

**ಉದಾಹರಣಾ ಕೋಡ್ (Microsoft Agent Framework)**:

```python
# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿಕೊಂಡು ಒಟ್ಟಿಗೆ ಕೆಲಸ ಮಾಡುವ ಬಹು ಏಜೆಂಟ್ ಗಳನ್ನು ರಚಿಸಲಾಗುತ್ತಿದೆ

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ಡೇಟಾ ತೆಗೆದುಕೊಂಡು ಬರಿಸುವ ಏಜೆಂಟ್
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# ಡೇಟಾ ವಿಶ್ಲೇಷಣಾ ಏಜೆಂಟ್
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# ಒಂದು ಕೆಲಸದಲ್ಲಿ ಕ್ರಮವಾಗಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ಓಡಿಸುವುದು
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ನೀವು ನೋಡಬಹುದು, ಹಲವು ಏಜೆಂಟ್‌ಗಳು ಒಟ್ಟಾಗಿ ಕೆಲಸ ಮಾಡುವ ಕಾರ್ಯವನ್ನು ರಚಿಸಲಾಗಿದೆ, ಪ್ರತಿ ಏಜೆಂಟ್ ನಿರ್ದಿಷ್ಟ ಕಾರ್ಯ ನಿರ್ವಹಿಸುತ್ತದೆ, ಕಾರ್ಯ ಉದ್ದೇಶ ಪೂರೈಕೆಗಾಗಿ ಏಜೆಂಟ್‌ಗಳ ಸಮನ್ವಯವಿದೆ. ಸಮರ್ಪಿತ ಕಾರ್ಯಗಳೊಂದಿಗೆ ಪರಿಣಿತ ಏಜೆಂಟ್‌ಗಳನ್ನು ಸೃಷ್ಠಿಸುವ ಮೂಲಕ, ಕಾರ್ಯದಕ್ಷತೆಯನ್ನು ಮತ್ತು ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸುಧಾರಿಸಬಹುದು.

### ನೇರವೇಳೆ ಕಲಿಯಿರಿ

ಪ್ರगत ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ನೇರ ಕಾಲ ಸಂದರ್ಭ ಅರಿವು ಮತ್ತು ಹೊಂದಾಣಿಕೆಗೆ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.

**ತಂಡಗಳು ಹೇಗೆ ಬಳಸಬಹುದು**: ತಂಡಗಳು ಪ್ರತಿಕ್ರಿಯಾ ಲೂಪ್‌ಗಳನ್ನು ಜಾರಿಗೊಳಿಸಬಹುದು, ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನಗಳಿಂದ ಕಲಿತು ತಾವುದ ವರ್ತನೆಯನ್ನು ತಿದ್ದುಪಡಿಸಬಹುದು, ಇದು ನಿರಂತರ ಸುಧಾರಣೆ ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳ ಉದ್ಧಾರಕ್ಕೆ ಕಾರಣವಾಗಿದೆ.

**ವಾಸ್ತವಿಕ ಅನುಭವದಲ್ಲಿ ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ಏಜೆಂಟ್‌ಗಳು ಬಳಕೆದಾರ ಪ್ರತಿಕ್ರಿಯೆ, ಪರಿಸರದ ಡೇಟಾ ಮತ್ತು ಕಾರ್ಯ ಫಲಿತಾಂಶಗಳ ವಿಶ್ಲೇಷಣೆ ಮಾಡಿ ಜ್ಞಾನಾಧಾರವನ್ನು ನವೀಕರಿಸುತ್ತವೆ, ನಿರ್ಧಾರ-ಮಾದರಿಗಳನ್ನು ತಿದ್ದುಪಡಿಸಿ ಸಮಯದ ಜೊತೆಗೆ ಕಾರ್ಯಕ್ಷಮತೆಯನ್ನು ಸುಧಾರಿಸುತ್ತವೆ. ಈ ಪುನರಾವರ್ತಿತ ಕಲಿಕೆ ಪ್ರಕ್ರಿಯೆ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಬದಲಾಗುತ್ತಿರುವ ಪರಿಸ್ಥಿತಿಗಳಿಗೆ ಮತ್ತು ಬಳಕೆದಾರ ಇಚ್ಚೆಗಳಿಗೂ ಹೊಂದಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ, ಇದರಿಂದ ಒಟ್ಟಾರೆ ವ್ಯವಸ್ಥೆಯ ಪ್ರಭಾವಕಾರಿತ್ವ ಹೆಚ್ಚುತ್ತದೆ.

## Microsoft Agent Framework ಮತ್ತು Microsoft Foundry Agent Service ನಡುವೆ有什么 ವೈಶಿಷ್ಟ್ಯಗಳಿವೆ?

ಈ ವಿಧಾನಗಳನ್ನು ಹೋಲಿಸುವ ಹಲವು ಮಾರ್ಗಗಳಿವೆ, ಆದರೆ ಅವರ ವಿನ್ಯಾಸ, ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಗುರಿತARGET ಬಳಕೆ ಪ್ರಕರಣಗಳ ದೃಷ್ಟಿಯಿಂದ ಕೆಲವು ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳಿವೆ:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `FoundryChatClient` ಬಳಸಿ AI ಏಜೆಂಟ್ ಗಳನ್ನು ನಿರ್ಮಿಸಲು ತುಂಡು-ಮಟ್ಟದ SDK ಒದಗಿಸುತ್ತದೆ. ಇದು ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಉಪಕರಣ ಕರೆ, ಸಂಭಾಷಣೆ ನಿರ್ವಹಣೆ, ಮತ್ತು Azure ಗುರುತಿನ ಮೂಲಕ ಉದ್ಯಮ ಮಟ್ಟದ ಸುರಕ್ಷತೆಯನ್ನು ಒದಗಿಸುವ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.

**ಬಳಕೆ ಪ್ರಕರಣಗಳು**: ಉಪಕರಣ ಬಳಕೆ, ಬಹು ಹಂತದ ಕಾರ್ಯಪ್ರವಾಹಗಳು, ಮತ್ತು ಉದ್ಯಮ ಸಂಯೋಜನೆ ಸನ್ನಿವೇಶಗಳೊಂದಿಗೆ ಉತ್ಪಾದನಾ-ಸಿದ್ಧ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು.

Microsoft Agent Framework ನ ಕೆಲವು ಪ್ರಮುಖ ಮೂಲ ಅಂಶಗಳು:

- **ಏಜೆಂಟ್‌ಗಳು**. `FoundryChatClient` ಮೂಲಕ ಏಜೆಂಟ್ ರಚಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ಹೆಸರು, ಸೂಚನೆಗಳು ಮತ್ತು ಉಪಕರಣಗಳೊಂದಿಗೆ ಸಂರಚಿತ ಮಾಡಲಾಗುತ್ತದೆ. ಏಜೆಂಟ್ ಆ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಹೊಂದಿದೆ:
  - **ಬಳಕೆದಾರ ಸಂದೇಶಗಳನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡುವುದು** ಮತ್ತು Azure OpenAI ಮಾದರಿಗಳನ್ನು ಉಪಯೋಗಿಸಿ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ರಚಿಸುವುದು.
  - **ಸಂಭಾಷಣೆ ಸನ್ನಿವೇಶದ ಆಧಾರದ ಮೇಲೆ** ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಉಪಕರಣಗಳನ್ನು ಕರೆಸುವುದು.
  - **ಬಹುಸಂವಹನದ ಸಂಭಾಷಣೆ ಸ್ಥಿತಿಯನ್ನು ಇಡಿಸುವುದು**.

  ಈ ರೀತಿ ಏಜೆಂಟ್ ರಚಿಸುವುದಕ್ಕೆ ಒಂದು ಕೋಡ್ ತುಂಡು ಇಲ್ಲಿದೆ:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **ಉಪಕರಣಗಳು**. ಫ್ರೇಮ್ವರ್ಕ್ ಆಗಾಗ Python ಕಾರ್ಯಗಳಾಗಿ ಉಪಕರಣಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. ಉಪಕರಣಗಳು ಏಜೆಂಟ್ ಸೃಷ್ಟಿಸುವಾಗ ನೋಂದಾಯಿಸಲಾಗುತ್ತದೆ:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **ಬಹು ಏಜೆಂಟ್ ಸಮನ್ವಯ**. ವಿಭಿನ್ನ ವಿಶಿಷ್ಟತೆಯ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಿ ಅವರ ಕಾರ್ಯಗಳನ್ನು ಸಮನ್ವಯಗೊಳಿಸಬಹುದು:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure ಗುರುತುಮುಖ ಸಂಯೋಜನೆ**. `AzureCliCredential` ಅಥವಾ `DefaultAzureCredential` ಬಳಸಿ ನಿರೀಕ್ಷಿತ ಸುರಕ್ಷಿತ, ಕೀ-ರಹಿತ ದೃಢೀಕರಣವನ್ನು ಒದಗಿಸಲಾಗುತ್ತದೆ, API ಕীগಳ ನಿರ್ವಹಣೆಯ ಅಗತ್ಯವಿಲ್ಲ.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service ನವೀನ ಸೇವೆಯಾಗಿದೆ, Microsoft Ignite 2024 ನಲ್ಲಿ ಪರಿಚಯಿಸಲಾಯಿತು. ಇದು ಹೆಚ್ಚು ನೇರ-ಸ್ವತಂತ್ರ ಮಾದರಿಗಳನ್ನು, ಉದಾಹರಣೆಗಾಗಿ ಲ್ಲಾಮಾ 3, ಮಿಸ್ಟ್ರಲ್ ಮತ್ತು ಕೋಹೀರ್ ಮುಂತಾದ ಓಪನ್-ಸೋರ್ಸ್ LLM ಗಳನ್ನು ಕರೆಸುವ ಸಾಮರ್ಥ್ಯವಿದೆ.

Microsoft Foundry Agent Service ಮಿಗಿಲಾದ ಉದ್ಯಮ ಸುರಕ್ಷತಾ ಉಪಾಯಗಳು ಮತ್ತು ಡೇಟಾ ಸಂಗ್ರಹಣಾ ವಿಧಾನಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ, ಇದರಿಂದ ಅದು ಉದ್ಯಮ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಸೂಕ್ತವಾಗಿದೆ.

ಇದು Microsoft Agent Framework ಜೊತೆಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ ಮತ್ತು ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವ ಹಾಗೆ ನಿಯೋಜಿಸಲು ನೆರವಾಗುತ್ತದೆ.

ಈ ಸೇವೆ ಪ್ರಸ್ತುತ ಸಾರ್ವಜನಿಕ ಪೂರ್ವದರ್ಶನದಲ್ಲಿ ಇರುತ್ತದೆ ಮತ್ತು Python ಮತ್ತು C# ನಲ್ಲಿ ಏಜೆಂಟ್ ನಿರ್ಮಾಣವನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.

Microsoft Foundry Agent Service Python SDK ಬಳಸಿ, ನಾವು ಬಳಕೆದಾರ-ವ್ಯಾಖ್ಯಾನಿತ ಉಪಕರಣ ಹೊಂದಿರುವ ಏಜೆಂಟ್ ರಚಿಸಬಹುದು:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ಸಾಧನ ಕಾರ್ಯಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
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
        model="gpt-5-mini",
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

### ಮೂಲ ಅಂಶಗಳು

Microsoft Foundry Agent Service ನ ಈ ಕೆಳಗಿನ ಪ್ರಮುಖ ಅಂಶಗಳಿವೆ:

- **ಏಜೆಂಟ್**. Microsoft Foundry Agent Service Microsoft Foundry ಜೊತೆ ಸಂಯೋಜನೆ ಹೊಂದಿದೆ. Microsoft Foundry ಒಳಗೊಂಡು, AI ಏಜೆಂಟ್ "ಚತುರ" ಮೈಕ್ರೋಸರ್ಸ್ ಆಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸುವುದು (RAG), ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುವುದು, ಅಥವಾ ಪೂರ್ಣಸ್ವರೂಪ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವುದು. ಇದು ಜನರೇಟಿವ್ AI ಮಾದರಿಗಳ ಶಕ್ತಿ ಮತ್ತು ನೈಜ-ವಿಶ್ವ ಡೇಟಾ ಮೂಲಗಳನ್ನು ಪ್ರಾಪ್ಟ್ ಮಾಡುವ ಸಾಧನಗಳನ್ನು ಸಂಯೋಜಿಸುವ ಮೂಲಕ ಸಾಧಿಸುತ್ತದೆ. ಈ ಕೆಳಗಿನ ಉದಾಹರಣೆ ಏಜೆಂಟ್:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ಈ ಉದಾಹರಣೆಯಲ್ಲಿ, `gpt-5-mini` ಮಾದರಿ, `my-agent` ಹೆಸರು ಮತ್ತು `You are helpful agent` ಸೂಚನೆಗಳೊಂದಿಗೆ ಏಜೆಂಟ್ ರಚಿಸಲಾಗಿದೆ. ಈ ಏಜೆಂಟ್ ಕೋಡ್ ವಿವರಣೆ ಕಾರ್ಯಗಳಿಗೆ ಉಪಕರಣಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳೊಂದಿಗೆ ಸಜ್ಜುಗೊಂಡಿದೆ.

- **ಥ್ರೆಡ್ ಮತ್ತು ಸಂದೇಶಗಳು**. ಥ್ರೆಡ್ ಇನ್ನೊಂದು ಮುಖ್ಯ ಅಂಶವಾಗಿದೆ. ಇದು ಏಜೆಂಟ್ ಮತ್ತು ಬಳಕೆದಾರರ ನಡುವಿನ ಸಂಭಾಷಣೆ ಅಥವಾ ಸಂವಹನವನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತದೆ. ಥ್ರೆಡ್ಗಳನ್ನು ಸಂಭಾಷಣೆಯ ಪ್ರಗತಿ, ಸಂದರ್ಭ ಮಾಹಿತಿ ಸಂಗ್ರಹಣೆ ಮತ್ತು ಸಂವಹನ ಸ್ಥಿತಿಯನ್ನು ನಿರ್ವಹಿಸಲು ಬಳಸಬಹುದು. ಈ ಕೆಳಗಿನ ಥ್ರೆಡ್ ಉದಾಹರಣೆ:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ಏಜೆಂಟ್‌ನಿಂದ ಥ್ರೆಡ್‌ನಲ್ಲಿ ಕೆಲಸ ಮಾಡಲು ಕೇಳಿ
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ಏಜೆಂಟ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೋಡಲು ಎಲ್ಲಾ ಸಂದೇಶಗಳನ್ನು ತೆಗೆದು ದಾಖಲಿಸಿ
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ಹಿಂದಿನ ಕೋಡ್‌ನಲ್ಲಿ ಥ್ರೆಡ್ ರಚಿಸಲಾಗಿದೆ. ನಂತರ, ಥ್ರೆಡ್‌ಗೆ ಸಂದೇಶ ಕಳುಹಿಸಲಾಗಿದೆ. `create_and_process_run` ಅನ್ನು ಕರೆದು ಏಜೆಂಟ್‌ಗೆ ಥ್ರೆಡ್ ಮೇಲೆ ಕಾರ್ಯನಿರ್ವಹಿಸಲು ಕೇಳಲಾಗಿದೆ. ಕೊನೆಯಲ್ಲಿ, ಸಂದೇಶಗಳನ್ನು ಪಡೆದು ಏಜೆಂಟ್ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಲಾಗ್ ಮಾಡಲಾಗಿದೆ. ಈ ಸಂದೇಶಗಳು ಬಳಕೆದಾರ ಮತ್ತು ಏಜೆಂಟ್ ನಡುವಿನ ಸಂಭಾಷಣೆಯ ಪ್ರಗತಿಯನ್ನು ಸೂಚಿಸುತ್ತವೆ. ಸಂದೇಶಗಳು ಪಠ್ಯ, ಚಿತ್ರ ಅಥವಾ ಕಡತ ಹೀಗೆ ವಿವಿಧ ಸ್ವರೂಪದ ಇರಬಹುದು, ಉದಾಹರಣೆಗೆ ಏಜೆಂಟ್ ಕೆಲಸದಿಂದ ಚಿತ್ರ ಅಥವಾ ಪಠ್ಯ ಪ್ರತಿಕ್ರಿಯೆ ಬರುತ್ತದೆ. ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಾಗಿ ನೀವು ಈ ಮಾಹಿತಿಯನ್ನು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ಮತ್ತಷ್ಟು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಅಥವಾ ಬಳಕೆದಾರರಿಗೆ ಪ್ರದರ್ಶಿಸಲು ಬಳಸಬಹುದು.

- **Microsoft Agent Framework ಜೊತೆಗೆ ಸಂಯೋಜನೆ**. Microsoft Foundry Agent Service ಸುಗಮವಾಗಿ Microsoft Agent Framework ಜೊತೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ, ಇದರಿಂದ ನೀವು `FoundryChatClient` ಉಪಯೋಗಿಸಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿ, ಅವನ್ನು Agent Service ಮೂಲಕ ಉತ್ಪಾದನಾ ಸನ್ನಿವೇಶಕ್ಕೆ ನಿಯೋಜಿಸಬಹುದು.

**ಬಳಕೆ ಪ್ರಕರಣಗಳು**: Microsoft Foundry Agent Service ಸೆಕ್ಯುರಿಟಿ, ವಿಸ್ತರಣೆ ಮತ್ತು ಮಾರುಕಟ್ಟೆಯ ಅನುಕೂಲತೆ ಹೊಂದಿದ ಉದ್ಯಮ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ.

## ಈ ವಿಧಾನಗಳ ನಡುವಿನ有什么 ವ್ಯತ್ಯಾಸಗಳಿವೆ?
 
ಹೊಂದಾಣಿಕೆ ಇದೆ ಎಂದು ಕಾಣಬಹುದು, ಆದರೆ ಅವುಗಳ ವಿನ್ಯಾಸ, ಸಾಮರ್ತ್ಯಗಳು ಮತ್ತು ಗುರಿ ಬಳಕೆ ಪ್ರಕರಣಗಳ ಮೇಲೆ ಕೆಲವು ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳಿವೆ:
 
- **Microsoft Agent Framework (MAF)**: AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಉತ್ಪಾದನಾ-ಸಿದ್ಧ SDK. ಉಪಕರಣ ಕರೆ, ಸಂಭಾಷಣೆ ನಿರ್ವಹಣೆ ಮತ್ತು Azure ಗುರುತುಮುಖ ಸಂಯೋಜನೆಗಾಗಿ ಸರಳ API ಒದಗಿಸುತ್ತದೆ.
- **Microsoft Foundry Agent Service**: Microsoft Foundryದಲ್ಲಿನ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಮತ್ತು ನಿಯೋಜನಾ ಸೇವೆ. ಅದು Azure OpenAI, Azure AI Search, Bing Search ಮತ್ತು ಕೋಡ್ ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆಗೆ ನೇರ ಸಂಪರ್ಕವನ್ನು ಒದಗಿಸುತ್ತದೆ.
 
ಇನ್ನೂ ನಿರ್ಧಾರ ಮಾಡಿಕೊಂಡಿಲ್ಲವೇ?

### ಬಳಕೆ ಪ್ರಕರಣಗಳು
 
ಕೆಲವು ಸಾಮಾನ್ಯ ಬಳಕೆ ಪ್ರಕರಣಗಳನ್ನು ನೋಡಿ ನಿಮಗೆ ಸಹಾಯ ಮಾಡೋಣ:
 
> ಪ್ರಶ್ನೆ: ನಾನು ಉತ್ಪಾದನಾ AI ಏಜೆಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುತ್ತಿದ್ದೇನೆ ಮತ್ತು ತ್ವರಿತ ಪ್ರಾರಂಭ ಪಡೆಯಲು ಇಚ್ಛಿಸುತ್ತೇನೆ
>

>ಉತ್ತರ: Microsoft Agent Framework ಅತ್ಯುತ್ತಮ ಆಯ್ಕೆ. ಇದು `FoundryChatClient` ಮೂಲಕ ಸರಳ Pythonಿಕ API ಒದಗಿಸಿ, ಕೆಲ ಸಾಲು ಕೋಡ್ ಆಧರಿಸಿ ಉಪಕರಣಗಳು ಮತ್ತು ಸೂಚನೆಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.

>ಪ್ರಶ್ನೆ: ನನ್ನಿಗೆ ಉದ್ಯಮ ಮಟ್ಟದ ನಿಯೋಜನೆ, Search ಮತ್ತು ಕೋಡ್ ಕಾರ್ಯಗತಗೊಳಿಸುವಿಕೆ ಮುಂತಾದ Azure ಸಂಯೋಜನೆ ಬೇಕು
>
>ಉತ್ತರ: Microsoft Foundry Agent Service ಉತ್ತಮ ಹೊಂದಾಣಿಕೆ. ಇದು ವಿವಿಧ ಮಾದರಿ, Azure AI Search, Bing Search ಮತ್ತು Azure Functions ನ್ನು ಒಳಗೊಂಡಿರುವ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್ ಸೇವೆಯಾಗಿದ್ದು, Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಏಜೆಂಟ್ ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಮತ್ತು ವಿಸ್ತರಿಸಲು ಸುಲಭವಾಗಿಸುತ್ತದೆ.
 
> ಪ್ರಶ್ನೆ: ನಾನು ಇನ್ನೂ ಗೊಂದಲದಲ್ಲಿದ್ದೇನೆ, ಒಬ್ಬ ಆಯ್ಕೆಯನ್ನು ಕೊಡಿ
>
>ಉತ್ತರ: ಮೊದಲು Microsoft Agent Framework ನಿಂದ ನಿಮ್ಮ ಏಜೆಂಟ್ ಗಳನ್ನು ನಿರ್ಮಿಸಿ ಮತ್ತು ಉತ್ಪಾದನೆಯಲ್ಲಿ ನಿಯೋಜನೆ ಮತ್ತು ವಿಸ್ತರಣೆಗೆ Microsoft Foundry Agent Service ಬಳಸಿ. ಈ ವಿಧಾನವು ತ್ವರಿತ ಪುನರಾವರ್ತನೆಗೆ ಅನುಕೂಲ ಮಾಡಿಕೊಡುತ್ತದೆ ಮತ್ತು ಉದ್ಯಮ ನಿಯೋಜನೆಯ ಸ್ಪಷ್ಟ ಮಾರ್ಗವನ್ನು ಒದಗಿಸುತ್ತದೆ.
 
ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳನ್ನು ಟೇಬಲ್‌ನಲ್ಲಿ ಸಾರಾಂಶಿಸೋಣ:

| ಫ್ರೇಮ್ವರ್ಕ್ | ಕೇಂದ್ರಿತ | ಮೂಲ ಅಂಶಗಳು | ಬಳಕೆ ಪ್ರಕರಣಗಳು |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ಸಾಧನ ಕರೆಗಳೊಂದಿಗೆ ಸುಗಮಗೊಳಿಸಿದ ಏಜೆಂಟ್ SDK | ಏಜೆಂಟ್‌ಗಳು, ಉಪಕರಣಗಳು, Azure ಗುರುತುಮುಖ | AI ಏಜೆಂಟ್ ನಿರ್ಮಾಣ, ಉಪಕರಣ ಬಳಕೆ, ಬಹು ಹಂತದ ಕಾರ್ಯಪ್ರವಾಹಗಳು |
| Microsoft Foundry Agent Service | ವಿನ್ಯಸುಲಭ ಮಾದರಿ, ಉದ್ಯಮ ಸುರಕ್ಷತೆ, ಕೋಡ್ ರಚನೆ, ಉಪಕರಣ ಕರೆ | ಘಟಕೀಕರಣ, ಸಹಕಾರ, ಪ್ರಕ್ರಿಯಾ ಸಂಯೋಜನೆ | ಸುರಕ್ಷಿತ, ವಿಸ್ತಾರಗೊಳ್ಳುವ, ಮತ್ತು ವಿನ್ಯಾಸಗೊಳಿಸಿದ AI ಏಜೆಂಟ್ ನಿಯೋಜನೆ |

## ನನ್ನ ಇತ್ತೀಚಿನ Azure ಪರಿಸರದ ಸಾಧನಗಳನ್ನು ನೇರವಾಗಿ ಸಂಯೋಜಿಸಬಹುದೇ ಅಥವಾ ಸ್ವತಂತ್ರ ಪರಿಹಾರಗಳ ಅಗತ್ಯವಿದೆಯೇ?


ಉತ್ತರ ಹೌದು, ನೀವು ನಿಮ್ಮ ಈಗಿನ ಅಜೂರು ಪರಿಸರದಲ್ಲಿ ಇರುವ ಸಾಧನಗಳನ್ನು ನೇರವಾಗಿ Microsoft Foundry Agent Service ಜೊತೆ ಏಕೀಕರಿಸಬಹುದು, ವಿಶೇಷವಾಗಿ ಇದು ಇತರೆ ಅಜೂರು ಸೇವೆಗಳೊಂದಿಗೆ ಸುಗಮವಾಗಿ ಕೆಲಸ ಮಾಡುವಂತೆ ನಿರ್ಮಿಸಲಾಗಿದ್ದು. ಉದಾಹರಣೆಗೆ ನೀವು Bing, Azure AI Search, ಮತ್ತು Azure Functions ಅನ್ನು ಏಕೀಕರಿಸಬಹುದು. Microsoft Foundry ಜೊತೆ ಕೂಡ ಆಳವಾದ ಏಕೀಕರಣವಿದೆ.

Microsoft Agent Framework ಕೂಡ `FoundryChatClient` ಮತ್ತು ಅಜೂರಿನ ಗುರುತು ಇಲ್ಲದ ಸೇವೆಗಳ ಮೂಲಕ ಅಜೂರು ಸೇವೆಗಳಿಗೆ ಏಕೀಕರಿಸುತ್ತದೆ, ಇದು ನಿಮ್ಮ ಏಜೆಂಟ್ ಸಾಧನಗಳಿಂದ ನೇರವಾಗಿ ಅಜೂರು ಸೇವೆಗಳನ್ನು ಕರೆಸಲು ಅನುಮತಿಸುತ್ತದೆ.

## ಉದಾಹರಣಾ ಕೋಡ್ಗಳು

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಕುರಿತು ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿಸಿದ್ದೇ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ಗೆ ಸೇರಿ, ಇತರ ಕಲಿಯುವವರನ್ನೊಡನೆ ಭೇಟಿ ಮಾಡಿ, ಆಫೀಸ್ ಹೋಗಲು ಹಾಗೂ ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಪಡೆಯಿರಿ.

## ಉಲ್ಲೇಖಗಳು

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">ಅಜೂರು ಏಜೆಂಟ್ ಸೇವೆ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - ಅಜೂರು OpenAI ಪ್ರತಿಕ್ರಿಯೆಗಳು</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## ಹಿಂದಿನ ಪಾಠ

[AI ಏಜೆಂಟ್‌ಗಳ ಪರಿಚಯ ಮತ್ತು ಏಜೆಂಟ್ ಬಳಕೆಯ ಪ್ರಕರಣಗಳು](../01-intro-to-ai-agents/README.md)

## ಮುಂದಿನ ಪಾಠ

[ಏಜೆಂಟಿಕ್ ವಿನ್ಯಾಸ ಮಾದರಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->