# ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೆಮ್ವರ್ಕ್ ವರ್ಕ್‌ಫ್ಲೋ ಬಳಸಿ ಬಹು-ಏಜೆಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು

ಈ ಟ್ಯುಟೋರಿಯಲ್‌ನಲ್ಲಿ ನೀವು ಮೈಕ್ಟ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೆಮ್ವರ್ಕ್ ಬಳಸಿ ಬಹು-ಏಜೆಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದರ ಮೂಲಕ ಮತ್ತು ನಿರ್ಮಿಸುವುದರ ಮೂಲಕ ಮಾರ್ಗದರ್ಶನ ಮಾಡಲಾಗುತ್ತದೆ. ನಾವು ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಗಳ ಮೂಲ ತತ್ವಗಳನ್ನು ಅನ್ವೇಷಿಸುವುದೆಂದು, ಫ್ರೆಮ್ವರ್ಕ್‌ನ ವರ್ಕ್‌ಫ್ಲೋ ಅಂಗಡಿಯ ಆರ್ಕಿಟೆಕ್ಟچر ಅನ್ನು ಪರಿಶೀಲಿಸುವುದೆಂದು, ಮತ್ತು ವಿಭಿನ್ನ ವರ್ಕ್‌ಫ್ಲೋ ಮಾದರಿಗಳಿಗೆ Python ಮತ್ತು .NET ರಲ್ಲಿ ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳನ್ನು ಪರಿಶೀಲಿಸುವುದೆಂದು ಇರುತ್ತೇವೆ.

## 1\. ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು

ಏಐ ಏಜೆಂಟ್‍ನೋಡಿದರೆ ಅದು ಸಾಮಾನ್ಯ ಲಾರ್ಜ್ ಲ್ಯಾಂಗುಯೇಜ್ ಮಾದರಿಯನ್ನು (LLM) ಮೀರಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ವ್ಯವಸ್ಥೆಯಾಗಿದೆ. ಇದು ಅದರ ಪರಿಸರವನ್ನು ತಿಳಿದುಕೊಳ್ಳಬಹುದು, ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಬಹುದು ಮತ್ತು ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ಕ್ರಮಗಳನ್ನು ಕೈಗೊಳ್ಳಬಹುದು. ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ ಇಂತಹ ಹಲವಾರು ಏಜೆಂಟ್‌ಗಳು ಸಂಪರ್ಕ ನೀತಿಯೊಂದಿಗೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ, ಇದರಿಂದ ಒಬ್ಬ ಏಜೆಂಟ್‌ಗೆ ಅಷ್ಟೊಂದು ಕಷ್ಟ ಅಥವಾ ಅಸಾಧ್ಯವಾಗುವ ಸಮಸ್ಯೆಯನ್ನು ಪರಿಹರಿಸಬಹುದು.

### ಸಾಮಾನ್ಯ ಅಪ್ಲಿಕೇಶನ್ ದೃಶ್ಯಗಳು

  * **ಸಂಕೀರ್ಣ ಸಮಸ್ಯೆ ಪರಿಹಾರ**: ದೊಡ್ಡ ಕೆಲಸವನ್ನು (ಉದಾ: ಕಂಪನಿ-ವ್ಯಾಪ್ತಿ ಘಟನೆ ಯೋಜನೆ) ವಿಸ್ತಾರಿಸಿಬಿಡಿ ಮತ್ತು ವಿಶಿಷ್ಟ ಕಾರ್ಯಗಳನ್ನು ಪರಿಣತ ಏಜೆಂಟ್‌ಗಳು (ಉದಾ: ಬಜೆಟ್ ಏಜೆಂಟ್, ಲಾಜಿಸ್ಟಿಕ್ಸ್ ಏಜೆಂಟ್, ಮಾರ್ಕೆಟಿಂಗ್ ಏಜೆಂಟ್) ನೋಡಿಕೊಳ್ಳುವಂತೆ ಮಾಡುವುದು.
  * **ವಸ್ತುನಿಷ್ಠ ಸಹಾಯಕರು**: ಮುಖ್ಯ ಸಹಾಯಕ ಏಜೆಂಟ್ ಶೆಡ್ಯೂಲಿಂಗ್, ಸಂಶೋಧನೆ, ಬುಕ್ಕಿಂಗ್ ಹೀಗೆ ಕಾರ್ಯಗಳನ್ನು ఇతర ಪರಿಣತ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಹಂಚುವುದು.
  * **ಸ್ವಯಂಚಾಲಿತ ವಿಷಯ ಸೃಷ್ಟಿ**: ಒಂದು ಏಜೆಂಟ್ ವಿಷಯವನ್ನು ರಚಿಸುವುದರಲ್ಲಿ, ಮತ್ತೊಂದು ಅದನ್ನು ನಿಖರತೆ ಮತ್ತು ಟೋನ್‌ಗಾಗಿ ಪರಿಷೀಲಿಸುವುದರಲ್ಲಿ ಮತ್ತು ಮೂರನೇ ಅದನ್ನು ಪ್ರಕಟಿಸುವುದರಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ವರ್ಕ್ಫ್ಲೋ.

