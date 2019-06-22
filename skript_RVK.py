$ spyder
import urllib.request
import pandas as pd

# Festlegen der URL, aus der bezogen werden soll
url = "https://raw.githubusercontent.com/adalka/Malis18_T9.2_Automatisierte_Schlagwort_RVK-Notationsvergabe/master/2019-05-27_P1000_sortiert_mit_ISBN_Exnr_als_Text.csv?token=AL2CQ2U54CB47YPFZWB7RR25A5EFS"
apc_file = "2019-05-27_P1000_sortiert_mit_ISBN_Exnr_als_Text.csv"

urllib.request.url
retrieve(url, apc_file)

('2019-05-27_P1000_sortiert_mit_ISBN_Exnr_als_Text.csv',
 <http.client.HTTPMessage at 0x23ba1595c50>)

apcs = pd.read_csv(apc_file)
apcs

# Anwenden des csv.reader (https://docs.python.org/3/library/csv.html#csv.DictReader)
import csv
import csv
with open('2019-05-27_P1000_sortiert_mit_ISBN_Exnr_als_Text.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# Tool zur Übernahme der RVK-Notationen liegt als json-file vor
# Nächster Schritt: Testen, ob ISBN aus csv das gewünschte Ergebnis liefert (https://2.python-requests.org//de/latest/user/quickstart.html)
import requests
r = requests.get('http://data.bib.uni-mannheim.de/malibu/isbn/gbv.php?isbn=3-85460-115-8&format=json')
r.json()

## Nächster Schritt: RVK auslesen und mit ISBN verknüpfen

    


