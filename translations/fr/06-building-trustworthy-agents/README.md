[![Agents IA Fiables](../../../translated_images/fr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Cliquez sur l’image ci-dessus pour regarder la vidéo de cette leçon)_

# Construire des Agents IA Fiables

## Introduction

Cette leçon couvrira :

- Comment construire et déployer des agents IA sûrs et efficaces
- Les considérations importantes de sécurité lors du développement des agents IA.
- Comment préserver la confidentialité des données et des utilisateurs lors du développement des agents IA.

## Objectifs d’apprentissage

Après avoir terminé cette leçon, vous saurez comment :

- Identifier et atténuer les risques lors de la création d’agents IA.
- Mettre en œuvre des mesures de sécurité pour garantir la bonne gestion des données et des accès.
- Créer des agents IA qui préservent la confidentialité des données et offrent une expérience utilisateur de qualité.

## Sécurité

Commençons par examiner la construction d’applications agentiques sûres. La sécurité signifie que l’agent IA fonctionne comme prévu. En tant que développeurs d’applications agentiques, nous disposons de méthodes et d’outils pour maximiser la sécurité :

### Construction d’un Cadre de Message Système

Si vous avez déjà construit une application IA utilisant des modèles de langage de grande taille (LLM), vous connaissez l’importance de concevoir une consigne système robuste ou un message système. Ces consignes établissent les règles méta, les instructions et les lignes directrices sur la façon dont le LLM interagira avec l’utilisateur et les données.

Pour les agents IA, la consigne système est encore plus importante car les agents IA auront besoin d’instructions très spécifiques pour accomplir les tâches que nous avons conçues pour eux.

Pour créer des consignes système évolutives, nous pouvons utiliser un cadre de message système pour construire un ou plusieurs agents dans notre application :

![Construction d’un Cadre de Message Système](../../../translated_images/fr/system-message-framework.3a97368c92d11d68.webp)

#### Étape 1 : Créer un Message Métasystème

La consigne méta sera utilisée par un LLM pour générer les consignes système pour les agents que nous créons. Nous la concevons comme un modèle pour pouvoir créer efficacement plusieurs agents si nécessaire.

Voici un exemple de message métasystème que nous donnerions au LLM :

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```


#### Étape 2 : Créer une consigne basique

L’étape suivante consiste à créer une consigne basique pour décrire l’agent IA. Vous devez inclure le rôle de l'agent, les tâches que l’agent accomplira, ainsi que toute autre responsabilité de l’agent.

Voici un exemple :

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```


#### Étape 3 : Fournir la consigne basique au LLM

Nous pouvons maintenant optimiser ce message système en fournissant le message métasystème comme message système ainsi que notre message système basique.

Cela produira un message système mieux conçu pour guider nos agents IA :

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

La valeur de ce cadre de message système est de pouvoir faciliter la création de messages système pour plusieurs agents ainsi que d’améliorer vos messages système au fil du temps. Il est rare qu’un message système fonctionne parfaitement du premier coup pour votre cas d’usage complet. Pouvoir faire de petits ajustements et améliorations en modifiant le message système basique et en le traitant via le système vous permettra de comparer et d’évaluer les résultats.

## Comprendre les Menaces

Pour construire des agents IA dignes de confiance, il est important de comprendre et d’atténuer les risques et menaces pesant sur votre agent IA. Examinons seulement certaines des différentes menaces pesant sur les agents IA et comment vous pouvez mieux planifier et vous préparer à celles-ci.

![Comprendre les Menaces](../../../translated_images/fr/understanding-threats.89edeada8a97fc0f.webp)

### Tâche et Instruction

**Description :** Les attaquants tentent de modifier les instructions ou les objectifs de l’agent IA par des consignes ou en manipulant les entrées.

**Atténuation** : Exécutez des contrôles de validation et des filtres d’entrée pour détecter les consignes potentiellement dangereuses avant qu’elles ne soient traitées par l’agent IA. Comme ces attaques nécessitent généralement une interaction fréquente avec l’agent, limiter le nombre de tours dans une conversation est une autre manière de prévenir ce type d’attaque.

### Accès aux Systèmes Critiques

**Description :** Si un agent IA a accès à des systèmes et services qui stockent des données sensibles, les attaquants peuvent compromettre la communication entre l’agent et ces services. Cela peut être des attaques directes ou des tentatives indirectes pour obtenir des informations sur ces systèmes via l’agent.

**Atténuation** : Les agents IA devraient avoir accès aux systèmes uniquement en fonction des besoins afin de prévenir ce type d’attaque. La communication entre l’agent et le système devrait également être sécurisée. Mettre en œuvre une authentification et un contrôle d’accès est une autre méthode pour protéger cette information.

### Surcharge des Ressources et Services

**Description :** Les agents IA peuvent accéder à différents outils et services pour accomplir des tâches. Les attaquants peuvent exploiter cette capacité en envoyant un grand nombre de requêtes via l’agent IA, ce qui peut entraîner des défaillances système ou des coûts élevés.

**Atténuation :** Implémentez des politiques pour limiter le nombre de requêtes qu’un agent IA peut effectuer vers un service. Limiter le nombre de tours de conversation et de requêtes à votre agent IA est une autre manière de prévenir ce type d’attaque.

### Empoisonnement de la Base de Connaissances

**Description :** Ce type d’attaque ne cible pas directement l’agent IA, mais vise la base de connaissances et d’autres services que l’agent IA utilisera. Cela pourrait impliquer la corruption des données ou informations utilisées par l’agent, entraînant des réponses biaisées ou non désirées à l’utilisateur.

**Atténuation :** Effectuez des vérifications régulières des données que l’agent IA utilise dans ses flux de travail. Assurez-vous que l’accès à ces données est sécurisé et ne peut être modifié que par des individus de confiance pour éviter ce type d’attaque.

### Erreurs en Cascade

**Description :** Les agents IA accèdent à divers outils et services pour accomplir des tâches. Les erreurs causées par des attaquants peuvent entraîner des défaillances d’autres systèmes connectés à l’agent IA, rendant l’attaque plus étendue et plus difficile à dépanner.

**Atténuation** : Une méthode pour éviter cela est de faire fonctionner l’agent IA dans un environnement limité, comme exécuter des tâches dans un conteneur Docker, afin de prévenir les attaques directes sur le système. Créer des mécanismes de secours et une logique de réessai lorsque certains systèmes répondent par une erreur est une autre manière de prévenir des défaillances système plus larges.

## Humain dans la Boucle

Une autre manière efficace de construire des systèmes d’agents IA fiables est d’utiliser un humain dans la boucle. Cela crée un flux où les utilisateurs peuvent fournir des retours aux agents pendant l’exécution. Les utilisateurs agissent essentiellement comme des agents dans un système multi-agent en donnant leur approbation ou en arrêtant le processus en cours.

![Humain dans la Boucle](../../../translated_images/fr/human-in-the-loop.5f0068a678f62f4f.webp)

Voici un extrait de code utilisant le Microsoft Agent Framework pour montrer comment ce concept est implémenté :

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Créez le fournisseur avec une approbation humaine en boucle
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Créez l'agent avec une étape d'approbation humaine
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

Construire des agents IA dignes de confiance nécessite une conception soignée, des mesures de sécurité robustes, et une itération continue. En mettant en œuvre des systèmes structurés de méta-consignes, en comprenant les menaces potentielles, et en appliquant des stratégies d’atténuation, les développeurs peuvent créer des agents IA à la fois sûrs et efficaces. De plus, intégrer une approche humaine dans la boucle garantit que les agents IA restent alignés avec les besoins des utilisateurs tout en minimisant les risques. À mesure que l’IA évolue, garder une posture proactive sur la sécurité, la confidentialité, et les considérations éthiques sera essentiel pour favoriser la confiance et la fiabilité dans les systèmes pilotés par l’IA.

## Exemples de Code

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb) : démonstration pas à pas du cadre méta-consigne système.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb) : Portes d’approbation avant action, hiérarchisation des risques, et journalisation des audits pour agents fiables.

### Vous avez d’autres questions sur la construction d’agents IA fiables ?

Rejoignez le [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) pour rencontrer d’autres apprenants, participer aux heures de bureau, et obtenir des réponses à vos questions sur les agents IA.

## Ressources supplémentaires

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vue d’ensemble de l’IA responsable</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Évaluation des modèles IA générative et des applications IA</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Messages système de sécurité</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Modèle d’évaluation des risques</a>

## Leçon précédente

[Agentic RAG](../05-agentic-rag/README.md)

## Leçon suivante

[Modèle de conception de planification](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->