### ಬಹು-ಏಜೆಂಟ್ ಮಾದರಿಗಳು

ಬಹು-ಏಜೆಂಟ್ ವ್ಯವಸ್ಥೆಗಳನ್ನು ಅವರು ಹೇಗೆ ಸಂಪರ್ಕ ಹೊಂದುತ್ತಾರೆ ಎಂಬುದರ ಆಧಾರದ ಮೇಲೆ ವಿವಿಧ ಮಾದರಿಗಳಲ್ಲಿ ಸಂಘಟಿಸಬಹುದು:

  * **ಕ್ರಮಬद्ध (Sequential)**: ಏಜೆಂಟ್‌ಗಳು ಮುಂಚಿತ ಕ್ರಮದಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತಾರೆ, ಅಸೆಂಬ್ಲಿ ಲೈನ್ ಹಾಗೆ. ಒಂದು ಏಜೆಂಟ್‌ನ output ಅನ್ನು ಇನ್ನೊಂದು ಏಜೆಂಟ್‌ಗೆ input ಆಗಿ ನೀಡಲಾಗುತ್ತದೆ.
  * **ಸಮಾನಕಾಲೀನ (Concurrent)**: ಏಜೆಂಟ್‌ಗಳು ಒಂದೇ ವೇಳೆ ವಿಭಿನ್ನ ಭಾಗಗಳ ಮೇಲೆ ಕೆಲಸ ಮಾಡುತ್ತವೆ, ಮತ್ತು ಅವರ ಫಲಿತಾಂಶಗಳನ್ನು ಕೊನೆಯಲ್ಲಿ ಒಟ್ಟುಗೂಡಿಸಲಾಗುತ್ತದೆ.
  * **ಶರತ್ಮಕ (Conditional)**: ಎಂದರೆ, ಏಜೆಂಟ್‌ನ output ಆಧಾರವಾಗಿ ವರ್ಕ್‌ಫ್ಲೋ ವಿಭಿನ್ನ ದಾರಿಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ, if-then-else ಹೇಳಿಕೆಗೆ ಹೋಲುವದು.

## 2\. ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೆಮ್ವರ್ಕ್ ವರ್ಕ್‌ಫ್ಲೋ ಆರ್ಕಿಟೆಕ್ಚರ್

