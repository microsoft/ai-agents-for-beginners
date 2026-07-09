# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ವರ್ಕ್‌ಫ್ಲೋ ಬಳಸಿ ಬಹು-ಏಜೆಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ನಿರ್ಮಿಸುವುದು

ಈ ಟ್ಯುಟೋರಿಿಯಲ್ ನಿಮಗೆ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ ಬಹು-ಏಜೆಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಮತ್ತು ನಿರ್ಮಿಸಲು ಮಾರ್ಗದರ್ಶನ ನೀಡುತ್ತದೆ. ನಾವು ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಗಳ ಮೂಲ ಸಂವೇದನೆಗಳನ್ನು ಪರಿಶೀಲಿಸುವೆವು, ಫ್ರೇಮ್ವರ್ಕ್‌ನ ವರ್ಕ್‌ಫ್ಲೋ ಘಟಕದ ವಾಸ್ತುಶಿಲ್ಪವನ್ನು ಅನ್ವೇಷಿಸುವೆವು ಮತ್ತು ವಿವಿಧ ವರ್ಕ್‌ಫ್ಲೋ ನಕ್ಷತ್ರಗಳಿಗೆ ಪೈಥಾನ್ ಮತ್ತು .NET ನಲ್ಲಿ ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳನ್ನು ನಡೆಸುತ್ತೇವೆ.

## 1\. ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಗಳ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು

AI ಏಜೆಂಟ್ ಒಂದು ಸಾಮಾನ್ಯ ಲಾರ್ಜ್ ಲ್ಯಾಂಗ್ವೇಜ್ ಮಾದರಿ (LLM) ಗಿಂತ ಹೊರಗಿನ ಸಿಸ್ಟಮ್ ಆಗಿದೆ. ಇದು ತನ್ನ ಪರಿಸರವನ್ನು ಗ್ರಹಿಸಿ, ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದು, ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ಕ್ರಿಯೆಗಳನ್ನು ಚಲಿಸುತ್ತుంది. ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ ಇಂತಹ ಹಲವಾರು ಏಜೆಂಟ್‌ಗಳು ಸೇರಿ ಒಂದೇ ಏಜೆಂಟ್‌ಗಾಗಿ ನಡೆಸಲು ಕಷ್ಟವಾದ ಅಥವಾ ಅಸಾಧ್ಯವಾದ ಸಮಸ್ಯೆಯನ್ನು ಸಹಕಾರದಿಂದ ಪರಿಹರಿಸುತ್ತವೆ.

### ಸಾಮಾನ್ಯ ಅಪ್ಲಿಕೇಶನ್ ದೃಶ್ಯಗಳು

  * **ಸಂಕೀರ್ಣ ಸಮಸ್ಯೆ ಪರಿಹಾರ**: ದೊಡ್ಡ ಕಾರ್ಯವನ್ನು (ಉದಾ. ಕಂಪನಿ-ವ್ಯಾಪ್ತ ಕಾರ್ಯಕ್ರಮದ ಯೋಜನೆ) ವಿಶೇಷತೆಯ ಆಯುಕ್ತರು (ಉದಾ. ಬಜೆಟ್ ಏಜೆಂಟ್, ಲಾಜಿಸ್ಟಿಕ್ಸ್ ಏಜೆಂಟ್, ಮಾರುಕಟ್ಟೆ ಏಜೆಂಟ್) ಕೈಗಾರಿಕೆಗೊಳಿಸುವ ಸಣ್ಣ ಉಪಕಾರ್ಯಗಳಾಗಿ ವಿಭಜಿಸುವುದು.
  * **ವರ್ಚುವಲ್ ಸಹಾಯಕರು**: ಪ್ರಾಥಮಿಕ ಸಹಾಯಕ ಏಜೆಂಟ್ షೆಡ್ಯೂಲಿಂಗ್, ಸಂಶೋಧನೆ ಮತ್ತು ಬುಕ್ಕಿಂಗ್ ಮುಂತಾದ ಕಾರ್ಯಗಳನ್ನು ಇತರ ವಿಶೇಷ ಆಯುಕ್ತರಿಗೆ ನಿಯೋಜಿಸುವುದು.
  * **ಸ್ವಯಂಚಲಿತ ವಿಷಯ ಸೃಷ್ಟಿ**: ಒಂದು ಏಜೆಂಟ್ ವಿಷಯವನ್ನು ಕರಡುಮಾಡುವುದರಲ್ಲಿ ಇದ್ದರೆ, ಇನ್ನೊಂದು ಅದನ್ನು ನಿಖರತೆ ಮತ್ತು ಶ್ರುತಿಮತ್ತೆಗಾಗಿ ಪರಿಶೀಲಿಸುವುದು, ಮೂರನೇದು ಪ್ರಕಟಿಸುವುದು.

