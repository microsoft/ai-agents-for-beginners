[![AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳನ್ನು ಅನ್ವೇಷಣೆ ಮಾಡುವುದು](../../../translated_images/kn/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ಈ ಪಾಠದ ವಿಡಿಯೋ ನೋಡುವುದಕ್ಕಾಗಿ ಮೇಲಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ)_

# AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳನ್ನು ಅನ್ವೇಷಿಸಿ

AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು AI ಏಜೆಂಟ್‌ಗಳ ನಿರ್ಮಾಣ, ನಿಯೋಜನೆ ಮತ್ತು ನಿರ್ವಹಣೆಯನ್ನು ಸರಳಗೊಳಿಸುವ ಉದ್ದೇಶದ ಸಾಫ್ಟ್‌ವೇರ್ ವೇದಿಕೆಗಳಾಗಿವೆ. ಈ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳು, ಗಣನೆಗಳು ಮತ್ತು ಉಪಕರಣಗಳನ್ನು ಒದಗಿಸಿ ಜಟಿಲ AI ವ್ಯವಸ್ಥೆಗಳ ಅಭಿವೃದ್ಧಿಯನ್ನು ಸುಗಮಗೊಳಿಸುತ್ತವೆ.

ಈ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಸಾಮಾನ್ಯ ಸವಾಲುಗಳಿಗೆ ಮಾನಕ ವಿಧಾನಗಳನ್ನು ಒದಗಿಸುವ ಮೂಲಕ ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ತಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ಗಳ ವಿಶಿಷ್ಟ ಅಂಶಗಳ ಮೇಲೆ ಗಮನ ಹರಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ. ಇವು AI ವ್ಯವಸ್ಥೆಗಳ ನಿರ್ಮಾಣದಲ್ಲಿ ಪ್ರಮಾಣಬದ್ಧತೆ, ಪ್ರಾಪ್ಯತೆ ಮತ್ತು ಕಾರ್ಯದಕ್ಷತೆ ಹೆಚ್ಚಿಸುತ್ತವೆ.

## ಪರಿಚಯ

ಈ ಪಾಠದಲ್ಲಿ ನಾವು ಏನು ಕಾಣಲಿದ್ದು:

- AI ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಏನು ಮತ್ತು ಅವು ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಏನು ಸಾಧಿಸಲು ಅನುಮತಿಸುತ್ತವೆ?
- ತಂಡಗಳು ತನ್ನ ಏಜೆಂಟ್‌ಗಳ ಸಾಮರ್ಥ್ಯವನ್ನು ಬೇಗನೆ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡುವುದು, ಪುನರಾವರ್ತನೆ ಮಾಡುವುದು ಮತ್ತು ಸುಧಾರಿಸುವುದು ಹೇಗೆ?
- Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ಮತ್ತು <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>) ರಚಿಸಿದ ಫ್ರೇಮ್ವರ್ಕ್ ಮತ್ತು ಉಪಕರಣಗಳ ನಡುವೆ有什么 ವ್ಯತ್ಯಾಸಗಳಿವೆ?
- ಈಗಿರುವ Azure ಪರಿಸರ ಉಪಕರಣಗಳನ್ನು ನೇರವಾಗಿ ಎಂಟಿಗ್ರೇಟ್ ಮಾಡಬಹುದೇ, ಅಥವಾ ಸ್ವತಂತ್ರ ಪರಿಹಾರಗಳು ಬೇಕಾಗುತ್ತವೆ?
- Microsoft Foundry Agent Service ಎಂದರೆ ಏನು ಮತ್ತು ಇದು ನನಗೆ ಹೇಗೆ ಸಹಾಯ ಮಾಡುತ್ತಿದೆ?

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪಾಠದ ಉದ್ದೇಶಗಳು ನಿಮಗೆ ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಹಾಯ ಮಾಡುವುದು:

- AI Agent Frameworks ರ ಪಾತ್ರ AI ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ.
- ಬುದ್ದಿಮಂತ ಏಜೆಂಟ್‌ಗಳ ನಿರ್ಮಾಣಕ್ಕೆ AI Agent Frameworks ಬಳಸುವುದು ಹೇಗೆ.
- AI Agent Frameworks ಸಕ್ರಿಯಗೊಳಿಸುವ ಪ್ರಮುಖ ಸಾಮರ್ಥ್ಯಗಳು.
- Microsoft Agent Framework ಮತ್ತು Microsoft Foundry Agent Service ನಡುವಿನ ವ್ಯತ್ಯಾಸಗಳು.

## AI Agent Frameworks ಏನು ಮತ್ತು ಅವು ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ ಏನು ಮಾಡಲು ಅನುಮತಿಸುತ್ತವೆ?

ಸಾಂಪ್ರದಾಯಿಕ AI ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ AI ಸೇರಿಸಲು ಮತ್ತು ಈ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಕೆಳಗಿನ ರೀತಿಗಳಲ್ಲಿ ಉತ್ತಮಗೊಳಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ:

