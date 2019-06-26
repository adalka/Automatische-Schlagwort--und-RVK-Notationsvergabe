$ spyder
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 21:40 2019
@author: A. Karsten
"""

# # Schritt 1 
# - Ermitteln des umzusystematisierenden Bestands mit SQL-Befehl, Ausgabe: csv-Datei  
# - sortiert nach Spalten (Signaturen, Mediennummern, Kurztitel, Autor, Reihentitel, ISBN, neue Notation, neue Schlagwörter, neue Gesamtsignatur)  
# - Signaturen numerisch aufsteigend sortieren mit zuvor geschriebenem Makro (statt P1, P10, P100 > P1, P2, P3 ...)  

# In[51]:


import urllib.request
import pandas as pd


# In[83]:


url = "https://raw.githubusercontent.com/adalka/Malis18_T9.2_Automatisierte_Schlagwort_RVK-Notationsvergabe/master/2019-05-27_P1000_sortiert_mit_ISBN_Exnr_als_Text.csv?token=AL2CQ2UFKFNHCJUZXEH623S5CPDNG"
apc_file = "2019-05-27_P1000_sortiert_mit_ISBN_Exnr_als_Text.csv"


# In[84]:


urllib.request.urlretrieve(url, apc_file)


# In[37]:


# csv-Datei wird Zeile für Zeile ausgegeben
for line in open(apc_file):
    print(line)


# In[85]:


# apcs = neue Variable, pd= Pandas, read=zeigt an; nur Dateiname muss angegeben werden; Data-Frames werden generiert
apcs = pd.read_csv(apc_file)


# In[35]:


# print = zeigt allesan
print(apcs)


# In[86]:


apcs


# In[87]:


# Spalten sollen angezeigt werden
apcs.columns


# In[41]:


# nur ISBN sollen gezeigt werden
apcs.ISBN


# In[88]:


import csv
with open('2019-05-27_P1000_sortiert_mit_ISBN_Exnr_als_Text.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/gbv.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)


# # Schritt 2: Werte aus URL in JSON beziehen
# - RVK-Notationen können importiert werden, z.B. =ImportJSON("http://data.bib.uni-mannheim.de/malibu/isbn/swb.php?isbn="ISBN"&format=json"; "/rvk"; "noHeaders")  
# - Befehl ausführen: JSON-basierte Antwortdaten (s. https://2.python-requests.org//de/latest/user/quickstart.html)  

# In[89]:


import requests
r = requests.get('http://data.bib.uni-mannheim.de/malibu/isbn/gbv.php?isbn=3-85460-115-8&format=json')
r.json()


# In[90]:


# RVK-Notationen auslesen
import requests


# In[91]:


r = requests.get('http://data.bib.uni-mannheim.de/malibu/isbn/gbv.php?isbn=3-85460-115-8&format=json')


# In[92]:


r.text


# In[ ]:




