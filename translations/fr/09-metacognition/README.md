[![Conception multi-agent](../../../translated_images/fr/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Cliquez sur l'image ci-dessus pour voir la vidéo de cette leçon)_
# Métacognition chez les agents IA

## Introduction

Bienvenue dans la leçon sur la métacognition chez les agents IA ! Ce chapitre est conçu pour les débutants curieux de savoir comment les agents IA peuvent réfléchir à leurs propres processus de pensée. À la fin de cette leçon, vous comprendrez les concepts clés et serez équipé d'exemples pratiques pour appliquer la métacognition dans la conception d'agents IA.

## Objectifs d'apprentissage

Après avoir terminé cette leçon, vous serez capable de :

1. Comprendre les implications des boucles de raisonnement dans la définition des agents.
2. Utiliser des techniques de planification et d'évaluation pour aider les agents à s'auto-corriger.
3. Créer vos propres agents capables de manipuler du code pour accomplir des tâches.

## Introduction à la métacognition

La métacognition désigne les processus cognitifs de haut niveau impliquant la réflexion sur sa propre pensée. Pour les agents IA, cela signifie être capable d’évaluer et d’ajuster leurs actions en fonction de la conscience de soi et des expériences passées. La métacognition, ou « penser à la pensée », est un concept important dans le développement des systèmes IA agentiques. Elle implique que les systèmes IA soient conscients de leurs propres processus internes et capables de surveiller, réguler et adapter leur comportement en conséquence. Comme nous le faisons lorsque nous lisons l'atmosphère ou analysons un problème. Cette conscience de soi peut aider les systèmes IA à prendre de meilleures décisions, identifier des erreurs et améliorer leurs performances au fil du temps — ce qui renvoie de nouveau au test de Turing et au débat sur la prise de pouvoir éventuelle de l’IA.

Dans le contexte des systèmes IA agentiques, la métacognition peut aider à relever plusieurs défis, tels que :
- Transparence : Assurer que les systèmes IA peuvent expliquer leur raisonnement et leurs décisions.
- Raisonnement : Améliorer la capacité des systèmes IA à synthétiser l'information et à prendre des décisions solides.
- Adaptation : Permettre aux systèmes IA de s’ajuster à de nouveaux environnements et à des conditions changeantes.
- Perception : Améliorer la précision des systèmes IA dans la reconnaissance et l’interprétation des données de leur environnement.

### Qu'est-ce que la métacognition ?

La métacognition, ou « penser à la pensée », est un processus cognitif de haut niveau impliquant la conscience de soi et l'autorégulation de ses propres processus cognitifs. Dans le domaine de l'IA, la métacognition permet aux agents d’évaluer et d’adapter leurs stratégies et actions, conduisant à des capacités améliorées de résolution de problèmes et de prise de décision. En comprenant la métacognition, vous pouvez concevoir des agents IA non seulement plus intelligents, mais aussi plus adaptables et efficaces. Dans une véritable métacognition, on verrait l'IA raisonner explicitement sur son propre raisonnement.

Exemple : « J'ai priorisé les vols moins chers parce que... je pourrais manquer des vols directs, alors je vais revérifier. ».
Suivre comment ou pourquoi il a choisi un certain itinéraire.
- Noter qu'il a fait des erreurs parce qu’il s’est trop appuyé sur les préférences utilisateurs de la dernière fois, donc il modifie sa stratégie de prise de décision, pas seulement la recommandation finale.
- Diagnostiquer des schémas comme : « Chaque fois que je vois l’utilisateur mentionner ‘trop bondé’, je ne devrais pas seulement éliminer certaines attractions mais aussi réfléchir que ma méthode de sélection des ‘meilleures attractions’ est défaillante si je classe toujours par popularité. »

### Importance de la métacognition chez les agents IA

La métacognition joue un rôle crucial dans la conception des agents IA pour plusieurs raisons :

![Importance de la métacognition](../../../translated_images/fr/importance-of-metacognition.b381afe9aae352f7.webp)

- Auto-réflexion : Les agents peuvent évaluer leur propre performance et identifier des domaines à améliorer.
- Adaptabilité : Les agents peuvent modifier leurs stratégies en fonction des expériences passées et des environnements changeants.
- Correction d’erreurs : Les agents peuvent détecter et corriger les erreurs de manière autonome, menant à des résultats plus précis.
- Gestion des ressources : Les agents peuvent optimiser l’utilisation des ressources, telles que le temps et la puissance de calcul, en planifiant et évaluant leurs actions.

## Composants d'un agent IA

Avant d’aborder les processus métacognitifs, il est essentiel de comprendre les composants de base d’un agent IA. Un agent IA se compose généralement de :

- Persona : La personnalité et les caractéristiques de l’agent qui définissent comment il interagit avec les utilisateurs.
- Outils : Les capacités et fonctions que l’agent peut exécuter.
- Compétences : Les connaissances et expertises que l’agent possède.

Ces composants travaillent ensemble pour créer une « unité d’expertise » capable de réaliser des tâches spécifiques.

**Exemple** :
Considérez un agent de voyage, un service d'agent qui non seulement planifie vos vacances mais ajuste également son chemin en fonction des données en temps réel et des expériences antérieures des clients.

### Exemple : Métacognition dans un service d’agent de voyage

Imaginez que vous concevez un service d’agent de voyage propulsé par IA. Cet agent, « Agent de Voyage », assiste les utilisateurs dans la planification de leurs vacances. Pour incorporer la métacognition, l’Agent de Voyage doit évaluer et ajuster ses actions en fonction de la conscience de soi et des expériences passées. Voici comment la métacognition pourrait intervenir :

#### Tâche actuelle

La tâche actuelle est d’aider un utilisateur à planifier un voyage à Paris.

#### Étapes pour accomplir la tâche

1. **Recueillir les préférences de l'utilisateur** : Demandez à l'utilisateur ses dates de voyage, budget, intérêts (par exemple, musées, cuisine, shopping), et toute exigence spécifique.
2. **Récupérer les informations** : Recherchez des options de vols, hébergements, attractions, et restaurants correspondant aux préférences de l'utilisateur.
3. **Générer des recommandations** : Fournissez un itinéraire personnalisé avec détails des vols, réservations d’hôtel, et activités suggérées.
4. **Ajuster selon les retours** : Demandez à l'utilisateur des retours sur les recommandations et effectuez les ajustements nécessaires.

#### Ressources requises

- Accès aux bases de données de vols et réservations d’hôtels.
- Informations sur les attractions et restaurants parisiens.
- Données de retours utilisateurs issues des interactions précédentes.

#### Expérience et auto-réflexion

L'Agent de Voyage utilise la métacognition pour évaluer ses performances et apprendre des expériences passées. Par exemple :

1. **Analyse des retours utilisateurs** : L'Agent de Voyage révise les retours pour déterminer quelles recommandations ont été bien reçues et lesquelles ne l'ont pas été. Il ajuste ses suggestions futures en conséquence.
2. **Adaptabilité** : Si un utilisateur a mentionné précédemment qu'il n'aime pas les endroits bondés, l'Agent de Voyage évitera de recommander des sites touristiques populaires aux heures de pointe à l'avenir.
3. **Correction d’erreur** : Si l'Agent de Voyage a commis une erreur dans une réservation passée, comme suggérer un hôtel complet, il apprend à vérifier plus rigoureusement la disponibilité avant de faire des recommandations.

#### Exemple pratique pour développeur

Voici un exemple simplifié de ce à quoi pourrait ressembler le code de l'Agent de Voyage incorporant la métacognition :

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Rechercher des vols, hôtels et attractions en fonction des préférences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyser les retours et ajuster les recommandations futures
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Exemple d'utilisation
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Pourquoi la métacognition est importante

- **Auto-réflexion** : Les agents peuvent analyser leurs performances et identifier les domaines à améliorer.
- **Adaptabilité** : Les agents peuvent modifier leurs stratégies selon les retours et les conditions changeantes.
- **Correction d’erreurs** : Les agents peuvent détecter et corriger les erreurs de manière autonome.
- **Gestion des ressources** : Les agents peuvent optimiser l'utilisation des ressources telles que le temps et la puissance de calcul.

En incorporant la métacognition, l'Agent de Voyage peut offrir des recommandations de voyage plus personnalisées et précises, améliorant ainsi l'expérience utilisateur globale.

---

## 2. Planification chez les agents

La planification est un composant critique du comportement des agents IA. Elle consiste à définir les étapes nécessaires pour atteindre un objectif, en tenant compte de l’état actuel, des ressources et des obstacles possibles.

### Éléments de la planification

- **Tâche actuelle** : Définir clairement la tâche.
- **Étapes pour accomplir la tâche** : Décomposer la tâche en étapes réalisables.
- **Ressources nécessaires** : Identifier les ressources requises.
- **Expérience** : Utiliser les expériences passées pour guider la planification.

**Exemple** :
Voici les étapes que l'Agent de Voyage doit suivre pour aider efficacement un utilisateur à planifier son voyage :

### Étapes pour l'Agent de Voyage

1. **Recueillir les préférences de l'utilisateur**
   - Demandez à l'utilisateur des détails concernant ses dates de voyage, budget, intérêts, et exigences spécifiques.
   - Exemples : « Quand prévoyez-vous de voyager ? » « Quel est votre budget ? » « Quelles activités appréciez-vous en vacances ? »

2. **Récupérer les informations**
   - Recherchez des options de voyage pertinentes selon les préférences de l'utilisateur.
   - **Vols** : Cherchez des vols disponibles dans le budget et pour les dates choisies.
   - **Hébergements** : Trouvez des hôtels ou locations correspondant aux préférences de localisation, prix et commodités.
   - **Attractions et restaurants** : Identifiez des attractions populaires, activités et options de restauration alignées avec les intérêts de l'utilisateur.

3. **Générer des recommandations**
   - Compilez les informations récupérées dans un itinéraire personnalisé.
   - Fournissez les détails comme les options de vol, réservations d’hôtel, et activités suggérées, en adaptant les recommandations aux préférences de l'utilisateur.

4. **Présenter l’itinéraire à l'utilisateur**
   - Partagez l’itinéraire proposé pour qu’il soit examiné par l'utilisateur.
   - Exemple : « Voici un itinéraire suggéré pour votre voyage à Paris. Il inclut les détails des vols, les réservations d’hôtel, et une liste d’activités et restaurants recommandés. Qu’en pensez-vous ? »

5. **Collecter les retours**
   - Demandez à l’utilisateur son avis sur l’itinéraire proposé.
   - Exemples : « Aimez-vous les options de vol ? » « L’hôtel convient-il à vos besoins ? » « Y a-t-il des activités que vous souhaitez ajouter ou supprimer ? »

6. **Ajuster selon les retours**
   - Modifiez l’itinéraire en fonction des retours de l’utilisateur.
   - Effectuez les changements nécessaires concernant les vols, hébergement et activités afin de mieux correspondre aux préférences.

7. **Confirmation finale**
   - Présentez l’itinéraire mis à jour pour confirmation finale par l’utilisateur.
   - Exemple : « J’ai effectué les ajustements selon vos retours. Voici l’itinéraire mis à jour. Tout vous convient-il ? »

8. **Réserver et confirmer les réservations**
   - Une fois l'itinéraire approuvé par l'utilisateur, procédez à la réservation des vols, hébergements et activités pré-planifiées.
   - Envoyez les détails de confirmation à l'utilisateur.

9. **Offrir un support continu**
   - Restez disponible pour assister l'utilisateur en cas de modifications ou demandes supplémentaires avant et pendant son voyage.
   - Exemple : « Si vous avez besoin d’aide supplémentaire durant votre voyage, n'hésitez pas à me contacter à tout moment ! »

### Exemple d’interaction

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Exemple d'utilisation dans une demande de réservation
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Système RAG correctif

Commençons par comprendre la différence entre l’outil RAG et le chargement préventif de contexte.

![RAG vs Chargement du contexte](../../../translated_images/fr/rag-vs-context.9eae588520c00921.webp)

### Génération augmentée par récupération (RAG)

RAG combine un système de récupération avec un modèle génératif. Lorsqu’une requête est faite, le système de récupération extrait des documents ou données pertinents depuis une source externe, et ces informations récupérées sont utilisées pour enrichir l’entrée du modèle génératif. Cela aide le modèle à générer des réponses plus précises et contextuellement pertinentes.

Dans un système RAG, l’agent récupère des informations pertinentes d’une base de connaissances et les utilise pour générer des réponses ou actions appropriées.

### Approche RAG correctrice

L’approche RAG correctrice met l’accent sur l’utilisation des techniques RAG pour corriger les erreurs et améliorer la précision des agents IA. Cela implique :

1. **Technique de prompt** : Utiliser des prompts spécifiques pour guider l’agent dans la récupération d’informations pertinentes.
2. **Outil** : Implémenter des algorithmes et mécanismes permettant à l’agent d’évaluer la pertinence des informations récupérées et de générer des réponses précises.
3. **Évaluation** : Évaluer en continu les performances de l’agent et effectuer des ajustements pour améliorer précision et efficacité.

#### Exemple : RAG correcteur dans un agent de recherche

Considérez un agent de recherche qui récupère des informations sur le web pour répondre aux requêtes des utilisateurs. L’approche RAG correctrice pourrait inclure :

1. **Technique de prompt** : Formuler des requêtes de recherche basées sur l’entrée utilisateur.
2. **Outil** : Utiliser des algorithmes de traitement du langage naturel et apprentissage automatique pour classer et filtrer les résultats de recherche.
3. **Évaluation** : Analyser les retours utilisateurs pour identifier et corriger les inexactitudes des informations récupérées.

### RAG correcteur dans l'Agent de Voyage

Le RAG correcteur (Génération augmentée par récupération) améliore la capacité d’une IA à récupérer et générer des informations tout en corrigeant ses inexactitudes. Voyons comment l’Agent de Voyage peut utiliser cette approche RAG correctrice pour fournir des recommandations de voyage plus précises et pertinentes.

Cela implique :

- **Technique de prompt :** Utiliser des prompts spécifiques pour guider l’agent dans la récupération d’informations pertinentes.
- **Outil :** Implémenter des algorithmes et mécanismes qui permettent à l’agent d’évaluer la pertinence des informations récupérées et de générer des réponses précises.
- **Évaluation :** Évaluer continuellement la performance de l’agent et faire des ajustements pour améliorer sa précision et efficacité.

#### Étapes pour implémenter le RAG correctif dans l’Agent de Voyage

1. **Interaction initiale avec l’utilisateur**
   - L’Agent de Voyage recueille les préférences initiales de l’utilisateur, telles que destination, dates de voyage, budget, et centres d’intérêt.
   - Exemple :

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Récupération des informations**
   - L’Agent de Voyage récupère des informations sur les vols, hébergements, attractions, et restaurants en fonction des préférences utilisateurs.
   - Exemple :

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Génération des recommandations initiales**
   - L’Agent de Voyage utilise les informations récupérées pour générer un itinéraire personnalisé.
   - Exemple :

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Collecte des retours utilisateurs**
   - L’Agent de Voyage demande à l’utilisateur ses retours sur les recommandations initiales.
   - Exemple :

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Processus RAG correctif**
   - **Technique de prompt** : L’Agent de Voyage formule de nouvelles requêtes de recherche basées sur les retours de l’utilisateur.
     - Exemple :

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Outil** : L’Agent de Voyage utilise des algorithmes pour classer et filtrer les nouveaux résultats de recherche, en mettant l’accent sur la pertinence basée sur les retours utilisateurs.
     - Exemple :

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Évaluation** : L’Agent de Voyage évalue continuellement la pertinence et la précision de ses recommandations en analysant les retours et en ajustant les résultats.
     - Exemple :

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Exemple pratique

Voici un exemple simplifié de code Python incorporant l’approche RAG correctrice dans l’Agent de Voyage :

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Exemple d'utilisation
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Chargement préventif de contexte


Le chargement préventif du contexte consiste à charger les informations pertinentes ou le contexte de fond dans le modèle avant de traiter une requête. Cela signifie que le modèle a accès à ces informations dès le début, ce qui peut l’aider à générer des réponses plus informées sans avoir besoin de récupérer des données supplémentaires pendant le processus.

Voici un exemple simplifié de ce à quoi pourrait ressembler un chargement préventif du contexte pour une application d’agent de voyage en Python :

```python
class TravelAgent:
    def __init__(self):
        # Précharger les destinations populaires et leurs informations
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Récupérer les informations de destination à partir du contexte préchargé
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Exemple d'utilisation
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Explication

1. **Initialisation (méthode `__init__`)** : La classe `TravelAgent` précharge un dictionnaire contenant des informations sur des destinations populaires telles que Paris, Tokyo, New York et Sydney. Ce dictionnaire inclut des détails comme le pays, la monnaie, la langue et les principales attractions pour chaque destination.

2. **Récupération d’informations (méthode `get_destination_info`)** : Lorsqu’un utilisateur interroge sur une destination spécifique, la méthode `get_destination_info` récupère les informations pertinentes à partir du dictionnaire de contexte préchargé.

En préchargeant le contexte, l’application d’agent de voyage peut répondre rapidement aux requêtes des utilisateurs sans avoir à récupérer ces informations depuis une source externe en temps réel. Cela rend l’application plus efficace et réactive.

### Initialiser le plan avec un objectif avant d’itérer

Initialiser un plan avec un objectif consiste à commencer avec un objectif clair ou un résultat ciblé en tête. En définissant cet objectif dès le départ, le modèle peut l’utiliser comme principe directeur tout au long du processus itératif. Cela aide à garantir que chaque itération se rapproche de l’atteinte du résultat souhaité, rendant le processus plus efficace et ciblé.

Voici un exemple de comment vous pourriez initialiser un plan de voyage avec un objectif avant d’itérer pour un agent de voyage en Python :

### Scénario

Un agent de voyage souhaite planifier des vacances personnalisées pour un client. L’objectif est de créer un itinéraire de voyage qui maximise la satisfaction du client en fonction de ses préférences et de son budget.

### Étapes

1. Définir les préférences et le budget du client.
2. Initialiser le plan initial basé sur ces préférences.
3. Itérer pour affiner le plan, en optimisant la satisfaction du client.

#### Code Python

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Exemple d'utilisation
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Explication du code

1. **Initialisation (méthode `__init__`)** : La classe `TravelAgent` est initialisée avec une liste de destinations potentielles, chacune ayant des attributs comme le nom, le coût, et le type d’activité.

2. **Initialisation du plan (méthode `bootstrap_plan`)** : Cette méthode crée un plan de voyage initial basé sur les préférences et le budget du client. Elle parcourt la liste des destinations et les ajoute au plan si elles correspondent aux préférences du client et rentrent dans le budget.

3. **Correspondance des préférences (méthode `match_preferences`)** : Cette méthode vérifie si une destination correspond aux préférences du client.

4. **Itération du plan (méthode `iterate_plan`)** : Cette méthode affine le plan initial en essayant de remplacer chaque destination du plan par une meilleure, en tenant compte des préférences du client et des contraintes budgétaires.

5. **Calcul du coût (méthode `calculate_cost`)** : Cette méthode calcule le coût total du plan courant, incluant une destination potentielle nouvelle.

#### Exemple d’utilisation

- **Plan initial** : L’agent de voyage crée un plan initial basé sur les préférences du client pour les visites touristiques et un budget de 2000 $.
- **Plan affiné** : L’agent de voyage itère le plan, optimisant en fonction des préférences du client et du budget.

En initialisant le plan avec un objectif clair (par exemple, maximiser la satisfaction du client) et en itérant pour affiner le plan, l’agent de voyage peut créer un itinéraire personnalisé et optimisé pour le client. Cette approche garantit que le plan de voyage correspond aux préférences et au budget du client dès le départ et s’améliore à chaque itération.

### Tirer parti des LLM pour le reclassement et le scoring

Les grands modèles de langage (LLM) peuvent être utilisés pour le reclassement et le scoring en évaluant la pertinence et la qualité des documents récupérés ou des réponses générées. Voici comment cela fonctionne :

**Récupération :** L’étape initiale de récupération obtient un ensemble de documents ou de réponses candidats à partir de la requête.

**Reclassement :** Le LLM évalue ces candidats et les reclassifie en fonction de leur pertinence et qualité. Cette étape garantit que les informations les plus pertinentes et de haute qualité sont présentées en premier.

**Scoring :** Le LLM attribue des scores à chaque candidat, reflétant leur pertinence et qualité. Cela aide à sélectionner la meilleure réponse ou document pour l’utilisateur.

En exploitant les LLM pour le reclassement et le scoring, le système peut fournir des informations plus précises et contextuellement pertinentes, améliorant l’expérience globale utilisateur.

Voici un exemple de comment un agent de voyage pourrait utiliser un grand modèle de langage (LLM) pour le reclassement et le scoring de destinations en fonction des préférences utilisateurs en Python :

#### Scénario - Voyage basé sur les préférences

Un agent de voyage souhaite recommander les meilleures destinations à un client selon ses préférences. Le LLM aidera à reclasser et scorer les destinations afin de présenter les options les plus pertinentes.

#### Étapes :

1. Collecter les préférences de l’utilisateur.
2. Récupérer une liste de destinations potentielles.
3. Utiliser le LLM pour reclasser et scorer les destinations selon les préférences utilisateur.

Voici comment vous pouvez mettre à jour l’exemple précédent pour utiliser les services Azure OpenAI :

#### Prérequis

1. Vous devez avoir un abonnement Azure.
2. Créez une ressource Azure OpenAI et obtenez votre clé API.

#### Exemple de code Python

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Générer une invite pour Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Définir les en-têtes et la charge utile pour la requête
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Appeler l'API Azure OpenAI pour obtenir les destinations reclassées et notées
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extraire et retourner les recommandations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Exemple d'utilisation
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Explication du code - Gestionnaire de préférences

1. **Initialisation** : La classe `TravelAgent` est initialisée avec une liste de destinations potentielles, chacune ayant des attributs comme le nom et la description.

2. **Obtention des recommandations (méthode `get_recommendations`)** : Cette méthode génère une requête pour le service Azure OpenAI basée sur les préférences de l’utilisateur et effectue une requête HTTP POST à l’API Azure OpenAI pour obtenir les destinations reclassées et scorées.

3. **Génération de la requête (méthode `generate_prompt`)** : Cette méthode construit une requête pour Azure OpenAI, incluant les préférences utilisateur et la liste des destinations. La requête guide le modèle pour reclasser et scorer les destinations selon les préférences fournies.

4. **Appel API** : La bibliothèque `requests` est utilisée pour effectuer une requête HTTP POST à l’endpoint Azure OpenAI. La réponse contient les destinations reclassées et scorées.

5. **Exemple d’utilisation** : L’agent de voyage collecte les préférences utilisateur (par exemple, intérêt pour les visites culturelles et la diversité culturelle) et utilise le service Azure OpenAI pour obtenir des recommandations reclassées et scorées pour les destinations.

Veillez à remplacer `your_azure_openai_api_key` par votre clé API Azure OpenAI réelle et `https://your-endpoint.com/...` par l’URL réelle de votre déploiement Azure OpenAI.

En utilisant le LLM pour le reclassement et le scoring, l’agent de voyage peut fournir des recommandations plus personnalisées et pertinentes, améliorant ainsi l’expérience client globale.

### RAG : Technique de Prompting vs Outil

Le Retrieval-Augmented Generation (RAG) peut être à la fois une technique de prompting et un outil dans le développement d’agents IA. Comprendre la distinction entre les deux peut vous aider à exploiter RAG plus efficacement dans vos projets.

#### RAG en tant que Technique de Prompting

**Qu’est-ce que c’est ?**

- En tant que technique de prompting, RAG consiste à formuler des requêtes ou prompts spécifiques pour guider la récupération d’informations pertinentes à partir d’un grand corpus ou d’une base de données. Ces informations sont ensuite utilisées pour générer des réponses ou actions.

**Comment ça marche :**

1. **Formuler les prompts** : Créer des prompts ou requêtes bien structurés basés sur la tâche ou l’entrée utilisateur.
2. **Récupérer les informations** : Utiliser les prompts pour rechercher des données pertinentes dans une base de connaissances ou un jeu de données préexistant.
3. **Générer une réponse** : Combiner les informations récupérées avec des modèles d’IA génératifs pour produire une réponse complète et cohérente.

**Exemple avec un agent de voyage** :

- Entrée utilisateur : "Je veux visiter des musées à Paris."
- Prompt : "Trouve les meilleurs musées à Paris."
- Informations récupérées : Détails sur le Louvre, Musée d’Orsay, etc.
- Réponse générée : "Voici quelques-uns des musées les plus célèbres à Paris : le Louvre, le Musée d’Orsay et le Centre Pompidou."

#### RAG en tant qu’Outil

**Qu’est-ce que c’est ?**

- En tant qu’outil, RAG est un système intégré qui automatise le processus de récupération et de génération, facilitant pour les développeurs l’implémentation de fonctionnalités IA complexes sans avoir à créer manuellement des prompts pour chaque requête.

**Comment ça marche :**

1. **Intégration** : Intégrer RAG dans l’architecture de l’agent IA, lui permettant de gérer automatiquement la récupération et la génération.
2. **Automatisation** : L’outil gère tout le processus, de la réception de l’entrée utilisateur à la génération de la réponse finale, sans nécessiter de prompts explicites à chaque étape.
3. **Efficacité** : Améliore les performances de l’agent en rationalisant le processus de récupération et de génération, permettant des réponses plus rapides et précises.

**Exemple avec un agent de voyage** :

- Entrée utilisateur : "Je veux visiter des musées à Paris."
- Outil RAG : Récupère automatiquement les informations sur les musées et génère une réponse.
- Réponse générée : "Voici quelques-uns des musées phares à Paris : le Louvre, le Musée d’Orsay et le Centre Pompidou."

### Comparaison

| Aspect                 | Technique de Prompting                                     | Outil                                                 |
|------------------------|-----------------------------------------------------------|-------------------------------------------------------|
| **Manuel vs Automatique**| Formulation manuelle des prompts pour chaque requête.     | Processus automatisé de récupération et génération.   |
| **Contrôle**            | Offre plus de contrôle sur le processus de récupération.  | Rationalise et automatise la récupération et génération.|
| **Flexibilité**         | Permet des prompts personnalisés selon les besoins.       | Plus efficace pour les implémentations à grande échelle.|
| **Complexité**          | Nécessite la création et l’ajustement des prompts.        | Plus facile à intégrer dans l’architecture d’un agent IA.|

### Exemples pratiques

**Exemple de technique de prompting :**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Exemple d’outil :**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Évaluation de la pertinence

L’évaluation de la pertinence est un aspect crucial des performances d’un agent IA. Elle garantit que les informations récupérées et générées sont appropriées, exactes et utiles pour l’utilisateur. Explorons comment évaluer la pertinence dans les agents IA, avec des exemples pratiques et des techniques.

#### Concepts clés dans l’évaluation de la pertinence

1. **Conscience du contexte** :
   - L’agent doit comprendre le contexte de la requête utilisateur pour récupérer et générer des informations pertinentes.
   - Exemple : Si un utilisateur demande « meilleurs restaurants à Paris », l’agent doit considérer les préférences de l’utilisateur, comme le type de cuisine ou le budget.

2. **Exactitude** :
   - Les informations fournies par l’agent doivent être factuellement correctes et à jour.
   - Exemple : Recommander des restaurants actuellement ouverts avec de bonnes critiques, plutôt que des options obsolètes ou fermées.

3. **Intention utilisateur** :
   - L’agent doit déduire l’intention derrière la requête pour fournir l’information la plus pertinente.
   - Exemple : Si un utilisateur demande des « hôtels économiques », l’agent doit prioriser des options abordables.

4. **Boucle de retour** :
   - Collecter et analyser continuellement les retours utilisateurs aide l’agent à affiner son processus d’évaluation de la pertinence.
   - Exemple : Intégrer les évaluations et retours sur les recommandations précédentes pour améliorer les réponses futures.

#### Techniques pratiques pour évaluer la pertinence

1. **Scorage de pertinence** :
   - Attribuer un score de pertinence à chaque élément récupéré selon sa correspondance avec la requête et les préférences de l’utilisateur.
   - Exemple :

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Filtrage et classement** :
   - Filtrer les éléments non pertinents et classer les restants selon leurs scores de pertinence.
   - Exemple :

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Retourner les 10 éléments les plus pertinents
     ```

3. **Traitement du langage naturel (NLP)** :
   - Utiliser des techniques de NLP pour comprendre la requête utilisateur et récupérer des informations pertinentes.
   - Exemple :

     ```python
     def process_query(query):
         # Utilisez le TAL pour extraire les informations clés de la requête de l'utilisateur
         processed_query = nlp(query)
         return processed_query
     ```

4. **Intégration des retours utilisateur** :
   - Recueillir les retours utilisateurs sur les recommandations fournies et les utiliser pour ajuster l’évaluation de la pertinence à l’avenir.
   - Exemple :

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Exemple : Évaluation de la pertinence dans un agent de voyage

Voici un exemple pratique de la manière dont Travel Agent peut évaluer la pertinence des recommandations de voyage :

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Retourner les 10 éléments les plus pertinents

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Exemple d'utilisation
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Recherche avec intention

La recherche avec intention consiste à comprendre et interpréter le but ou l’objectif sous-jacent d’une requête utilisateur pour récupérer et générer l’information la plus pertinente et utile possible. Cette approche va au-delà de la simple correspondance de mots-clés et vise à cerner les besoins réels et le contexte de l’utilisateur.

#### Concepts clés dans la recherche avec intention

1. **Compréhension de l’intention utilisateur** :
   - L’intention utilisateur peut être catégorisée en trois types principaux : informationnelle, navigationnelle et transactionnelle.
     - **Intention informationnelle** : L’utilisateur cherche des informations sur un sujet (ex : « Quels sont les meilleurs musées à Paris ? »).
     - **Intention navigationnelle** : L’utilisateur veut accéder à un site ou une page spécifique (ex : « site officiel du Musée du Louvre »).
     - **Intention transactionnelle** : L’utilisateur souhaite effectuer une transaction, comme réserver un vol ou un achat (ex : « Réserver un vol pour Paris »).

2. **Conscience du contexte** :
   - Analyser le contexte de la requête permet d’identifier précisément l’intention. Cela inclut les interactions précédentes, les préférences utilisateur et les détails spécifiques de la requête en cours.

3. **Traitement du langage naturel (NLP)** :
   - Des techniques de NLP sont employées pour comprendre et interpréter les requêtes en langage naturel des utilisateurs. Cela inclut la reconnaissance d’entités, l’analyse de sentiments, et le parsing de requêtes.

4. **Personnalisation** :
   - Personnaliser les résultats de recherche selon l’historique, les préférences et les retours utilisateur améliore la pertinence des informations fournies.

#### Exemple pratique : Recherche avec intention dans Travel Agent

Prenons Travel Agent en exemple pour voir comment la recherche avec intention peut être mise en œuvre.

1. **Collecte des préférences utilisateur**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Compréhension de l’intention utilisateur**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Conscience du contexte**


   ```python
   def analyze_context(query, user_history):
       # Combiner la requête actuelle avec l'historique de l'utilisateur pour comprendre le contexte
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Rechercher et Personnaliser les Résultats**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Exemple de logique de recherche pour une intention informative
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Exemple de logique de recherche pour une intention de navigation
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Exemple de logique de recherche pour une intention transactionnelle
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Exemple de logique de personnalisation
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Retourner les 10 meilleurs résultats personnalisés
   ```

5. **Exemple d'Utilisation**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Générer du Code en Tant qu'Outil

Les agents générateurs de code utilisent des modèles d'IA pour écrire et exécuter du code, résoudre des problèmes complexes et automatiser des tâches.

### Agents Générateurs de Code

Les agents générateurs de code utilisent des modèles d'IA générative pour écrire et exécuter du code. Ces agents peuvent résoudre des problèmes complexes, automatiser des tâches et fournir des informations précieuses en générant et exécutant du code dans divers langages de programmation.

#### Applications Pratiques

1. **Génération Automatisée de Code** : Générer des extraits de code pour des tâches spécifiques, telles que l'analyse de données, le scraping web ou l'apprentissage automatique.
2. **SQL comme RAG** : Utiliser des requêtes SQL pour récupérer et manipuler des données depuis des bases de données.
3. **Résolution de Problèmes** : Créer et exécuter du code pour résoudre des problèmes spécifiques, comme l'optimisation d'algorithmes ou l'analyse de données.

#### Exemple : Agent Générateur de Code pour l'Analyse de Données

Imaginez que vous concevez un agent générateur de code. Voici comment cela pourrait fonctionner :

1. **Tâche** : Analyser un jeu de données pour identifier des tendances et des motifs.
2. **Étapes** :
   - Charger le jeu de données dans un outil d'analyse de données.
   - Générer des requêtes SQL pour filtrer et agréger les données.
   - Exécuter les requêtes et récupérer les résultats.
   - Utiliser les résultats pour générer des visualisations et des insights.
3. **Ressources Nécessaires** : Accès au jeu de données, outils d'analyse de données et capacités SQL.
4. **Expérience** : Utiliser les résultats d'analyses passées pour améliorer la précision et la pertinence des analyses futures.

### Exemple : Agent Générateur de Code pour Agent de Voyage

Dans cet exemple, nous allons concevoir un agent générateur de code, Agent de Voyage, pour aider les utilisateurs à planifier leurs voyages en générant et exécutant du code. Cet agent peut gérer des tâches telles que la récupération d'options de voyage, le filtrage des résultats et la compilation d'un itinéraire en utilisant l'IA générative.

#### Vue d'Ensemble de l'Agent Générateur de Code

1. **Collecte des Préférences Utilisateur** : Récupère les entrées utilisateur telles que la destination, les dates de voyage, le budget et les intérêts.
2. **Génération de Code pour Récupérer des Données** : Génère des extraits de code pour obtenir des données sur les vols, hôtels et attractions.
3. **Exécution du Code Généré** : Exécute le code généré pour récupérer des informations en temps réel.
4. **Génération d'Itinéraire** : Compile les données récupérées en un plan de voyage personnalisé.
5. **Ajustement Basé sur les Retours** : Reçoit les retours utilisateur et régénère le code si nécessaire pour affiner les résultats.

#### Implémentation Étape par Étape

1. **Collecte des Préférences Utilisateur**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Génération de Code pour Récupérer des Données**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Exemple : Générer du code pour rechercher des vols en fonction des préférences de l'utilisateur
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Exemple : Générer du code pour rechercher des hôtels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Exécution du Code Généré**

   ```python
   def execute_code(code):
       # Exécutez le code généré en utilisant exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Génération d'Itinéraire**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Ajustement Basé sur les Retours**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Ajuster les préférences en fonction des retours des utilisateurs
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Régénérer et exécuter le code avec des préférences mises à jour
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Tirer parti de la conscience environnementale et du raisonnement

Se baser sur le schéma de la table peut en effet améliorer le processus de génération des requêtes en tirant parti de la conscience de l'environnement et du raisonnement.

Voici un exemple de comment cela peut être fait :

1. **Compréhension du Schéma** : Le système comprendra le schéma de la table et utilisera cette information pour ancrer la génération des requêtes.
2. **Ajustement Basé sur les Retours** : Le système ajustera les préférences utilisateur en fonction des retours et raisonnera sur les champs du schéma à mettre à jour.
3. **Génération et Exécution des Requêtes** : Le système générera et exécutera des requêtes pour récupérer des données mises à jour sur les vols et hôtels selon les nouvelles préférences.

Voici un exemple de code Python mis à jour qui intègre ces concepts :

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Ajuster les préférences en fonction des retours des utilisateurs
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Raisonnement basé sur le schéma pour ajuster les autres préférences liées
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Logique personnalisée pour ajuster les préférences en fonction du schéma et des retours
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Générer du code pour récupérer les données de vol en fonction des préférences mises à jour
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Générer du code pour récupérer les données d'hôtel en fonction des préférences mises à jour
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simuler l'exécution du code et retourner des données factices
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Générer un itinéraire basé sur les vols, hôtels et attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Exemple de schéma
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Exemple d'utilisation
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Régénérer et exécuter le code avec les préférences mises à jour
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Explication - Réservation Basée sur les Retours

1. **Connaissance du Schéma** : Le dictionnaire `schema` définit comment les préférences doivent être ajustées en fonction des retours. Il inclut des champs comme `favorites` et `avoid`, avec des ajustements correspondants.
2. **Ajustement des Préférences (méthode `adjust_based_on_feedback`)** : Cette méthode ajuste les préférences selon les retours utilisateur et le schéma.
3. **Ajustements Basés sur l'Environnement (méthode `adjust_based_on_environment`)** : Cette méthode personnalise les ajustements en fonction du schéma et des retours.
4. **Génération et Exécution des Requêtes** : Le système génère du code pour récupérer des données mises à jour sur les vols et hôtels en fonction des préférences ajustées et simule l'exécution de ces requêtes.
5. **Génération d'Itinéraire** : Le système crée un itinéraire mis à jour basé sur les nouvelles données de vols, hôtels et attractions.

En rendant le système conscient de l'environnement et en raisonnant à partir du schéma, il peut générer des requêtes plus précises et pertinentes, conduisant à de meilleures recommandations de voyage et une expérience utilisateur plus personnalisée.

### Utiliser SQL comme technique de génération augmentée par la récupération (RAG)

SQL (Structured Query Language) est un outil puissant pour interagir avec les bases de données. Lorsqu'il est utilisé dans le cadre d'une approche Retrieval-Augmented Generation (RAG), SQL peut récupérer des données pertinentes dans des bases pour informer et générer des réponses ou actions dans les agents d'IA. Explorons comment SQL peut être utilisé comme technique RAG dans le contexte d'Agent de Voyage.

#### Concepts Clés

1. **Interaction avec la Base de Données** :
   - SQL est utilisé pour interroger les bases, récupérer l'information pertinente et manipuler les données.
   - Exemple : Récupérer les détails des vols, informations d'hôtel et attractions depuis une base de données de voyages.

2. **Intégration avec RAG** :
   - Des requêtes SQL sont générées en fonction des entrées et préférences utilisateur.
   - Les données récupérées sont ensuite utilisées pour générer des recommandations ou actions personnalisées.

3. **Génération Dynamique des Requêtes** :
   - L'agent IA génère des requêtes SQL dynamiques basées sur le contexte et les besoins utilisateur.
   - Exemple : Personnaliser les requêtes SQL pour filtrer les résultats selon budget, dates et intérêts.

#### Applications

- **Génération Automatisée de Code** : Générer des extraits de code pour des tâches spécifiques.
- **SQL comme RAG** : Utiliser des requêtes SQL pour manipuler des données.
- **Résolution de Problèmes** : Créer et exécuter du code pour résoudre des problèmes.

**Exemple** :
Un agent d'analyse de données :

1. **Tâche** : Analyser un jeu de données pour trouver des tendances.
2. **Étapes** :
   - Charger le jeu de données.
   - Générer des requêtes SQL pour filtrer les données.
   - Exécuter les requêtes et récupérer les résultats.
   - Générer des visualisations et des insights.
3. **Ressources** : Accès au jeu de données, capacités SQL.
4. **Expérience** : Utiliser les résultats passés pour améliorer les analyses futures.

#### Exemple Pratique : Utiliser SQL dans Agent de Voyage

1. **Collecte des Préférences Utilisateur**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Génération des Requêtes SQL**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Exécution des Requêtes SQL**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Génération des Recommandations**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Exemples de Requêtes SQL

1. **Requête de Vol**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Requête d'Hôtel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Requête d'Attraction**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

En tirant parti de SQL comme partie de la technique Retrieval-Augmented Generation (RAG), les agents IA comme Agent de Voyage peuvent récupérer dynamiquement et utiliser des données pertinentes pour fournir des recommandations précises et personnalisées.

### Exemple de Métacognition

Pour démontrer une implémentation de métacognition, créons un agent simple qui *réfléchit à son processus de prise de décision* tout en résolvant un problème. Pour cet exemple, nous construirons un système où un agent essaie d'optimiser le choix d'un hôtel, mais ensuite évalue son propre raisonnement et ajuste sa stratégie lorsqu'il fait des erreurs ou des choix sous-optimaux.

Nous allons simuler cela en utilisant un exemple basique où l'agent sélectionne des hôtels en fonction d'une combinaison de prix et de qualité, mais il va "réfléchir" à ses décisions et s'ajuster en conséquence.

#### Comment ceci illustre la métacognition :

1. **Décision Initiale** : L'agent choisira l'hôtel le moins cher, sans comprendre l'impact de la qualité.
2. **Réflexion et Évaluation** : Après le choix initial, l'agent vérifiera si l'hôtel est un "mauvais" choix via les retours utilisateur. S'il trouve que la qualité de l'hôtel était trop basse, il réfléchira à son raisonnement.
3. **Ajustement de la Stratégie** : L'agent adapte sa stratégie en fonction de sa réflexion en passant de "le moins cher" à "la meilleure qualité", améliorant ainsi son processus de prise de décision dans les itérations futures.

Voici un exemple :

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stocke les hôtels choisis précédemment
        self.corrected_choices = []  # Stocke les choix corrigés
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Stratégies disponibles

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Supposons que nous ayons des retours d'utilisateurs qui nous disent si le dernier choix était bon ou non
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Ajuster la stratégie si le choix précédent était insatisfaisant
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simuler une liste d'hôtels (prix et qualité)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Créer un agent
agent = HotelRecommendationAgent()

# Étape 1 : L'agent recommande un hôtel en utilisant la stratégie "la moins chère"
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Étape 2 : L'agent réfléchit au choix et ajuste la stratégie si nécessaire
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Étape 3 : L'agent recommande à nouveau, cette fois en utilisant la stratégie ajustée
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Capacités de Métacognition des Agents

L'essentiel ici est la capacité de l'agent à :
- Évaluer ses choix précédents et son processus de prise de décision.
- Ajuster sa stratégie basée sur cette réflexion, soit la métacognition en action.

Il s'agit d'une forme simple de métacognition où le système est capable d'ajuster son raisonnement basé sur un retour interne.

### Conclusion

La métacognition est un outil puissant qui peut significativement améliorer les capacités des agents IA. En incorporant des processus métacognitifs, vous pouvez concevoir des agents plus intelligents, adaptatifs et efficaces. Utilisez les ressources supplémentaires pour explorer plus avant le monde fascinant de la métacognition dans les agents IA.

### Vous avez d'autres questions sur le modèle de conception Métacognition ?

Rejoignez le [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) pour rencontrer d'autres apprenants, assister aux heures de bureau et obtenir des réponses à vos questions sur les Agents IA.

## Leçon Précédente

[Modèle de Conception Multi-Agent](../08-multi-agent/README.md)

## Leçon Suivante

[Agents IA en Production](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue native doit être considéré comme la source faisant autorité. Pour les informations critiques, il est recommandé de recourir à une traduction professionnelle réalisée par un humain. Nous ne saurions être tenus responsables des malentendus ou erreurs d'interprétation découlant de l'utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->