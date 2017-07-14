# Feuille technique pour le hackathon

OpenReg s’engage résoudre un des plus grands problèmes de notre génération : le surdose d’information. Notre but est de rendre les chercheurs meilleurs à ce qu’ils font : trouvé l’information qui a de l’impact. Notre mandat est de trouver le meilleur moyen de regrouper les articles trop similaires ensemble. 

Nous allons vous offrir une plage de données et proposer quelques méthodes différents, mais ultimement nous vous laissons libre de  déterminer quel est le meilleur moyen de regrouper les articles ensemble. Ce mandat vous offrira également la chance de gagner de l’expérience avec le Traitement automatique du langage naturel (NLP). 

## Le jeu de données
Le jeu de données est dans ce repo. Le jeu a 3 colonnes: `URL`, `TITLE`, `TEXT`.
Nettoyer et segmenter le jeu de données avant d'appliquer les algorithmes de regroupement (clustering). Les visualisations sont les bienvenues. Le regroupement des articles peut être basé sur les titres ou les textes, mais les regroupements basés sur les urls ne sont pas ce que nous cherchons. 

## Quelques resources
Quelques outils utiles: [Jupyter Notebook](http://jupyter.org/install.html), [Scikit-Learn](http://scikit-learn.org/stable/modules/clustering.html), [Matplotlib](https://matplotlib.org/), [NLTK](http://www.nltk.org/) ect... 
Utilisez ce que vous voulez pour votre développement de science des données et de traitement automatique du language naturel.

## Plus de resources
Voici un exemple de regroupment d’articles sur le web: www.yippy.com 

Voici des liens avec des suggestion de méthodologie à utiliser: http://brandonrose.org/clustering

https://stackoverflow.com/questions/1789254/clustering-text-in-python

https://pdfs.semanticscholar.org/88c2/5e2481ba49cbac75575485cba1759fa4ebcc.pdf 

http://www.site.uottawa.ca/~diana/csi5180/TextClustering.pdf

https://www.slideshare.net/kanimozhiu/text-clustering 

Voici des API de regroupment d’articles: 

http://www.yippyinc.com/yippy-searchappliance 

https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster.html