- **ವೈಯಕ್ತೀಕರಣ**: AI ಬಳಕೆದಾರರು ನಡೆಸುವ ಕ್ರಿಯೆಗಳ ಮತ್ತು ಇಷ್ಟಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ ವೈಯಕ್ತಿಕೃತ ಶಿಫಾರಸುಗಳು, ವಿಷಯ ಮತ್ತು ಅನುಭವಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.
ಉದಾಹರಣೆ: Netflix ಮುಂತಾದ ಸ್ಟ್ರೀಮಿಂಗ್ ಸೇವೆಗಳು ನೋಡುವ ಇತಿಹಾಸದ ಆಧಾರದ ಮೇಲೆ ಚಲನಚಿತ್ರಗಳು ಮತ್ತು ಶೋಗಳನ್ನು ಶಿಫಾರಸು ಮಾಡಲು AI ಅನ್ನು ಬಳಸುತ್ತವೆ, ಬಳಕೆದಾರನ ತೃಪ್ತಿ ಮತ್ತು ತೊಡಕನ್ನು ಹೆಚ್ಚಿಸುವುದು.
- **ಸ್ವಯಂಚಾಲಿತ ಮತ್ತು ಕಾರ್ಯದಕ್ಷತೆ**: AI ಪುನರಾವೃತ ಕೆಲಸಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಿ, ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಸರಳಗೊಳಿಸಿ ಮತ್ತು ಕಾರ್ಯಾಚರಣೆ ಕಾರ್ಯದಕ್ಷತೆಯನ್ನು ಸುಧಾರಿಸುತ್ತದೆ.
ಉದಾಹರಣೆ: ಗ್ರಾಹಕ ಸೇವೆ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಸಾಮಾನ್ಯ ಪ್ರಶ್ನೆಗಳನ್ನು ನಿಭಾಯಿಸಲು AI ಸಕ್ರಿಯ ಚಾಟ್‌ಬಾಟ್‌ಗಳನ್ನು ಬಳಸುತ್ತವೆ, ಪ್ರತಿಕ್ರಿಯಾ ಸಮಯವನ್ನು ಕಡಿಮೆ ಮಾಡುತ್ತವೆ ಮತ್ತು ಮಾನವ ಏಜೆಂಟ್‌ಗಳನ್ನು ಮತ್ತಷ್ಟು ಜಟಿಲ ವಿಷಯಗಳಿಗೆ ಮುಕ್ತಗೊಳಿಸುತ್ತವೆ.
- **ಉತ್ತಮ ಬಳಕೆದಾರ ಅನುಭವ**: AI ಧ್ವನಿ ಗುರುತರಿಕೆ, ಸಹಜ ಭಾಷಾ ಪ್ರಕ್ರಿಯೆ ಮತ್ತು ಮುನ್ಸೂಚಿಸಿದ ಪಠ್ಯ ಮುಂತಾದ ಬುದ್ಧಿವಂತ ಉಪಕರಣಗಳನ್ನು ಒದಗಿಸುವ ಮೂಲಕ ಒಟ್ಟು ಬಳಕೆದಾರ ಅನುಭವವನ್ನು ಉತ್ತಮಗೊಳಿಸುತ್ತದೆ.
ಉದಾಹರಣೆ: Siri ಮತ್ತು Google ಸಹಾಯಕರು ಧ್ವನಿ ಆಜ್ಞೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಮತ್ತು ಪ್ರತಿಕ್ರಿಯಿಸಲು AI ಬಳಸಿ ಬಳಕೆದಾರರಿಗೆ ಉಪಕರಣಗಳೊಂದಿಗೆ ಸುಲಭವಾಗಿ ಸಂವಹನ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.

### ಏನೊ ಅದೆಲ್ಲಾ ಚೆನ್ನಾಗಿದೆ, ಆದ್ರೆ ನಾವು AI Agent Framework ಬೇಕಾಗಿರುವುದು ಏಕೆ?

AI Agent ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಕೇವಲ AI ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳಲ್ಲ. ಅವು ಬುದ್ದಿವಂತ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ರೂಪುಗೊಂಡಿವೆ, ಅದು ಬಳಕೆದಾರರು, ಇತರೆ ಏಜೆಂಟ್‌ಗಳು ಮತ್ತು ಪರಿಸರದೊಂದಿಗೆ ಸಂವಹನ ನಡೆಸಿ ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸುತ್ತವೆ. ಈ ಏಜೆಂಟ್‌ಗಳು ಸ್ವಯಂ ಚಾಲಿತಾಳತನ ಪ್ರದರ್ಶಿಸಬಹುದು, ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಬಹುದು ಮತ್ತು ಬದಲಿಸುತ್ತಿರುವ ಪರಿಸ್ಥಿತಿಗಳಿಗೆ ಹೊಂದಿಕೊಳ್ಳಬಹುದು. AI Agent Frameworks ಸಕ್ರಿಯಗೊಳಿಸುವ ಕೆಲವು ಪ್ರಮುಖ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ನೋಡಿ:

- **ಏಜೆಂಟ್ ಸಹಕಾರ ಮತ್ತು ಸಂಯೋಜನೆ**: ಜಟಿಲ ಕಾರ್ಯಗಳನ್ನು ಬಗೆಹರಿಸಲು ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು AI ಏಜೆಂಟ್‌ಗಳು ಸೇರಿಕೊಂಡು ಕೆಲಸ ಮಾಡಲು, ಸಂವಹನ ಮಾಡಲು ಮತ್ತು ಸಂಯೋಜನೆ ಮಾಡಲು ಅನುಮತಿಸುತ್ತದೆ.
- **ಕಾರ್ಯ ಸ್ವಯಂಚಾಲನೆ ಮತ್ತು ನಿರ್ವಹಣೆ**: ಬಹು ಹಂತ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುವ ವ್ಯವಸ್ಥೆಗಳು, ಕಾರ್ಯ ವಿತರಣೆ ಮತ್ತು ಏಜೆಂಟ್‌ಗಳ ನಡುವೆ ಪ್ರಗತಿಪರ ಕಾರ್ಯ ನಿರ್ವಹಣೆ ಒದಗಿಸುತ್ತದೆ.
- **ಪರಿಣಾಮೂಲಾಗಿರುವ ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ ಮತ್ತು ಹೊಂದಿಕೆ**: ಸಂಬಂಧಿತ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಸಾಮರ್ಥ್ಯ, ಬದಲಿಯುತ್ತಿರುವ ಪರಿಸರಗಳೊಂದಿಗೆ ಹೊಂದಿಕೊಳ್ಳುವ ಮತ್ತು ನೈಜ-ಸಮಯ ಮಾಹಿತಿಯನ್ನು ಆಧರಿಸಿ ನಿರ್ಧಾರಗಳ ಕೈಗೊಳ್ಳುವ ಸಾಮರ್ಥ್ಯ.

ಸಾರಾಂಶವಾಗಿ, ಏಜೆಂಟ್‌ಗಳು ನಿಮಗೆ ಹೆಚ್ಚುವರಿ ಚಟುವಟಿಕೆಗಳನ್ನು ಅನುಮತಿಸುತ್ತವೆ, ಸ್ವಯಂಚಾಲನೆಯ ಮುಂದುವರಿದ ದರ್ಜೆಗೆ ಕಳೆಯಲು, ಬುದ್ಧಿವಂತ ವ್ಯವಸ್ಥೆಗಳನ್ನು ರಚಿಸಲು ಮತ್ತು ಅವು ಪರಿಸರದಿಂದ ಕಲಿಯುವಂತಿರುತ್ತವೆ.

## ಏಜೆಂಟ್ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಬೇಗನೆ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡುವುದು, ಪುನರಾವರ್ತನೆ ಮತ್ತು ಸುಧಾರಣೆ ಮಾಡುವುದು ಹೇಗೆ?

