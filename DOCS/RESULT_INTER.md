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
- Le modèle Logit à produit des résultats moyen mais au dessus de l'aléatoire. Ce qui montre qu'avec peu de données, il reste meilleur qu'un réseau de neurone.
  - Résultats :
    - 
- Les modèles du type decision tree ont eu de très bon résultat.

**Voici la visualisation de leurs prédictions :**


## Analyse des résultats par l'IA
**Demandez à l’IA une analyse similaire.**
## Commentaire
Proposez une analyse du résultat et, le cas échéant, modifiez votre travail en fonction.
# Page suivante/Précedente
[DATA MODELISATION](DATA_MOD.md)/[RETOUR SUR EXPERIENCE](FEEDBACK.md)
