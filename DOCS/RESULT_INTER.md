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
    - 'R2': -0.23111349803079118, ==> aberrant
    - 'RMSE': 0.5547001962252291,
    - 'MAE': 0.3076923076923077,
    - 'Precision': 0.6923076923076923
    - 'f1_score' : 0.4890829694323144
  - Résultats du modèle regressor sur l'augmentation du prix du BTC :
      - 'R2': 0.4642677093973947,
      - 'RMSE': 0.16158200478263618,
      - 'MAE': 0.12987705475997963,
      - 'Precision': 0.4642677093973947
- Le modèle Logit à produit des résultats moyen mais au dessus de l'aléatoire. Ce qui montre qu'avec peu de données, il reste meilleur qu'un réseau de neurone. Il différencie un peu les classes.
  - Résultats :
    - 'Precision': 0.7157190635451505
    - 'f1_score': 0.669260700389105
      Le modèle logit est donc un peu meilleur que l'aléatoire et différencie mieux les classes que le modèle MLP.
- Les modèles du type decision tree ont eu de très bon résultat.
  - Résultats regressor :
    - 'R2': 0.8274397939842713,
    - 'RMSE': 0.09549287420375932,
    - 'MAE': 0.062075381236736435,
    - 'Precision': 0.8274397939842713
  - Résultats classifier :
    - 'R2': 0.10342821339061947,
    - 'RMSE': 0.4733711731385092,
    - 'MAE': 0.22408026755852842,
    - 'Precision': 0.7759197324414716
      
      Ici on a de très bonne metrics, certainement dû à un sur-entrainement. Pourtant voici les hyperparamêtre : criterion='entropy', max_depth=3, min_samples_leaf=4. Ils devraient pourtant permettre de ne pas trop over-fitter les données.
**Voici la visualisation des prédictions des modèles regressors :**

![image](https://github.com/user-attachments/assets/1403d6a6-fb1f-4cef-85cb-d70cad36fc4b)

Comme on le vois les prédictions des modèles regressors ne sont pas excellente bien que l'arbre de décision s'approche bien plus de la courbe. On peut imaginer qu'il y a un peu d'overfitting dans tout ça malgrès les reglages des hyperparamêtres.

## Analyse des résultats par l'IA
**Demandez à l’IA une analyse similaire.**

## Réseau de Neurones

### Classifier

- **R2** : -0.231
- **RMSE** : 0.555
- **MAE** : 0.308
- **Precision** : 0.692
- **f1_score** : 0.489

### Regressor

- **R2** : 0.464
- **RMSE** : 0.162
- **MAE** : 0.130
- **Precision** : 0.464

### Interprétation des Métriques

1. **R2 (Coefficient de Détermination)** :
   - **Classifier** : -0.231
     - Un R2 négatif indique que le modèle performe moins bien que la moyenne des données. C'est un signe de mauvaise généralisation.
   - **Regressor** : 0.464
     - Un R2 de 0.464 montre que le modèle explique environ 46.4% de la variance des données, ce qui est modéré mais insuffisant pour des prédictions précises.

2. **RMSE (Erreur Quadratique Moyenne)** :
   - **Classifier** : 0.555
     - Une RMSE élevée indique que les prédictions sont en moyenne éloignées des valeurs réelles, ce qui est un signe de mauvaise performance.
   - **Regressor** : 0.162
     - Une RMSE plus faible montre que les prédictions sont plus proches des valeurs réelles, mais il y a encore de la place pour l'amélioration.

3. **MAE (Erreur Absolue Moyenne)** :
   - **Classifier** : 0.308
     - Une MAE élevée indique que les prédictions sont en moyenne éloignées des valeurs réelles, ce qui est un signe de mauvaise performance.
   - **Regressor** : 0.130
     - Une MAE plus faible montre que les prédictions sont plus proches des valeurs réelles, mais il y a encore de la place pour l'amélioration.

4. **Precision** :
   - **Classifier** : 0.692
     - Une précision de 0.692 indique que le modèle a une capacité modérée à prédire correctement les classes positives.
   - **Regressor** : 0.464
     - Une précision de 0.464 montre que le modèle a une capacité modérée à prédire correctement les valeurs réelles.

5. **f1_score** :
   - **Classifier** : 0.489
     - Un f1_score de 0.489 indique un équilibre modéré entre la précision et le rappel, mais reste insuffisant pour des prédictions précises.

## Modèle Logit

- **Precision** : 0.716
- **f1_score** : 0.669

### Interprétation des Métriques

1. **Precision** :
   - Une précision de 0.716 indique que le modèle a une capacité modérée à prédire correctement les classes positives, légèrement meilleure que le réseau de neurones.

2. **f1_score** :
   - Un f1_score de 0.669 montre un équilibre modéré entre la précision et le rappel, légèrement meilleur que le réseau de neurones mais encore insuffisant pour des prédictions précises.

## Modèles de Type Decision Tree

### Regressor

- **R2** : 0.827
- **RMSE** : 0.095
- **MAE** : 0.062
- **Precision** : 0.827

### Classifier

- **R2** : 0.103
- **RMSE** : 0.473
- **MAE** : 0.224
- **Precision** : 0.776

### Interprétation des Métriques

1. **R2 (Coefficient de Détermination)** :
   - **Regressor** : 0.827
     - Un R2 de 0.827 indique que le modèle explique environ 82.7% de la variance des données, ce qui est excellent.
   - **Classifier** : 0.103
     - Un R2 de 0.103 montre que le modèle explique environ 10.3% de la variance des données, ce qui est modéré.

2. **RMSE (Erreur Quadratique Moyenne)** :
   - **Regressor** : 0.095
     - Une RMSE très faible indique que les prédictions sont très proches des valeurs réelles, ce qui est un signe de très bonne performance.
   - **Classifier** : 0.473
     - Une RMSE modérée montre que les prédictions sont raisonnablement proches des valeurs réelles.

3. **MAE (Erreur Absolue Moyenne)** :
   - **Regressor** : 0.062
     - Une MAE très faible indique que les prédictions sont très proches des valeurs réelles, ce qui est un signe de très bonne performance.
   - **Classifier** : 0.224
     - Une MAE modérée montre que les prédictions sont raisonnablement proches des valeurs réelles.

4. **Precision** :
   - **Regressor** : 0.827
     - Une précision de 0.827 indique que le modèle a une capacité excellente à prédire correctement les valeurs réelles.
   - **Classifier** : 0.776
     - Une précision de 0.776 montre que le modèle a une capacité très bonne à prédire correctement les classes positives.

## Conclusion

Les modèles de type Decision Tree semblent être les plus performants pour la prédiction du prix du Bitcoin, avec des résultats particulièrement impressionnants pour le regressor. Le modèle Logit offre des performances moyennes mais reste supérieur à un réseau de neurones, qui n'a pas réussi à généraliser correctement en raison du peu de données disponibles. Pour améliorer les performances, il serait bénéfique d'augmenter la quantité de données d'entraînement et d'explorer des techniques de régularisation pour éviter le sur-entraînement des modèles Decision Tree.


## Commentaire
**Proposez une analyse du résultat et, le cas échéant, modifiez votre travail en fonction.**

L'IA a proposer une analyse plutôt similaire. Les metrics du modèle final nous conviennent. Pas de modifications à effectuer. En sommes, l'IA à mieux expliquer que moi l'implication de ces metrics.

# Page suivante/Précedente
[DATA MODELISATION](DATA_MOD.md)/[RETOUR SUR EXPERIENCE](FEEDBACK.md)