ಇದು ವೇಗವಾಗಿ ಬದಲಾಗುವ ಪರಿಸರ, ಆದರೆ ಬಹುಮಟ್ಟಿನ AI Agent Frameworks ಸಾಮಾನ್ಯವಾದ ಕೆಲವು ಅಂಶಗಳು ಇವೆ, ಅವು ನಿಮ್ಮನ್ನು ಬೇಗನೆ ಪ್ರೋಟೋಟೈಪ್ ಮಾಡಲು ಮತ್ತು ಪುನರಾವರ್ತನೆ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ - ಅಂದರೆ ಘಟಕ ಘಟಕಗಳು, ಸಹಕಾರ ಉಪಕರಣಗಳು ಮತ್ತು ನೈಜ-ಸಮಯ ಕಲಿಕೆ. ಇಲ್ಲಿವೆ ಅವುಗಳ ವಿವರ:

- **ಘಟಕ ಘಟಕಗಳನ್ನು ಬಳಸಿ**: AI SDKಗಳು ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ, ಉದಾ: AI ಮತ್ತು ಮೆಮೊರಿ ಕನೆಕ್ಟర్లు, ಸಹಜ ಭಾಷೆ ಅಥವಾ ಕೋಡ್ ಪ್ಲಗಿನ್‌ಗಳ ಮೂಲಕ ಕಾರ್ಯ ಕರೆ, ಪ್ರಾಂಪ್ಟ್ ಟೆಂಪ್ಲೇಟುಗಳು ಇತ್ಯಾದಿ.
- **ಸಹಕಾರಿ ಉಪಕರಣಗಳನ್ನು ಉಪಯೋಗಿಸಿ**: ನಿರ್ದಿಷ್ಟ ಪಾತ್ರಗಳು ಮತ್ತು ಕಾರ್ಯಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿನ್ಯಾಸ ಮಾಡಿ, ಸಹಕಾರಿ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ಮತ್ತು ಸುಧಾರಣೆ ಮಾಡಬಹುದು.
- **ನೈಜ-ಸಮಯದಲ್ಲಿ ಕಲಿಯಿರಿ**: ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನಗಳಿಂದ ಕಲಿಯುವ ಮತ್ತು ತನ್ನ ವರ್ತನೆಯನ್ನು ಗುಣಾತ್ಮಕವಾಗಿ ಸರಿಹೊಂದಿಸುವ ಪ್ರತಿಕ್ರಿಯಾ ಲೂಪ್‌ಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ.

### ಘಟಕ ಘಟಕಗಳನ್ನು ಬಳಸಿ

ಮೈಸೋಫ್ಟ್ ಎಜಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಮುಂತಾದ SDKಗಳು ಪೂರ್ವ-ನಿರ್ಮಿತ ಘಟಕಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ, ಉದಾಹರಣೆಗೆ AI ಸಂಪರ್ಕಗಳು, ಉಪಕರಣ ವ್ಯಾಖ್ಯಾನಗಳು ಮತ್ತು ಏಜೆಂಟ್ ನಿರ್ವಹಣೆ.

**ತಂಡಗಳು ಇದನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು**: ತಂಡಗಳು ಶೂನ್ಯದಿಂದ ಆರಂಭಿಸದೆ ಕಾರ್ಯನಿರ್ವಹಣೀಯ ಪ್ರೋಟೋಟೈಪನ್ನು ಬೇಗನೆ ಸಂಯೋಜಿಸಿ ತ್ವರಿತ ಪ್ರಯೋಗ ಮತ್ತು ಪುನರಾವರ್ತನೆಗೆ ಅನುಮತಿಸುತ್ತದೆ.

**ಪ್ರಾಯೋಗಿಕವಾಗಿ ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ಬಳಕೆದಾರ ಇನ್‌ಪುಟ್‌ನಿಂದ ಮಾಹಿತಿ ಹೊರತೆಗೆಯಲು ಪೂರ್ವ-ನಿರ್ಮಿತ ಪಾರ್ಸರ್ ಬಳಸಬಹುದು, ಡೇಟಾವನ್ನು ಸಂಗ್ರಹಿಸಲು ಮತ್ತು ಹುಡುಕಲು ಮೆಮೊರಿ ಘಟಕ, ಬಳಕೆದಾರರೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ಪ್ರಾಂಪ್ಟ್ ಜನರೇಟರ್ ಬಳಸಬಹುದು, ಇವೆಲ್ಲವು ನಿಮ್ಮಿಂದ ಸೃಷ್ಟಿಸುವ ಅಗತ್ಯವಿಲ್ಲದೆ.

**ಉದಾಹರಣಾ ಕೋಡ್**. Microsoft Agent Framework ಮತ್ತು `FoundryChatClient` ಉಪಯೋಗಿಸಿ ಬಳಕೆದಾರ ಇನ್‌ಪುಟಿಗೆ ಉಪಕರಣ ಕರೆ ಮಾಡುವುದಾಗಿ ಮಾದರಿಯನ್ನು ಪ್ರತಿಕ್ರಿಯಿಸುವುದೇ ಹೇಗೆ ನೋಡೋಣ:

