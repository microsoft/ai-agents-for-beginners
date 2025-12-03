<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b39c052ef109db90ad9251183791e2d6",
  "translation_date": "2025-12-03T16:18:55+00:00",
  "source_file": "08-multi-agent/code_samples/workflows-agent-framework/README.md",
  "language_code": "kn"
}
-->
# Microsoft Agent Framework Workflow ಬಳಸಿ ಬಹು-ಏಜೆಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವುದು

ಈ ಟ್ಯುಟೋರಿಯಲ್ Microsoft Agent Framework ಬಳಸಿ ಬಹು-ಏಜೆಂಟ್ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಮತ್ತು ನಿರ್ಮಿಸಲು ನಿಮಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡುತ್ತದೆ. ನಾವು ಬಹು-ಏಜೆಂಟ್ ಸಿಸ್ಟಮ್‌ಗಳ ಮೂಲ ಪರಿಕಲ್ಪನೆಗಳನ್ನು ಅನ್ವೇಷಿಸುತ್ತೇವೆ, ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ Workflow ಘಟಕದ ಆರ್ಕಿಟೆಕ್ಚರ್‌ನಲ್ಲಿ ತೊಡಗುತ್ತೇವೆ ಮತ್ತು Python ಮತ್ತು .NET ನಲ್ಲಿ ವಿವಿಧ ವರ್ಕ್‌ಫ್ಲೋ ಮಾದರಿಗಳ ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳನ್ನು ನೋಡುತ್ತೇವೆ.

## 1\. ಬಹು-ಏಜೆಂಟ್ ಸಿಸ್ಟಮ್‌ಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದು

AI Agent ಎಂದರೆ ಸಾಮಾನ್ಯ Large Language Model (LLM) ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಮೀರಿದ ವ್ಯವಸ್ಥೆ. ಇದು ತನ್ನ ಪರಿಸರವನ್ನು ಗ್ರಹಿಸಬಹುದು, ನಿರ್ಧಾರಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಬಹುದು ಮತ್ತು ನಿರ್ದಿಷ್ಟ ಗುರಿಗಳನ್ನು ಸಾಧಿಸಲು ಕ್ರಮಗಳನ್ನು ಕೈಗೊಳ್ಳಬಹುದು. ಬಹು-ಏಜೆಂಟ್ ಸಿಸ್ಟಮ್‌ಗಳಲ್ಲಿ ಈ ಏಜೆಂಟ್‌ಗಳು ಹಲವಾರು ಸೇರಿ, ಒಂದು ಏಕ ಏಜೆಂಟ್‌ಗೆ ಕಷ್ಟಕರ ಅಥವಾ ಅಸಾಧ್ಯವಾಗುವ ಸಮಸ್ಯೆಯನ್ನು ಪರಿಹರಿಸಲು ಸಹಕರಿಸುತ್ತವೆ.

### ಸಾಮಾನ್ಯ ಅಪ್ಲಿಕೇಶನ್ ಸನ್ನಿವೇಶಗಳು

  * **ಸಂಕೀರ್ಣ ಸಮಸ್ಯೆ ಪರಿಹಾರ**: ದೊಡ್ಡ ಕಾರ್ಯವನ್ನು (ಉದಾ., ಕಂಪನಿಯ ವ್ಯಾಪಕ ಈವೆಂಟ್ ಯೋಜನೆ) ವಿಶೇಷ ಏಜೆಂಟ್‌ಗಳ ಮೂಲಕ ಚಿಕ್ಕ ಉಪ-ಕಾರ್ಯಗಳಲ್ಲಿ ವಿಭಜಿಸುವುದು (ಉದಾ., ಬಜೆಟ್ ಏಜೆಂಟ್, ಲಾಜಿಸ್ಟಿಕ್ಸ್ ಏಜೆಂಟ್, ಮಾರ್ಕೆಟಿಂಗ್ ಏಜೆಂಟ್).
  * **ವರ್ಚುವಲ್ ಅಸಿಸ್ಟೆಂಟ್‌ಗಳು**: ಪ್ರಾಥಮಿಕ ಅಸಿಸ್ಟೆಂಟ್ ಏಜೆಂಟ್, ಶೆಡ್ಯೂಲಿಂಗ್, ಸಂಶೋಧನೆ ಮತ್ತು ಬುಕ್ಕಿಂಗ್ ಮುಂತಾದ ಕಾರ್ಯಗಳನ್ನು ಇತರ ವಿಶೇಷ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಹಂಚುತ್ತದೆ.
  * **ಸ್ವಯಂಚಾಲಿತ ವಿಷಯ ರಚನೆ**: ಒಂದು ಏಜೆಂಟ್ ವಿಷಯವನ್ನು ಡ್ರಾಫ್ಟ್ ಮಾಡುತ್ತದೆ, ಮತ್ತೊಂದು ಅದನ್ನು ಶುದ್ಧತೆ ಮತ್ತು ಶೈಲಿಗಾಗಿ ಪರಿಶೀಲಿಸುತ್ತದೆ, ಮತ್ತು ಮೂರನೆಯದು ಅದನ್ನು ಪ್ರಕಟಿಸುತ್ತದೆ.

