# Automatisierte Schlagwort- und RVK-Notationsvergabe 

### Projekt: Umsystematisierung der Bibliotheksbestände der LWL-Archäologie für Westfalen
Seit Längerem besteht der Wunsch, die Bestände der archäologischen Spezialbibliothek systematisch aufzustellen. 
Man entschied sich für die [Regensburger Verbundklassifikation](https://rvk.uni-regensburg.de/regensburger-verbundklassifikation-online) (RVK) als Ordnungssystem. Da die Bibliothek nicht Mitglied in einem Verbund ist und über die vorhandene Bibliothekssoftware keine automatische Übernahme von Fremddaten, d.h. Schlagwörter und RVK-Notationen, möglich ist, muss dies auf einem alternativen Weg vonstattengehen. 

### Einführung
In diesem Projekt soll versucht werden, die Schlagwort- und Notationsvergabe der RVK (Regensburger Verbundklassifikation) automatisch in einer Excel-Liste erfolgen zu lassen. Grundlage für die automatische Vergabe ist u.a. eine csv-/Excel-Datei und ein webbasiertes Tool namens [Malibu](http://data.bib.uni-mannheim.de/malibu/isbn/suche.html).

### Möglicher Projektablauf
Aus diesem Tool werden die in den großen deutschsprachigen Bibliotheksverbünden generierten Schlagwörter und RVK-Notationen mit den ISBN bzw. PPN des Bibliotheksbestands der LWL-Archäologie vorhandenen Titel abgeglichen und im Anschluss in eine Excel-Liste gespeist:
* Zunächst werden alle in der Bibliothek umzusystematisierenden Werke über einen SQL-Befehl in einer csv-Datei erfasst. Diese wurde nach Spalten (Signaturen, Mediennummern, Kurztitel, Autor, Reihentitel, ISBN, neue Notation, neue Schlagwörter, neue Gesamtsignatur) und nach Signaturen aufsteigend sortiert.
* Schließlich kommt ein Skript zum Einsatz, das die ISBN bzw. PPN aus der entsprechenden Zeile in das Malibu-Tool setzt.
* Danach werden die in den Verbünden vergebenen RVK-Notationen in die Spalte "neue Notation" gesetzt, die Schlagwörter in die Spalte "neue Schlagwörter". 
* Mit einer For Loop soll dann in Python/Jupyter die Anfrage für alle 30.000 Monographien der Bibliothek durchgeführt werden.
* Zur weiteren kollaborativen Bearbeitung wird eine Excel-Datei erstellt. Nicht zuletzt wegen der besseren Ansicht für die Bearbeiter_innen.

### Ziel
Die Vergabe von Schlagwörtern und Notationen soll somit automatisiert werden, um die Umsystematisierung der beteiligten Mitarbeiterinnen und Mitarbeiter zu erleichtern. RVK-Notationen und Schlagwörter könnten somit zunächst maschinell und ggfls. intellektuell erfasst werden.