``` python
# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಪೈಥಾನ್ ಉದಾಹರಣೆ

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# ಪ್ರಯಾಣ ಬುಕಿಂಗ್ ಮಾಡಲು ಒಂದು نمೂನಾ ಉಪಕರಣ ಫಂಕ್ಷನ್ ಅನ್ನು นิৰ್ದಿಷ್ಟ ಮಾಡಿ
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
    # ಉದಾಹರಣೆ ಔಟ್ಪುಟ್: ಜನವರಿ 1, 2025 ರಂದು ನ್ಯೂಯಾರ್ಕ್ಗೆ ನಿಮ್ಮ ವಿಮಾನ ಯಶಸ್ವಿಯಾಗಿ ಬುಕ್ ಮಾಡಲಾಗಿದೆ. ಸುರಕ್ಷಿತ ಪ್ರಯಾಣ! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ಈ ಉದಾಹರಣೆಯಿಂದ ನೀವು ನೋಡಬಹುದಾದುದು, ಬಳಕೆದಾರ ಇನ್‌ಪುಟಿನಿಂದ ಪ್ರಮುಖ ಮಾಹಿತಿಗಳನ್ನು (ಹಂಗಾಮಿ, ಗಮ್ಯಸ್ಥಾನ, ದಿನಾಂಕ) ಹೊರತೆಗೆಯಲು ಪೂರ್ವ-ನಿರ್ಮಿತ ಪಾರ್ಸರ್ ಬಳಸುವ ಇಂಗಿತ. ಈ ಘಟಕ ವಿಧಾನವು ಮೇಲ್ಮಟ್ಟ ಲಾಜಿಕ್ ಮೇಲೆ ನಿಮ್ಮನ್ನು ಕೇಂದ್ರೀಕರಿಸಲು ಅವಕಾಶ ನೀಡುತ್ತದೆ.

### ಸಹಕಾರಿ ಉಪಕರಣಗಳನ್ನು ಉಪಯೋಗಿಸಿ

Microsoft Agent Framework ಮುಂತಾದ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಏಜೆಂಟ್‌ಗಳು ಸೇರಿಕೊಂಡು ಕೆಲಸ ಮಾಡಲು ಅನುಕೂಲ ಮಾಡಿಕೊಡುತ್ತವೆ.

**ತಂಡಗಳು ಇದನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು**: ತಂಡಗಳು ನಿರ್ದಿಷ್ಟ ಪಾತ್ರಗಳು ಮತ್ತು ಕಾರ್ಯಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವಿನ್ಯಾಸ ಮಾಡಿ, ಸಹಕಾರಿ ಕಾರ್ಯಪ್ರವಾಹಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ಮತ್ತು ಸುಧಾರಣೆ ಮಾಡಬಹುದು ಮತ್ತು ಒಟ್ಟು ವ್ಯವಸ್ಥೆಯ ಕಾರ್ಯದಕ್ಷತೆಯನ್ನು ಹೆಚ್ಚಿಸಬಹುದು.

**ಪ್ರಾಯೋಗಿಕವಾಗಿ ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ನೀವು ಡೇಟಾ ಪಡೆಯುವುದು, ವಿಶ್ಲೇಷಣೆ, ನಿರ್ಧಾರ ಕೈಗೊಳ್ಳುವುದು ಮುಂತಾದ ವಿಶೇಷ ಕಾರ್ಯಗಳನ್ನು ಹೊಂದಿರುವ ಏಜೆಂಟ್‌ಗಳ ತಂಡವನ್ನು ರಚಿಸಬಹುದು. ಈ ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನ ಮಾಡಿಕೊಳ್ಳಿ ಮತ್ತು ಮಾತನಾಡಿ ಸಾಧನ ಗುರಿಯಿಗಾಗಿ ಮಾಹಿತಿ ಹಂಚಿಕೊಳ್ಳುತ್ತವೆ, ಉದಾಹರಣೆಗೆ ಬಳಕೆದಾರ ಪ್ರಶ್ನೆಗೆ ಉತ್ತರಿಸುವ ಅಥವಾ ಕಾರ್ಯ ನೆರವೇರಿಸುವಂತೆ.

**ಉದಾಹರಣಾ ಕೋಡ್ (Microsoft Agent Framework)**:

```python
# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ ಒಟ್ಟಿಗೆ ಕೆಲಸ ಮಾಡುವ ಬಹು ಏಜೆಂಟ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸುವುದು

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ಡೇಟಾ ಪಡೆಯುವ ಏಜೆಂಟ್
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

# ಕೆಲಸದ ಮೇಲೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ಕ್ರಮವಾಗಿ ರನ್ ಮಾಡುವುದು
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ ನೀವು ನೋಡುತ್ತಿರುವುದು, ಡೇಟಾವನ್ನು ವಿಶ್ಲೇಷಿಸಲು ಏಜೆಂಟ್‌ಗಳು ಸೇರಿಕೊಂಡು ಕಾರ್ಯ ನಿರ್ವಹಿಸುವ ಕಾರ್ಯವನ್ನು ಹೇಗೆ ರಚಿಸುವುದು. ಪ್ರತಿ ಏಜೆಂಟ್ ವಿಶೇಷ ಕಾರ್ಯವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ಕಾರ್ಯವನ್ನು ವಹಿಸಿ ನಿಶ್ಚಿತ ಫಲಿತಾಂಶವನ್ನು ಸಾಧಿಸಲು ಏಜೆಂಟ್‌ಗಳನ್ನು ಸಂಯೋಜಿಸಲಾಗುತ್ತದೆ. ವಿಶೇಷ ಪಾತ್ರಗಳೊಂದಿಗೆ ನಿಗದಿತ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವ ಮೂಲಕ ಕಾರ್ಯದಕ್ಷತೆ ಮತ್ತು ಪ್ರದರ್ಶನ ಹೆಚ್ಚುತ್ತದೆ.

### ನೈಜ-ಸಮಯದಲ್ಲಿ ಕಲಿಯಿರಿ

ನಿರ್ದಿಷ್ಟ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ನೈಜ-ಸಮಯ ಸಂಬಂಧಿತ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಮತ್ತು ಹೊಂದಿಕೊಳ್ಳುವ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.

**ತಂಡಗಳು ಇದನ್ನು ಹೇಗೆ ಬಳಸಬಹುದು**: ತಂಡಗಳು ಪ್ರತಿಕ್ರಿಯಾ ಚుట్టುಹಾಕುವಿಕೆಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ, ಏಜೆಂಟ್‌ಗಳು ಸಂವಹನಗಳಿಂದ ಕಲಿಯುವ ಮತ್ತು ತನ್ನ ವರ್ತನೆಯನ್ನು ಬದಲಿಸಿಕೊಂಡು ನಿರಂತರ ಸುಧಾರಣೆಗೆ ಮುನ್ನಡೆಯಬಹುದು.

**ಪ್ರಾಯೋಗಿಕವಾಗಿ ಇದು ಹೇಗೆ ಕೆಲಸ ಮಾಡುತ್ತದೆ**: ಏಜೆಂಟ್‌ಗಳು ಬಳಕೆದಾರ ಪ್ರತಿಕ್ರಿಯೆ, ಪರಿಸರದ ಡೇಟಾ ಮತ್ತು ಕಾರ್ಯ ಫಲಿತಾಂಶಗಳನ್ನು ವಿಶ್ಲೇಷಿಸಿ, ತಮ್ಮ ಜ್ಞಾನ ಭಂಡಾರವನ್ನು నవೀಕರಿಸುತ್ತವೆ, ನಿರ್ಧಾರದ ಆಲ್ಗೊರಿಥಮ್‌ಗಳನ್ನು ಸರಿಹೊಂದಿಸುತ್ತವೆ ಮತ್ತು ಸಮಯಕ್ಕಾಗಿ ಪ್ರದರ್ಶನವನ್ನು ಸುಧಾರಿಸುತ್ತವೆ. ಈ ಪುನರಾವರ್ತಿತ ಕಲಿಕೆ ಪ್ರಕ್ರಿಯೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ಬದಲಾಗುತ್ತಿರುವ ಸ್ಥಿತಿಗಳೊಂದಿಗೆ ಮತ್ತು ಬಳಕೆದಾರ ಇಷ್ಟಗಳೊಂದಿಗೆ ಹೊಂದಿಕೊಳ್ಳಲು ನೆರವು ಮಾಡುತ್ತದೆ, ಒಟ್ಟಾರೆ ವ್ಯವಸ್ಥೆಯ ಪರಿಣಾಮಕಾರಿತ್ವವನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.

