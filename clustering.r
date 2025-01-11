#Code de preparations des données
library(explor)
library(FactoMineR)
library(FactoInvestigate)
library(ggplot2)
library(factoextra)
#library(Factoshiny)
library(dplyr)


set.seed(1)
###############################################################################################
#                                               Partie2
###############################################################################################

#data
data_mots=read.csv('C:/Users/lenovo/Desktop/Cours/35_ML4DS/data/word_count.csv',sep=',',row.names=1)

df_afc <- data_mots %>% mutate_all(as.numeric)
#Dataframe des variables réseaux et mobiles
df_afc=t(df_afc)
afc= CA(df_afc,
                     ncp = 4, graph=FALSE) #nombre d'axes à retenir
explor(afc)
#Classification hiérarchique 
HCPC=HCPC(afc, nb.clust=5,graph = FALSE)
fviz_cluster(HCPC,axis=c(1,2), geom = "point", main = "Clusters des non-clients",show.clust.cent=TRUE)
write.csv(HCPC_noncli$data.clust,'data/cluster_noncli_all.csv',row.names=FALSE)