# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:19:43 2019

@author: AK
"""

# # Automatisierte Schlagwort- und RVK-Notationsvergabe
# ## Hintergrund-Informationen
# Seit Längerem besteht der Wunsch, die Bestände einer archäologischen Spezialbibliothek systematisch aufzustellen. Man entschied sich für die [Regensburger Verbundklassifikation (RVK)](https://rvk.uni-regensburg.de/regensburger-verbundklassifikation-online) als Ordnungssystem. Da die Bibliothek nicht Mitglied in einem Verbund ist und über die vorhandene Bibliothekssoftware keine automatische Übernahme von Fremddaten, d.h. Schlagwörter und RVK-Notationen, möglich ist, muss dies auf einem alternativen Weg vonstattengehen.
# Hierfür wurde das folgende Skript erstellt, das auch anderen zur RVK umsystematisierenden Bibliotheken dabei helfen soll, Vorgänge mithilfe IT-basierter Möglichkeiten zu optimieren, um personelle und finanzielle Ressourcen zu sparen.
# 
# ## Projekt-Beschreibung
# In diesem Projekt wird die Schlagwort- und Notationsvergabe der RVK (Regensburger Verbundklassifikation) automatisch in einer Excel-Liste erfolgen. Grundlage für die automatische Vergabe ist u.a. eine csv-/Excel-Datei und ein webbasiertes Tool namens [Malibu](https://github.com/UB-Mannheim/malibu). Dieses ist auch im JSON-Format vorhanden.
# 
# ## Skript-Beschreibung
# Bei diesem Skript handelt es sich um einen Prototyp, der um beliebige Anfragen erweitert bzw. reduziert werden kann.
# Aus dem Malibu-Tool bzw. mittels [JSON-basierter Antwortdaten](https://2.python-requests.org//de/latest/user/quickstart.html) werden die in den großen deutschsprachigen Bibliotheksverbünden generierten Schlagwörter und RVK-Notationen mit den ISBN bzw. PPN des Bibliotheksbestands der LWL-Archäologie vorhandenen Titel abgeglichen und final in eine Excel-Liste gespeist:
# 
# * Zunächst werden alle in der Bibliothek umzusystematisierenden Werke über einen SQL-Befehl in einer csv-Datei erfasst.
# * Diese wurde nach Spalten, z. B. Signaturen, Mediennummern, Kurztitel, Autor, Reihentitel, ISBN, neue Notation, neue Schlagwörter, neue Gesamtsignatur, und nach Signaturen aufsteigend sortiert.
# * Schließlich kommt das hier gezeigte Skript zum Einsatz, das die [ISBN](https://de.wikipedia.org/wiki/Internationale_Standardbuchnummer) bzw. später auch [PPN](https://de.wikipedia.org/wiki/OCLC_PICA#Geschichte) aus der entsprechenden Zeile in das Malibu-Tool im JSON-Format setzt.
# * Danach werden die in den Verbünden vergebenen RVK-Notationen in die Spalte "neue Notation" gesetzt, die Schlagwörter in die Spalte "neue Schlagwörter"
# * Es sollen alle Verbünde einzeln betrachtet werden können, weshalb diese hier auch einzeln dargestellt werden. Nicht für jede Bibliothek sind alle Verbünde gleichermaßen relevant.
# * Mit einer For Loop wird die Anfrage für alle 30.000 Monographien der Bibliothek durchgeführt werden.
# * Zur weiteren kollaborativen Bearbeitung (mit MS Office 365) wird eine csv- und dann eine Excel-Datei erstellt. Nicht zuletzt wegen der besseren Ansicht für die Bearbeiter_innen.
# 
# ## Ziel
# Die Vergabe von Schlagwörtern und Notationen soll somit automatisiert werden, um die Umsystematisierung der beteiligten Mitarbeiterinnen und Mitarbeiter zu erleichtern. RVK-Notationen und Schlagwörter könnten somit zunächst maschinell und ggfls. intellektuell erfasst werden.  

# # Skript:
# # Schritt 1
# * Vorarbeit: Ermitteln des umzusystematisierenden Bestands mit SQL-Befehl, Ausgabe: als csv-Datei  
# * sortiert nach Spalten (Signaturen, Mediennummern, Kurztitel, Autor, Reihentitel, ISBN, neue Notation, neue Schlagwörter, neue Gesamtsignatur)  
# * Signaturen numerisch aufsteigend sortieren, z. B. in diesem Fall mit zuvor geschriebenem Excel-Makro (statt P1, P10, P100 > P1, P2, P3 ...)
# * csv-Datei wird auf minimale Informationen reduziert  
# * im Folgenden wird das Skript als Prototyp für eine Liste von 15 ISBN/Titeln getestet:

# In[1]:
# pandas wird als „pd“ abgekürzt
import urllib.request
import pandas as pd

# In[2]:
# url stammt aus github, darin befindet sich eine Liste aus 15 Titeln mit und ohne ISBN, die probehalber getestet werden
# so wird der Ordner benannt, der dann auch hier sichtbar wird
url = "https://raw.githubusercontent.com/adalka/Malis18_T9.2_Automatisierte_Schlagwort_RVK-Notationsvergabe/master/2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv"
apc_file = "2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv"

# In[3]:
# Befehl: Datei runterladen 
urllib.request.urlretrieve(url, apc_file)

# In[4]:
# csv-Datei, links Exemplarnummer aus dem Bibliothekskatalog (so wird das Werk eindeutig zuweisbar) und rechts dazugehörige ISBN, wird Zeile für Zeile ausgegeben
for line in open(apc_file):
    print(line)

# In[5]:
# apcs = neue Variable, pd= Pandas, read=zeigt an; nur Dateiname muss angegeben werden; Data-Frames werden generiert
apcs = pd.read_csv(apc_file)

# In[6]:
# print = zeigt alles an
print(apcs)
apcs.head()

# In[7]:
apcs
apcs.head()

# In[8]:
# Spalten sollen angezeigt werden
apcs.columns
apcs.head()

# In[9]:
# nur ISBN sollen gezeigt werden
apcs.ISBN
apcs.head()

# In[10]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/gbv.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # SWB
# (Südwestdeutscher Bibliotheksverbund)  
# Nun auch für den SWB (Südwestdeutscher Bibliotheksverbund Baden-Württemberg, Saarland, Sachsen) durchführen mithilfe von http://data.bib.uni-mannheim.de/malibu/isbn/swb.php?isbn= &format=json:

# In[11]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/swb.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # B3Kat
# (gemeinsame Katalogisierungsplattform der Bibliotheksverbünde BVB und KOBV)  
# Nun auch für den B3Kat durchführen mithilfe von http://data.bib.uni-mannheim.de/malibu/isbn/b3kat.php?isbn= &format=json:

# In[12]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/b3kat.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # HeBIS
# (Hessisches BibliotheksInformationsSystem)  
# Nun auch für den HeBIS durchführen mithilfe von http://data.bib.uni-mannheim.de/malibu/isbn/hebis.php?isbn= &format=json:

# In[13]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/hebis.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # HBZ 
# (Hochschulbibliothekszentrum NRW)  
# Nun auch für das hbz durchführen mithilfe von http://data.bib.uni-mannheim.de/malibu/isbn/hbz.php?isbn= &format=json:

# In[14]:
import csv
with open('2019-07-09_P1000_sortiert_mit_ISBN_Exnr.csv', newline='') as f:    
    reader = csv.reader(f)
    for row in reader:
        url = "http://data.bib.uni-mannheim.de/malibu/isbn/hbz.php?isbn=" + str(row[1]) + "&format=json"  
        print(url)

# # Schritt 2: Werte aus URL in JSON beziehen
# - RVK-Notationen können importiert werden  
#     z.B. über =ImportJSON("http://data.bib.uni-mannheim.de/malibu/isbn/swb.php?isbn="ISBN"&format=json"; "/rvk"; "noHeaders")    
# - Befehl ausführen: JSON-basierte Antwortdaten (s. https://2.python-requests.org//de/latest/user/quickstart.html)  

# In[15]:
# http-Anforderung senden, um request-Modul zu importieren
# r = response, wir bekommen ein object response im JSON-Format (s. https://2.python-requests.org//de/latest/user/quickstart.html)
# dies wird nun mit der ersten in der Liste stehenden ISBN beispielhaft getestet:

import requests
r = requests.get('http://data.bib.uni-mannheim.de/malibu/isbn/hbz.php?isbn=3-85460-115-8&format=json')
r.json()

# In[16]:
# Das vorige Ergebnis zeigt alle Exemplar-relevanten Informationen. 
# Unter "rvk" verbirgt sich die RVK-Notation, die in dem ausgewählten Verbund (in diesem Fall HBZ) vergeben wurde. 
# Unter "sw" befinden sich Schlagwörter.
# Wie lautet die RVK-Notation für einen bestimmten String? (s. https://www.w3schools.com/python/python_json.asp)
# Bilden von Variablen (x= RVK+Notation, y= Notation)

import json
x = '{ "rvk":"NF 3270"}'
y = json.loads(x)
print(y["rvk"])

# In[17]:
# Weiter oben wurde die ISBN testweise händisch eingegeben.  
# So sieht der Befehl mit einem string aus (vgl. https://automatetheboringstuff.com/chapter6/):
url = "http://data.bib.uni-mannheim.de/malibu/isbn/gbv.php?isbn=" 
isbn = str(row[1])
end = "&format=json"

# In[18]:
print("{}/{}/{}".format(url, isbn, end))

# In[19]:
f"{url}/{isbn}/{end}"

# # Schritt 3:
# Alle RVK-Notationen für alle ISBN in allen Verbünden in eine csv-Datei exportieren und nicht benötigte Werte ignorieren.  
#     

# In[20]:
import json 
import pandas

# In[21]:
data= [{"id": "", "isbn": "", "dnbNr": "", "oclcNr": "", "titel": "", "untertitel": "", "autor": "", "gesamttitel": "",     "hochschulvermerk": "",
    "auflage": "", "erscheinungsinfo": "", "umfang": "", "links": "", "bestand": "", "rvk": "", "ddc": "", "sw": [], "produktSigel": "",
    "einzelaufnahmen": ""}]

# In[22]:

pandas.read_json(json.dumps(data)).to_csv('pandas.csv')

# In[23]:
with open('pandas.csv') as f:
    print(f.read())

# # Schritt 4:
# Dies für alle JSON-Strings (mit allen ISBN und den jeweils vergebenen RVK-Notationen für alle Verbünde) durchführen.
# Mögliches Vorgehen:  
# * Wie ist eine RVK-Notation aufgebaut? Wie viele Zeichen hat eine RVK-Notation? 
# * Sie setzt sich aus 1) aus 2 Buchstaben zusammen; 2) einem Leerzeichen; 3) es folgen zwischen 3 und 5 Ziffern
# * Hierfür könnte mit einem regulären Ausdruck gearbeitet werden:  
# * 1) 2 Buchstaben zwisch a bis z [a-z], 2) Leerzeichen wie Tab, Space, ... \s und 3) 3 bis 5 Zahlen von 0-9: \d, [0-9]
# * Die Zahl, die an letzter Stelle steht, ist mindestens 3-stellig und höchstens 5-stellig: {m, n} Der Ausdruck kommt mindestens m-mal, höchstens n-mal vor; z. B. \w{3, 5} (vgl. https://docs.python.org/2/library/re.html)

# In[24]:
# regulären Ausdruck importieren
import re

# In[25]:
# an dieser Stelle endet der Prototyp vorerst, wird jedoch weitergepflegt