### ಬಹು-ಏಜೆಂಟ್ ಮಾದರಿಗಳು

ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಗಳು ವಿವಿಧ ಮಾದರಿಗಳಲ್ಲಿ ಸಂಯೋಜಿಸಬಹುದಾದವು, ಅವುಗಳ ಪರಸ್ಪರ ಕ್ರಿಯೆಯನ್ನು ನಿರ್ಧರಿಸುವುದು:

  * **ಕ್ರಮೇಣ (Sequential)**: ಏಜೆಂಟ್‌ಗಳು ಪೂರ್ವನಿಶ್ಚಿತ ಆದೇಶದಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತವೆ, ಸರ್ವಾಗಿ ಸಾಲುಗಳಂತೆ. ಒಂದನೇ ಏಜೆಂಟ್‌ನ ಔಟ್‌ಪುಟ್ ಮುಂದಿನ ಏಜೆಂಟ್‌ಗೆ ಸೂಚನೆ ಆಗುತ್ತದೆ.
  * **ಸಮಾನಕಾಲಿಕ (Concurrent)**: ಏಜೆಂಟ್‌ಗಳು ವಿಭಿನ್ನ ಭಾಗಗಳಲ್ಲಿ ಸಮಕಾಲೀನವಾಗಿ ಕೆಲಸಮಾಡುತ್ತವೆ ಮತ್ತು ಅವರ ಫಲಿತಾಂಶಗಳನ್ನು ಕೊನೆಯಲ್ಲಿ ಸಂಗ್ರಹಿಸಲಾಗುತ್ತದೆ.
  * **ಶರತುಕ (Conditional)**: ಏಜೆಂಟ್‌ನ ಔಟ್‌ಪುಟ್ ಆಧಾರದ ಮೇಲೆ ವರ್ಕ್‌ಫ್ಲೋ ವಿಭಿನ್ನ ದಾರಿಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ, if-then-else ಹೇಳಿಕೆಯನ್ನು ಹೋಲುತ್ತದೆ.

