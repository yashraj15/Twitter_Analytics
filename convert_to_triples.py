import re
import stanza
import csv
import os
import pandas as pd

import execnet
#import spacy
#from spacy import displacy



from openie import StanfordOpenIE



art1 = pd.read_csv("D:\\Sem 3\\OSNA\\Project 2\\dEFEND data\\politifact_content_no_ignore.tsv",sep = '\t')
art1head = art1.head()

art2 = pd.read_csv("D:\\Sem 3\\OSNA\\Project 2\\dEFEND data\\gossipcop_content_no_ignore.tsv",sep = '\t')
art2head = art2.head()

    

with StanfordOpenIE() as client:

    for i in art1["content"]:
        
        triple1 = pd.DataFrame(client.annotate(i))
	
    triple1.to_csv("D:\\Sem 3\\OSNA\\p2new\\triples2.csv", index = False)
        

        
    for i in art2["content"]:
        
        triple2 = pd.DataFrame(client.annotate(i))
    triple2.to_csv("D:\\Sem 3\\OSNA\\Project 2\\triples.csv", index = False)
