#!/usr/bin/env python
# coding: utf-8

# # Automatisierte Schlagwort- und RVK-Notationsvergabe
# ## Projekt: Umsystematisierung der Bibliotheksbestände einer archäologischen Spezialbibliothek
# Seit Längerem besteht der Wunsch, die Bestände der archäologischen Spezialbibliothek systematisch aufzustellen. Man entschied sich für die Regensburger Verbundklassifikation (RVK) als Ordnungssystem. Da die Bibliothek nicht Mitglied in einem Verbund ist und über die vorhandene Bibliothekssoftware keine automatische Übernahme von Fremddaten, d.h. Schlagwörter und RVK-Notationen, möglich ist, muss dies auf einem alternativen Weg vonstattengehen.
# 
# ## Einführung
# In diesem Projekt soll versucht werden, die Schlagwort- und Notationsvergabe der RVK (Regensburger Verbundklassifikation) automatisch in einer Excel-Liste erfolgen zu lassen. Grundlage für die automatische Vergabe ist u.a. eine csv-/Excel-Datei und ein webbasiertes Tool namens Malibu. Dieses ist auch im JSON-Format vorhanden.
# 
# ## Möglicher Projektablauf
# Aus diesem Tool bzw. mittels JSON-basierter Antwortdaten[^1] werden die in den großen deutschsprachigen Bibliotheksverbünden generierten Schlagwörter und RVK-Notationen mit den ISBN bzw. PPN des Bibliotheksbestands der LWL-Archäologie vorhandenen Titel abgeglichen und im Anschluss in eine Excel-Liste gespeist:
# 
# * Zunächst werden alle in der Bibliothek umzusystematisierenden Werke über einen SQL-Befehl in einer csv-Datei erfasst. Diese wurde nach Spalten (Signaturen, Mediennummern, Kurztitel, Autor, Reihentitel, ISBN, neue Notation, neue Schlagwörter, neue Gesamtsignatur) und nach Signaturen aufsteigend sortiert.
# * Schließlich kommt das hier gezeigte Skript zum Einsatz, das die ISBN bzw. später auch PPN aus der entsprechenden Zeile in das Malibu-Tool im JSON-Format setzt.
# * Danach werden die in den Verbünden vergebenen RVK-Notationen in die Spalte "neue Notation" gesetzt, die Schlagwörter in die Spalte "neue Schlagwörter". Es sollen alle Verbünde einzeln betrachtet werden können, weshalb diese hier auch einzeln dargestellt werden.
# * Mit einer For Loop soll dann die Anfrage für alle 30.000 Monographien der Bibliothek durchgeführt werden.
# * Zur weiteren kollaborativen Bearbeitung (mit MS Office 365) wird eine csv- und dann eine Excel-Datei erstellt. Nicht zuletzt wegen der besseren Ansicht für die Bearbeiter_innen.
# 
# ## Ziel
# Die Vergabe von Schlagwörtern und Notationen soll somit automatisiert werden, um die Umsystematisierung der beteiligten Mitarbeiterinnen und Mitarbeiter zu erleichtern. RVK-Notationen und Schlagwörter könnten somit zunächst maschinell und ggfls. intellektuell erfasst werden.
# 
# Quellen
# [^1]: Python Requests: Schnellstart. URL: https://2.python-requests.org//de/latest/user/quickstart.html [letzter Zugriff: 09.07.2019]

# # Schritt 1
# * Vorarbeit: Ermitteln des umzusystematisierenden Bestands mit SQL-Befehl, Ausgabe: csv-Datei  
# * sortiert nach Spalten (Signaturen, Mediennummern, Kurztitel, Autor, Reihentitel, ISBN, neue Notation, neue Schlagwörter, neue Gesamtsignatur)  
# * Signaturen numerisch aufsteigend sortieren mit zuvor geschriebenem Excel-Makro (statt P1, P10, P100 > P1, P2, P3 ...)
# * csv-Datei wird auf minimale Informationen reduziert  
# * im Folgenden wird das Skript für eine Liste von 15 ISBN/Titeln getestet.  

# In[5]:
# pandas wird als „pd“ abgekürzt
import urllib.request
import pandas as pd

# In[6]:
# url stammt aus github (hier entsteht eine Fehlermeldung, wenn die url nicht frisch generiert wird, da das Repositorium privat ist!)
# so wird der Ordner benannt, der dann auch hier sichtbar wird
url = "https://raw.githubusercontent.com/adalka/Malis18_T9.2_Automatisierte_Schlagwort_RVK-Notationsvergabe/master/2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv"
apc_file = "2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv"

# In[7]:
# Befehl: Datei runterladen 
urllib.request.urlretrieve(url, apc_file)

# In[8]:
# csv-Datei wird Zeile für Zeile ausgegeben
for line in open(apc_file):
    print(line)

# In[9]:
# apcs = neue Variable, pd= Pandas, read=zeigt an; nur Dateiname muss angegeben werden; Data-Frames werden generiert
apcs = pd.read_csv(apc_file)

# In[10]:
# print = zeigt alles an
print(apcs)
apcs.head()

# In[11]:
apcs
apcs.head()

# In[12]:
# Spalten sollen angezeigt werden
apcs.columns
apcs.head()

# In[13]:
# nur ISBN sollen gezeigt werden
apcs.ISBN
apcs.head()

# In[14]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/gbv.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # SWB
# (Südwestdeutscher Bibliotheksverbund)  
# Nun auch für den SWB (Südwestdeutscher Bibliotheksverbund Baden-Württemberg, Saarland, Sachsen) durchführen mithilfe von http://data.bib.uni-mannheim.de/malibu/isbn/swb.php?isbn= &format=json:

# In[15]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/swb.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # B3Kat
# (gemeinsame Katalogisierungsplattform der Bibliotheksverbünde BVB und KOBV)  
# Nun auch für den B3Kat durchführen mithilfe von http://data.bib.uni-mannheim.de/malibu/isbn/b3kat.php?isbn= &format=json:

# In[16]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/b3kat.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # HeBIS
# (Hessisches BibliotheksInformationsSystem)  
# Nun auch für den HeBIS durchführen mithilfe von http://data.bib.uni-mannheim.de/malibu/isbn/hebis.php?isbn= &format=json:

# In[17]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/hebis.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # HBZ 
# (Hochschulbibliothekszentrum NRW)  
# Nun auch für das hbz durchführen mithilfe von http://data.bib.uni-mannheim.de/malibu/isbn/hbz.php?isbn= &format=json:

# In[18]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/hbz.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # Schritt 2: Werte aus URL in JSON beziehen
# - RVK-Notationen können importiert werden, 
#     z.B. über =ImportJSON("http://data.bib.uni-mannheim.de/malibu/isbn/swb.php?isbn="ISBN"&format=json"; "/rvk"; "noHeaders")  
# - Befehl ausführen: JSON-basierte Antwortdaten (s. https://2.python-requests.org//de/latest/user/quickstart.html)  

# In[51]:
# http-Anforderung senden, um request-Modul zu importieren
# r = response, wir bekommen ein object response im JSON-Format (s. https://2.python-requests.org//de/latest/user/quickstart.html)
# dies wird nun mit der ersten in der Liste stehenden ISBN beispielhaft getestet:

import requests
r = requests.get('http://data.bib.uni-mannheim.de/malibu/isbn/gbv.php?isbn=3-85460-115-8&format=json')
r.text

# In[20]:

# Wie lautet die RVK-Notation für einen bestimmten String? (s. https://www.w3schools.com/python/python_json.asp)
# Bilden von Variablen (x= RVK+Notation, y= Notation)

import json
x = '{ "rvk":"NF 1665"}'
y = json.loads(x)
print(y["rvk"])

# In[35]:

# Weiter oben wurde die ISBN testweise händisch eingegeben. So sieht der Befehl mit einem string aus (vgl. https://automatetheboringstuff.com/chapter6/):
url = "http://data.bib.uni-mannheim.de/malibu/isbn/gbv.php?isbn=" 
isbn = str(row[1])
end = "&format=json"

# In[36]:

print("{}/{}/{}".format(url, isbn, end))

# In[37]:

f"{url}/{isbn}/{end}"

# # Schritt 3:
# Dies für alle JSON-Strings (mit allen ISBN und den jeweils vergebenen RVK-Notationen für alle Verbünde) durchführen.
# Mögliches Vorgehen:  
# * Wie ist eine RVK-Notation aufgebaut? Wie viele Zeichen hat eine RVK-Notation? 
# * Sie setzt sich aus 1) aus 2 Buchstaben zusammen; 2) einem Leerzeichen; 3) es folgen zwischen 3 und 5 Ziffern
# * Hierfür könnte mit einem regulären Ausdruck gearbeitet werden:  
# * 1) 2 Buchstaben zwisch a bis z [a-z], 2) Leerzeichen wie Tab, Space, ... \s und 3) 3 bis 5 Zahlen von 0-9: \d, [0-9]
# * Die Zahl, die an letzter Stelle steht, ist mindestens 3-stellig und höchstens 5-stellig: {m, n} Der Ausdruck kommt mindestens m-mal, höchstens n-mal vor; z. B. \w{3, 5} (vgl. https://docs.python.org/2/library/re.html)

# In[69]:

# regulären Ausdruck importieren
import re

# # Alternative/Schritt 4:
# Alle RVK-Notationen für alle ISBN in allen Verbünden in eine csv-Datei exportieren und nicht benötigte Werte ignorieren.  
#     

# In[76]:

import json 
import pandas

# In[77]:

data= [{"id": "", "isbn": "", "dnbNr": "", "oclcNr": "", "titel": "", "untertitel": "", "autor": "", "gesamttitel": "",     "hochschulvermerk": "",
    "auflage": "", "erscheinungsinfo": "", "umfang": "", "links": "", "bestand": "", "rvk": "", "ddc": "", "sw": [], "produktSigel": "",
    "einzelaufnahmen": ""}]

# In[78]:

pandas.read_json(json.dumps(data)).to_csv('pandas.csv')

# In[66]:

with open('pandas.csv') as f:
    print(f.read())

# In[ ]:


