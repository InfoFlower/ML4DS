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
length(rownames(data_mots))
#Dataframe des variables réseaux et mobiles
afc= CA(data_mots,ncp = 4, graph=FALSE) #nombre d'axes à retenir
#Classification hiérarchique 
HCPC=HCPC(afc, nb.clust=3,graph = FALSE)
fviz_cluster(HCPC,axis=c(1,2), geom = "point", main = "Clusters des non-clients",show.clust.cent=TRUE)
write.csv(HCPC$data.clust,'data/temp/cluster_web.csv')
View(HCPC$data.clust)