### ಬಹು-ಏಜೆಂಟ್ ಮಾದರಿಗಳು

ಬಹು-ಏಜೆಂಟ್ ಸಿಸ್ಟಮ್‌ಗಳನ್ನು ಹಲವಾರು ಮಾದರಿಗಳಲ್ಲಿ ಸಂಘಟಿಸಬಹುದು, ಅವುಗಳು ಹೇಗೆ ಪರಸ್ಪರ ಕ್ರಿಯೆಗೊಳ್ಳುತ್ತವೆ ಎಂಬುದನ್ನು ನಿರ್ಧರಿಸುತ್ತವೆ:

  * **ಕ್ರಮಬದ್ಧ**: ಏಜೆಂಟ್‌ಗಳು ಪೂರ್ವನಿರ್ಧಾರಿತ ಕ್ರಮದಲ್ಲಿ ಕೆಲಸ ಮಾಡುತ್ತವೆ, ಅಸೆಂಬ್ಲಿ ಲೈನ್‌ನಂತೆ. ಒಂದು ಏಜೆಂಟ್‌ನ ಔಟ್‌ಪುಟ್ ಮುಂದಿನ ಏಜೆಂಟ್‌ಗೆ ಇನ್‌ಪುಟ್ ಆಗುತ್ತದೆ.
  * **ಸಮಕಾಲೀನ**: ಏಜೆಂಟ್‌ಗಳು ಕಾರ್ಯದ ವಿಭಿನ್ನ ಭಾಗಗಳಲ್ಲಿ ಸಮಾನಾಂತರವಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತವೆ, ಮತ್ತು ಅವರ ಫಲಿತಾಂಶಗಳನ್ನು ಕೊನೆಯಲ್ಲಿ ಒಗ್ಗೂಡಿಸಲಾಗುತ್ತದೆ.
  * **ಶರ್ತಾಧಾರಿತ**: ವರ್ಕ್‌ಫ್ಲೋ ಏಜೆಂಟ್‌ನ ಔಟ್‌ಪುಟ್ ಆಧರಿಸಿ ವಿಭಿನ್ನ ಮಾರ್ಗಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ, if-then-else ಹೇಳಿಕೆಯಂತೆ.

## 2\. Microsoft Agent Framework Workflow ಆರ್ಕಿಟೆಕ್ಚರ್

