# AI Agents for Beginners - Guide d'étude & Résumé du cours

This guide provides a summary of the "AI Agents for Beginners" course and explains key concepts, frameworks, and design patterns for building AI Agents.

## 1. Introduction aux agents d'IA

**Que sont les agents d'IA ?**
AI Agents are systems that extend the capabilities of Large Language Models (LLMs) by giving them access to **tools**, **knowledge**, and **memory**. Unlike a standard LLM chatbot that only generates text based on training data, an AI Agent can:
- **Perceive** its environment (via sensors or inputs).
- **Reason** about how to solve a problem.
- **Act** to change the environment (via actuators or tool execution).

**Composants clés d'un agent:**
- **Environnement**: The space where the agent operates (e.g., a booking system).
- **Capteurs**: Mechanisms to gather information (e.g., reading an API).
- **Actionneurs**: Mechanisms to perform actions (e.g., sending an email).
- **Cerveau (LLM)**: The reasoning engine that plans and decides which actions to take.

## 2. Cadres agentiques

Le cours utilise **Microsoft Agent Framework (MAF)** avec **Azure AI Foundry Agent Service V2** pour building agents:

| Composant | Objectif | Idéal pour |
|-----------|-------|----------|
| **Microsoft Agent Framework** | SDK Python/C# unifié pour agents, outils et flux de travail | Création d'agents avec des outils, flux de travail multi-agents et modèles de production. |
| **Azure AI Foundry Agent Service** | Runtime cloud géré | Déploiement sécurisé et évolutif avec gestion d'état intégrée, observabilité et confiance. |

## 3. Patrons de conception agentiques

Les patrons de conception aident à structurer le fonctionnement des agents pour résoudre des problèmes de manière fiable.

### **Patron d'utilisation d'outils** (Leçon 4)
Ce patron permet aux agents d'interagir avec le monde extérieur.
- **Concept**: On fournit à l'agent un "schéma" (une liste des fonctions disponibles et de leurs paramètres). Le LLM décide *quel* outil appeler et avec *quels* arguments en fonction de la demande de l'utilisateur.
- **Flux**: User Request -> LLM -> **Tool Selection** -> **Tool Execution** -> LLM (with tool output) -> Final Response.
- **Cas d'utilisation**: Retrieving real-time data (weather, stock prices), performing calculations, executing code.

### **Patron de planification** (Leçon 7)
Ce patron permet aux agents de résoudre des tâches complexes en plusieurs étapes.
- **Concept**: L'agent décompose un objectif de haut niveau en une succession de sous-tâches plus petites.
- **Approches**:
  - **Décomposition des tâches**: Splitting "Plan a trip" into "Book flight", "Book hotel", "Rent car".
  - **Planification itérative**: Réévaluer le plan en fonction des résultats des étapes précédentes (e.g., if the flight is full, choose a different date).
- **Implémentation**: Often involves a "Planner" agent that generates a structured plan (e.g., JSON) which is then executed by other agents.

## 4. Principes de conception

Lors de la conception d'agents, considérez trois dimensions:
- **Espace**: Agents should connect people and knowledge, be accessible but unobtrusive.
- **Temps**: Agents should learn from the *Past*, provide relevant nudges in the *Now*, and adapt for the *Future*.
- **Noyau**: Embrace uncertainty but establish trust through transparency and user control.

## 5. Résumé des leçons clés

- **Leçon 1**: Agents are systems, not just models. They perceive, reason, and act.
- **Leçon 2**: Microsoft Agent Framework abstracts the complexity of tool calling and state management.
- **Leçon 3**: Design with transparency and user control in mind.
- **Leçon 4**: Tools are the "hands" of the agent. Schéma definition is crucial for the LLM to understand how to use them.
- **Leçon 7**: Planning is the "executive function" of the agent, enabling it to tackle complex workflows.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Avertissement :
Ce document a été traduit à l'aide du service de traduction par IA [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'être précis, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original, dans sa langue d'origine, doit être considéré comme la version faisant foi. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un traducteur humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->