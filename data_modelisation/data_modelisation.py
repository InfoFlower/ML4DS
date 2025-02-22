#Fonctions faites pour MLOPS à la base

from datetime import datetime 
import logging
import pandas as pd
import mlflow as mf
from sklearn.model_selection import train_test_split
logging.getLogger('matplotlib').setLevel(logging.WARNING)
logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s', level=logging.WARNING)
from mlflow.models import infer_signature
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

mf.set_tracking_uri("file:../mlruns")
logging.info(f'Mlflow tracking uri : {mf.get_tracking_uri()}')

def log_model_version(model,model_name,signature,data,scores,hyperparam_value,exprience_name,version):
    """
    procedure permettant de log le model dans ml flow
    parameters:
        model : model sklearn à enregistrer
        model_name : Nom du model
        signature : Signature du model (mlflow.infersignature)
        data : Dataframe
        scores (dict): Scores (dictionnaire)
        hyperparam_value (dict): hyperparametres du model 
        exprience_name : Nom de l'experience à incrémenter 
        version : Version du model
    """
    now = datetime.now()
    mf.set_experiment(experiment_name=exprience_name)
    data.to_csv('data/temp/train_data.csv')
    data_file_path='data/temp/train_data.csv'
    logging.info(f'Data user for training located in {data_file_path}')
    mf.log_param("version", version)
    run_name=f'{version}_{model_name}_{now.strftime("%Y_%m_%d")}'
    mf.end_run()
    with mf.start_run(run_name=run_name) as run:
        mf.sklearn.log_model(model,model_name,signature= signature)
        if scores is not None:
            for metric_name, metric_value in scores.items():
                mf.log_metric(metric_name, metric_value)
        for param_name, param_value in hyperparam_value.items():
            mf.log_param(param_name, param_value)
        logging.info(f"Model logged with run_id: {run.info.run_id}")


class model_maker_tester:
    def __init__(self,cat_cols,fit_cols,y_col):
        """
        Initializes the model_maker_tester class with categorical columns, fit columns, and target column.

        Args:
            cat_cols (list): List of categorical columns.
            fit_cols (list): List of columns to fit the model.
            y_col (str): Name of the target column.
        """
        self.cat_cols=cat_cols
        self.fit_cols=fit_cols
        self.y_col=y_col

    def score(self,model, X_test, y_test):
        """
        Calcul les métriques de qualité des modeles de régression
        R², RMSE, MAE, accuracy
        parameters :
            model : Model à scorer
            X_test : Dataframe des variables explicatives
            y_test : Array des prédictions attendues
        
        return :
            dico_metrics : dictionnaire des metrics
        """
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred) 
        score = model.score(X_test,y_test)
        dico_metrics={"R2":r2, "RMSE":float(rmse), "MAE": mae, "Precision": score}
        return dico_metrics

    def make_dummies_X_y(self,data,flg_train_test,test_size=0.33,rnd_state=42):
        if self.cat_cols is not None : Xy=pd.get_dummies(data,columns=self.cat_cols,drop_first=False)
        else : Xy=data
        logging.debug(f'Jeu de donnee : {Xy}')
        X=Xy[self.fit_cols]
        y=data[self.y_col]
        logging.info('CREATION TRAIN TEST DATASETS')
        if flg_train_test : ret=train_test_split(X,y,test_size=test_size,random_state=rnd_state)
        else : ret = X,y
        return ret
    
    def __call__(self,model,model_name,data,version,param_grid,experience_name='Velib',flg_first=False,flg_train_test=False):
        """
        Fonction permettant l'entrainement, la prédiction et le score d'un modèle

        params :
            model : Modele SKlearn d'entrée
            model_name : Nom donné au model
            data : Dataframe pandas pour l'entrainement, le score ou la prédiction du modèle
            version : Version du modèle
            param_grid : Grille de paramêtre pour l'entrainement par grid_search
            experience_name : Nom de l'experience MLflow à implémenter
            flg_to_score : Flag si la fonction ne doit que scorer le modèle
            flg_first : Flag si la fonction doit fit le modèle avec les données
        
        Returns:
            Model (pkl): Model utilisé ou entrainé
        """
        logging.debug(f'DATA : {data}')
        X,y=self.make_dummies_X_y(data,flg_train_test=False)
        logging.debug(f'Data to fit or predict : {X,y}')
        if flg_first:
            logging.info('FITTING DATA')
            grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy',n_jobs=-1)
            grid_search.fit(X, y)
            model = grid_search
            signature=infer_signature(X,model.predict(X))
            log_model_version(model.best_estimator_,model_name,signature,data,scores=None,hyperparam_value=model.get_params(),exprience_name=experience_name,version=version)
        else:
            score=self.score(model,X,y)
            signature=infer_signature(X,model.predict(X))
            log_model_version(model,model_name,signature,data,score,model.get_params(),experience_name,version)
            return model, score
        return model