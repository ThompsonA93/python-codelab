# Datenstrukturen

## Typen
Daten werden üblicherweise über verschiedene Ansätze gespeichert. Diese Prinzipien finden sich auch in den üblichen Datenbankmanagementsystemen (DBMS) wieder:
- Schlüssel-Wert: Ein eindeutiger Schlüssel zeigt auf einen spezifischen Wert.
- Wide-Column: Ein Index zeigt auf einen Block von Daten
- Relational: Daten werden zu Zeilen und Spalten verwaltet. Daten einer Zeile hängen zusammen, während Spalten die Attribute der Daten beschreiben.
- Dokumente: Dokumente beinhalten Schlüssel-Wert-Paare, wobei mehrere Dokumente zusammenhängen.
- Graphen: Ein Knoten bzw. Vertex beschreibt ein spezifisches Objekt. Verlinkungen bzw. Kanten beschreiben Relationen zwischen Knoten.
- Multi-Model: Multi-Model Frameworks beinhalten mehrere der vorgenannten Typen, um spezifische Operationen performanter zu gestalten (auf anderweitige Kosten hin).

## Objekte
Simpel ausgedrückt, ist eine Datenstruktur ein virtuelles Objekt in dem Daten gespeichert und organisiert werden.
Datenstrukturen zeichnen sich zudem dadurch aus, wie auf diese Daten zugegriffen wird, i.e. erschaffen, lesen und schreiben.

Die üblichsten Datenstrukturen in Python sind:
  - Set: Eine Menge an Daten ohne spezifische Ordnung. Daten müssen einzigartig sein und können nicht modifiziert werden.
    > set = (5, 2, 10, 3)\
    > set = ("a", "b", "c", "d")
  - Array: Eine Datenstruktur die mehrere Variable desselben Types aneinanderfolgend speichert. Zugriff mittels Index, beginnend mit 0.
    > array1 = []\
    > array2 = [5, 2, 3, 4]\
    > array3 = [[2, 5, 2], [5, 6, 1]]\
    > ...
  - Dictionary: Eine Datenstruktur welches ein Schlüssel-Wert-Prinzip implementiert.
    > dict1 = {5: 2, 2: 5}\
    > dict2 = {5: {'hallo': 2}, 3: {'welt': 3}}
    > ...

Zudem gibt es weitere integrierte Datenstrukturen welche man nutzen kann.
Dazu zählen **Tupel**, **Maps**, **Hashtables**, **Trees**, und **Graphs**.

