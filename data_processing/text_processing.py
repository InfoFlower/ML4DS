#Fonction faite en analyse textuelle
import treetaggerwrapper
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import pandas as pd

def proc_make_csv():
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tagger=treetaggerwrapper.TreeTagger(TAGLANG="en", TAGDIR='TreeTagger', TAGPARFILE='english.par')
    directory = r'data\html'
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for i in range(len(files)):
        f=open('data/html/'+files[i],"r")   
        textebrut = f.read()
        textebrut=textebrut.lower()
        files[i] = re.sub(r"[.’%:'«»;,?=@€!\n*]+\d*()"""," ",textebrut) # remplacement de la ponctuation par des blancs, dont les retours à la ligne (\n)
    nt = len(files)
    texte_nosw = [mot for mot in files[0].split() if mot.lower() not in stop_words]
    textes_tags = tagger.tag_text(texte_nosw)
    textevv=[]
    for i in files:
        texte_nosw = [mot for mot in i.split() if mot.lower() not in stop_words]
        textes_tags = tagger.tag_text(texte_nosw)
        #'KON' not in mot.split("\t")[1] and 'ADV' not in mot.split("\t")[1] 
        texte_lem = [mot.split("\t")[2] for mot in textes_tags if mot.split("\t")[2] != '@card@' and 'PRO' not in mot.split("\t")[1] and mot.split("\t")[2]!='avoir']
        texte_filtré = ' '.join(texte_lem)
        textevv.append(texte_filtré)
    motot={} 
    for txt in range(len(textevv)):
        for m in textevv[txt].split(' '):
            if m not in motot: motot[m]=[0]*nt
            motot[m][txt]+=1
    motex = {}
    for mot in motot:
        motex[mot] = [0]*nt   # chaque mot du dictionnaire est associé à une liste d'effectifs plutôt qu'à un effectif simple (en vue de la construction de la table lexicale)
    for i in range(nt):   
    	for mot in textevv[i].split():
    		if mot in motex.keys():
                   motex[mot][i] += 1   # chaque mot est associé à son effectif dans chaque texte
    motexx={}
    compte=0
    for i in motex:
        if re.match(r'\b[a-zA-Z]+\b',i) and len(i)>2:
            motexx[i]=motex[i]
        else:
            compte+=1
    return pd.DataFrame(motexx,index=[i[:-4] for i in os.listdir('data/html')])