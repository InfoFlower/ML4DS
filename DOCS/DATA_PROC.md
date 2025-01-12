# Exploration et traitement des données
## Identifiez et décrivez les caractéristiques des données. Effectuez les
prétraitements nécessaires à ce stade.

1. Caractéristiques des données de marché :

    - Open time: The timestamp (in milliseconds) indicating when the candlestick period starts.
    - Open: The opening price of the asset for the candlestick period.
    - High: The highest price of the asset during the candlestick period.
    - Low: The lowest price of the asset during the candlestick period.
    - Close: The closing price of the asset for the candlestick period.
    - Volume: The trading volume of the asset for the candlestick period.
    - Close time: The timestamp (in milliseconds) indicating when the candlestick period ends.
    - Quote asset volume: The trading volume of the quote asset for the candlestick period.
    - Number of trades: The number of trades that occurred during the candlestick period.
    - Taker buy base asset volume: The volume of the base asset involved in taker trades during the candlestick period.
    - Taker buy quote asset volume: The volume of the quote asset involved in taker trades during the candlestick period.
    - Ignore: This column is typically ignored and contains no relevant data.

- On décide de ne garder que les données avec le traitement décris :
    - Open time: On va cinder cette variable dépendamment du jour de la semaine, du jour de l'année, ...
    
    - Quote asset volume 
    - Number of trades 
    - Taker buy base asset volume 
    - Taker buy quote asset volume
        Pour l'ensemble de ces variables on utilise un scaler pour les mettre en 0 et 1.

    - Close: Variable expliquée, on utilisera aussi un scaler pour la mettre en 0 et 1. (Pour les modèles de type regressor)
    - Close increase: Variable expliquée, on utilisera aussi l'évolution par rapport à la période n-1 pour la mettre en 0 et 1 (augmentation ou non).

2. Charactéristiques des données web :
    Ce sont des pages HTML avec des images, des titres, des textes, etc...

- On décide de ne garder que les données avec le traitement décris :
    Tout d'abord on utilise un script de scrapping pour ne récuperer que le contenu des balises voulu (Hn, p, a et div). Ensuite on passera le texte créé dans un script d'analyse textuel permettant de compter les mots et de supprimer ceux inutiles (exemple : "the" en anglais). Ensuite, avec un algorithme de selection. On choisi les mots à analyser dans l'AFC. La règle de décision étant :
        Nous voulons qu'un mot n'apparaisse pas dans au moins une des pages à travers le temps (pour éviter les mots du type "login", utilisé par le site comme mot technique pour se connecter.) Ensuite on veut que le mot ai été utilisé au moins une fois dans 50% des pages récupérées.
    On créé ensuite l'AFC avec ces mots séléctionnés. On utilise une HCPC pour créer des cluster pour enfin les réinjecter dans les données grâce à une jointure sur la date.
    
## Demandez à l’IA de critiquer constructivement votre approche.

### Caractéristiques des Données de Marché

#### Points Forts

- Sélection des Variables Pertinentes :
    La décision de ne garder que les variables pertinentes (Open time, Quote asset volume, Number of trades, Taker buy base asset volume, Taker buy quote asset volume, Close, Close increase) est judicieuse. Cela permet de se concentrer sur les informations les plus significatives pour l'analyse.
- Scaling des Variables :
    L'utilisation d'un scaler pour normaliser les variables entre 0 et 1 est une bonne pratique. Cela permet de standardiser les données et d'améliorer la performance des modèles de machine learning.
- Création de la Variable Close increase :
    La création de la variable Close increase pour représenter l'évolution du prix par rapport à la période précédente est une bonne idée. Cela permet de capturer la dynamique du marché.

#### Points Faibles et Améliorations Potentielles
- Traitement de Open time :
    La description du traitement de Open time est vague. Il serait utile de préciser comment cette variable sera transformée (par exemple, extraction du jour de la semaine, du jour de l'année, etc.).
- Justification des Variables Sélectionnées :
    Il serait bénéfique de fournir une justification plus détaillée pour le choix des variables sélectionnées. Par exemple, pourquoi Quote asset volume est-il plus pertinent que Volume ?
- Gestion des Valeurs Manquantes :
    Il n'est pas mentionné comment les valeurs manquantes seront gérées. Il est important de définir une stratégie pour traiter les valeurs manquantes (imputation, suppression, etc.).
### Caractéristiques des Données Web
#### Points Forts
- Scrapping et Sélection des Balises :
    L'utilisation d'un script de scrapping pour extraire le contenu des balises pertinentes (Hn, p, a, div) est une bonne approche. Cela permet de se concentrer sur les informations textuelles pertinentes.
- Analyse Textuelle :
    L'utilisation d'un script d'analyse textuelle pour compter les mots et supprimer les mots inutiles est une étape importante. Cela permet de nettoyer les données et de se concentrer sur les mots significatifs.
- Sélection des Mots pour l'AFC :
    La règle de décision pour sélectionner les mots à analyser dans l'AFC est bien pensée. Cela permet d'éviter les mots techniques et de se concentrer sur les mots pertinents.
#### Points Faibles et Améliorations Potentielles
- Justification de la Règle de Décision :
    Il serait utile de fournir une justification plus détaillée pour la règle de décision utilisée pour sélectionner les mots. Par exemple, pourquoi choisir un mot qui apparaît dans au moins 50% des pages ?
- Gestion des Synonymes :
    Il n'est pas mentionné comment les synonymes seront gérés. Il serait bénéfique d'utiliser des techniques de lemmatisation ou de stemming pour regrouper les mots similaires.
- Validation de l'AFC :
    Il serait utile de valider l'AFC en comparant les résultats avec d'autres techniques de réduction de dimensionnalité (par exemple, PCA).
### Jointure des Données
#### Points Forts
- Utilisation de la Jointure sur la Date :
    L'utilisation de la jointure sur la date pour combiner les données de marché et les données web est une bonne approche. Cela permet de synchroniser les deux jeux de données.
#### Points Faibles et Améliorations Potentielles
- Gestion des Dates Manquantes :
    Il n'est pas mentionné comment les dates manquantes seront gérées. Il serait important de définir une stratégie pour traiter les dates manquantes (imputation, suppression, etc.).
- Validation de la Jointure :
    Il serait utile de valider la jointure en vérifiant la cohérence des données combinées. Par exemple, vérifier que les dates correspondent bien entre les deux jeux de données.

― Proposez une analyse du résultat et, le cas échéant, modifiez votre travail en
fonction.