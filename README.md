# Automatisierte Schlagwort- und RVK-Notationsvergabe
## Hintergrund-Informationen
Seit Längerem besteht der Wunsch, die Bestände einer archäologischen Spezialbibliothek systematisch aufzustellen. Man entschied sich für die Regensburger Verbundklassifikation (RVK) als Ordnungssystem. Da die Bibliothek nicht Mitglied in einem Verbund ist und über die vorhandene Bibliothekssoftware keine automatische Übernahme von Fremddaten, d.h. Schlagwörter und RVK-Notationen, möglich ist, muss dies auf einem alternativen Weg vonstattengehen. Hierfür wurde das folgende Skript erstellt, das auch anderen zur RVK umsystematisierenden Bibliotheken dabei helfen soll, Vorgänge mithilfe IT-basierter Möglichkeiten zu optimieren, um personelle und finanzielle Ressourcen zu sparen.

## Projekt-Beschreibung
In diesem Projekt wird die Schlagwort- und Notationsvergabe der RVK (Regensburger Verbundklassifikation) automatisch in einer Excel-Liste erfolgen. Grundlage für die automatische Vergabe ist u. a. eine csv-/Excel-Datei und ein webbasiertes Tool namens [Malibu](https://github.com/UB-Mannheim/malibu). Dieses ist auch im JSON-Format vorhanden.

## Skript-Beschreibung
Bei diesem Skript handelt es sich um einen Prototyp, der um beliebige Anfragen erweitert bzw. reduziert werden kann. Aus dem Malibu-Tool bzw. mittels JSON-basierter Antwortdaten werden die in den großen deutschsprachigen Bibliotheksverbünden generierten Schlagwörter und RVK-Notationen mit den ISBN bzw. PPN des Bibliotheksbestands der LWL-Archäologie abgeglichen und final in eine Excel-Liste gespeist:

* Zunächst werden alle in der Bibliothek umzusystematisierenden Werke über einen SQL-Befehl in einer csv-Datei erfasst.
* Diese wurde nach Spalten, z. B. Signaturen, Mediennummern, Kurztitel, Autor, Reihentitel, ISBN, neue Notation, neue Schlagwörter, neue Gesamtsignatur, und nach Signaturen aufsteigend sortiert.
* Schließlich kommt das hier gezeigte Skript zum Einsatz, das die ISBN bzw. später auch PPN aus der entsprechenden Zeile in das Malibu-Tool im JSON-Format setzt.
* Danach werden die in den Verbünden vergebenen RVK-Notationen in die Spalte "neue Notation" gesetzt, die Schlagwörter in die Spalte "neue Schlagwörter"
* Es sollen alle Verbünde einzeln betrachtet werden können, weshalb diese hier auch einzeln dargestellt werden. Nicht für jede Bibliothek sind alle Verbünde gleichermaßen relevant.
* Mit einer For Loop wird die Anfrage für alle 30.000 Monographien der Bibliothek durchgeführt werden.
Zur weiteren kollaborativen Bearbeitung (mit MS Office 365) und nicht zuletzt wegen der besseren Ansicht für die Bearbeiter_innen wird eine csv- und dann eine Excel-Datei erstellt.

## Ziel
Die Vergabe von Schlagwörtern und Notationen soll somit automatisiert werden, um die Umsystematisierung der beteiligten Mitarbeiterinnen und Mitarbeiter zu erleichtern. RVK-Notationen und Schlagwörter könnten somit zunächst maschinell und ggfls. intellektuell erfasst werden.

## Meilensteine
1. csv-Datei wird in github angezeigt (Ende Mai 2019)
2. Informationen zu einzelnen Titeln werden mittels ISBN und Json-Files zugeordnet (Anfang Juni 2019)
3. for-Schleife für alle 15 Titel und alle großen Verbünde (Ende Juni 2019)
4. Alle RVK-Notationen für alle ISBN in allen Verbünden in eine csv-Datei exportieren und nicht benötigte Werte ignorieren. (10.07.2019)
5. Dies für alle Titel durchzuführen (17.07.2019)

## Desiderata
Dies für alle JSON-Strings (mit allen ISBN und den jeweils vergebenen RVK-Notationen für alle Verbünde) durchführen. Mögliches Vorgehen:
* Wie ist eine RVK-Notation aufgebaut? Wie viele Zeichen hat eine RVK-Notation?
* Sie setzt sich aus 1) 2 Buchstaben 2) 1 Leerzeichen 3) und 3 und 5 Ziffern zusammen.
* Hierfür könnte mit einem regulären Ausdruck gearbeitet werden:
* 1) 2 Buchstaben zwischen a bis z [a-z], 2) Leerzeichen wie Tab, Space, ... \s und 3) 3 bis 5 Zahlen von 0-9: \d, [0-9]
* Die Zahl, die an letzter Stelle steht, ist mindestens 3-stellig und höchstens 5-stellig: {m, n} Der Ausdruck kommt mindestens m-mal, höchstens n-mal vor; z. B. \w{3, 5} (vgl. https://docs.python.org/2/library/re.html)
