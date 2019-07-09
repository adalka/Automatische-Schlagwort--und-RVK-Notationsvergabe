# Automatisierte Schlagwort- und RVK-Notationsvergabe
## Projekt: Umsystematisierung der Bibliotheksbestände einer archäologischen Spezialbibliothek
Seit Längerem besteht der Wunsch, die Bestände der archäologischen Spezialbibliothek systematisch aufzustellen. Man entschied sich für die Regensburger Verbundklassifikation (RVK) als Ordnungssystem. Da die Bibliothek nicht Mitglied in einem Verbund ist und über die vorhandene Bibliothekssoftware keine automatische Übernahme von Fremddaten, d.h. Schlagwörter und RVK-Notationen, möglich ist, muss dies auf einem alternativen Weg vonstattengehen.

## Einführung
In diesem Projekt soll versucht werden, die Schlagwort- und Notationsvergabe der RVK (Regensburger Verbundklassifikation) automatisch in einer Excel-Liste erfolgen zu lassen. Grundlage für die automatische Vergabe ist u.a. eine csv-/Excel-Datei und ein webbasiertes Tool namens Malibu. Dieses ist auch im JSON-Format vorhanden.

## Möglicher Projektablauf
Aus diesem Tool bzw. mittels JSON-basierter Antwortdaten[^1] werden die in den großen deutschsprachigen Bibliotheksverbünden generierten Schlagwörter und RVK-Notationen mit den ISBN bzw. PPN des Bibliotheksbestands der LWL-Archäologie vorhandenen Titel abgeglichen und im Anschluss in eine Excel-Liste gespeist:

* Zunächst werden alle in der Bibliothek umzusystematisierenden Werke über einen SQL-Befehl in einer csv-Datei erfasst. Diese wurde nach Spalten (Signaturen, Mediennummern, Kurztitel, Autor, Reihentitel, ISBN, neue Notation, neue Schlagwörter, neue Gesamtsignatur) und nach Signaturen aufsteigend sortiert.
* Schließlich kommt das hier gezeigte Skript zum Einsatz, das die ISBN bzw. später auch PPN aus der entsprechenden Zeile in das Malibu-Tool im JSON-Format setzt.
* Danach werden die in den Verbünden vergebenen RVK-Notationen in die Spalte "neue Notation" gesetzt, die Schlagwörter in die Spalte "neue Schlagwörter". Es sollen alle Verbünde einzeln betrachtet werden können, weshalb diese hier auch einzeln dargestellt werden.
* Mit einer For Loop soll dann die Anfrage für alle 30.000 Monographien der Bibliothek durchgeführt werden.
* Zur weiteren kollaborativen Bearbeitung (mit MS Office 365) wird eine csv- und dann eine Excel-Datei erstellt. Nicht zuletzt wegen der besseren Ansicht für die Bearbeiter_innen.

## Ziel
Die Vergabe von Schlagwörtern und Notationen soll somit automatisiert werden, um die Umsystematisierung der beteiligten Mitarbeiterinnen und Mitarbeiter zu erleichtern. RVK-Notationen und Schlagwörter könnten somit zunächst maschinell und ggfls. intellektuell erfasst werden.

Quellen
[^1]: Python Requests: Schnellstart. URL: https://2.python-requests.org//de/latest/user/quickstart.html [letzter Zugriff: 09.07.2019]
