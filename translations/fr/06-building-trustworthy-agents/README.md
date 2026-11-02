[![Agents d'IA dignes de confiance](../../../translated_images/fr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_

# Construire des agents d'IA dignes de confiance

## Introduction

Cette leçon couvrira :

- Comment construire et déployer des agents d'IA sûrs et efficaces
- Considérations importantes en matière de sécurité lors du développement d'agents d'IA.
- Comment protéger les données et la vie privée des utilisateurs lors du développement d'agents d'IA.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous saurez comment :

- Identifier et atténuer les risques lors de la création d'agents d'IA.
- Mettre en œuvre des mesures de sécurité pour garantir une bonne gestion des données et des accès.
- Créer des agents d'IA qui préservent la confidentialité des données et offrent une expérience utilisateur de qualité.

## Sécurité

Examinons d'abord comment construire des applications agentiques sûres. La sécurité signifie que l'agent IA fonctionne comme prévu. En tant que concepteurs d'applications agentiques, nous disposons de méthodes et d'outils pour maximiser la sécurité :

### Construire un cadre pour les messages système

Si vous avez déjà construit une application d'IA en utilisant des modèles de langage large (LLM), vous connaissez l'importance de concevoir une invite système robuste ou un message système. Ces invites établissent les règles méta, instructions et directives sur la façon dont le LLM interagira avec l'utilisateur et les données.

Pour les agents d'IA, l'invite système est encore plus importante car les agents d'IA auront besoin d'instructions très spécifiques pour accomplir les tâches que nous avons conçues pour eux.

Pour créer des invites système évolutives, nous pouvons utiliser un cadre de message système pour construire un ou plusieurs agents dans notre application :

![Construire un cadre pour les messages système](../../../translated_images/fr/system-message-framework.3a97368c92d11d68.webp)

#### Étape 1 : Créer un message système méta

Le méta-invite sera utilisé par un LLM pour générer les invites système pour les agents que nous créons. Nous le concevons comme un modèle afin de pouvoir créer efficacement plusieurs agents si nécessaire.

Voici un exemple de message système méta que nous donnerions au LLM :

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Étape 2 : Créer une invite de base

L'étape suivante consiste à créer une invite de base pour décrire l'agent d'IA. Vous devez inclure le rôle de l'agent, les tâches que l'agent accomplira et toute autre responsabilité de l'agent.

Voici un exemple :

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Étape 3 : Fournir le message système de base au LLM

Maintenant, nous pouvons optimiser ce message système en fournissant le message système méta comme message système et notre message système de base.

Cela produira un message système mieux conçu pour guider nos agents d'IA :

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Étape 4 : Itérer et améliorer

La valeur de ce cadre de message système est de pouvoir facilement créer des messages système évolutifs pour plusieurs agents ainsi que d'améliorer vos messages système au fil du temps. Il est rare d'avoir un message système qui fonctionne parfaitement du premier coup pour votre cas d'utilisation complet. Pouvoir apporter de petits ajustements et améliorations en modifiant le message système de base et en le passant à travers le système vous permettra de comparer et d'évaluer les résultats.

## Comprendre les menaces

Pour construire des agents d'IA dignes de confiance, il est important de comprendre et d'atténuer les risques et menaces auxquels votre agent d'IA est exposé. Examinons quelques-unes des différentes menaces pour les agents d'IA et comment mieux planifier et vous y préparer.

![Comprendre les menaces](../../../translated_images/fr/understanding-threats.89edeada8a97fc0f.webp)

### Tâche et instruction

**Description :** Les attaquants tentent de modifier les instructions ou objectifs de l'agent d'IA via des invites ou en manipulant les entrées.

**Atténuation** : Effectuer des vérifications de validation et des filtres d'entrée pour détecter les invites potentiellement dangereuses avant qu'elles ne soient traitées par l'agent d'IA. Comme ces attaques nécessitent généralement une interaction fréquente avec l'agent, limiter le nombre de tours dans une conversation est une autre manière d'empêcher ce type d'attaques.

### Accès aux systèmes critiques

**Description :** Si un agent d'IA a accès à des systèmes et services qui stockent des données sensibles, les attaquants peuvent compromettre la communication entre l'agent et ces services. Il peut s'agir d'attaques directes ou de tentatives indirectes d'obtenir des informations sur ces systèmes via l'agent.

**Atténuation** : Les agents d'IA ne devraient avoir accès aux systèmes qu'en cas de besoin pour prévenir de tels types d'attaques. La communication entre l'agent et le système doit également être sécurisée. Mettre en place une authentification et un contrôle d'accès est une autre méthode pour protéger ces informations.

### Surcharge des ressources et services

**Description :** Les agents d'IA peuvent accéder à différents outils et services pour accomplir des tâches. Les attaquants peuvent exploiter cette capacité pour attaquer ces services en envoyant un grand volume de requêtes via l'agent d'IA, ce qui peut entraîner des défaillances du système ou des coûts élevés.

**Atténuation :** Mettre en œuvre des règles pour limiter le nombre de requêtes qu'un agent d'IA peut effectuer vers un service. Limiter le nombre de tours de conversation et de requêtes à votre agent d'IA est une autre manière de prévenir ce type d'attaques.

### Empoisonnement de la base de connaissances

**Description :** Ce type d'attaque ne cible pas directement l'agent d'IA mais la base de connaissances et d'autres services que l'agent d'IA utilisera. Cela peut impliquer la corruption des données ou informations que l'agent d'IA va utiliser pour accomplir une tâche, entraînant des réponses biaisées ou non désirées à l'utilisateur.

**Atténuation :** Effectuer des vérifications régulières des données que l'agent d'IA utilisera dans ses flux de travail. Assurer la sécurité de l'accès à ces données et qu'elles ne soient modifiées que par des personnes de confiance pour éviter ce type d'attaque.

### Erreurs en cascade

**Description :** Les agents d'IA accèdent à divers outils et services pour accomplir des tâches. Les erreurs causées par des attaquants peuvent entraîner des défaillances d'autres systèmes auxquels l'agent d'IA est connecté, rendant l'attaque plus étendue et plus difficile à diagnostiquer.

**Atténuation :** Une méthode pour éviter cela est de faire fonctionner l'agent d'IA dans un environnement limité, comme l'exécution des tâches dans un conteneur Docker, pour prévenir les attaques directes sur le système. Créer des mécanismes de secours et une logique de nouvelle tentative lorsque certains systèmes répondent par une erreur est une autre façon d'éviter de plus grandes défaillances.

## Humain dans la boucle

Une autre méthode efficace pour construire des systèmes agents d'IA dignes de confiance est d'utiliser un humain dans la boucle. Cela crée un flux où les utilisateurs peuvent fournir des retours aux agents pendant l'exécution. Essentiellement, les utilisateurs agissent comme agents dans un système multi-agent en fournissant une approbation ou en interrompant le processus en cours.

![Humain dans la boucle](../../../translated_images/fr/human-in-the-loop.5f0068a678f62f4f.webp)

Voici un extrait de code utilisant le cadre Microsoft Agent Framework pour montrer comment ce concept est implémenté :

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Créer le fournisseur avec approbation humaine intégrée
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Créer l'agent avec une étape d'approbation humaine
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# L'utilisateur peut examiner et approuver la réponse
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Conclusion

Construire des agents d'IA dignes de confiance nécessite une conception soignée, des mesures de sécurité robustes, et une itération continue. En mettant en œuvre des systèmes structurés de méta-invites, en comprenant les menaces potentielles, et en appliquant des stratégies d'atténuation, les développeurs peuvent créer des agents d'IA à la fois sûrs et efficaces. De plus, l'intégration d'une approche avec un humain dans la boucle garantit que les agents d'IA restent alignés avec les besoins des utilisateurs tout en minimisant les risques. À mesure que l'IA continue d'évoluer, adopter une posture proactive sur la sécurité, la confidentialité et les considérations éthiques sera la clé pour favoriser la confiance et la fiabilité des systèmes pilotés par l'IA.

## Exemples de code

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb) : démonstration étape par étape du cadre méta-invite de message système.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb) : portes d'approbation pré-action, hiérarchisation des risques, et journalisation d'audit pour agents dignes de confiance.

### Vous avez d'autres questions sur la construction d'agents d'IA dignes de confiance ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d'autres apprenants, assister aux heures de bureau et faire répondre vos questions sur les agents d'IA.

## Ressources supplémentaires

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Présentation de l'IA responsable</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Évaluation des modèles d'IA générative et des applications AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Messages système sécurisés</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Modèle d'évaluation des risques</a>

## Leçon précédente

[Agentic RAG](../05-agentic-rag/README.md)

## Leçon suivante

[Modèle de conception de planification](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->