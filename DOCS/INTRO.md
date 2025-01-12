# Introduction / Sélection des données 
## Identifiez au moins un jeu de données pour le projet. Décrivez vos motivations, le processus de recherche.
1. Jeu de données utilisé :
   - Les données marché du BitCoin jour par jour depuis 17 08 2017 (Début des données de l'API binance)
   - Les données web de [News Bitcoin](https://news.bitcoin.com) grâce à [WayBackMachine](https://archive.org/help/wayback_api.php)
   
      A partir du 18 05 2023 les données sont corrompues, les pages webs ne sont pas accessibles. Nous aurons alors les données du 17 août 2017 au 18 mai 2023 pour entrainer et tester notre modèle.

2. Motivations :
    - Création manuelle du jeu de données
    - Jointure entre le web et les données marché
    - Scrapping pour organiser les données web
    - Utilisation d'une ACM pour formaliser les données webs
    - Imaginons que les metrics soient bonnes, on gagne de l'argent !
3. Processus de recherche :
    1. Collecte des données web et marché
    2. Scrapping des pages pour récuperer les balises pertinentes
    3. Utilisation des outils d'analyses textuelles apris en cours (Statistiques textuelles)
    4. Utilisation du clustering comme appris en cours (Clustering)
    5. Jointure entre les deux jeux de données
    6. Utilisation des pratiques ML pour trouver le meilleur modèle
    7. Utilisation des pratiques de MLops pour versionner le code et les modèles

## Utilisez l’IA pour explorer des sources de données ouvertes, générer des idées de problématiques ou identifier des angles d’analyse inédits.

### Réponse de l'IA :

#### Exploration des sources de données ouvertes, génération d'idées de problématiques ou identification des angles d’analyse inédits

- Sources de données ouvertes :
    - CoinMarketCap : Données historiques sur les prix, les volumes de trading, et les capitalisations de marché de diverses cryptomonnaies.
    - CryptoCompare : Données sur les prix, les volumes, et les indicateurs techniques pour différentes cryptomonnaies.
    - Google Trends : Données sur les tendances de recherche liées au Bitcoin et aux cryptomonnaies.
    - Reddit API : Données des discussions et des sentiments des utilisateurs sur les forums liés au Bitcoin.

- Idées de problématiques :
    - Impact des nouvelles sur les prix du Bitcoin : Analyser comment les nouvelles positives ou négatives influencent les fluctuations du marché.
    - Sentiment Analysis : Utiliser des techniques de NLP pour analyser le sentiment des articles et des discussions en ligne et corréler cela avec les mouvements de prix.
    - Prédiction des prix : Développer des modèles de prédiction des prix du Bitcoin en utilisant des données historiques et des indicateurs techniques.
    - Détection d'anomalies : Identifier des anomalies dans les données de marché qui pourraient indiquer des opportunités de trading ou des risques.

- Angles d’analyse inédits :
    - Analyse des réseaux sociaux : Étudier l'impact des discussions sur les réseaux sociaux (Twitter, Reddit) sur les prix du Bitcoin.
    - Analyse des tendances de recherche : Utiliser les données de Google Trends pour comprendre l'intérêt du public pour le Bitcoin et corréler cela avec les mouvements de prix.
    - Analyse des corrélations inter-cryptomonnaies : Étudier comment les mouvements de prix d'autres cryptomonnaies influencent le Bitcoin.
    - Analyse des cycles de marché : Identifier des cycles récurrents dans les données de marché et utiliser ces insights pour améliorer les stratégies de trading.
En combinant ces différentes sources de données et en explorant ces angles d'analyse, nous pouvons obtenir une compréhension plus complète et nuancée des facteurs influençant le marché du Bitcoin.

### Analyse critique : L’outil a-t-il proposé des idées pertinentes ou redondantes ?

Nous répondrons partie par partie

- Exploration des sources de données ouvertes, génération d'idées de problématiques ou identification des angles d’analyse inédits

    Les sources de données proposées sont bonne, il n'a pas pris en compte les idées que j'avais déjà proposées.
    Les providers de données marchés auraient pu être utilisé
    Les providers de données sur les tendances et sentiments sont plutôt bonnes, elles ne répondent pas aux motivations de web scrapping. De plus, les données de Reddit API ne permettent pas d'avoir des discussions datées, nous pourrions récuperer la date de chacuns des posts mais rien ne nous assure une continuité dans le temps. Nous explorerons cette possibilité si il reste du temps. (As t'on eu le temps ? Non)

- Idées de problématiques :

    Très générique, pas d'idées novatrices. Ceci dit, cela permet d'avoir une ébauche de problématique.

- Angles d’analyse inédits :

    Il n'y a rien d'inédits dans les propositions de l'IA. Cela s'explique par son fonctionnement.

### Faites le choix définitif du jeu de données. Expliquez ce choix.

On décide finalement d'utiliser les données Binance sur le prix du bitcoin par rapport au dollars. Nous utiliserons les données de [Binance news](https://news.binance.com) jour par jour grâce à [WaybackMachine](https://web.archive.org/). Pour les données manquantes, nous utiliserons un KNN pour prédire le cluster de la date indiquée. Enfin on pourra utiliser les techniques de prédictions connues pour les données marchées ou faire un pipline classique d'entrainement et de test du modèle.
# Page suivante/Précedente
[MAIN](../README.md)/[DATA PROCESSING](DATA_PROC.md)
