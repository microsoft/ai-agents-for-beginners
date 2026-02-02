# Agents IA pour Débutants - Guide d'Étude & Résumé du Cours

Ce guide fournit un résumé du cours "Agents IA pour Débutants" et explique les concepts clés, les frameworks et les modèles de conception pour construire des Agents IA.

## 1. Introduction aux Agents IA

**Qu’est-ce que les Agents IA ?**  
Les Agents IA sont des systèmes qui étendent les capacités des Modèles de Langage Large (LLMs) en leur donnant accès à des **outils**, des **connaissances** et une **mémoire**. Contrairement à un chatbot standard basé sur un LLM qui se contente de générer du texte à partir de données d'entraînement, un Agent IA peut :  
- **Percevoir** son environnement (via des capteurs ou des entrées).  
- **Raisonner** sur la manière de résoudre un problème.  
- **Agir** pour modifier l’environnement (via des actionneurs ou l’exécution d’outils).

**Composants clés d’un Agent :**  
- **Environnement** : L’espace où l’agent opère (par exemple, un système de réservation).  
- **Capteurs** : Mécanismes pour recueillir des informations (par exemple, lire une API).  
- **Actionneurs** : Mécanismes pour réaliser des actions (par exemple, envoyer un e-mail).  
- **Cerveau (LLM)** : Le moteur de raisonnement qui planifie et décide quelles actions entreprendre.

## 2. Frameworks Agentiques

Le cours couvre trois frameworks principaux pour construire des agents :

| Framework | Focus | Meilleur pour |
|-----------|-------|---------------|
| **Semantic Kernel** | SDK prêt pour la production en .NET/Python | Applications en entreprise, intégration de l'IA avec du code existant. |
| **AutoGen** | Collaboration multi-agent | Scénarios complexes nécessitant plusieurs agents spécialisés communiquant entre eux. |
| **Azure AI Agent Service** | Service cloud managé | Déploiement sécurisé et évolutif avec gestion d’état intégrée. |

## 3. Modèles de Conception Agentique

Les modèles de conception aident à structurer le fonctionnement des agents pour résoudre les problèmes de manière fiable.

### **Modèle d’Utilisation d’Outil** (Leçon 4)  
Ce modèle permet aux agents d’interagir avec le monde extérieur.  
- **Concept** : L’agent reçoit un "schéma" (une liste de fonctions disponibles et leurs paramètres). Le LLM décide *quel* outil appeler et avec *quels* arguments selon la demande de l’utilisateur.  
- **Flux** : Demande utilisateur -> LLM -> **Sélection de l’outil** -> **Exécution de l’outil** -> LLM (avec sortie de l’outil) -> Réponse finale.  
- **Cas d’usage** : Récupération de données en temps réel (météo, valeurs boursières), calculs, exécution de code.

### **Modèle de Planification** (Leçon 7)  
Ce modèle permet aux agents de résoudre des tâches complexes en plusieurs étapes.  
- **Concept** : L’agent décompose un objectif général en une séquence de sous-tâches plus petites.  
- **Approches** :  
  - **Décomposition de Tâche** : Diviser "Planifier un voyage" en "Réserver un vol", "Réserver un hôtel", "Louer une voiture".  
  - **Planification Itérative** : Réévaluer le plan à partir du résultat des étapes précédentes (par exemple, si le vol est complet, choisir une autre date).  
- **Implémentation** : Souvent impliquant un agent "Planificateur" qui génère un plan structuré (par ex. JSON) puis exécuté par d’autres agents.

## 4. Principes de Conception

Lors de la conception d’agents, considérer trois dimensions :  
- **Espace** : Les agents doivent connecter les personnes et les connaissances, être accessibles sans être intrusifs.  
- **Temps** : Les agents doivent apprendre du *Passé*, fournir des incitations pertinentes dans le *Présent*, et s’adapter pour le *Futur*.  
- **Cœur** : Accepter l’incertitude tout en établissant la confiance par la transparence et le contrôle utilisateur.

## 5. Résumé des Leçons Clés

- **Leçon 1** : Les agents sont des systèmes, pas seulement des modèles. Ils perçoivent, raisonnent et agissent.  
- **Leçon 2** : Les frameworks comme Semantic Kernel et AutoGen simplifient la complexité des appels d’outils et la gestion d’état.  
- **Leçon 3** : Concevoir avec transparence et contrôle utilisateur en tête.  
- **Leçon 4** : Les outils sont les "mains" de l’agent. La définition du schéma est cruciale pour que le LLM sache comment les utiliser.  
- **Leçon 7** : La planification est la "fonction exécutive" de l’agent, lui permettant de gérer des workflows complexes.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->