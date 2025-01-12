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
data_mots=read.csv('data/temp/word_count.csv',sep=',',row.names=1)
length(rownames(data_mots))
data_mots=t(data_mots)
data_mots=data_mots
length(rownames(data_mots))
View(data_mots)
#Dataframe des variables réseaux et mobiles
AFC= CA(data_mots, graph=FALSE) #nombre d'axes à retenir
#Classification hiérarchique 
HCPC=HCPC(afc, nb.clust=3,graph = FALSE)
fviz_cluster(HCPC,axis=c(1,3), geom = "point", main = "Clusters des non-clients",show.clust.cent=TRUE)
write.csv(HCPC$data.clust,'data/temp/cluster_web.csv')
View(HCPC$data.clust)
explor(afc)
