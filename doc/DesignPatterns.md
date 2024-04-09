# Design Patterns

Design patterns (de.: Entwurfsmuster) sind Vorangehensweisen zu typischen Programmierproblemen.

Man spricht, im Kontext von Design Patterns, in erster Linie von objektorientierter Programmierung. 
Im Vergleich zu z.B. prozeduraler Programmierungm existieren ähnliche Paradigmen, welche aber gänzlich anders genannt und implementiert werden.

Objektorientiert    | Prozedural
-- | --
Methode             | Funktion
Objekt              | Struktur  
Klasse              | Modul


## Objektorientiertes Programmieren
Um objektorientierte Patterns entwickeln zu können, ist (no-na-net) eine gute Grundlage in Programmierfähigkeiten vonnöten.

- Überladen (en.: Overloading): Funktionen werden Überladen, indem man ihnen denselben Namen, aber unterschiedliche Parameter gibt.
- Überschatten (en.: Shadowing): Variablen (variable shadowing) und Klassen (subclass shadowing) können in Python überschattet werden. 
- Datenkapselung (en.: Encapsulation): Bestimmte Funktionen und Variablen einer Klasse werden vor unintendierten Zugriff verborgen.
- Vererbung (en.: Inheritance): Ein Objekt kann Daten und Funktionen einer anderen Klasse kopieren.
- Polymorphismus (en.: Polymorphism): Eine Funktionalität wird mehrmals für verschiedene Eingaben implementiert.

## Typen von Design patterns
Man unterscheidet zwischen 3 Arten der Muster, bestimmt durch dessen Funktion im Programm.

### Erschaffende Muster
Erschaffende Muster (en.: creational pattern)
- Factory: Instanziert ein Objekt über gemeinsame Schnittstelle.
- Prototype: Erlaubt Kopierung (ie. klonen) vollständiger Datenobjekte
- Singleton: Instanzierung eines Objektes wird nur einmal erlaubt

### Strukturelle Muster
Strukturelle Muster (en.: structural pattern)
- Adapter: Erlaubt die Zusammenarbeit nicht-kompatibler Objekte
- Decorator: Erweitert bestehenden Code mit zusätzlichen Funktionalitäten
- Proxy: Eine Klasse umhüllt eine andere.

### Verhaltensspezifische Muster
Verhaltensspezifische Muster (en.: behavioral pattern)
- Iterator: Ermöglicht das durchsuchen von Objekten ohne unspezifische Objektinformationen preiszugeben.
- Mediator: Ein 'Controller' durch welches andere, miteinander verlinkte Objekte arbeiten können.
- Observer: Eine Komponente, welches Signale aussendet wenn eine verlinkte Funktionalität ausgeführt wird  
- Strategy: Ein Pattern welches für ein Problem verschiedene Funktionsausführungen initiieren kann
- Template: Eine Funktionalität wird abstrahiert dargestellt und von konkreten Funktionen genutzt wird.