Agent Framework‌ನ ವರ್ಕ್‌ಫ್ಲೋ ಸಿಸ್ಟಮ್ ಬಹು-ಏಜೆಂಟ್‌ಗಳ ನಡುವಿನ ಸಂಕೀರ್ಣ ಪರಸ್ಪರ ಕ್ರಿಯೆಗಳನ್ನು ನಿರ್ವಹಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾದ ಪ್ರಗತಿಶೀಲ ಆರ್ಕೆಸ್ಟ್ರೇಷನ್ ಎಂಜಿನ್ ಆಗಿದೆ. ಇದು [Pregel-ಶೈಲಿ ಕಾರ್ಯಾಚರಣೆ ಮಾದರಿ](https://kowshik.github.io/JPregel/pregel_paper.pdf) ಬಳಸಿ ಗ್ರಾಫ್-ಆಧಾರಿತ ಆರ್ಕಿಟೆಕ್ಚರ್‌ನಲ್ಲಿ ನಿರ್ಮಿಸಲಾಗಿದೆ, ಅಲ್ಲಿ ಪ್ರಕ್ರಿಯೆ "supersteps" ಎಂದು ಕರೆಯುವ ಸಮನ್ವಯಿತ ಹಂತಗಳಲ್ಲಿ ನಡೆಯುತ್ತದೆ.

### ಮೂಲ ಘಟಕಗಳು

ಆರ್ಕಿಟೆಕ್ಚರ್ ಮೂರು ಮುಖ್ಯ ಭಾಗಗಳಿಂದ ಕೂಡಿದೆ:

1.  **Executors**: ಇವು ಮೂಲ ಪ್ರಕ್ರಿಯೆ ಘಟಕಗಳು. ನಮ್ಮ ಉದಾಹರಣೆಗಳಲ್ಲಿ, `Agent` ಒಂದು ರೀತಿಯ ಎಕ್ಸಿಕ್ಯೂಟರ್ ಆಗಿದೆ. ಪ್ರತಿ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸ್ವೀಕರಿಸಿದ ಸಂದೇಶದ ಪ್ರಕಾರ ಕರೆಯಲಾಗುವ ಹಲವಾರು ಸಂದೇಶ ಹ್ಯಾಂಡ್ಲರ್‌ಗಳು ಇರಬಹುದು.
2.  **Edges**: ಇವು ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳ ನಡುವೆ ಸಂದೇಶಗಳು ತೆಗೆದುಕೊಳ್ಳುವ ಮಾರ್ಗವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತವೆ. Edges‌ಗಳಿಗೆ ಶರ್ತಗಳು ಇರಬಹುದು, ಇದು ವರ್ಕ್‌ಫ್ಲೋ ಗ್ರಾಫ್ ಮೂಲಕ ಮಾಹಿತಿಯ ಡೈನಾಮಿಕ್ ಮಾರ್ಗವನ್ನು ಅನುಮತಿಸುತ್ತದೆ.
3.  **Workflow**: ಈ ಘಟಕ ಸಂಪೂರ್ಣ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಆರ್ಕೆಸ್ಟ್ರೇಟ್ ಮಾಡುತ್ತದೆ, ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳು, ಎಡ್ಜ್‌ಗಳು ಮತ್ತು ಕಾರ್ಯಾಚರಣೆಯ ಒಟ್ಟು ಹರಿವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ. ಇದು ಸಂದೇಶಗಳನ್ನು ಸರಿಯಾದ ಕ್ರಮದಲ್ಲಿ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಮತ್ತು ವೀಕ್ಷಣಾತ್ಮಕತೆಯಿಗಾಗಿ ಈವೆಂಟ್‌ಗಳನ್ನು ಸ್ಟ್ರೀಮ್ ಮಾಡಲು ಖಾತರಿಪಡಿಸುತ್ತದೆ.

*ವರ್ಕ್‌ಫ್ಲೋ ಸಿಸ್ಟಮ್‌ನ ಮೂಲ ಘಟಕಗಳನ್ನು ಚಿತ್ರಿಸುವ ಡಯಾಗ್ರಾಮ್.*

ಈ ರಚನೆ ಸರಳ ಕ್ರಮಬದ್ಧ ಶ್ರೇಣಿಗಳು, ಸಮಾನಾಂತರ ಪ್ರಕ್ರಿಯೆಗಾಗಿ fan-out/fan-in, ಮತ್ತು ಶರ್ತಾಧಾರಿತ ಹರಿವಿಗೆ switch-case ಲಾಜಿಕ್ ಮುಂತಾದ ಮೂಲ ಮಾದರಿಗಳನ್ನು ಬಳಸಿಕೊಂಡು ಬಲವಾದ ಮತ್ತು ಮಿತವ್ಯಯದ ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲು ಅನುಮತಿಸುತ್ತದೆ.

## 3\. ಪ್ರಾಯೋಗಿಕ ಉದಾಹರಣೆಗಳು ಮತ್ತು ಕೋಡ್ ವಿಶ್ಲೇಷಣೆ

ಈಗ, ಫ್ರೇಮ್‌ವರ್ಕ್ ಬಳಸಿ ವಿಭಿನ್ನ ವರ್ಕ್‌ಫ್ಲೋ ಮಾದರಿಗಳನ್ನು ಹೇಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸಬಹುದು ಎಂಬುದನ್ನು ಅನ್ವೇಷಿಸೋಣ. ನಾವು ಪ್ರತಿ ಉದಾಹರಣೆಗೆ Python ಮತ್ತು .NET ಕೋಡ್ ಅನ್ನು ನೋಡುತ್ತೇವೆ.

### ಪ್ರಕರಣ 1: ಮೂಲ ಕ್ರಮಬದ್ಧ ವರ್ಕ್‌ಫ್ಲೋ

ಇದು ಅತ್ಯಂತ ಸರಳ ಮಾದರಿ, ಅಲ್ಲಿ ಒಂದು ಏಜೆಂಟ್‌ನ ಔಟ್‌ಪುಟ್ ನೇರವಾಗಿ ಮತ್ತೊಂದಕ್ಕೆ ಪಾಸಾಗುತ್ತದೆ. ನಮ್ಮ ಸನ್ನಿವೇಶದಲ್ಲಿ, ಹೋಟೆಲ್ `FrontDesk` ಏಜೆಂಟ್ ಒಂದು ಪ್ರಯಾಣ ಶಿಫಾರಸು ಮಾಡುತ್ತದೆ, ಇದನ್ನು ನಂತರ `Concierge` ಏಜೆಂಟ್ ಪರಿಶೀಲಿಸುತ್ತದೆ.

*ಮೂಲ FrontDesk -\> Concierge ವರ್ಕ್‌ಫ್ಲೋ ಡಯಾಗ್ರಾಮ್.*

#### ಸನ್ನಿವೇಶ ಹಿನ್ನೆಲೆ

ಒಬ್ಬ ಪ್ರಯಾಣಿಕನು ಪ್ಯಾರಿಸ್‌ನಲ್ಲಿ ಶಿಫಾರಸನ್ನು ಕೇಳುತ್ತಾನೆ.

1.  `FrontDesk` ಏಜೆಂಟ್, ಸಂಕ್ಷಿಪ್ತತೆಯೊಂದಿಗೆ ವಿನ್ಯಾಸಗೊಳಿಸಲಾಗಿದೆ, ಲೂವರ್ ಮ್ಯೂಸಿಯಂಗೆ ಭೇಟಿ ನೀಡಲು ಶಿಫಾರಸು ಮಾಡುತ್ತದೆ.
2.  `Concierge` ಏಜೆಂಟ್, ಪ್ರಾಮಾಣಿಕ ಅನುಭವಗಳನ್ನು ಆದ್ಯತೆ ನೀಡುತ್ತದೆ, ಈ ಶಿಫಾರಸನ್ನು ಸ್ವೀಕರಿಸುತ್ತದೆ. ಇದು ಶಿಫಾರಸನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ ಮತ್ತು ಸ್ಥಳೀಯ, ಕಡಿಮೆ ಪ್ರವಾಸಿಗರ ಪರ್ಯಾಯವನ್ನು ಶಿಫಾರಸು ಮಾಡುತ್ತದೆ.

#### Python ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

Python ಉದಾಹರಣೆಯಲ್ಲಿ, ನಾವು ಮೊದಲಿಗೆ ಎರಡು ಏಜೆಂಟ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಿ ರಚಿಸುತ್ತೇವೆ, ಪ್ರತಿ ಏಜೆಂಟ್‌ಗಳಿಗೆ ವಿಶೇಷ ಸೂಚನೆಗಳೊಂದಿಗೆ.

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
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

ನಂತರ, `WorkflowBuilder` ಅನ್ನು ಬಳಸಿ ಗ್ರಾಫ್ ಅನ್ನು ನಿರ್ಮಿಸಲಾಗುತ್ತದೆ. `front_desk_agent` ಅನ್ನು ಪ್ರಾರಂಭ ಬಿಂದು ಎಂದು ಹೊಂದಿಸಲಾಗುತ್ತದೆ, ಮತ್ತು ಅದರ ಔಟ್‌ಪುಟ್ ಅನ್ನು `reviewer_agent` ಗೆ ಸಂಪರ್ಕಿಸಲು ಒಂದು ಎಡ್ಜ್ ರಚಿಸಲಾಗುತ್ತದೆ.

```python
# 01.python-ಏಜೆಂಟ್-ಫ್ರೇಮ್‌ವರ್ಕ್-ವರ್ಕ್‌ಫ್ಲೋ-ಘಮೋಡಲ್-ಮೂಲ.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

ಕೊನೆಗೆ, ಪ್ರಾರಂಭಿಕ ಬಳಕೆದಾರ ಪ್ರಾಂಪ್ಟ್‌ನೊಂದಿಗೆ ವರ್ಕ್‌ಫ್ಲೋ ಕಾರ್ಯಗತಗೊಳಿಸಲಾಗುತ್ತದೆ.

```python
# 01.python-ಏಜೆಂಟ್-ಫ್ರೇಮ್ವರ್ಕ್-ಕಾರ್ಯಪ್ರವಾಹ-ಘಮೋಡಲ್-ಮೂಲಭೂತ.ipynb

result =''
# ರನ್_ಸ್ಟ್ರೀಮ್ ವಿಧಾನವು ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಕಾರ್ಯಗತಗೊಳಿಸುತ್ತದೆ ಮತ್ತು ಈವೆಂಟ್‌ಗಳನ್ನು ಸ್ಟ್ರೀಮ್ ಮಾಡುತ್ತದೆ.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

.NET ಅನುಷ್ಠಾನವು ಬಹಳ ಸಮಾನವಾದ ತರ್ಕವನ್ನು ಅನುಸರಿಸುತ್ತದೆ. ಮೊದಲಿಗೆ, ಏಜೆಂಟ್‌ಗಳ ಹೆಸರು ಮತ್ತು ಸೂಚನೆಗಳಿಗಾಗಿ ಸ್ಥಿರಾಂಕಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲಾಗುತ್ತದೆ.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`OpenAIClient` ಬಳಸಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಲಾಗುತ್ತದೆ, ನಂತರ `WorkflowBuilder` ಕ್ರಮಬದ್ಧ ಹರಿವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುತ್ತದೆ, `frontDeskAgent` ನಿಂದ `reviewerAgent` ಗೆ ಒಂದು ಎಡ್ಜ್ ಸೇರಿಸುವ ಮೂಲಕ.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

ಬಳಕೆದಾರನ ಸಂದೇಶದೊಂದಿಗೆ ವರ್ಕ್‌ಫ್ಲೋ ಕಾರ್ಯಗತಗೊಳಿಸಲಾಗುತ್ತದೆ, ಮತ್ತು ಫಲಿತಾಂಶಗಳನ್ನು ಸ್ಟ್ರೀಮ್ ಮೂಲಕ ಹಿಂದಿರುಗಿಸಲಾಗುತ್ತದೆ.

### ಪ್ರಕರಣ 2: ಬಹು-ಹಂತದ ಕ್ರಮಬದ್ಧ ವರ್ಕ್‌ಫ್ಲೋ

ಈ ಮಾದರಿ ಮೂಲ ಕ್ರಮವನ್ನು ವಿಸ್ತರಿಸಿ ಹೆಚ್ಚು ಏಜೆಂಟ್‌ಗಳನ್ನು ಸೇರಿಸುತ್ತದೆ. ಇದು ಹಲವಾರು ಹಂತಗಳ ಶುದ್ಧೀಕರಣ ಅಥವಾ ಪರಿವರ್ತನೆ ಅಗತ್ಯವಿರುವ ಪ್ರಕ್ರಿಯೆಗಳಿಗೆ ಸೂಕ್ತವಾಗಿದೆ.

#### ಸನ್ನಿವೇಶ ಹಿನ್ನೆಲೆ

ಒಬ್ಬ ಬಳಕೆದಾರ ಲಿವಿಂಗ್ ರೂಮ್‌ನ ಚಿತ್ರವನ್ನು ಒದಗಿಸುತ್ತಾನೆ ಮತ್ತು ಫರ್ನಿಚರ್ ಕ್ವೋಟ್ ಕೇಳುತ್ತಾನೆ.

1.  **Sales-Agent**: ಚಿತ್ರದಲ್ಲಿ ಫರ್ನಿಚರ್ ಐಟಂಗಳನ್ನು ಗುರುತಿಸಿ ಪಟ್ಟಿ ರಚಿಸುತ್ತದೆ.
2.  **Price-Agent**: ಐಟಂಗಳ ಪಟ್ಟಿಯನ್ನು ತೆಗೆದುಕೊಂಡು, ಬಜೆಟ್, ಮಧ್ಯಮ ಶ್ರೇಣಿ ಮತ್ತು ಪ್ರೀಮಿಯಂ ಆಯ್ಕೆಗಳೊಂದಿಗೆ ವಿವರವಾದ ಬೆಲೆ ವಿವರವನ್ನು ಒದಗಿಸುತ್ತದೆ.
3.  **Quote-Agent**: ಬೆಲೆಪಟ್ಟಿಯನ್ನು ಸ್ವೀಕರಿಸಿ, Markdown ನಲ್ಲಿ ಅಧಿಕೃತ ಕ್ವೋಟ್ ಡಾಕ್ಯುಮೆಂಟ್ ಅನ್ನು ರೂಪಿಸುತ್ತದೆ.

*Sales -\> Price -\> Quote ವರ್ಕ್‌ಫ್ಲೋ ಡಯಾಗ್ರಾಮ್.*

#### Python ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

ಮೂರು ಏಜೆಂಟ್‌ಗಳನ್ನು ವ್ಯಾಖ್ಯಾನಿಸಲಾಗುತ್ತದೆ, ಪ್ರತಿ ಏಜೆಂಟ್‌ಗಳಿಗೆ ವಿಶೇಷ ಪಾತ್ರವಿದೆ. `add_edge` ಬಳಸಿ ವರ್ಕ್‌ಫ್ಲೋವನ್ನು ನಿರ್ಮಿಸಲಾಗುತ್ತದೆ: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# ಮೂರು ವಿಶೇಷ ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸಿ
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# ಕ್ರಮಬದ್ಧ ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ನಿರ್ಮಿಸಿ
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ಇನ್‌ಪುಟ್ ಒಂದು `ChatMessage` ಆಗಿದ್ದು, ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ URI ಅನ್ನು ಒಳಗೊಂಡಿರುತ್ತದೆ. ಫ್ರೇಮ್‌ವರ್ಕ್ ಪ್ರತಿ ಏಜೆಂಟ್‌ನ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಕ್ರಮಬದ್ಧವಾಗಿ ಮುಂದಿನ ಏಜೆಂಟ್‌ಗೆ ಪಾಸಾಗುವಂತೆ ನಿರ್ವಹಿಸುತ್ತದೆ, ಕೊನೆಗೆ ಅಂತಿಮ ಕ್ವೋಟ್ ರಚಿಸಲಾಗುತ್ತದೆ.

```python
# 02.python-ಏಜೆಂಟ್-ಫ್ರೇಮ್ವರ್ಕ್-ಕಾರ್ಯಪ್ರವಾಹ-ಘಮೋಡಲ್-ಅನುಕ್ರಮಿಕ.ipynb

# ಬಳಕೆದಾರರ ಸಂದೇಶದಲ್ಲಿ ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ ಎರಡೂ ಒಳಗೊಂಡಿವೆ
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಚಲಾಯಿಸಿ
async for event in workflow.run_stream(message):
    ...
```

#### .NET (C\#) ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

.NET ಉದಾಹರಣೆ Python ಆವೃತ್ತಿಯನ್ನು ಪ್ರತಿಬಿಂಬಿಸುತ್ತದೆ. ಮೂರು ಏಜೆಂಟ್‌ಗಳನ್ನು (`salesagent`, `priceagent`, `quoteagent`) ರಚಿಸಲಾಗುತ್ತದೆ. `WorkflowBuilder` ಅವುಗಳನ್ನು ಕ್ರಮಬದ್ಧವಾಗಿ ಸಂಪರ್ಕಿಸುತ್ತದೆ.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

ಬಳಕೆದಾರನ ಸಂದೇಶವನ್ನು ಚಿತ್ರ ಡೇಟಾ (bytes ರೂಪದಲ್ಲಿ) ಮತ್ತು ಪಠ್ಯ ಪ್ರಾಂಪ್ಟ್‌ನೊಂದಿಗೆ ರಚಿಸಲಾಗುತ್ತದೆ. `InProcessExecution.StreamAsync` ವಿಧಾನವು ವರ್ಕ್‌ಫ್ಲೋ ಪ್ರಾರಂಭಿಸುತ್ತದೆ, ಮತ್ತು ಅಂತಿಮ ಔಟ್‌ಪುಟ್ ಸ್ಟ್ರೀಮ್‌ನಿಂದ ಹಿಡಿಯಲಾಗುತ್ತದೆ.

### ಪ್ರಕರಣ 3: ಸಮಕಾಲೀನ ವರ್ಕ್‌ಫ್ಲೋ

ಈ ಮಾದರಿ ಕಾರ್ಯಗಳನ್ನು ಒಂದೇ ಸಮಯದಲ್ಲಿ ನಿರ್ವಹಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ, ಸಮಯವನ್ನು ಉಳಿಸಲು. ಇದು "fan-out" ಅನ್ನು ಹಲವಾರು ಏಜೆಂಟ್‌ಗಳಿಗೆ ಮತ್ತು "fan-in" ಅನ್ನು ಫಲಿತಾಂಶಗಳನ್ನು ಒಗ್ಗೂಡಿಸಲು ಒಳಗೊಂಡಿರುತ್ತದೆ.

#### ಸನ್ನಿವೇಶ ಹಿನ್ನೆಲೆ

ಒಬ್ಬ ಬಳಕೆದಾರ ಸಿಯಾಟಲ್‌ಗೆ ಪ್ರಯಾಣವನ್ನು ಯೋಜಿಸಲು ಕೇಳುತ್ತಾನೆ.

1.  **Dispatcher (Fan-Out)**: ಬಳಕೆದಾರನ ವಿನಂತಿಯನ್ನು ಒಂದೇ ಸಮಯದಲ್ಲಿ ಎರಡು ಏಜೆಂಟ್‌ಗಳಿಗೆ ಕಳುಹಿಸಲಾಗುತ್ತದೆ.
2.  **Researcher-Agent**: ಡಿಸೆಂಬರ್‌ನಲ್ಲಿ ಸಿಯಾಟಲ್‌ಗೆ ಪ್ರಯಾಣಕ್ಕೆ ಆಕರ್ಷಣೆಗಳು, ಹವಾಮಾನ ಮತ್ತು ಪ್ರಮುಖ ವಿಚಾರಗಳನ್ನು ಸಂಶೋಧಿಸುತ್ತದೆ.
3.  **Plan-Agent**: ಸ್ವತಂತ್ರವಾಗಿ ದಿನ-ಪ್ರತಿ-ದಿನದ ಪ್ರಯಾಣ ಯೋಜನೆಯನ್ನು ರಚಿಸುತ್ತದೆ.
4.  **Aggregator (Fan-In)**: ಸಂಶೋಧಕ ಮತ್ತು ಯೋಜಕನ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ, ಅಂತಿಮ ಫಲಿತಾಂಶವಾಗಿ ಒಟ್ಟಿಗೆ ಪ್ರಸ್ತುತಪಡಿಸುತ್ತದೆ.

*Concurrent Researcher ಮತ್ತು Planner ವರ್ಕ್‌ಫ್ಲೋ ಡಯಾಗ್ರಾಮ್.*

#### Python ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

`ConcurrentBuilder` ಈ ಮಾದರಿಯನ್ನು ರಚಿಸುವುದನ್ನು ಸರಳಗೊಳಿಸುತ್ತದೆ. ನೀವು ಭಾಗವಹಿಸುವ ಏಜೆಂಟ್‌ಗಳ ಪಟ್ಟಿ ನೀಡುತ್ತೀರಿ, ಮತ್ತು ಬಿಲ್ಡರ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅಗತ್ಯವಾದ fan-out ಮತ್ತು fan-in ಲಾಜಿಕ್ ಅನ್ನು ರಚಿಸುತ್ತದೆ.

```python
# 03.python-ಏಜೆಂಟ್-ಫ್ರೇಮ್‌ವರ್ಕ್-ಕಾರ್ಯಪ್ರವಾಹ-ಘಮೋಡಲ್-ಸಮಕಾಲಿಕ.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ಫ್ಯಾನ್-ಔಟ್/ಫ್ಯಾನ್-ಇನ್ ತರ್ಕವನ್ನು ನಿರ್ವಹಿಸುತ್ತದೆ
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# ಕಾರ್ಯಪ್ರವಾಹವನ್ನು ಚಲಾಯಿಸಿ
events = await workflow.run("Plan a trip to Seattle in December")
```

ಫ್ರೇಮ್‌ವರ್ಕ್ `research_agent` ಮತ್ತು `plan_agent` ಅನ್ನು ಸಮಾನಾಂತರವಾಗಿ ಕಾರ್ಯಗತಗೊಳಿಸುತ್ತದೆ, ಮತ್ತು ಅವರ ಅಂತಿಮ ಔಟ್‌ಪುಟ್‌ಗಳನ್ನು ಪಟ್ಟಿ ರೂಪದಲ್ಲಿ ಸಂಗ್ರಹಿಸುತ್ತದೆ.

#### .NET (C\#) ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

.NET ನಲ್ಲಿ, ಈ ಮಾದರಿಯು ಹೆಚ್ಚು ಸ್ಪಷ್ಟ ವ್ಯಾಖ್ಯಾನವನ್ನು ಅಗತ್ಯವಿರುತ್ತದೆ. fan-out ಮತ್ತು fan-in ಲಾಜಿಕ್ ಅನ್ನು ನಿರ್ವಹಿಸಲು ಕಸ್ಟಮ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳನ್ನು (`ConcurrentStartExecutor` ಮತ್ತು `ConcurrentAggregationExecutor`) ರಚಿಸಲಾಗುತ್ತದೆ.

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

`WorkflowBuilder` ನಂತರ ಈ ಕಸ್ಟಮ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳು ಮತ್ತು ಏಜೆಂಟ್‌ಗಳೊಂದಿಗೆ ಗ್ರಾಫ್ ಅನ್ನು ರಚಿಸಲು `AddFanOutEdge` ಮತ್ತು `AddFanInEdge` ಅನ್ನು ಬಳಸುತ್ತದೆ.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### ಪ್ರಕರಣ 4: ಶರ್ತಾಧಾರಿತ ವರ್ಕ್‌ಫ್ಲೋ

ಶರ್ತಾಧಾರಿತ ವರ್ಕ್‌ಫ್ಲೋಗಳು ಶಾಖೆ ಲಾಜಿಕ್ ಅನ್ನು ಪರಿಚಯಿಸುತ್ತವೆ, ಮಧ್ಯಂತರ ಫಲಿತಾಂಶಗಳ ಆಧಾರದ ಮೇಲೆ ವ್ಯವಸ್ಥೆ ವಿಭಿನ್ನ ಮಾರ್ಗಗಳನ್ನು ತೆಗೆದುಕೊಳ್ಳಲು ಅನುಮತಿಸುತ್ತದೆ.

#### ಸನ್ನಿವೇಶ ಹಿನ್ನೆಲೆ

ಈ ವರ್ಕ್‌ಫ್ಲೋ ತಾಂತ್ರಿಕ ಟ್ಯುಟೋರಿಯಲ್ ರಚನೆ ಮತ್ತು ಪ್ರಕಟಣೆಯನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸುತ್ತದೆ.

1.  **Evangelist-Agent**: ನೀಡಲಾದ ಔಟ್‌ಲೈನ್ ಮತ್ತು URL‌ಗಳ ಆಧಾರದ ಮೇಲೆ ಟ್ಯುಟೋರಿಯಲ್ ಡ್ರಾಫ್ಟ್ ಅನ್ನು ಬರೆಯುತ್ತದೆ.
2.  **ContentReviewer-Agent**: ಡ್ರಾಫ್ಟ್ ಅನ್ನು ಪರಿಶೀಲಿಸುತ್ತದೆ. ಇದು ಪದಗಳ ಸಂಖ್ಯೆಯನ್ನು 200 ಪದಗಳಿಗಿಂತ ಹೆಚ್ಚು ಎಂದು ಪರಿಶೀಲಿಸುತ್ತದೆ.
3.  **ಶರ್ತಾಧಾರಿತ ಶಾಖೆ**:
      * **ಅನುಮೋದಿತ (`Yes`)**: ವರ್ಕ್‌ಫ್ಲೋ `Publisher-Agent` ಗೆ ಮುಂದುವರಿಯುತ್ತದೆ.
      * **ನಿರಾಕರಿತ (`No`)**: ವರ್ಕ್‌ಫ್ಲೋ ನಿಲ್ಲುತ್ತದೆ ಮತ್ತು ನಿರಾಕರಣೆಯ ಕಾರಣವನ್ನು ಔಟ್‌ಪುಟ್ ಮಾಡುತ್ತದೆ.
4.  **Publisher-Agent**: ಡ್ರಾಫ್ಟ್ ಅನುಮೋದಿತವಾದರೆ, ಈ ಏಜೆಂಟ್ ವಿಷಯವನ್ನು Markdown ಫೈಲ್‌ಗೆ ಉಳಿಸುತ್ತದೆ.

#### Python ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

ಈ ಉದಾಹರಣೆಯು ಶರ್ತ ಲಾಜಿಕ್ ಅನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಲು ಕಸ್ಟಮ್ ಫಂಕ್ಷನ್, `select_targets`, ಅನ್ನು ಬಳಸುತ್ತದೆ. ಈ ಫಂಕ್ಷನ್ `add_multi_selection_edge_group` ಗೆ ಪಾಸಾಗುತ್ತದೆ ಮತ್ತು `review_result` ಕ್ಷೇತ್ರದ ಆಧಾರದ ಮೇಲೆ ವರ್ಕ್‌ಫ್ಲೋ ಅನ್ನು ನಿರ್ದೇಶಿಸುತ್ತದೆ.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ಈ ಕಾರ್ಯವು ವಿಮರ್ಶಾ ಫಲಿತಾಂಶದ ಆಧಾರದ ಮೇಲೆ ಮುಂದಿನ ಹಂತವನ್ನು ನಿರ್ಧರಿಸುತ್ತದೆ
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ಅನುಮೋದಿತವಾದರೆ, 'save_draft' ಕಾರ್ಯನಿರ್ವಾಹಕಕ್ಕೆ ಮುಂದುವರಿಯಿರಿ
        return [save_draft_id]
    else:
        # ತಿರಸ್ಕೃತವಾದರೆ, ವಿಫಲತೆಯನ್ನು ವರದಿ ಮಾಡಲು 'handle_review' ಕಾರ್ಯನಿರ್ವಾಹಕಕ್ಕೆ ಮುಂದುವರಿಯಿರಿ
        return [handle_review_id]

# ಕಾರ್ಯಪ್ರವಾಹ ನಿರ್ಮಾಪಕ ಮಾರ್ಗದರ್ಶನಕ್ಕಾಗಿ ಆಯ್ಕೆ ಕಾರ್ಯವನ್ನು ಬಳಸುತ್ತದೆ
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # ಬಹು-ಆಯ್ಕೆ ಅಂಚು ಶರತಾಲೋಚನೆಯನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುತ್ತದೆ
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` ಮುಂತಾದ ಕಸ್ಟಮ್ ಎಕ್ಸಿಕ್ಯೂಟರ್‌ಗಳನ್ನು JSON ಔಟ್‌ಪುಟ್ ಅನ್ನು ಪಾರ್ಸ್ ಮಾಡಲು ಮತ್ತು ಆಯ್ಕೆ ಫಂಕ್ಷನ್ ಪರಿಶೀಲಿಸಬಹುದಾದ ಬಲವಾದ-ಟೈಪ್‌ ಮಾಡಿದ ಆಬ್ಜೆಕ್ಟ್‌ಗಳಿಗೆ ಪರಿವರ್ತಿಸಲು ಬಳಸಲಾಗುತ್ತದೆ.

#### .NET (C\#) ಅನುಷ್ಠಾನ ವಿಶ್ಲೇಷಣೆ

.NET ಆವೃತ್ತಿ ಶರ್ತ ಫಂಕ್ಷನ್‌ನೊಂದಿಗೆ ಸಮಾನವಾದ ದೃಷ್ಠಿಕೋನವನ್ನು ಬಳಸುತ್ತದೆ. `Func<object?, bool>` ಅನ್ನು `ReviewResult` ಆಬ್ಜೆಕ್ಟ್‌ನ `Result` ಪ್ರಾಪರ್ಟಿಯನ್ನು ಪರಿಶೀಲಿಸಲು ವ್ಯಾಖ್ಯಾನಿಸಲಾಗುತ್ತದೆ.

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

`AddEdge` ವಿಧಾನದ `condition` ಪಾರಾಮೀಟರ್ `WorkflowBuilder` ಗೆ ಶಾಖೆ ಮಾರ್ಗವನ್ನು ರಚಿಸಲು ಅನುಮತಿಸುತ್ತದೆ. `GetCondition(expectedResult: "Yes")` ಶರ್ತವು true ಅನ್ನು ಹಿಂದಿರುಗಿಸಿದರೆ ಮಾತ್ರ ವರ್ಕ್‌ಫ್ಲೋ `publishExecutor` ಗೆ ಮಾರ್ಗವನ್ನು ಅನುಸರಿಸುತ್ತದೆ. ಇಲ್ಲವಾದರೆ, ಇದು `sendReviewerExecutor` ಮಾರ್ಗವನ್ನು ಅನುಸರಿಸುತ್ತದೆ.

## ತೀರ್ಮಾನ

Microsoft Agent Framework Workflow ಬಹು-ಏಜೆಂಟ್ ಸಿಸ್ಟಮ್‌ಗಳನ್ನು ಆರ್ಕೆಸ್ಟ್ರೇಟ್ ಮಾಡಲು ಬಲವಾದ ಮತ್ತು ಲಚೀಲವಾದ ಅಡಿಪಾಯವನ್ನು ಒದಗಿಸುತ್ತದೆ. ಅದರ ಗ್ರಾಫ್-ಆಧಾರಿತ ಆರ್ಕಿಟೆಕ್ಚರ್ ಮತ್ತು ಮೂಲ ಘಟಕಗಳನ್ನು ಬಳಸಿಕೊಂಡು, ಡೆವಲಪರ್‌ಗಳು Python ಮತ್ತು .NET ನಲ್ಲಿ ಸುಧಾರಿತ ವರ್ಕ್‌ಫ್ಲೋಗಳನ್ನು ವಿನ್ಯಾಸಗೊಳಿಸಿ ಅನುಷ್ಠಾನಗೊಳಿಸಬಹುದು. ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ಸರಳ ಕ್ರಮಬದ್ಧ ಪ್ರಕ್ರಿಯೆ, ಸಮಾನಾಂತರ ಕಾರ್ಯಾಚರಣೆ, ಅಥವಾ ಡೈನಾಮಿಕ್ ಶರ್ತ ಲಾಜಿಕ್ ಅಗತ್ಯವಿದ್ದರೂ, ಫ್ರೇಮ್‌ವರ್ಕ್ ಬಲವಾದ, ಮಿತವ್ಯಯದ ಮತ್ತು ಟೈಪ್-ಸೇಫ್ AI-ಚಾಲಿತ ಪರಿಹಾರಗಳನ್ನು ನಿರ್ಮಿಸಲು ಸಾಧನಗಳನ್ನು ಒದಗಿಸುತ್ತದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸಮೀಕ್ಷೆ**:  
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಖಚಿತತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮರ್ಪಕತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆ ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುಅರ್ಥಗಳು ಅಥವಾ ತಪ್ಪುಅನ್ವಯಗಳುಗಾಗಿ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->