## Microsoft Agent Framework ಮತ್ತು Microsoft Foundry Agent Service ನಡುವಿನ ವ್ಯತ್ಯಾಸಗಳು?

ಇವುಗಳನ್ನು ಹೋಲಿಸಲು ಅನೇಕ ರೀತಿಗಳು ಇವೆ, ಆದರೆ ಅವುಗಳ ವಿನ್ಯಾಸ, ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಗುರಿ ಬಳಕೆ ಪ್ರಕರಣಗಳ ದೃಷ್ಟಿಯಿಂದ ಕೆಲವು ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳನ್ನು ನೋಡೋಣ:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework `FoundryChatClient` ಬಳಸಿ AI ಏಜೆಂಟ್‌ಗಳ ನಿರ್ಮಾಣಕ್ಕೆ ಸರಳ SDK ಒದಗಿಸುತ್ತದೆ. ಇದು ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಿಗೆ Azure OpenAI ಮಾದರಿಗಳನ್ನು ಉಪಕರಣ ಕರೆ, ಸಂಭಾಷಣೆ ನಿರ್ವಹಣೆ ಮತ್ತು Azure ಗುರುತಿನ ಮೂಲಕ ಎಂಟರ್‌ಪ್ರೈಸ್-ಗ್ರೇಡ್ ಭದ್ರತೆ ಸಹಿತ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.

**ಬಳಕೆ ಪ್ರಕರಣಗಳು**: ಉಪಕರಣ ಬಳಕೆ, ಬಹು ಹಂತದ ಕಾರ್ಯಪ್ರವಾಹಗಳು ಮತ್ತು ಎಂಟರ್‌ಪ್ರೈಸ್ ಏಕರೂಪತೆ ಸೂಚಿಸುವ ಪ್ರೊಡಕ್ಷನ್-ತಯಾರ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು.

Microsoft Agent Framework ನ ಪ್ರಮುಖ ಮುಖ್ಯ ಅಂಶಗಳು ಇವು:

- **ಏಜೆಂಟ್‌ಗಳು**. `FoundryChatClient` ಮೂಲಕ ಏಜೆಂಟ್ ರಚಿಸಿ ಮತ್ತು ಹೆಸರು, ಸೂಚನೆಗಳು ಮತ್ತು ಉಪಕರಣಗಳೊಂದಿಗೆ ವ್ಯವಸ್ಥಿತಗೊಳಿಸಲಾಗುತ್ತದೆ. ಏಜೆಂಟ್:
  - **ಬಳಕೆದಾರ ಸಂದೇಶಗಳನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ** ಮತ್ತು Azure OpenAI ಮಾದರಿಗಳನ್ನು ಬಳಸಿ ಪ್ರತಿಕ್ರಿಯೆಗಳನ್ನು ರಚಿಸುತ್ತವೆ.
  - **ಸಂಭಾಷಣೆಯ.Context ಆಧಾರದ ಮೇಲೆ ಸಲಕರಣೆಗಳನ್ನು** ಸ್ವಯಂಚಾಲಿತ ಕರೆ ಮಾಡುತ್ತದೆ.
  - **ಬಹು ಸಂವಹನದ ರಾಜ್ಯವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ**.

  ಏಜೆಂಟ್ ರಚಿಸುವುದಕ್ಕಾಗಿ ಈ ಕೆಳಗಿನ ಕೋಡ್ ತುಣುಕು ನೋಡಿರಿ:

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

- **ಉಪಕರಣಗಳು**. ಫ್ರೇಮ್ವರ್ಕ್ ಏಜೆಂಟ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕರೆ ಮಾಡಬಹುದಾದ ಪೈಥಾನ್ ಕಾರ್ಯಗಳಾಗಿ ಉಪಕರಣಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವುದನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ. ಉಪಕರಣಗಳನ್ನು ಒಂದು ಏಜೆಂಟ್ ರಚಿಸುವಾಗ ನೋಂದಣಿ ಮಾಡಲಾಗುತ್ತದೆ:

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

- **ಬಹು-ಏಜೆಂಟ್ ಸಂಯೋಜನೆ**. ವಿಭಿನ್ನ ವಿಶೇಷತೆಗಳೊಂದಿಗೆ ಅನೇಕ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಿ ಮತ್ತು ಅವುಗಳ ಕೆಲಸವನ್ನು ಸಂಯೋಜಿಸಬಹುದು:

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

- **Azure ಗುರುತು ಏಕೀಕರಣ**. ಫ್ರೇಮ್ವರ್ಕ್ ಸುರಕ್ಷಿತ ಹಾಗೂ ಕೀಲಿಕೈ ಇಲ್ಲದ ಪ್ರಾಮಾಣೀಕರಣಕ್ಕಾಗಿ `AzureCliCredential` (ಅಥವಾ `DefaultAzureCredential`) ಬಳಸುತ್ತದೆ, API ಕೀಲಿಗಳನ್ನು ನೇರವಾಗಿ ನಿರ್ವಹಿಸುವ ಅಗತ್ಯವಿಲ್ಲ.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service 2024ರ Microsoft Ignite ನಲ್ಲಿ ಪರಿಚಯಿಸಲ್ಪಟ್ಟ ನವೀನ ಸೇವೆ. ಇದು ಕ್ರಿಯಾಶೀಲ ಎಲೆ=open-source LLMs(Llama 3, Mistral, Cohere ಮುಂತಾದ) ನೇರ ಕರೆ ಸೇರಿಕೊಂಡು AI ಏಜೆಂಟ್‌ಗಳ ಅಭಿವೃದ್ಧಿ ಮತ್ತು ನಿಯೋಜನೆಯನ್ನು ಹೆಚ್ಚು ಫ್ಲೆಕ್ಸಿಬಲ್ ಮಾದರಿಗಳೊಂದಿಗೆ ಅನುಮತಿಸುತ್ತದೆ.

