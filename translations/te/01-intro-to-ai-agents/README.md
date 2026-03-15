[![AI ఏజెంట్లు ఏమిటి?](../../../translated_images/te/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(ఈ పాఠంలోని వీడియోను చూడటానికి పై చిత్రం క్లిక్ చేయండి)_


# AI ఏజెంట్లు మరియు ఏజెంట్ వినియోగ సందర్భాల పరిచయం

Welcome to the "AI Agents for Beginners" course! This course provides fundamental knowledge and applied samples for building AI Agents.

Join the <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord కమ్యూనిటీ</a> to meet other learners and AI Agent Builders and ask any questions you have about this course.

To start this course, we begin by getting a better understanding of what AI Agents are and how we can use them in the applications and workflows we build.

## Introduction

This lesson covers:

- AI ఏజెంట్లు ఏమిటి మరియు ఏవే వేరు రకాల ఏజెంట్లు ఉన్నాయో?
- ఏ వినియోగ సందర్భాలు AI ఏజెంట్లకు ఉత్తమంగా అనుకూలమవుతాయి మరియు అవి మనకు ఎలా సహాయపడతాయి?
- ఏజెంటిక్ పరిష్కారాలను డిజైన్ చేసినప్పుడు కొన్ని ప్రాథమిక నిర్మాణ భాగాలు ఏమిటి?

## Learning Goals
After completing this lesson, you should be able to:

- AI ఏజెంట్ సంకల్పనలను మరియు అవి ఇతర AI పరిష్కారాల నుండి ఎలా భిన్నమవుతాయో అర్థం చేసుకోవడం.
- AI ఏజెంట్లను అత్యంత సమర్థవంతంగా అప్లై చేయడం.
- వినియోగదారులకు మరియు ఖాతాదారులకు ఉత్పాదకంగా ఏజెంటిక్ పరిష్కారాలను డిజైన్ చేయడం.

## Defining AI Agents and Types of AI Agents

### What are AI Agents?

AI Agents are **systems** that enable **Large Language Models(LLMs)** to **perform actions** by extending their capabilities by giving LLMs **access to tools** and **knowledge**.

Let's break this definition into smaller parts:

- **System** - It's important to think about agents not as just a single component but as a system of many components. At the basic level, the components of an AI Agent are:
  - **Environment** - The defined space where the AI Agent is operating. For example, if we had a travel booking AI Agent, the environment could be the travel booking system that the AI Agent uses to complete tasks.
  - **Sensors** - Environments have information and provide feedback. AI Agents use sensors to gather and interpret this information about the current state of the environment. In the Travel Booking Agent example, the travel booking system can provide information such as hotel availability or flight prices.
  - **Actuators** - Once the AI Agent receives the current state of the environment, for the current task the agent determines what action to perform to change the environment. For the travel booking agent, it might be to book an available room for the user.

![AI ఏజెంట్లు ఏమిటి?](../../../translated_images/te/what-are-ai-agents.1ec8c4d548af601a.webp)

**Large Language Models** - The concept of agents existed before the creation of LLMs. The advantage of building AI Agents with LLMs is their ability to interpret human language and data. This ability enables LLMs to interpret environmental information and define a plan to change the environment.

**Perform Actions** - Outside of AI Agent systems, LLMs are limited to situations where the action is generating content or information based on a user's prompt. Inside AI Agent systems, LLMs can accomplish tasks by interpreting the user's request and using tools that are available in their environment.

**Access To Tools** - What tools the LLM has access to is defined by 1) the environment it's operating in and 2) the developer of the AI Agent. For our travel agent example, the agent's tools are limited by the operations available in the booking system, and/or the developer can limit the agent's tool access to flights.

**Memory+Knowledge** - Memory can be short-term in the context of the conversation between the user and the agent. Long-term, outside of the information provided by the environment, AI Agents can also retrieve knowledge from other systems, services, tools, and even other agents. In the travel agent example, this knowledge could be the information on the user's travel preferences located in a customer database.

### The different types of agents

Now that we have a general definition of AI Agents, let us look at some specific agent types and how they would be applied to a travel booking AI agent.

| **ఏజెంట్ రకం**                | **వివరణ**                                                                                                                       | **ఉదాహరణ**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **సింపుల రిఫ్లెక్స్ ఏజెంట్లు**      | పూర్వనిర్ధారిత నియమాల ఆధారంగా తక్షణ చర్యలు చేపడతాయి.                                                                                  | ప్రయాణ ఏజెంట్ ఇమెయిల్ సందర్భాన్ని అర్థం చేసుకుని ప్రయాణ సంబంధిత ఫిర్యాదులను కస్టమర్ సర్వీస్‌కి ఫార్వర్డ్ చేస్తుంది.                                                                                                                          |
| **మోడల్-ఆధారిత రిఫ్లెక్స్ ఏజెంట్లు** | ప్రపంచ మోడల్ మరియు ఆ మోడల్‌లో మార్పుల ఆధారంగా చర్యలు చేపడతాయి.                                                              | చరిత్రాత్మక ధర డేటాకు ప్రాప్తి ఆధారంగా గణనీయ ధర మార్పులున్న రూట్లకు ప్రయాణ ఏజెంట్ ప్రాధాన్యత ఇస్తుంది.                                                                                                             |
| **లక్ష్య-ఆధారిత ఏజెంట్లు**         | లక్ష్యాన్ని అర్థం చేసుకొని దానిని చేరుకోవడానికి అవసరమైన చర్యలను నిర్ణయించి ప్రణాళికలు తయారు చేస్తాయి.                                  | ప్రస్తుత స్థలం నుంచి గమ్యస్థానం చేరేందుకు అవసరమైన ప్రయాణ ఏర్పాట్లు (కారు, ప్రజా రవాణా, విమానాలు) నిర్ణయించి ప్రయాణం బుక్ చేస్తుంది.                                                                                |
| **యుటిలిటీ-ఆధారిత ఏజెంట్లు**      | ప్రాధాన్యాలను పరిగణలోకి తీసుకుని ట్రేడ్-ఆఫ్లను లెక్కలుగా మూల్యాంకనం చేసి లక్ష్యాలను ఎలా సాధించాలో నిర్ణయిస్తాయి.                                               | ప్రయాణ బుకింగ్ సమయంలో సౌకర్యం మరియు ఖర్చు మధ్య తులన చేసి ప్రయోజనాన్ని గరిష్ట పరిమితికి తీసుకెళ్తుంది.                                                                                                                                          |
| **లెర్నింగ్ ఏజెంట్లు**           | ఫీడ్‌బ్యాక్‌కు స్పందించి చర్యలను సర్దుబాటు చేయడం ద్వారా సమయానికొచ్చే మెరుగుదల చూపుతాయి.                                                        | పోస్ట్‑ట్రిప్ సర్వేల నుండి వచ్చిన కస్టమర్ ఫీడ్‌బ్యాక్‌ను ఉపయోగించి భవిష్యత్తు బుకింగ్‌లలో సవరణలు చేయడం ద్వారా ప్రయాణ ఏజెంట్ మెరుగవుతుంది.                                                                                                               |
| **హైరార్కికల్ ఏజెంట్లు**       | పటములో అనేక ఏజెంట్లు ఉండి, ఉన్నత-స్థాయి ఏజెంట్లు పనులను ఉప‑పనులుగా విభజించి తక్కువ-స్థాయి ఏజెంట్లు పూర్తి చేస్తాయి. | ప్రయాణ ఏజెంట్ ఒక ప్రయాణాన్ని రద్దు చేయడానికి పనిని ఉప‑పనులుగా విభజించి (ఉదాహరణకు, నిర్దిష్ట బుకింగ్‌లను రద్దు చేయడం) తక్కువ‑స్థాయి ఏజెంట్లు వాటిని పూర్తి చేసి ఉన్నత‑స్థాయి ఏజెంట్‌కు నివేదిక ఇస్తాయి.                                     |
| **బహుళ ఏజెంట్ సిస్టమ్స్ (MAS)** | ఏజెంట్లు స్వతంత్రంగా, సహకారంగా లేదా పోటీగా పనులను పూర్తి చేస్తాయి.                                                           | సహకారాత్మక: అనేక ఏజెంట్లు హోటల్లు, విమానాలు, వినోదం వంటి నిర్దిష్ట ప్రయాణ సేవలను బుక్ చేస్తాయి. పోటీదారుల: అనేక ఏజెంట్లు భాగస్వామ్య హోటల్ బుకింగ్ కాలెండర్‌పై నిర్వహణ చేసి కస్టమర్లను బుక్ చేయడంలో పోటీ పడతాయి. |

## When to Use AI Agents

In the earlier section, we used the Travel Agent use-case to explain how the different types of agents can be used in different scenarios of travel booking. We will continue to use this application throughout the course.

Let's look at the types of use cases that AI Agents are best used for:

![ఎప్పుడు AI ఏజెంట్లను ఉపయోగించాలి?](../../../translated_images/te/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Open-Ended Problems** - LLM కు టాస్క్ పూర్తి చేయడానికి అవసరమైన దశలను నిర్ణయించేందుకు అనుమతించడం, ఎందుకంటే అవి ఎప్పుడూ వర్క్‌ఫ్లోలో హార్డ్‑కోడ్ చేయలేవు.
- **Multi-Step Processes** - పలు దశల్లో టూల్స్ లేదా సమాచారాన్ని ఉపయోగించడం అవసరమయ్యే స్థాయి సంక్లిష్టత ఉన్న పనులు, ఒకే సారి పొందే రిట్రీవల్ కు బదులు పలుకు మార్గాల్లో పనిచేసే అవసరం ఉంటుంది.  
- **Improvement Over Time** - ఏజెంట్ తన పరిసరంనుండి లేదా వినియోగదారుల నుండి ఫీడ్‌బ్యాక్ పొందుతూ కాలక్రమేణా మెరుగుపడే విధంగా ఉండే పనులు, తద్వారా మెరుగైన ప్రయోజనాన్ని అందించగలవు.

We cover more considerations of using AI Agents in the Building Trustworthy AI Agents lesson.

## Basics of Agentic Solutions

### Agent Development

The first step in designing an AI Agent system is to define the tools, actions, and behaviors. In this course, we focus on using the **Azure AI Agent Service** to define our Agents. It offers features like:

- Selection of Open Models such as OpenAI, Mistral, and Llama
- Use of Licensed Data through providers such as Tripadvisor
- Use of standardized OpenAPI 3.0 tools

### Agentic Patterns

Communication with LLMs is through prompts. Given the semi-autonomous nature of AI Agents, it isn't always possible or required to manually reprompt the LLM after a change in the environment. We use **Agentic Patterns** that allow us to prompt the LLM over multiple steps in a more scalable way.

This course is divided into some of the current popular Agentic patterns.

### Agentic Frameworks

Agentic Frameworks allow developers to implement agentic patterns through code. These frameworks offer templates, plugins, and tools for better AI Agent collaboration. These benefits provide abilities for better observability and troubleshooting of AI Agent systems.

In this course, we will explore the Microsoft Agent Framework (MAF) for building production-ready AI agents.

## Sample Codes

- Python: [ఏజెంట్ ఫ్రేమ్‌వర్క్](./code_samples/01-python-agent-framework.ipynb)
- .NET: [ఏజెంట్ ఫ్రేమ్‌వర్క్](./code_samples/01-dotnet-agent-framework.md)

## Got More Questions about AI Agents?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Previous Lesson

[కోర్సు సెటప్](../00-course-setup/README.md)

## Next Lesson

[Agentic ఫ్రేమ్‌వర్క్‌లను అన్వేషించడం](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
నిరాకరణ:
ఈ పత్రాన్ని AI అనువాద సేవ Co-op Translator (https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి యత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా లోపాలు ఉండవచ్చు. మూల భాషలో ఉన్న అసలు పత్రాన్ని ప్రామాణిక మూలంగా పరిగణించండి. కీలకమైన సమాచారానికి వృత్తిపరమైన మానవ అనువాదాన్ని సూచిస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వలన ఏర్పడే ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడాల‌కు మేము బాధ్యులు కాదని దయచేసి గమనించండి.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->