ಏಜೆಂಟ್ ಫ್ರೆಮ್ವರ್ಕ್ ನ ವರ್ಕ್‌ಫ್ಲೋ ವ್ಯವಸ್ಥೆ ಬಹು ಏಜೆಂಟ್‌ಗಳ ನಡುವೆ ಸಂಕೀರ್ಣ ಸಂವಹನಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಸುಧಾರಿತ ಒರ್ಪೂಟೋಪಕ್ವೆ ತಂತ್ರಜ್ಞಾನವಾಗಿದೆ. ಇದು [Pregel-ಶೈಲಿಯ ಕಾರ್ಯಗತಗೊಳಿಸುವ ಮಾದರಿಯನ್ನು](https://kowshik.github.io/JPregel/pregel_paper.pdf) ಆಧರಿಸಿ, "ಸೂಪರ್‌ಸ್ಟೆಪ್ಸ್" ಎಂದು ಕರೆಯುವ ಸಮಕಾಲೀನ ಹಂತಗಳಲ್ಲಿ ಸಂಯೋಜಿತವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವ ಗ್ರಾಫ್ ಆಧಾರಿತ ಆರ್ಕಿಟೆಕ್ಟರ್ಚರ್‌ನ ಮೇಲೆ ನಿರ್ಮಿತವಾಗಿದೆ.

### ಮೂಲ ಘಟಕಗಳು

ಆರ್ಕಿಟೆಕ್ಟರ್ಚರ್ ಮೂರು ಪ್ರಮುಖ ಭಾಗಗಳಿಂದ ಕೂಡಿದೆ:

1.  **ಕಾರ್ಯನಿರ್ವಹಣಾಕಾರರು (Executors)**: ಇವು ಮೂಲ ಪ್ರಕ್ರಿಯೆ ಘಟಕಗಳು. ನಮಗೆ ಉದಾಹರಣೆಯಲ್ಲಿ, `Agent` ಒಂದು ಎಕ್ಸಿಕ್ಯೂಟರ್ ಪ್ರಕಾರ. ಪ್ರತಿ ಕಾರ್ಯನಿರ್ವಹಣಾಕಾರರಿಗೆ ವಿವಿಧ ಸಂದೇಶ ಹ್ಯಾಂಡ್ಲರ್‌ಗಳಿರಬಹುದು, ಅವು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪಡೆದ ಸಂದೇಶದ ವರೆಗೆ ಕರೆಯಲ್ಪಡುತ್ತವೆ.
2.  **ಎಡ್ಗಸ್ (Edges)**: ಕಾರ್ಯನಿರ್ವಹಣಾಕಾರರ ನಡುವೆ ಸಂದೇಶಗಳು ಸಾಗುವ ದಾರಿಯನ್ನು ನಿರ್ಧಾರ ಮಾಡುತ್ತವೆ. ಎಡ್ಗ್‌ಗಳಿಗೆ ಶರತ್ತುಗಳೂ ಇರಬಹುದು, ಇದರಿಂದ ಗಮನದಿಂದ ಸೆಟ್ಟಿಂಗ್ ಮಾಡಿದ ದಾರಿತೀರ್ಮಾನ ಮಾಡಬಹುದು.
3.  **ವರ್ಕ್ಫ್ಲೋ**: ಪ್ರಕ್ರಿಯೆಯ ಸಮಗ್ರ ನಿರ್ವಹಣೆಯನ್ನು ಈ ಘಟಕ ಮಾಡುತ್ತದೆ, ಕಾರ್ಯನಿರ್ವಹಣಾಕಾರರು, ಎಡ್ಗಸ್, ಮತ್ತು ಕಾರ್ಯನಿರ್ವಹಣೆಯ ಸರಾಸರಿ ಹರಿವು ಹಿಡಿದಿಡುತ್ತದೆ. ಸಂದೇಶಗಳು ಸರಿಯಾದ ಕ್ರಮದಲ್ಲಿ ಕಾರ್ಯಗತಗೊಳಿಸುವುದನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ ಮತ್ತು ಅವಲೋಕನಕ್ಕೆ ಘಟನೆಗಳನ್ನು ಹರಡುತ್ತದೆ.

*ವರ್ಕ್ಫ್ಲೋ ವ್ಯವಸ್ಥೆಯ ಮೂಲ ಘಟಕಗಳನ್ನು ಚಿತ್ರಿಸುವ ಚಿತ್ರ.*

ಈ ರಚನೆ ಅನುಕ್ರಮ ಚೈನ್ಸ್, ಪ್ಯಾರಲಲ್ ಪ್ರಕ್ರಿಯೆಗಾಗಿ ಫ್ಯಾನ್-ಔಟ್/ಫ್ಯಾನ್-ಇನ್, ಮತ್ತು ಶರತ್ಮಕ ಹರಿವುಗಳಿಗೆ ಸ್ವಿಚ್-ಕೇಸ್ ಲಾಜಿಕ್ പോലെയുള്ള ಮೂಲ ಮಾದರಿಗಳ ಬಳಕೆ ಮೂಲಕ ದೃಢ ಮತ್ತು ವಿಸ್ತರಿಸುವ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಅನುಕೂಲ ಮಾಡಿಕೊಡುತ್ತದೆ.

## 3\. ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳು ಮತ್ತು ಕೋಡ್ ವಿಶ್ಲೇಷಣೆ

ಈಗ, ನಾವು ಫ್ರೆಮ್ವರ್ಕ್ ಬಳಸಿ ವಿಭಿನ್ನ ವರ್ಕ್‌ಫ್ಲೋ ಮಾದರಿಗಳನ್ನು ಹೇಗೆ ಜಾರಿಗೊಳಿಸಬೇಕೆಂದು ಅನ್ವೇಷಿಸೋಣ. ಪ್ರತಿಯೊಂದು ಉದಾಹರಣೆಗೆ Python ಮತ್ತು .NET ಕೋಡ್ ಎರಡಕ್ಕೂ ನೋಡೋಣ.

### ಪ್ರಕರಣ 1: ಮೂಲ ಅನುಕ್ರಮ ವರ್ಕ್‌ಫ್ಲೋ

ಇದು ಅತ್ಯಂತ ಸರಳ ಮಾದರಿ, ಇಲ್ಲಿ ಒಂದೇ ಏಜೆಂಟ್‌ನ output ನೇರವಾಗಿ ಇನ್ನೊಂದು ಏಜೆಂಟ್‌ಗೆ ನೀಡಲ್ಪಡುತ್ತದೆ. ನಮ್ಮ ದೃಶ್ಯದಲ್ಲಿ, ಒಂದು ಹೋಟೆಲ್ `FrontDesk` ಏಜೆಂಟ್ ಪ್ರಯಾಣ ಶಿಫಾರಸು ಮಾಡುತ್ತದೆ, ಅದನ್ನು `Concierge` ಏಜೆಂಟ್ ಪರಿಶೀಲಿಸಿ.

*ಮೂಲ FrontDesk -> Concierge ವರ್ಕ್‌ಫ್ಲೋ ಚಿತ್ರ.*

#### ದೃಶ್ಯ ಹಿನ್ನೆಲೆ

ಪ್ರಯಾಣಿಕನು ಪ್ಯಾರಿಸ್‌ನಲ್ಲಿ ಶಿಫಾರಸು ಕೇಳುತ್ತಾನೆ.

1.  `FrontDesk` ಏಜೆಂಟ್, ಸರಳ ಮೂಲದೊಂದಿಗೆ, ಲುವ್ರೆ ಮ್ಯೂಸಿಯಂ ತೆರವಬೇಕು ಎಂದು ಸಲಹೆ ನೀಡುತ್ತಾನೆ.
2.  `Concierge` ಏಜೆಂಟ್, ಸತ್ಯಸಂಧ ಅನುಭವಗಳ ಮೇಲೆ ತೂಕ ನೀಡುತ್ತಾನೆ, ಈ ಶಿಫಾರಸನ್ನು ಸ್ವೀಕರಿಸಿ ಪರಿಶೀಲನೆ ಮಾಡಿ ಮತ್ತು ಹೆಚ್ಚು ಸ್ಥಳೀಯ, ಕಡಿಮೆ ಪ್ರವಾಸಿಗಾರು ಸಹಿತ ಪರ್ಯಾಯವನ್ನು ಸೂಚಿಸುತ್ತಾನೆ.

#### Python ಜಾರಿಗೆ ವಿಶ್ಲೇಷಣೆ

Python ಉದಾಹರಣೆಯಲ್ಲಿ, ಮೊದಲು ಎರಡು ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿರ್ವಚಿಸಿ ಮತ್ತು ರಚಿಸಲಾಗುತ್ತದೆ, ಪ್ರತಿ ಏಜೆಂಟ್‌ಗೆ ವಿಶೇಷ ಸೂಚನೆಗಳಿವೆ.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# ಏಜೆಂಟ್ ಪಾತ್ರಗಳು ಮತ್ತು ಸೂಚನೆಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# ಏಜೆಂಟ್ ಇಂಡೆಸ್ಟೆನ್ಸುಗಳನ್ನು ರಚಿಸಿ
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

ನಂತರ `WorkflowBuilder` ಅನ್ನು ಗ್ರಾಫ್ ನಿರ್ಮಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ. `front_desk_agent` ಶುರುವಾಗುವ ಬಿಂದುವಾಗಿ ಸೆಟ್ ಮಾಡಲಾಗುತ್ತದೆ ಮತ್ತು ಅದರ output ಅನ್ನು `reviewer_agent` ಗೆ ಸಂಪರ್ಕಿಸುವ ಎಡ್ಗ್ ಸೃಷ್ಟಿಸಲಾಗುತ್ತದೆ.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

ಕೊನೆಗೆ, ಪ್ರಾಥಮಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್ ಸಹಾಯದಿಂದ ವರ್ಕ್‌ಫ್ಲೋ ಕಾರ್ಯಗತಗೊಳ್ಳುತ್ತದೆ.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# ರನ್ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಕಾರ್ಯಗತರಿಸುತ್ತದೆ; get_outputs() ಔಟ್‌ಪುಟ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ನ ಫಲಿತಾಂಶವನ್ನು ಹಿಂದಿರುಗಿಸುತ್ತದೆ.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) ಜಾರಿಗೆ ವಿಶ್ಲೇಷಣೆ

.NET ಜಾರಿಗೆ ಬಹುಮುಖ್ಯ ಲಾಜಿಕ್ ಸಹ Python ಹಾಗೆಯೇ ಅನುಸರಿಸಲಾಗುತ್ತದೆ. ಮೊದಲಿಗೆ ಏಜೆಂಟ್‌ಗಳ ಹೆಸರು ಮತ್ತು ಸೂಚನೆಗಳಿಗೆ ಶಾಶ್ವತ ಸಂಖ್ಯೆಗಳನ್ನು ಡಿಫೈನ್ ಮಾಡಲಾಗುತ್ತದೆ.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ಏಜೆಂಟ್‌ಗಳನ್ನು `AzureOpenAIClient` (Responses API) ಬಳಸಿ ರಚಿಸಲಾಗುತ್ತದೆ ಮತ್ತು ನಂತರ `WorkflowBuilder` ಮೂಲಕ ಅನುಕ್ರಮದ ಹರಿವು ಪರಿಗಣಿಸಲು `frontDeskAgent` ನಿಂದ `reviewerAgent` ಗೆ ಎಡ್ಜ್ ಸೇರಿಸಲಾಗುತ್ತದೆ.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

ಬಳಕೆದಾರನ ಸಂದೇಶದೊಂದಿಗೆ ವರ್ಕ್‌ಫ್ಲೋ ಕಾರ್ಯಗತಗೊಳ್ಳುತ್ತದೆ ಮತ್ತು ಫಲಿತಾಂಶಗಳು ಸ್ಟ್ರೀಮ್ ಆಗಿ ಹಿಂದಿರುಗುತ್ತದೆ.

### ಪ್ರಕರಣ 2: ಬಹು ಹಂತ ಅನುಕ್ರಮ ವರ್ಕ್‌ಫ್ಲೋ

ಈ ಮಾದರಿ ಮೂಲ ಅನುಕ್ರಮವನ್ನು ವಿಸ್ತರಿಸಿ ಹೆಚ್ಚುವರಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ಒಳಗೊಂಡಿದೆ. ಇದು ಹಲವಾರು ಹಂತಗಳ ಮಧ್ಯಂತರ ಪರಿಷ್ಕರಣೆ ಅಥವಾ ಪರಿವರ್ತನೆಯ ಅಗತ್ಯವಿರುವ ಪ್ರಕ್ರಿಯೆಗಳಿಗೆ ಸೂಕ್ತವಾಗಿದೆ.

#### ದೃಶ್ಯ ಹಿನ್ನೆಲೆ

ಬಳಕೆದಾರನು a ಜಿವನ ಕೋಣೆಯ ಚಿತ್ರ ಒದಗಿಸಿ ಫರ್ನಿಚರ್ ಕೊಟ್ ಅನ್ನು ಕೇಳುತ್ತಾನೆ.

1.  **ವ್ಯಾಪಾರ-ಏಜೆಂಟ್**: ಚಿತ್ರದಲ್ಲಿನ ಫರ್ನಿಚರ್ ವಸ್ತುಗಳನ್ನು ಗುರುತಿಸಿ ಪಟ್ಟಿಂಗ್ಗೊಳಿಸುತ್ತದೆ.
2.  **ಬೆಲೆ-ಏಜೆಂಟ್**: ವಸ್ತುಗಳ ಪಟ್ಟಿಯನ್ನು ತೆಗೆದು ಬಜೆಟ್, ಮಧ್ಯಮ, ಪ್ರೀಮಿಯಂ ಆಯ್ಕೆಗಳು ಸೇರಿದಂತೆ ವಿವರವಾದ ಬೆಲೆಬೇಕು ಒದಗಿಸುತ್ತದೆ.
3.  **ಕೊಟ್-ಏಜೆಂಟ್**: ಬೆಲೆಯ ಪಟ್ಟಿಯನ್ನು ಸ್ವೀಕರಿಸಿ Markdownನಲ್ಲಿ ಅಧಿಕೃತ ಕೊಟ್ ಡಾಕ್ಯುಮೆಂಟ್ ರೂಪ ನೀಡುತ್ತದೆ.

*Sales -> Price -> Quote ವರ್ಕ್‌ಫ್ಲೋ диаг್ರಾಮ್.*

#### Python ಜಾರಿಗೆ ವಿಶ್ಲೇಷಣೆ

ಮೂರು ಏಜೆಂಟ್‌ಗಳನ್ನು ಪರಿಭಾಷಿಸುವಾಗ ಪ್ರತಿ ಏಜೆಂಟ್‌ಗೆ ವಿಶೇಷ ಪಾತ್ರ ಇದೆ. ವರ್ಕ್‌ಫ್ಲೋ `add_edge` ಬಳಸಿ ಸರಳ ಚೈನ್ ರೂಪುತ್ತದೆ: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ಮೂರು ವಿಶಿಷ್ಟ ಏಜೆಂಟುಗಳನ್ನು ರಚಿಸಿ
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# ಕ್ರಮಬದ್ಧ ಕಾರ್ಯಪ್ರವahaವನ್ನು ನಿರ್ಮಿಸಿ
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ಇನ್‌ಪುಟ್ ಒಂದು `ChatMessage` ಆಗಿದ್ದು ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ URI ಎರಡನ್ನೂ ಒಳಗೊಂಡಿದೆ. ಪ್ರತಿ ಏಜೆಂಟ್‌ನ output ಅನ್ನು ಮುಂದಿನ ಏಜೆಂಟ್‌ಗೆ ಸರಬರಾಜು ಮಾಡುವ ಕಾರ್ಯವನ್ನು ಫ್ರೆಮ್ವರ್ಕ್ ನೋಡಿಕೊಳ್ಳುತ್ತದೆ, ಕೊನೆಯ ಕೊಟ್ ರಚನೆಯವರೆಗೆ.

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

# ಕಾರ್ಯಪ್ರवाहವನ್ನು 실행ಿಸಿ
events = await workflow.run(message)
```

#### .NET (C\#) ಜತೆಗೆ ವಿಶ್ಲೇಷಣೆ

.NET ಉದಾಹರಣೆ Python ಆವೃತ್ತಿಯನ್ನು ಹೊಂದಿದೆ. ಮೂರು ಏಜೆಂಟ್‌ಗಳು (`salesagent`, `priceagent`, `quoteagent`) ರಚಿಸಲಾಗುತ್ತವೆ. `WorkflowBuilder` ಅವನ್ನು ಅನುಕ್ರಮವಾಗಿ ಲಿಂಕ್ ಮಾಡುತ್ತದೆ.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ಬಳಕೆದಾರ ಸಂದೇಶವು ಚಿತ್ರ ಡೇಟಾ (bytes ರೂಪದಲ್ಲಿ) ಮತ್ತು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್ ಎರಡನ್ನೂ ಹೊಂದಿದೆ. `InProcessExecution.RunStreamingAsync` ವಿಧಾನವು ವರ್ಕ್‌ಫ್ಲೋ ಆರಂಭಿಸುತ್ತದೆ ಮತ್ತು अंतिम output ಸ್ಟ್ರೀಮ್ ನಲ್ಲಿ ಹಿಡಿಯಲ್ಪಡುತ್ತದೆ.

### ಪ್ರಕರಣ 3: ಸಮಾನಕಾಲೀನ ವರ್ಕ್‌ಫ್ಲೋ

ಸಮಯ ಉಳಿಸಲು ಕೆಲಸಗಳನ್ನು ಒಂದೇಸಾರಿಗೆ ನಡೆಸುವಾಗ ಈ ಮಾದರಿ ಬಳಸಲಾಗುತ್ತದೆ. ಇದು ಹಲವು ಏಜೆಂಟ್‌ಗಳಿಗೆ "ಫ್ಯಾನ್ ಔಟ್" ಮತ್ತು ಫಲಿತಾಂಶಗಳನ್ನು ಒಟ್ಟುಗೂಡಿಸುವ "ಫ್ಯಾನ್ ಇನ್" ರೀತಿ ಸೇರಿದೆ.

#### ದೃಶ್ಯ ಹಿನ್ನೆಲೆ

ಬಳಕೆದಾರನು ಸೀಯಾಟಲ್ ಗೆ ಪ್ರವಾಸ ಯೋಜಿಸಲು ಕೇಳುತ್ತಾನೆ.

1.  **ವಿತರಕ (Dispatcher (Fan-Out))**: ಬಳಕೆದಾರನ ವಿನಂತಿಯನ್ನು ಒಂದೇ ಸಮಯದಲ್ಲಿ ಎರಡು ಏಜೆಂಟ್‌ಗಳಿಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ.
2.  **ಸಂಶೋಧಕ ಏಜೆಂಟ್ (Researcher-Agent)**: ಡಿಸೆಂಬರ್‌ನಲ್ಲಿ ಸೀಯಾಟಲ್ ಪ್ರವಾಸದ ಆಕರ್ಷಣೆಗಳು, ಹವಾಮಾನ, ಪ್ರ ಮುಖ್ಯ ವಿಚಾರಗಳನ್ನು ಸಂಶೋಧಿಸುತ್ತದೆ.
3.  **ಯೋಜನೆ ಏಜೆಂಟ್ (Plan-Agent)**: ಸ್ವತಂತ್ರವಾಗಿ ಅನೇಕ ದಿನಗಳ ಪ್ರವಾಸ ಯೋಜನೆಯನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ.
4.  **ಒಟ್ಟುಗೂಡಿಸುವವರು (Aggregator (Fan-In))**: ಸಂಶೋಧಕ ಮತ್ತು ಯೋಜಕ ಎರಡರ output‌ಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ ಅಂತಿಮ ಫಲಿತಾಂಶವಾಗಿ ನಿರೂಪಿಸುತ್ತಾರೆ.

*Concurrent Researcher ಮತ್ತು Planner ವರ್ಕ್‌ಫ್ಲೋ диаг್ರಾಮ್.*

#### Python ಜಾರಿಗೆ ವಿಶ್ಲೇಷಣೆ

`ConcurrentBuilder` ಈ ಮಾದರಿಯನ್ನು ಸುಲಭಗೊಳಿಸುತ್ತದೆ. ನೀವು ಮಾತ್ರ ಭಾಗವಹಿಸುವ ಏಜೆಂಟ್‌ಗಳ ಪಟ್ಟಿಯನ್ನು ನೀಡಿದರೆ, ಬಿಲ್ಡರ್ ಫ್ಯಾನ್ ಔಟ್ ಮತ್ತು ಫ್ಯಾನ್ ಇನ್ ಲಾಜಿಕ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸೃಷ್ಟಿಸುತ್ತದೆ.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ಫ್ಯಾನ್-ಔಟ್/ಫ್ಯಾನ್-ಇನ್ ಲಾಜಿಕ್ ಅನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಚಾಲನೆ ಮಾಡಿ
events = await workflow.run("Plan a trip to Seattle in December")
```

ಫ್ರೆಮ್ವರ್ಕ್ `research_agent` ಮತ್ತು `plan_agent` ಎರಡು ಏಜೆಂಟ್‌ಗಳು ಸಮಕಾಲೀನವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ ಮತ್ತು ಕೊನೆಯ output ಗಳನ್ನು ಪಟ್ಟಿಯಲ್ಲಿ ಸಂಗ್ರಹಿಸುತ್ತದೆ.

#### .NET (C\#) ಜಾರಿಗೆ ವಿಶ್ಲೇಷಣೆ

.NET ನಲ್ಲಿ ಈ ಮಾದರಿ ಸ್ಪಷ್ಟ ವ್ಯಾಖ್ಯಾನ ಬೇಡಿಕೆ ಮಾಡುತ್ತದೆ. ಕಸ್ಟಮ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳು (`ConcurrentStartExecutor` ಮತ್ತು `ConcurrentAggregationExecutor`) ಫ್ಯಾನ್ ಔಟ್ ಮತ್ತು ಫ್ಯಾನ್ ಇನ್ ಲಾಜಿಕ್ ನಿರ್ವಹಿಸಲು ರಚಿಸಲಾಗಿದೆ.

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

ನಂತರ `WorkflowBuilder` `AddFanOutEdge` ಮತ್ತು `AddFanInEdge` ಬಳಸಿ ಈ ಕಸ್ಟಮ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳು ಮತ್ತು ಏಜೆಂಟ್‌ಗಳ ಗ್ರಾಫ್ ನಿರ್ಮಾಣ ಮಾಡುತ್ತದೆ.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### ಪ್ರಕರಣ 4: ಶರತ್ಮಕ ವರ್ಕ್‌ಫ್ಲೋ

ಶರತ್ಮಕ ವರ್ಕ್‌ಫ್ಲೋಗಳು ಶಾಖಾ ತಂತ್ರಜ್ಞಾನದ ಮೂಲಕ ವ್ಯವಸ್ಥೆಯು ಮಧ್ಯಂತರ ಫಲಿತಾಂಶಗಳ ಆಧಾರದ ಮೇಲೆ ವಿಭಿನ್ನ ದಾರಿಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು ಅನುಮತಿಸುತ್ತದೆ.

#### ದೃಶ್ಯ ಹಿನ್ನೆಲೆ

ಈ ವರ್ಕ್‌ಫ್ಲೋ ತಾಂತ್ರಿಕ ಟ್ಯುಟೋರಿಯಲ್ ರಚನೆ ಮತ್ತು ಪ್ರಕಟಣೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುತ್ತದೆ.

1.  **ಇವೆಂಜಲಿಸ್ಟ್ ಏಜೆಂಟ್**: ನೀಡಲಾದ ರೂಪರೇಖೆ ಮತ್ತು URL ಆಧರಿಸಿ ಟ್ಯುಟೋರಿಯಲ್‌ನ ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಬರೆಯುತ್ತದೆ.
2.  **ವಿಷಯ ಪರಿಶೀಲಕ ಏಜೆಂಟ್**: ಪ್ರಾತ್ಯಕ್ಷಿಕೆಯನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ. ಪದಗಳ ಸಂಖ್ಯೆ 200 ಕ್ಕಿಂತ ಹೆಚ್ಚಿದೆಯೇ ಎಂದು ತಪಾಸಣೆ ಮಾಡುತ್ತದೆ.
3.  **ಶರತ್ಮಕ ಶಾಖೆ**:
      * **ಅನುಮೋದನೆ (`ಹೌದು`)**: ವರ್ಕ್‌ಫ್ಲೋ `Publisher-Agent` ಕಡೆಗೆ ಸಾಗುತ್ತದೆ.
      * **ನಿರಾಕರಣೆ (`ಇಲ್ಲ`)**: ವರ್ಕ್‌ಫ್ಲೋ ನಿಲ್ಲುತ್ತದೆ ಮತ್ತು ನಿರಾಕರಣೆಯ ಕಾರಣವನ್ನು output ಮಾಡುತ್ತದೆ.
4.  **ಪ್ರಕಟಣೆಗಾರ ಏಜೆಂಟ್**: ಪ್ರಾತ್ಯಕ್ಷಿಕೆ ಅನುಮೋದಿತವಾದರೆ, ಈ ಏಜೆಂಟ್ ವಿಷಯವನ್ನು Markdown ಫೈಲ್‌ಗೆ ಉಳಿಸುತ್ತದೆ.

#### Python ಜಾರಿಗೆ ವಿಶ್ಲೇಷಣೆ

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಕಸ್ಟಮ್ ಫಂಕ್ಷನ್ `select_targets` ಬಳಸಲಾಗುತ್ತದೆ, ಇದು ಶರತ್ಮಕ ಲಾಜಿಕ್ ಜಾರಿಗೆ ಸಹಾಯಮಾಡುತ್ತದೆ. ಈ ಫಂಕ್ಷನ್ `add_multi_selection_edge_group` ಗೆ ನೀಡಲ್ಪಟುತ್ತದೆ ಮತ್ತು `review_result` ಕ್ಷೇತ್ರ ಆಧರಿಸಿ ವರ್ಕ್‌ಫ್ಲೋ ಮಾರ್ಗವನ್ನು ನಿಯಂತ್ರಿಸುತ್ತದೆ.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ಈ ಕಾರ್ಯವು ವಿಮರ್ಶಾ ಫಲಿತಾಂಶದ ಆಧಾರದಲ್ಲಿ ಮುಂದಿನ ಹಾದಿಯನ್ನು ನಿರ್ಧರಿಸುತ್ತದೆ
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ಅನುಮೋದಿತವಾದರೆ, 'save_draft' ಕಾರ್ಯನಿರ್ವಾಹಕನಿಗೆ ಮುಂದುವರೆಯಿರಿ
        return [save_draft_id]
    else:
        # ತಿರಸ್ಕೃತವಾದರೆ, ವೈಫಲ್ಯವನ್ನು ವರದಿ ಮಾಡಲು 'handle_review' ಕಾರ್ಯನಿರ್ವಾಹಕನಿಗೆ ಮುಂದುವರೆಯಿರಿ
        return [handle_review_id]

# ವರ್ಕ್‌ಫ್ಲೋ ನಿರ್ಮಾಪಕನು ಮಾರ್ಗದರ್ಶನಕ್ಕಾಗಿ ಆಯ್ಕೆ ಕಾರ್ಯವನ್ನು ಬಳಸುತ್ತಾನೆ
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # ಬಹು-ಆಯ್ಕೆ ಎಡ್ಜ್ ಶರತ್ತಿನ ಲಾಜಿಕ್ ಅನ್ನು ಆಗೂಹಿಸುತ್ತದೆ
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` ಮೊದಲಾದ ಕಸ್ಟಮ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳು ಏಜೆಂಟ್‌ನ JSON output ಅನ್ನು ಶಕ್ತಿಗೊಳಿಸಿದ ಕವರ್ ಮಾಡಲಾದ ವಸ್ತುಗಳಾಗಿ ಪರಿವರ್ತಿಸಿ, ಆಯ್ಕೆ ಫಂಕ್ಷನ್ ಅವುಗಳನ್ನು ಪರಿಶೀಲಿಸಲು ಸಹಾಯಮಾಡುತ್ತವೆ.

#### .NET (C\#) ಜಾರಿಗೆ ವಿಶ್ಲೇಷಣೆ

.NET ಆವೃತ್ತಿಯೂ ಅನುಕೂಲಕರ ವಿಧಾನವನ್ನು ಬಳಸಿ `Func<object?, bool>` ರೂಪದಲ್ಲಿ ಶರತ್ತು ಫಂಕ್ಷನ್ ಅನ್ನು ಡಿಫೈನ್ ಮಾಡುತ್ತದೆ, ಇದು `ReviewResult` ವಸ್ತುವಿನ `Result` ಗುಣಲಕ್ಷಣವನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ.

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

`AddEdge` ವಿಧಾನದಲ್ಲಿ `condition` ಪ್ಯಾರಾಮೀಟರ್ ಅನ್ನು ಬಳಸಿಕೊಂಡು `WorkflowBuilder` ಶಾಖಾ ದಾರಿಗಳನ್ನು ಸೃಷ್ಟಿಸುತ್ತದೆ. ವರ್ಕ್‌ಫ್ಲೋ ಶರತ್ತು `GetCondition(expectedResult: "Yes")` ಸತ್ಯವಾಗಿದ್ದರೆ ಮಾತ್ರ `publishExecutor` ಕಡೆಗೆ ಹೋಗುತ್ತದೆ, ಇಲ್ಲದಿದ್ದರೆ `sendReviewerExecutor` ದಾರಿಯನ್ನು ಅನುಸರಿಸುತ್ತದೆ.

## ನಿಯೋಜನೆ

ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೆಮ್ವರ್ಕ್ ವರ್ಕ್‌ಫ್ಲೋ ಉನ್ನತ ಮೌಲ್ಯದ ಮತ್ತು ಬಾಹುಮುಖ್ಯ ವ್ಯವಸ್ಥೆಗಳ ನಿರ್ವಹಣೆಗೆ ದೃಢ ಮತ್ತು ನಮ್ರ ಭೂಮಿಕೆ ಒದಗಿಸುತ್ತದೆ. ಇದರ ಗ್ರಾಫ್ ಆಧಾರಿತ ಆರ್ಕಿಟೆಕ್ಚರ್ ಮತ್ತು ಮೂಲ ಘಟಕಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಅಭಿವೃದ್ಧಿ ಪಡುವವರು Python ಮತ್ತು .NET ನಲ್ಲಿ ಸುಗಮ, ಗಾಢ, ಮತ್ತು ಪ್ರಬಲ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ವಿನ್ಯಾಸ ಮಾಡಿಕೊಂಡು ಜಾರಿಗೆ ತರಬಹುದು. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಸಾದಾ ಅನುಕ್ರಮ ಪ್ರಕ್ರಿಯೆ, ಪಾರಲಲ್ ಕಾರ್ಯನಿರ್ವಹಣೆ ಅಥವಾ ಡೈನಾಮಿಕ್ ಶರತ್ಮಕ ಲಾಜಿಕ್‍ಗಳಿಗೆ ಅವಶ್ಯಕತೆಯಿದ್ದರೂ, ಫ್ರೆಮ್ವರ್ಕ್ ಪ್ರಬಲ, ವಿಸ್ತರಿಸುವ ಮತ್ತು টাইಪ್-ಸೆಫ್ ಏಐ ಚಾಲಿತ ಪರಿಹಾರಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸಲಹೆಗಳನ್ನು ನೀಡುತ್ತದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->