Microsoft Foundry Agent Service ಬಲವಾದ ಎಂಟರ್‌ಪ್ರೈಸ್ ಭದ್ರತಾ ತಂತ್ರಗಳು ಮತ್ತು ಡೇಟಾ ಸಂಗ್ರಹಣಾ ವಿಧಾನಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ, ಇದರಿಂದ ಅದನ್ನು ಎಂಟರ್‌ಪ್ರೈಸ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಸೂಕ್ತ ಮಾಡುತ್ತದೆ.

Microsoft Agent Framework ಜೊತೆಗೆ ಈ ಸೇವೆ ಔಟ್-ಆಫ್-ದಿ-ಬಾಕ್ಸ್ ಕಾರ್ಯಾಚರಣೆಯೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳ ನಿರ್ಮಾಣ ಮತ್ತು ನಿಯೋಜನೆಗೆ ಸಕಾಯಕವಾಗಿದೆ.

ಈ ಸೇವೆ ಪ್ರಸ್ತುತ ಪಬ್ಲಿಕ್ ಪ್ರಿವ್ಯೂದಲ್ಲಿದೆ ಮತ್ತು Python ಮತ್ತು C# ಮೂಲಕ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಬೆಂಬಲ ನೀಡುತ್ತದೆ.

Microsoft Foundry Agent Service Python SDK ಉಪಯೋಗಿಸಿ, ಬಳಕೆದಾರ-ವ್ಯಾಖ್ಯಾನಿತ ಉಪಕರಣ ಒದಗಿಸಿ ಏಜೆಂಟ್ ರಚಿಸಬಹುದು:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# ಸಾಧನ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ದಿಷ್ಟಪಡಿಸಿ
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

### ಮೂಲ ಅಂಶಗಳು

Microsoft Foundry Agent Service ಈ ಕೆಳಗಿನ ಮೂಲ ಅಂಶಗಳನ್ನು ಹೊಂದಿದೆ:

- **ಏಜೆಂಟ್**. Microsoft Foundry Agent Service Microsoft Foundry ಜೊತೆಗೆ ಏಕೀಕರಿಸಲಾಗಿದೆ. Microsoft Foundry ಒಳಗೆ AI ಏಜೆಂಟ್ "ಬುದ್ಧಿವಂತ" ಮೈನಿಸರ್ವಿಸ್‌ ಆಗಿದ್ದು ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಲು (RAG), ಕ್ರಿಯೆಗಳು ನಿರ್ವಹಿಸಲು ಅಥವಾ ಕಾರ್ಯಪದ್ಧತಿಗಳನ್ನು ಪೂರ್ಣವಾಗಿ ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ. ಇದು ಜನರೇಟಿವ್ AI ಮಾದರಿಯ ಶಕ್ತಿಯೊಂದಿಗೆ ಉಪಕರಣಗಳನ್ನು ಸಂಯೋಜಿಸಿ ನೈಜ ಲೋಕದ ಡೇಟಾ ಮೂಲಗಳಿಗೆ ಪ್ರವೇಶ ಹಾಗೂ ಸಂವಹನವನ್ನು ಅನುಮತರಿಸುತ್ತದೆ. ಇಲ್ಲಿದೆ ಏಜೆಂಟ್ ಉದಾಹರಣೆ:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    ಈ ಉದಾಹರಣೆಯಲ್ಲಿ`gpt-4o-mini` ಮಾದರಿ, ಹೆಸರು `my-agent` ಮತ್ತು ಸೂಚನೆ `ನೀವು ಸಹಾಯಕ ಏಜೆಂಟ್` ಇವೆಂದು ಏಜೆಂಟ್ ರಚಿಸಲಾಗಿದೆ. ಈ ಏಜೆಂಟ್ ಕೋಡ್ ವಿವರಣೆ ಕಾರ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಉಪಕರಣಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲಗಳೊಂದಿಗೆ ಸಜ್ಜಾಗಿದೆ.

- **ಥ್ರೆಡ್ ಮತ್ತು ಸಂದೇಶಗಳು**. ಥ್ರೆಡ್ ಒಂದು ಇನ್ನೊಂದು ಪ್ರಮುಖ ಅಂಶ. ಇದು ಏಜೆಂಟ್ ಮತ್ತು ಬಳಕೆದಾರರ ನಡುವಿನ ಸಂಭಾಷಣೆ ಅಥವಾ ಸಂವಹನವನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತದೆ. ಥ್ರೆಡ್‌ಗಳನ್ನು ಸಂಭಾಷಣೆಯ ಪ್ರಗತಿಯನ್ನು ಹಂಗಿಸುವುದು, ಕಾಂ텍ಸ್ಟ್ ಮಾಹಿತಿಯನ್ನು ಸಂಗ್ರಹಿಸುವುದು ಮತ್ತು ಸಂವಹನದ ಸ್ಥಿತಿಯ ನಿರ್ವಹಣೆಗಾಗಿ ಬಳಸಬಹುದು. ಇಲ್ಲಿ ಥ್ರೆಡ್ ಉದಾಹರಣೆ:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # ಏಜೆಂಟ್‌ನ್ನು ಥ್ರೆಡ್‌ನಲ್ಲಿ ಕೆಲಸ ಮಾಡಲು ಕೇಳಿ
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # ಏಜೆಂಟ್‌ನ ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೋಡಲು ಎಲ್ಲಾ ಸಂದೇಶಗಳನ್ನು ಪಡೆಯಿರಿ ಮತ್ತು ದಾಖಲಿಸಿ
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    ಹಿಂದಿನ ಕೋಡಿನಲ್ಲಿ, ಥ್ರೆಡ್ ರಚಿಸಲಾಗಿದೆ. ನಂತರ, ಥ್ರೆಡ್‌ಗೆ ಸಂದೇಶ ಕಳುಹಿಸಲಾಗಿದೆ. `create_and_process_run` ಕರೆಯುವುದರಿಂದ, ಏಜೆಂಟ್ ಥ್ರೆಡ್ ಮೇಲೆ ಕಾರ್ಯ ನಿರ್ವಹಿಸಲು ಕೇಳಲಾಗಿದೆ. ಕೊನೆಯಲ್ಲಿ, ಸಂದೇಶಗಳು ಪಡೆದು ಪ್ರತಿಕ್ರಿಯೆ ಲಾಗ್ ಮಾಡಲಾಗಿದೆ. ಮಂದಿ ಮತ್ತು ಏಜೆಂಟ್ ನಡುವಿನ ಸಂಭಾಷಣೆಯ ಪ್ರಗತಿಯನ್ನು ಸಂದೇಶಗಳು ಸೂಚಿಸುತ್ತವೆ. ಸಂದೇಶಗಳು ಪಠ್ಯ, ಚಿತ್ರ ಅಥವಾ ಕಡತ ಮುಂತಾದ ವಿವಿಧ ಪ್ರಕಾರಗಳಾಗಿರಬಹುದು, ಉದಾಹರಣೆಗೆ ಏಜೆಂಟ್ ಕಾರ್ಯದ ಫಲವಾಗಿ ಚಿತ್ರ ಅಥವಾ ಪಠ್ಯ ಪ್ರತಿಕ್ರಿಯೆಯಾಗಿರಬಹುದು. ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರಾಗಿ ನೀವು ಈ ಮಾಹಿತಿಯನ್ನು ಇನ್ನಷ್ಟು ಪ್ರಕ್ರಿಯೆ ಮಾಡಲು ಅಥವಾ ಬಳಕೆದಾರರಿಗೆ ಪ್ರದರ್ಶಿಸಲು ಬಳಸಬಹುದು.

