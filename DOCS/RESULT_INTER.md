# Communication des résultats
1. [Analyse des résultats](#analyse-des-résultats)
2. [Analyse des résultats par l'IA](#analyse-des-résultats-par-lia)

3. [Commentaire](#commentaire)
## Analyse des résultats
**Produisez une analyse claire des résultats pour un public non technique.**
1. [Résultats du clustering](#résultats-du-clustering)
2. [Résultats des modèles](#résultats-des-modèles)
### Résultats du clustering

Les axes représentent bien l'inertie du jeu de données :

![{955EE42E-59DF-4EF2-BDC0-A6888CD8EB57}](https://github.com/user-attachments/assets/d428b604-2f30-42ee-a4a2-fb39a8e54c45)

Voici la représentation graphique de l'AFC :

![explor_var](https://github.com/user-attachments/assets/72b93daa-b63b-44ba-8712-c5dfafa690a6)

Voici les clusters créés grâce à l'AFC :

![image](https://github.com/user-attachments/assets/1b3ed17f-66a2-4559-b294-24aeabb006be)

Nous sommes satisfait par les résultats de l'AFC et utilisons les clusters. Voici leurs interpretations :
- Cluster 1 : Les institutions, avec des mots comme banque, finance et central, ce sont des jours où les posts faits parlent majoritairement des institution
- Cluster 2 : Le renouveaux, avec des mots comme cryptomonnaies, revolution et trading, ce sont des jours où les posts sont vers le future.
- Cluster 3 : Mixte, avezc des mots comme blockchain et gouvernements, ce sont des jours ou il n'y a pas qu'un type de posts.

### Résultats des modèles
**Ici nous exposerons nos résultats et les analyses**

L'ensemble des résultats est dans le [notebook modélisation](../modelisation.ipynb). Ici, nous n'exposeront pas les résultats. 
Dans l'ensemble : 
- Le réseau de neurones n'a pas réussi à avoir des bonnes prédictions que ce soit en problème classifier ou regressor. Le peu de données fait que le modèle n'arrivait pas à généraliser
  - Résultats du modèle classifier sur l'augmentation du prix du BTC :
    - 'R2': -0.9428733696290785, ==> Aberrant
    - 'RMSE': 0.6953011639636968,
    - 'MAE': 0.48344370860927155,
    - 'Precision': 0.5165562913907285
    - 'f1_score' : 0.626916524701874
- Le modèle Logit à produit des résultats moyen mais au dessus de l'aléatoire. Ce qui montre qu'avec peu de données, il reste meilleur qu'un réseau de neurone. Il différencie un peu les classes.
  - Résultats :
    - 'Precision': 0.5739514348785872
    - 'f1_score': 0.6614035087719298
      Le modèle logit est donc un peu meilleur que l'aléatoire et différencie mieux les classes que le modèle MLP.
- Les modèles du type decision tree ont eu de très bon résultat.
  - Résultats regressor :
    - 'R2': 0.8274397939842713,
    - 'RMSE': 0.09549287420375932,
    - 'MAE': 0.062075381236736435,
    - 'Precision': 0.8274397939842713
      Ici on a de très bonne metrics, certainement dû à un sur-entrainement. Pourtant voici les hyperparamêtre : criterion='entropy', max_depth=3, min_samples_leaf=4. Ils devraient pourtant permettre de ne pas trop over-fitter les données.
**Voici la visualisation des prédictions des modèles regressors :**
![image](https://github.com/user-attachments/assets/1c50c06b-9c16-4810-93bf-b9c71829dba7)
Comme on le vois les prédictions des modèles regressors ne sont pas excellente bien que l'arbre de décision s'approche bien plus de la courbe. On peut imaginer qu'il y a un peu d'overfitting dans tout ça malgrès les reglages des hyperparamêtres.

## Analyse des résultats par l'IA
**Demandez à l’IA une analyse similaire.**

1. Réseau de Neurones
Le réseau de neurones n'a pas réussi à produire de bonnes prédictions, que ce soit pour la classification ou la régression. Voici quelques points clés :

Problème de Généralisation : Le modèle n'a pas pu généraliser correctement en raison du peu de données disponibles. Cela signifie qu'il n'a pas pu apprendre efficacement à partir des données fournies.
- Résultats du Modèle Classifier :
  - R² : -0.94 (très mauvais, indique que le modèle ne capture pas la variabilité des données)
  - RMSE : 0.695 (erreur moyenne assez élevée)
  - MAE : 0.483 (erreur absolue moyenne élevée)
  - Précision : 0.517 (un peu mieux que le hasard)
  - <F1-score : 0.627 (performance moyenne)
Modèle Logit
Le modèle logistique (Logit) a produit des résultats moyens mais meilleurs que le hasard. Voici les points clés :

Performance : Le modèle a réussi à différencier les classes un peu mieux que le réseau de neurones.
Résultats :
Précision : 0.574 (meilleure que le hasard)
F1-score : 0.661 (performance acceptable)
Modèles de Type Arbre de Décision
Les modèles de type arbre de décision ont obtenu de très bons résultats. Voici les points clés :

Performance : Les métriques sont très bonnes, mais il y a un risque de sur-entraînement.
Résultats du Modèle Regressor :
R² : 0.827 (très bon, indique que le modèle capture bien la variabilité des données)
RMSE : 0.095 (erreur moyenne très faible)
MAE : 0.062 (erreur absolue moyenne très faible)
Précision : 0.827 (très bonne précision)
Interprétation des Résultats
Réseau de Neurones : Ce modèle n'a pas été efficace en raison du manque de données. Il n'a pas pu apprendre correctement à partir des données disponibles.
Modèle Logit : Ce modèle a montré des performances acceptables, meilleures que le hasard. Il est plus adapté pour des jeux de données limités.
Arbre de Décision : Ce modèle a obtenu les meilleurs résultats, mais il y a un risque de sur-entraînement. Cela signifie que le modèle pourrait être trop adapté aux données d'entraînement et moins performant sur de nouvelles données.
Conclusion
En résumé, les modèles de type arbre de décision ont montré les meilleures performances pour prédire les mouvements du prix du Bitcoin. Cependant, il est important de surveiller le risque de sur-entraînement. Le modèle logistique a également montré des résultats acceptables, tandis que le réseau de neurones n'a pas été efficace en raison du manque de données. Pour améliorer les performances, il serait bénéfique de collecter plus de données et d'explorer des techniques de régularisation pour éviter le sur-entraînement.
## Commentaire
Proposez une analyse du résultat et, le cas échéant, modifiez votre travail en fonction.
# Page suivante/Précedente
[DATA MODELISATION](DATA_MOD.md)/[RETOUR SUR EXPERIENCE](FEEDBACK.md)