## 2\. ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ವರ್ಕ್‌ಫ್ಲೋ ವಾಸ್ತುಶಿಲ್ಪ

ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್‌ನ ವರ್ಕ್‌ಫ್ಲೋ ಸಿಸ್ಟಮ್ ಬಹು-ಏಜೆಂಟ್‌ಗಳ ನೆಡೆಸುವ ಸಂಕೀರ್ಣ ಸಮ್ಪರ್ಕಗಳನ್ನು ನಿರ್ವಹಿಸಲು ವಿನ್ಯಾಸಗೊಳ್ಳಲಾದ ಉನ್ನತ ಆರ್ಕೆಸ್ಟ್ರೇಷನ್ ಎಂಜಿನ್ ಆಗಿದೆ. ಇದು [ಪ್ರೆಗೇಲ್-ಶೈಲಿ ಕಾರ್ಯಗತಗೊಳಿಸುವ മാതೃಕೆಯ (Pregel-style execution model)](https://kowshik.github.io/JPregel/pregel_paper.pdf) ಒಂದು ಗ್ರಾಫ್ ಆಧಾರಿತ ವಾಸ್ತುಶಿಲ್ಪದಲ್ಲಿ ನಿರ್ಮಿಸಲಾಗಿದೆ, ಇಲ್ಲಿ ಪ್ರಕ್ರಿಯೆ "ಸೂಪರ್‌ಸ್ಟೆಪ್ಸ್" ಎಂದು ಕರೆಯಲ್ಪಡುವ ಕಾಲಮಾನದಲ್ಲಿ ಸಮಯೋಜಿತವಾಗಿ ನಡೆಯುತ್ತದೆ.

### ಮೂಲ ಘಟಕಗಳು

ವಾಸ್ತುಶಿಲ್ಪವು ಮೂರು ಪ್ರಮುಖ ಭಾಗಗಳಾಗಿ ರೂಪಗೊಂಡಿದೆ:

1.  **ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳು**: ಇವು ಮೂಲ ಪ್ರಕ್ರಿಯಾಪ್ರಣಾಳಿಕ ಘಟಕಗಳು. ನಮ್ಮ ಉದಾಹರಣೆಗಳಲ್ಲಿ, `Agent` ಒಂದು ಪ್ರಕಾರದ ಎಕ್ಸಿಕ್ಯೂಟರ್ ಆಗಿದೆ. ಪ್ರತಿ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಾಗಿ ಸಂದೇಶದ ಪ್ರಕಾರಾಧಾರಿತವಾಗಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕರೆಸಲ್ಪಡುವ ಅನೇಕ ಸಂದೇಶ ನಿರ್ವಹಕರಿರುತ್ತವೆ.
2.  **ಎಡ್ಜ್‌ಗಳು**: ಇವು ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳ ನಡುವಿನ ಸಂದೇಶಗಳ ಮಾರ್ಗವನ್ನು ನಿರ್ಧರಿಸುತ್ತವೆ. ಎಡ್ಜ್‌ಗಳಿಗೆ ನಿಯಮಗಳು ಇರಬಹುದು, ಇದರಿಂದ ವರ್ಕ್‌ಫ್ಲೋ ಗ್ರಾಫ್ ಮೂಲಕ ಮಾಹಿತಿಯ ಡೈನಾಮಿಕ್ ರೌಟಿಂಗ್ ಸಾಧ್ಯವಾಗುತ್ತದೆ.
3.  **ವರ್ಕ್‌ಫ್ಲೋ**: ಈ ಘಟಕ ಸಂಪೂರ್ಣ ಪ್ರಕ್ರಿಯೆಯನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ, ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳು, ಎಡ್ಜ್‌ಗಳು ಮತ್ತು ಒಟ್ಟಾರೆ ಕಾರ್ಯ ನಿರ್ವಹಣೆಯನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ. ಇದು ಸಂದೇಶಗಳನ್ನು ಸರಿಯಾದ ಕ್ರಮದಲ್ಲಿ ಪ್ರಾಸೆಸ್ ಮಾಡುವಂತೆ ನೋಡಿಕೊಳ್ಳುತ್ತದೆ ಮತ್ತು ದೃಷ್ಠಿಗೊಬ್ಬ ಹಂಚಿಕೆಗೆ ಈವೆಂಟುಗಳನ್ನು ಸ್ಟ್ರೀಮ್ ಮಾಡುತ್ತದೆ.

*ವರ್ಕ್‌ಫ್ಲೋ ಸಿಸ್ಟಮ್‌ನ ಮೂಲ ಘಟಕಗಳನ್ನು ಚಿತ್ರಿಸುವ ಚಿತ್ರದೊಂದಿಗೆ.*

ಈ ವಿನ್ಯಾಸವು ಕ್ರಮೇಣ ಸರಪಳಿ, ಸಮಾಂತರ ಸಂಸ್ಕರಣೆಗೆ ಫ್ಯಾನ್-ಔಟ್/ಫ್ಯಾನ್-ಇನ್, ಮತ್ತು ಶರತುಕ ಮುಂತಾದ ತತ್ವಜ್ಞಾನಗಳ ಮೂಲಕ ದೃಢ ಮತ್ತು ತರುತ್ತೇಟು ಹೊಂದಿರುವ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸಲು ಅವಕಾಶ ಒದಗಿಸುತ್ತದೆ.

## 3\. ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳು ಮತ್ತು ಕೋಡ್ ವಿಶ್ಲೇಷಣೆ

ಈಗ, ಫ್ರೇಮ್ವರ್ಕ್ ಬಳಸಿ ವಿವಿಧ ವರ್ಕ್‌ಫ್ಲೋ ಮಾದರಿಗಳನ್ನು ಹೇಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸಬೇಕು ಅಂತ ನೋಡೋಣ. ಪ್ರತಿ ಉದಾಹರಣೆಗೆ ಪೈಥಾನ್ ಮತ್ತು .NET ಕೋಡ್ ಅನ್ನು ವೀಕ್ಷಿಸುವೆವು.

### ಪ್ರಕರಣ 1: ಮೂಲ ಕ್ರಮೇಣ ವರ್ಕ್‌ಫ್ಲೋ

ಇದು ಅತ್ಯಂತ ಸರಳ ಮಾದರಿ, ಒಂದೇ ಏಜೆಂಟ್‌ನ ಔಟ್‌ಪುಟ್ ನೇರವಾಗಿ ಇನ್ನೊಂದು ಏಜೆಂಟ್‌ಗೆ ನೀಡುತ್ತದೆ. ನಮ್ಮ ದೃಶ್ಯದಲ್ಲಿ `FrontDesk` ಹೆಸರಿನ ಹೋಟೆಲ್ ಏಜೆಂಟ್ ಪ್ರವಾಸ ಸಲಹೆಯನ್ನು ನೀಡುತ್ತದೆ, ಅದನ್ನು `Concierge` ಏಜೆಂಟ್ ಪರಿಶೀಲಿಸುತ್ತದೆ.

*ಮೂಲ FrontDesk -> Concierge ವರ್ಕ್‌ಫ್ಲೋ ಚಿತ್ರ.*

#### ದೃಶ್ಯ ಹಿನ್ನೆಲೆ

ಯಾತ್ರಿಕನು ಪ್ಯಾರಿಸ್ ನಲ್ಲಿ ಸಲಹೆ ಕೇಳಿದ್ದಾನೆ.

1.  `FrontDesk` ಏಜೆಂಟ್, ಸರಳವಾಗಿ ವಿನ್ಯಾಸಗೊಳ್ಳಲಾಗಿದೆ, Louvre ಮ್ಯೂಸ್ಯಿಯಂಗೆ ಭೇಟಿ ನೀಡಲು ಸಲಹೆ ನೀಡುತ್ತದೆ.
2.  `Concierge` ಏಜ್ಞೆಂಟ್, ಪ್ರಾಮಾಣಿಕ ಅನುಭವಗಳನ್ನು ಪ್ರಾಥಮ್ಯಮಾಡುವವನು, ಈ ಸಲಹೆಯನ್ನು ಸ್ವೀಕರಿಸಿ ಪರಿಶೀಲನೆ ಮಾಡುತ್ತಾನೆ ಮತ್ತು ಹೆಚ್ಚಿನ ಸ್ಥಳೀಯ, ಕಡಿಮೆ ಪ್ರವಾಸಿಗರ ಆಯ್ಕೆ ಸೂಕ್ತವೆಂದು ಸಲಹೆ ನೀಡುತ್ತಾನೆ.

#### ಪೈಥಾನ್ ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

ಪೈಥಾನ್ ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಮೊದಲಿಗೆ ಎರಡು ಏಜೆಂಟ್‌ಗಳನ್ನು ಸ್ಫಷ್ಟವಾಗಿ ನಿರ್ದಿಷ್ಟ ಮಾಡಿ ಸೃಷ್ಟಿಸುತ್ತೇವೆ, ಪ್ರತಿಯೊಂದು ವಿಶಿಷ್ಟ ಸೂಚನೆಗಳೊಂದಿಗೆ.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# ಏಜೆಂಟ್ ಪಾತ್ರಗಳು ಮತ್ತು ಸೂಚನೆಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# ಏಜೆಂಟ್ ಉದಾಹರಣೆಗಳನ್ನು ರಚಿಸಿ
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

ನಂತರ, `WorkflowBuilder` ಅನ್ನು ಬಳಸಿಕೊಂಡು ಗ್ರಾಫ್ ಅನ್ನು ನಿರ್ಮಿಸುತ್ತೇವೆ. `front_desk_agent` ಪ್ರಾರಂಭಿಕ ಬಿಂದುವಾಗಿ ಸೆಟ್ ಮಾಡಲಾಗುತ್ತದೆ ಮತ್ತು ಅದರ ಔಟ್‌ಪುಟ್ ಅನ್ನು `reviewer_agent` ಗೆ ಸಂಪರ್ಕಿಸಲು ಒಂದು ಎಡ್ಜ್ ಸೃಷ್ಟಿಸಲಾಗುತ್ತದೆ.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

ಕೊನೆಗೆ, ಆರಂಭಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಸಹಿತ ವರ್ಕ್‌ಫ್ಲೋ ನಿರ್ವಹಣೆ ಮಾಡಲಾಗುತ್ತದೆ.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# ರನ್ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು_executable; get_outputs() ಹೆಚ್ಚು ಪರಿಣಾಮದ ನಿರ್ಗಮನವನ್ನು ಹಿಂತಿರುಗಿಸುತ್ತದೆ.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

.NET ಅನುಷ್ಠಾನ ಬಹು ತಹ ಕಾಣಿಕೆ ಪ್ರಕಾರವನ್ನು ಅನುಸರಿಸುತ್ತದೆ. ಮೊದಲಿಗೆ, ಏಜೆಂಟ್‌ಗಳ ಹೆಸರು ಮತ್ತು ಸೂಚನೆಗಳಿಗಾಗಿ ಸ್ಥಿರಾಂಕಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲಾಗುತ್ತದೆ.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ಏಜೆಂಟ್‌ಗಳನ್ನು `AzureOpenAIClient` (ಪ್ರತಿಕ್ರಿಯೆಗಳ API) ಬಳಸಿ ಸೃಷ್ಟಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ನಂತರ `WorkflowBuilder` ಅಡಿಯಿಂದ `frontDeskAgent` ನಿಂದ `reviewerAgent` ಗೆ ಕ್ರಮೇಣ ನಡೆಯುವ ಪ್ರವಾಹವನ್ನೂ ಸೇರಿಸುತ್ತದೆ.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

ಬಳಕೆದಾರನ ಸಂದೇಶದೊಂದಿಗೆ ವರ್ಕ್‌ಫ್ಲೋ ಚಾಲನೆ ಮಾಡಲಾಗುತ್ತದೆ ಮತ್ತು ಫಲಿತಾಂಶಗಳು ಸ್ಟ್ರೀಮ್ ಆಗಿ ಹಿಂತಿರುಗಲ್ಪಡುತ್ತವೆ.

### ಪ್ರಕರಣ 2: ಬಹು-ಹಂತ ಕ್ರಮೇಣ ವರ್ಕ್‌ಫ್ಲೋ

ಈ ಮಾದರಿ ಮೂಲ ಸರಣಿಯನ್ನು ವಿಸ್ತರಿಸಿ ಹೆಚ್ಚು ಏಜೆಂಟ್‌ಗಳನ್ನೊಳಗೊಂಡಂತೆ ಮಾಡಲಾಗಿದೆ. ಇದು ಅನೇಕ ಹಂತಗಳ ಸಂಶೋಧನೆ ಅಥವಾ ಪರಿವರ್ತನೆ ಬೇಕಾದ ಪ್ರಕ್ರಿಯೆಗಳಿಗೆ ಅನುಕೂಲಕರವಾಗಿದೆ.

#### ದೃಶ್ಯ ಹಿನ್ನೆಲೆ

ಬಳಕೆದಾರನು ಲಿವಿಂಗ್ ರೂಂನ ಒಂದು ಚಿತ್ರವನ್ನು ಒದಗಿಸಿ ಫರ್ನಿಚರ್ ಕೋಟ್ ಕೇಳುತ್ತಾನೆ.

1.  **ಸೆಲ್ಸ್-ಏಜೆಂಟ್**: ಚಿತ್ರದಲ್ಲಿನ ಫರ್ನಿಚರ್ ವಸ್ತುಗಳನ್ನು ಗುರುತಿಸಿ ಪಟ್ಟಿ ರಚಿಸುವುದು.
2.  **ಪ್ರೈಸ್-ಏಜೆಂಟ್**: ವಸ್ತುಗಳ ಪಟ್ಟಿಯನ್ನು ಪಡೆಯುತ್ತಾ ವಿವರವಾದ ಬೆಲೆಯ ವಿವರಣೆ (ಬಜೆಟ್, ಮಧ್ಯಮ ಶ್ರೇಣಿ, ಪ್ರೀಮಿಯಂ ಆಯ್ಕೆಗಳು) ನೀಡುವುದು.
3.  **ಕೋಟ್-ಏಜೆಂಟ್**: ಬೆಲೆಪಟ್ಟಿಯನ್ನು ಸ್ವೀಕರಿಸಿ ಅದನ್ನು ಮೀಸಲಾದ ಮಾರ್ಕ್‌ಡೌನ್ ರೂಪದಲ್ಲಿ ಅಧಿಕೃತ ಹೇಳಿಕೆಯಾಗಿ ರೂಪಿಸುವುದು.

*ಸೆಲ್ಸ್ -> ಪ್ರೈಸ್ -> ಕೋಟ್ ವರ್ಕ್‌ಫ್ಲೋ ಚಿತ್ರ.*

#### ಪೈಥಾನ್ ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

ಮೂರು ಏಜೆಂಟ್‌ಗಳನ್ನು ಪ್ರತಿಭಟನೆ ಮಾಡಲಾಗಿದೆ, ಪ್ರತಿಯೊಂದು ವಿಶೇಷ ಪಾತ್ರ ಹೊಂದಿದೆ. `add_edge` ಬಳಸಿ ಸರಪಳಿ ರೂಪಿಕೊಳಹಾಗಿದ್ದು: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ಮೂರು ವಿಶೇಷಿಕೃತ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಿ
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# ಕ್ರಮಬದ್ಧ ವರ್ಕ್‌ಫ್ಲೋ ನಿರ್ಮಿಸಿ
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ಇನ್‌ಪುಟ್ `ChatMessage` ಆಗಿದ್ದು, ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ URL ಎರಡನ್ನೂ ಒಳಗೊಂಡಿದೆ. ಫ್ರೇಮ್ವರ್ಕ್ ಪ್ರತಿ ಏಜೆಂಟ್‌ನ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಮುಂದಿನ ಏಜೆಂಟ್‌ಗೆ ಸರಣಿಯಾಗಿ ಪಾಸ್ಸುಮಾಡುತ್ತದೆ, ಕೊನೆಗೆ ಕೋಟ್ ಸೃಷ್ಟಿಸಲಾಗುತ್ತದೆ.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ಬಳಕೆದಾರ ಸಂದೇಶದಲ್ಲಿ ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ ಎರಡೂ ಸೇರಿವೆ
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಚಾಲನೆ ಮಾಡು
events = await workflow.run(message)
```

#### .NET (C\#) ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

.NET ಉದಾಹರಣೆ ಪೈಥಾನ್ ಆವೃತ್ತಿಯನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ. ಮೂರು ಏಜೆಂಟ್‌ಗಳು (`salesagent`, `priceagent`, `quoteagent`) ಸೃಷ್ಟಿಸಲ್ಪಟ್ಟಿವೆ. `WorkflowBuilder` ಅವರನ್ನು ಕ್ರಮವಾಗಿ ಜೋಡಿಸುತ್ತದೆ.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ಬಳಕೆದಾರನ ಸಂದೇಶವು ಚಿತ್ರದ ಡೇಟಾವನ್ನು (ಬೈಟ್ಸ್ ಆಕಾರದಲ್ಲಿ) ಮತ್ತು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಅನ್ನು ಲಭ್ಯವಾಗಿಸುವಂತೆ నిర్మಿಸಲ್ಪಟ್ಟಿದೆ. `InProcessExecution.StreamAsync` ವಿಧಾನವು ವರ್ಕ್‌ಫ್ಲೋ ಆರಂಭಿಸುತ್ತದೆ ಮತ್ತು ಕೊನೆಯ ಔಟ್‌ಪುಟ್ ಸ್ಟ್ರೀಮ್‌ನಿಂದ ಹಿಡಿದಿಡಲಿದೆ.

### ಪ್ರಕರಣ 3: ಸಮಂತರ ವರ್ಕ್‌ಫ್ಲೋ

ಈ ಮಾದರಿ ಕಾರ್ಯಗಳನ್ನು ಸಮಯ ಸೇವಿಸುವ ಉದ್ದೇಶದಿಂದ ಸಮ್ಮಿಲಿತವಾಗಿ ನಡೆಸುತ್ತದೆ. ಇದು ಹಲವು ಏಜೆಂಟ್‌ಗಳಿಗೆ "ಫ್ಯಾನ್-ಔಟ್" ಮತ್ತು ಫಲಿತಾಂಶಗಳನ್ನು ಸಂಗ್ರಹಿಸಿದ್ದಕ್ಕಾಗಿ "ಫ್ಯಾನ್-ಇನ್" ಅನ್ನು ಒಳಗೊಂಡಿದೆ.

#### ದೃಶ್ಯ ಹಿನ್ನೆಲೆ

ಬಳಕೆದಾರನು ಸಿಯಾಟಲ್ ಪ್ರವಾಸ ಯೋಜನೆ ಕೇಳುತ್ತಾನೆ.

1.  **ಡಿಸ್ಪ್ಯಾಚರ್ (ಫ್ಯಾನ್-ಔಟ್)**: ಬಳಕೆದಾರನ ವಿನಂತಿ ಒಟ್ಟಿನಲ್ಲಿ ಎರಡು ಏಜೆಂಟ್‌ಗಳಿಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ.
2.  **ಸಂಶೋಧಕ-ಏಜೆಂಟ್**: ಸಿಯಾಟಲ್ ಡಿಸೆಂಬರ್ ಮಾಸದ ಪ್ರವಾಸಕ್ಕೆ ಆಕರ್ಷಣೆಗಳು, ಹವಾಮಾನ ಮತ್ತು ಮುಖ್ಯ ವಿಚಾರಗಳನ್ನು ಸಂಶೋಧಿಸುತ್ತದೆ.
3.  **ಯೋಜನೆ-ಏಜೆಂಟ್**: ಸ್ವತಂತ್ರವಾಗಿ ಪ್ರತಿದಿನದ ತಪಾಸಣೆಯ ಪ್ರಯಾಣ ಯೋಜನೆಯನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ.
4.  **ಸಂಗ್ರಹಕಾರಿ (ಫ್ಯಾನ್-ಇನ್)**: ಸಂಶೋಧಕ ಮತ್ತು ಯೋಜಕರಿಂದ ಫಲಿತಾಂಶಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿ ಅಂತಿಮ ಫಲಿತಾಂಶವಾಗಿ ಒಟ್ಟುಗೂಡಿಸುತ್ತದೆ.

*ಸಮಾನಕಾಲಿಕ ಸಂಶೋಧಕ ಮತ್ತು ಯೋಜಕ ವರ್ಕ್‌ಫ್ಲೋ ಚಿತ್ರ.*

#### ಪೈಥಾನ್ ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

`ConcurrentBuilder` ಈ ಮಾದರಿಯನ್ನು ಎಲ್ಲಿಗೆ ಸರಳಗೊಳಿಸುತ್ತದೆ. ನೀವು ಭಾಗವಹಿಸುವ ಏಜೆಂಟ್‌ಗಳ ಪಟ್ಟಿ ನೀಡುತ್ತೀರಿ, ಬಿಲ್ಡರ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅಗತ್ಯ ಫ್ಯಾನ್-ಔಟ್ ಮತ್ತು ಫ್ಯಾನ್-ಇನ್ ಲಾಜಿಕ್ಗಳನ್ನು ರಚಿಸುತ್ತದೆ.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ಫ್ಯಾನ್-ಔಟ್/ಫ್ಯಾನ್-ಇನ್ ಲಾಜಿಕ್ ಅನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಚಲಾಯಿಸಿ
events = await workflow.run("Plan a trip to Seattle in December")
```

ಫ್ರೇಮ್ವರ್ಕ್ `research_agent` ಮತ್ತು `plan_agent` ಅನ್ನು ಸಮಕಾಲೀನವಾಗಿ ನಿರ್ವಹಿಸುತ್ತದೆ ಮತ್ತು ಅವರ ಕೊನೆಯ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ಪಟ್ಟಿಯಾಗಿ ಸಂಗ್ರಹಿಸುತ್ತದೆ.

#### .NET (C\#) ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

.NET ನಲ್ಲಿ ಈ ಮಾದರಿ ಸ್ಪಷ್ಟವಾದ ವ್ಯಾಖ್ಯಾನವನ್ನು ಅವಶ್ಯಕವಿದ್ದು. ಕಸ್ಟಮ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳಾದ`ConcurrentStartExecutor` ಮತ್ತು `ConcurrentAggregationExecutor` ಉದ್ಯೋಗಕ್ಕೆ ಫ್ಯಾನ್-ಔಟ್ ಮತ್ತು ಫ್ಯಾನ್-ಇನ್ ಲಾಜಿಕ್ಸ್ ಹೊಂದುತ್ತವೆ.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

ಬಳಿಕ `WorkflowBuilder` ಈ ಕಸ್ಟಮ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳು ಮತ್ತು ಏಜೆಂಟ್‌ಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಗ್ರಾಫ್ ನಿರ್ಮಿಸಲು `AddFanOutEdge` ಮತ್ತು `AddFanInEdge` ಬಳಸುತ್ತದೆ.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### ಪ್ರಕರಣ 4: ಶರತುಕ ವರ್ಕ್‌ಫ್ಲೋ

ಶರತುಕ ವರ್ಕ್‌ಫ್ಲೋಗಳು ಶಾಖರೇಖಾ ತತ್ವಜ್ಞಾನವನ್ನು ಪರಿಚಯಿಸುತ್ತವೆ, ಮಧ್ಯಂತರ ಫಲಿತಾಂಶಗಳ ಆಧಾರದ ಮೇಲೆ ವ್ಯವಸ್ಥೆ ವಿಭಿನ್ನ ಮಾರ್ಗಗಳನ್ನು ಅನುಸರಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.

#### ದೃಶ್ಯ ಹಿನ್ನೆಲೆ

ಈ ವರ್ಕ್‌ಫ್ಲೋ ತಾಂತ್ರಿಕ ಟ್ಯುಟೋರಿಯಲ್ ರಚನೆ ಮತ್ತು ಪ್ರಕಟಣೆಗೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನೆರವಾಗುತ್ತದೆ.

1.  **ಇವರು-ಏಜೆಂಟ್**: ಒದಗಿಸಿರುವ ರೂಪರೇಖೆ ಮತ್ತು URLs ಆಧರಿಸಿ ಟ್ಯುಟೋರಿಯಲ್ ಕರಡು ಬರೆಯುತ್ತಾನೆ.
2.  **ವಿಷಯಪಠ್ಯಪರಿಶೀಲಕ-ಏಜೆಂಟ್**: ಕರಡನ್ನು ಪರಿಶೀಲಿಸುತ್ತಾನೆ. ಶಬ್ದಸಂಖ್ಯೆ 200 ಪದಕ್ಕಿಂತ ಮೇಲು ಇದ್ದರೆ ತಪಾಸಣೆ ಮಾಡುತ್ತದೆ.
3.  **ಶರತುಕ ಶಾಖೆ**:
      * **ಅನుమೋದಿಸಿದರೆ (`ಹೌದು`)**: ವರ್ಕ್‌ಫ್ಲೋ `Publisher-Agent` ಕಡೆ ಮುಂದುವರೆಯುತ್ತದೆ.
      * **ನಿರಾಕರಿಸಿದರೆ (`ಇಲ್ಲ`)**: ವರ್ಕ್‌ಫ್ಲೋ ನಿಲ್ಲುತ್ತದೆ ಮತ್ತು ನಿರಾಕರಣೆಯ ಕಾರಣವನ್ನು ಹೊರಡಿಸುತ್ತದೆ.
4.  **ಪ್ರಕಟಣೆ-ಏಜೆಂಟ್**: ಕರಡು ಅನುಮೋದಿತವಾದರೆ, ಈ ಏಜೆಂಟ್ ವಿಷಯವನ್ನು ಮಾರ್ಕ್‌ಡೌನ್ ಕಡತವಾಗಿ ಉಳಿಸುತ್ತದೆ.

#### ಪೈಥಾನ್ ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಶರತುಕ ತತ್ವಜ್ಞಾನವೆಂದು `select_targets` ಎಂಬ ಕಸ್ಟಮ್ ಫಂಕ್ಷನ್ ಬಳಸಲಾಗಿದೆ. ಇದು `add_multi_selection_edge_group` ಗೆ ಪಾಸಾಗುತ್ತದೆ ಮತ್ತು ವಿಮರ್ಶಕನ ಔಟ್‌ಪುಟ್‌ನ `review_result` ಕ್ಷೇತ್ರವನ್ನು ಆಧರಿಸಿ ವರ್ಕ್‌ಫ್ಲೋವನ್ನು ನಿರ್ದೇಶಿಸುತ್ತದೆ.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ಈ ಕಾರ್ಯವು ವಿಮರ್ಶೆ ಫಲಿತಾಂಶದ ಆಧಾರದಲ್ಲಿ ಮುಂದಿನ ಹಂತವನ್ನು ನಿರ್ಧರಿಸುತ್ತದೆ
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ಅನುಮೋದನೆ ಇದ್ದರೆ, 'save_draft' ಕಾರ್ಯಾಚರಣೆಗೆ ಮುಂದುವರೆಯಿರಿ
        return [save_draft_id]
    else:
        # ನಿರಾಕರಣೆ ಇದ್ದರೆ, ವಿಫಲತೆಯನ್ನು ವರದಿಮಾಡಲು 'handle_review' ಕಾರ್ಯಾಚರಣೆಗೆ ಮುಂದುವರೆಯಿರಿ
        return [handle_review_id]

# ವರ್ಕ್ಫ್ಲೋ ನಿರ್ಮಾಪಕವು ಮಾರ್ಗದರ್ಶನೆಗಾಗಿ ಆಯ್ಕೆ ಕಾರ್ಯವನ್ನು ಬಳಸುತ್ತದೆ
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # ಬಹು-ಆಯ್ಕೆ ಎಡ್ಜ್ ಶರತ್ತು ಲಾಜಿಕ್ ಅನ್ನು ಜಾರಿಗೊಳಿಸುತ್ತದೆ
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` ಮುಂತಾದ ಕಸ್ಟಮ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳು ಏಜೆಂಟ್‌ಗಳಿಂದ JSON ಔಟ್‌ಪುಟ್ ಅನ್ನು ಬಲಪಟ್ಟುಗೊಳ್ಳುವ ರೀತಿಯ ವಸ್ತುಗಳಿಗೆ ಪರಿವರ್ತಿಸುತ್ತವೆ, ಅವುಗಳನ್ನು ಆರಿಸುವ ಫಂಕ್ಷನ್ ಪರಿಶೀಲಿಸಬಹುದು.

#### .NET (C\#) ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

.NET ಆವೃತ್ತಿ ಸಹ ಅದರಂತೆಯೇ ಶರತುಕ ಕಾರ್ಯಾಚರಣೆಗಾಗಿ ಸಮಾನ ವಿಧಾನವನ್ನು ಉಪಯೋಗಿಸುತ್ತದೆ. `Func<object?, bool>` ವ್ಯಾಖ್ಯಾನ ಮಾಡಲಾಗಿದೆ, ಇದು `ReviewResult` ವಸ್ತುವಿನ `Result` ಗುಣಲಕ್ಷಣವನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

`AddEdge` ವಿಧಾನದ `condition` ಪ್ಯಾರಾಮೀಟರ್ `WorkflowBuilder` ಗೆ ಶಾಖರೇಖಾ ಮಾರ್ಗ ನಿರ್ಮಿಸಲು ಅನುಮತಿಸುತ್ತದೆ. `GetCondition(expectedResult: "Yes")` ಶರತಿನಾಗಿದ್ದರೆ ಮಾತ್ರ `publishExecutor` ಗೆ ಮಾರ್ಗ ಅನುಸರಿಸಲಾಗುತ್ತದೆ. ಇಲ್ಲದಿದ್ದರೆ, `sendReviewerExecutor` ಗೆ ಮಾರ್ಗ ಅನುಸರಿಸುತ್ತದೆ.

## ಸಮಾರೋಹ

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ವರ್ಕ್‌ಫ್ಲೋ ಸಂಕೀರ್ಣ, ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಗಳ ಒರಕೆಸ್ಟ್ರೇಷನ್‌ಗೆ ದೃಢ ಮತ್ತು ನಿಗದಿತ ಆಧಾರ ಒದಗಿಸುತ್ತದೆ. ಅದರ ಗ್ರಾಫ್ ಆಧಾರಿತ ವಾಸ್ತುಶಿಲ್ಪ ಮತ್ತು ಮೂಲ ಘಟಕಗಳ ಮೂಲಕ, ಅಭಿವೃದ್ಧಿಪಡಿಸುವವರು ಪೈಥಾನ್ ಮತ್ತು .NET ಎರಡರಲ್ಲಿಯೂ ನುಡಿಸಬಹುದಾದ, ಸುಂದರ ತಂತ್ರಜ್ಞಾನಗಳನ್ನು ವಿನ್ಯಾಸ ಮತ್ತು ಅನುಷ್ಠಾನಗೊಳಿಸಬಹುದು. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಸರಳ ಕ್ರಮೇಣ ಪ್ರಕ್ರಿಯೆ, ಸಮಾಂತರ ಕಾರ್ಯಾಚರಣೆ ಅಥವಾ ಡೈನಾಮಿಕ್ ಶರತುಕ ಲಾಜಿಕ್ಗಳ ಅಗತ್ಯವಿದ್ದರೂ, ಈ ಫ್ರೇಮ್ವರ್ಕ್ ಶಕ್ತಿಶಾಲಿ, ವಿಸ್ತರಿಸಬಹುದಾದ ಮತ್ತು ಪ್ರಕಾರ-ಸುರಕ್ಷಿತ AI-ನಿರ್ವಹಿತ ಪರಿಹಾರಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸಲಕರಣೆಗಳನ್ನ ಒದಗಿಸುತ್ತದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->