- **Microsoft Agent Framework ಜೊತೆಗೆ ಏಕೀಕರಣ**. Microsoft Foundry Agent Service Microsoft Agent Framework ಜೊತೆಗೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ, ಅಂದರೆ ನೀವು `FoundryChatClient` ಉಪಯೋಗಿಸಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಿ, ಅವುಗಳನ್ನು ಏಜೆಂಟ್ ಸೇವೆಯ ಮೂಲಕ ಉತ್ಪಾದನಾ ಪರಿಸರಗಳಲ್ಲಿ ನಿಯೋಜಿಸಬಹುದು.

**ಬಳಕೆ ಪ್ರಕರಣಗಳು**: Microsoft Foundry Agent Service ಸುರಕ್ಷಿತ, ಪ್ರಮಾಣಬದ್ಧ ಮತ್ತು ಫ್ಲೆಕ್ಸಿಬಲ್ AI ಏಜೆಂಟ್ ನಿಯೋಜನೆಯನ್ನು ಅಗತ್ಯವಿರುವ ಎಂಟರ್‌ಪ್ರೈಸ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಿಗೆ ಯೋಜಿಸಲಾಗಿದೆ.

## ಈ ವಿಧಾನಗಳ ನಡುವೆ ವ್ಯತ್ಯಾಸವೇನು?
 
ಅವುಗಳಲ್ಲಿ ಕೆಲವು ಆಸಕ್ತಿದಾಯಕ ಸಾಮಾನ್ಯತೆಗಳಿವೆ, ಆದರೆ ವಿನ್ಯಾಸ, ಸಾಮರ್ಥ್ಯಗಳು ಮತ್ತು ಗುರಿ ಬಳಸುವ ವಿಧಾನಗಳಲ್ಲಿ ಕೆಲ ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳಿವೆ:
 
- **Microsoft Agent Framework (MAF)**: AI ಏಜೆಂಟ್‌ಗಳ ನಿರ್ಮಾಣಕ್ಕೆ ಉತ್ಪಾದನಾ-ಸಿದ್ಧ SDK. ಉಪಕರಣ ಕರೆ, ಸಂಭಾಷಣೆ ನಿರ್ವಹಣೆ ಮತ್ತು Azure ಗುರುತು ಏಕೀಕರಣದೊಂದಿಗೆ ಸರಳ API ಒದಗಿಸುತ್ತದೆ.
- **Microsoft Foundry Agent Service**: Microsoft Foundryಯಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳಿಗೆ ವೇದಿಕೆ ಮತ್ತು ನಿಯೋಜನಾ ಸೇವೆ. ಇದು Azure OpenAI, Azure AI Search, Bing Search ಮತ್ತು ಕೋಡ್ ಕಾರ್ಯಾಚರಣೆಗೆ ಒಳಗೊಂಡ ಬಿಲ್ಟ್-ಇನ್ ಸಂಪರ್ಕವನ್ನು ನೀಡುತ್ತದೆ.
 
ಇನ್ನೂ ಯಾವದು ಆರಿಸುವುದು ತಿಳಿಯದಿದೇ?

### ಬಳಕೆ ಪ್ರಕರಣಗಳು
 
ಕೆಲವು ಸಾಮಾನ್ಯ ಬಳಕೆ ಪ್ರಕರಣಗಳಿಂದ ನಿಮಗೆ ಸಹಾಯ ಮಾಡುವುದಾಗಿ ನೋಡೋಣ:
 
> ಪ್ರಶ್ನೆ: ನಾನು ಪ್ರೊಡಕ್ಷನ್ AI ಏಜೆಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುತ್ತಿದ್ದೇನೆ ಮತ್ತು ಶೀಘ್ರ ಪ್ರಾರಂಭ ಮಾಡಬೇಕಾಗಿದೆ
>

>ಉತ್ತರ: Microsoft Agent Framework ಉತ್ತಮ ಆಯ್ಕೆ. ಇದು `FoundryChatClient` ಮೂಲಕ ಸರಳ, ಪೈಥಾನಿಕ್ API ನೀಡುತ್ತದೆ, ಇದು ಕೆಲ ಸಾಲು ಕೈಪಿಡಿಯಲ್ಲೇ ಉಪಕರಣಗಳೊಂದಿಗೆ ಏಜೆಂಟ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.

> ಪ್ರಶ್ನೆ: ನನಗೆ ಅನ್ವೇಷಣೆ ಮತ್ತು ಕೋಡ್ ಕಾರ್ಯಾಚರಣೆಗಳು ಹಾಗು Azure ಏಕೀಕರಣಗಳೊಂದಿಗೆ ಎಂಟರ್‌ಪ್ರೈಸ್-ಗ್ರೇಡ್ ನಿಯೋಜನೆ ಬೇಕು
>
> ಉತ್ತರ: Microsoft Foundry Agent Service ಅತ್ಯುತ್ತಮ. ಇದು ವಾನಿಗೋತ್ತಾದ ಡೇಟಾ ಮೂಲಗಳಿಗೆ ಸಂಪರ್ಕ, Azure AI Search, Bing Search ಮತ್ತು Azure Functions ಒಳಗೊಂಡ ವೇದಿಕೆ ಸೇವೆ. ನೀವು Foundry ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ಸುಲಭವಾಗಿ ನಿರ್ಮಿಸಿ ದೊಡ್ಡ ಪ್ರಮಾಣದಲ್ಲಿ ನಿಯೋಜಿಸಬಹುದು.
 
