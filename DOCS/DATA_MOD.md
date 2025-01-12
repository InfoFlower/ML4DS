# Modélisation et évaluation 
On décris ici notre séléction de modèle.
## Choix du modèle, pipeline ?
**Choisissez et construisez des modèles ou pipelines adaptés au problème.**
Notre processus de collecte de données ne permet pas de mettre en place un pipeline stable d'entrainement puis de test. On utilise un train, test split classique sur nos données déjà modifiées. 
Le [notebook de modélisation](../modelisation.ipynb) est alors un ensemble d'entrainement de modèle. Ils sont tous répértoriés sur MLFlow pour l'analyse du meilleur modèle créé.
On l'utilisera pour nos prédictions future. Le versionnage et l'extraction des modèles se fait facilement sur MLflow.

## Test des modèles
**Tester les modèles avec une méthodologie rigoureuse.**
Entrainement de l'ensemble des modèles avec le même jeu de données, le tout avec un train test split fixé celon un certain random state. Permet une analyse stable des modèles.
## Evaluation
**Évaluer les performances avec des métriques appropriées.**
On utilise l'accuracy et le R2 pour connaitre les performances de notre modèle de type regressor. Pour les modèles de classifications, on observe la matrice de confusion en plus de ces deux metrics.

― Demandez à l’IA de critiquer constructivement vos choix et votre approche.
Choix du Modèle et Pipeline
Points Forts
Utilisation de MLFlow :

L'utilisation de MLFlow pour le versionnage et l'extraction des modèles est une excellente pratique. Cela permet de suivre les expériences, de comparer les performances des modèles et de faciliter la reproductibilité.
Train-Test Split :

L'utilisation d'un train-test split classique est une méthode standard et bien acceptée pour évaluer les performances des modèles.
Points Faibles et Améliorations Potentielles
Pipeline Stable :

Il est mentionné que le processus de collecte de données ne permet pas de mettre en place un pipeline stable d'entraînement et de test. Il serait utile de préciser pourquoi cela n'est pas possible et d'explorer des solutions pour stabiliser le pipeline. Par exemple, l'automatisation de la collecte de données et l'utilisation de pipelines de prétraitement robustes peuvent aider à stabiliser le processus.
Validation Croisée :

L'utilisation d'un train-test split unique peut introduire une variabilité dans les résultats. Il serait bénéfique d'utiliser une validation croisée (k-fold cross-validation) pour obtenir une estimation plus robuste des performances des modèles.
Documentation du Notebook :

Il serait utile de fournir plus de détails sur le contenu du notebook de modélisation. Par exemple, quels modèles ont été testés, quelles hyperparamètres ont été ajustés, et quelles méthodes d'optimisation ont été utilisées.
Test des Modèles
Points Forts
Méthodologie Rigoureuse :
L'entraînement de l'ensemble des modèles avec le même jeu de données et un train-test split fixé selon un certain random state est une bonne pratique. Cela permet une comparaison stable des performances des modèles.
Points Faibles et Améliorations Potentielles
Diversité des Modèles :

Il serait bénéfique de préciser quels modèles ont été testés et pourquoi ces modèles ont été choisis. Par exemple, pourquoi certains modèles de régression ou de classification ont-ils été sélectionnés par rapport à d'autres ?
Hyperparamètres :

Il n'est pas mentionné comment les hyperparamètres des modèles ont été ajustés. Il serait utile de décrire les techniques d'optimisation des hyperparamètres utilisées (par exemple, Grid Search, Random Search, Bayesian Optimization).
Évaluation
Points Forts
Métriques Appropriées :
L'utilisation de l'accuracy et du R² pour évaluer les performances des modèles de régression est appropriée. Pour les modèles de classification, l'observation de la matrice de confusion en plus de ces métriques est une bonne pratique.
Points Faibles et Améliorations Potentielles
Métriques Supplémentaires :

Pour les modèles de régression, il serait utile d'ajouter d'autres métriques comme le Mean Absolute Error (MAE) et le Root Mean Squared Error (RMSE) pour obtenir une évaluation plus complète des performances.
Pour les modèles de classification, il serait bénéfique d'ajouter des métriques comme la précision, le rappel, et le F1-score pour obtenir une évaluation plus détaillée des performances.
Interprétation des Résultats :

Il serait utile de fournir une interprétation des résultats obtenus. Par exemple, quelles sont les implications des valeurs d'accuracy, de R², et de la matrice de confusion pour les décisions de trading ?
― Proposez une analyse du résultat et, le cas échéant, modifiez votre travail en
fonction.
