### Aufgabe: Zahleneingabe bei Input 

Was leistet das folgende Programm? Welchen Ergebnistyp liefert die input-Anweisung? 

``` python
a = input("What's your name? ")
print(a)
print(type(a))

print()

b = input("How old are you? ")
age = int(b)     # Was passiert hier?
# ... Antwort eintragen ...

print(b, age)
print(type(b), type(age))
```
---------------------------------------
---------------------------------------

##### Lösung

``` python
a = input("What's your name? ")
print(a)
print(type(a))

print()

b = input("How old are you? ")
age = int(b)     # Was passiert hier?
# Typumwandlung von der String-Variable b in eine Integer-Variable age

print(b, age)
print(type(b), type(age))
```
Antwort: Die input-Anweisung liefert stets ein Ergebnis vom Typ String.

##### Vorwissen

- Datentypen inkl. String 
- input-Anweisung
- type-Funktion

##### Lernhandlungen

1) Quelltext lesen und ausführen 
2) Bedeutung der int-Typumwandlunge verstehen
3) geforderten Kommentar aufschreiben 
4) ggf. Antwortsatz zur Frage bzgl. input-Anweisung schreiben

##### Lösungsprozess

... Abbildung in Toulmin-Notation

##### Unterstützende Informationen

Seiten im THEIß-Buch  
Weblink - TutorialsPoint

----
[//]: # "Lernziel: Zusammenhang zwischen input und Typumwandlung für num. Eingaben erkennen"
[//]: # "Thema: Variablen, Berechnung, Anzeige"
[//]: # "Komplexität: 1 - niedrig"
[//]: # "Aufgabentyp: vollständiges Beispiel"

Autor: Robert Ringel, Fakultät Informatik/Mathematik, HTW Dresden  
Version: 08/2024            
Lizenz: CC BY-SA 4.0