> ಪ್ರಶ್ನೆ: ನಾನು ಇನ್ನೂ ಗುರುತಿಸಲು ಗೊಂದಲದಲ್ಲಿದ್ದೇನೆ, ಒಂದೇ ಆಯ್ಕೆಯನ್ನು ನೀಡಿ
>
> ಉತ್ತರ: ನಿಮ್ಮ ಏಜೆಂಟ್‌ಗಳ ನಿರ್ಮಾಣಕ್ಕೆ ಮೊದಲು Microsoft Agent Framework ಬಳಸಿ ಪ್ರಾರಂಭಿಸಿ, ನಂತರ ಉತ್ಪಾದನೆಯಲ್ಲಿ ನಿಯೋಜನೆ ಮತ್ತು ಪ್ರಮಾಣಗೊಳಿಸಲು Microsoft Foundry Agent Service ಬಳಸಿರಿ. ಈ ವಿಧಾನದಿಂದ ನೀವು ವೇಗವಾಗಿ ಏಜೆಂಟ್ ತರ್ಕವನ್ನು ಪುನರಾವರ್ತಿಸಬಹುದು ಮತ್ತು ನಿರಂತರವಾಗಿ ಎಂಟರ್‌ಪ್ರೈಸ್ ನಿಯೋಜನೆಗೆ ಸಿದ್ಧ ಹೆಜ್ಜೆಯನ್ನು ಹೊಂದಬಹುದು.
 
ಪ್ರಮುಖ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಒಂದು ಪಟ್ಟಿಯಲ್ಲಿ ಸಂಕ್ಷಿಪ್ತಗೊಳಿಸೋಣ:

| ಫ್ರೇಮ್ವರ್ಕ್ | ಕೇಂದ್ರೀಕೃತಿ | ಮೂಲ ಅಂಶಗಳು | ಬಳಕೆ ಪ್ರಕರಣಗಳು |
| --- | --- | --- | --- |
| Microsoft Agent Framework | ಉಪಕರಣ ಕರೆ ಹೊಂದಿದ ಸರಳ ಏಜೆಂಟ್ SDK | ಏಜೆಂಟ್‌ಗಳು, ಉಪಕರಣಗಳು, Azure ಗುರುತು | AI ಏಜೆಂಟ್‌ಗಳ ನಿರ್ಮಾಣ, ಉಪಕರಣ ಬಳಕೆ, ಬಹು ಹಂತದ ಕಾರ್ಯಪ್ರವಾಹಗಳು |
| Microsoft Foundry Agent Service | ಫ್ಲೆಕ್ಸಿಬಲ್ ಮಾದರಿಗಳು, ಎಂಟರ್‌ಪ್ರೈಸ್ ಭದ್ರತೆ, ಕೋಡ್ ಜನರೇಶನ್, ಉಪಕರಣ ಕರೆ | ಘಟಕತೆ, ಸಹಕಾರ, ಪ್ರಕ್ರಿಯೆ ಸಂಯೋಜನೆ | ಸುರಕ್ಷಿತ, ಪ್ರಮಾಣಬದ್ಧ ಮತ್ತು ಫ್ಲೆಕ್ಸಿಬಲ್ AI ಏಜೆಂಟ್ ನಿಯೋಜನೆ |

## ಈಗಿರುವ Azure ಪರಿಸರ ಉಪಕರಣಗಳನ್ನು ನೇರವಾಗಿ ಎಂಟಿಗ್ರೇಟ್ ಮಾಡಬಹುದೇ, ಅಥವಾ ಸ್ವತಂತ್ರ ಪರಿಹಾರಗಳು ಬೇಕಾಗುತ್ತವೆ?


ಉತ್ತರ ಹೌದು, ನೀವು ನಿಮ್ಮ विद्यमान Azure ಪರಿparisara ಸಾಧನಗಳನ್ನು ನೇರವಾಗಿ Microsoft Foundry Agent Service ಜೊತೆಗೆ ಸಂಯೋಜಿಸಬಹುದು, ವಿಶೇಷವಾಗಿ ಇದು ಇತರ Azure ಸೇವೆಗಳೊಂದಿಗೆ ಸ್ಮೂತ್ ಆಗಿ ಕೆಲಸ ಮಾಡಲು ನಿರ್ಮಿಸಲಾಗಿದೆ. ಉದಾಹರಣೆಗೆ ನೀವು Bing, Azure AI Search, ಮತ್ತು Azure Functions ಅನ್ನು ಸಂಯೋಜಿಸಬಹುದು. Microsoft Foundry ಸಹ ತೀವ್ರ ಸಂಯೋಜನೆಯನ್ನು ಹೊಂದಿದೆ.

Microsoft Agent Framework ಕೂಡ `FoundryChatClient` ಮತ್ತು Azure identity ಮೂಲಕ Azure ಸೇವೆಗಳೊಂದಿಗೆ ಸಂಯೋಜಿಸುತ್ತದೆ, ಇದರಿಂದ ನೀವು ನಿರ್ದಿಷ್ಟವಾಗಿ ನಿಮ್ಮ ಏಜೆಂಟ್工具ಗಳಿಂದ Azure ಸೇವೆಗಳನ್ನು ಕರೆದೊಯ್ಯಬಹುದು.

## ಮಾದರಿ ಕೋಡ್‌ಗಳು

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್‌ಗಳ ಕುರಿತು ಇನ್ನಷ್ಟು ಪ್ರಶ್ನೆಗಳಿವರಾ?

ಬೇರೆಯ ಅಧ್ಯಯನಾರ್ಥಿಗಳನ್ನು ಭೇಟಿಯಾಗಲು, ಕಚೇರಿ ಸಮಯಗಳಲ್ಲಿ ಭಾಗವಹಿಸಲು ಮತ್ತು ನಿಮ್ಮ AI ಏಜೆಂಟ್ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರ ಪಡೆಯಲು [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ಅಥವಾ ಸೇರಿ.

## ಉಲ್ಲೇಖಗಳು

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## ಹಿಂದಿನ ಪಾಠ

[AI ಏಜೆಂಟ್ಗಳ ಪರಿಚಯ ಮತ್ತು ಏಜೆಂಟ್ ಬಳಕೆ ಪ್ರಕರಣಗಳು](../01-intro-to-ai-agents/README.md)

## ಮುಂದಿನ ಪಾಠ

[Agentic ವಿನ್ಯಾಸ ಮಾದರಿಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->