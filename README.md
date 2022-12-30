# Readme

boolGen ist ein kleines Programm zum Erzeugen von boolschen Ausdrücken
in KNF oder DNF. Das Ergebnis wird als Latex-Mathe-Formel ausgegeben.

boolGen kann mit den folgenden Parametern aufgerufen werden:

```bash
main.py ['-k', '--knf', '-d', '--dnf', '-h', '--help'] [Anzahl der Variablen (zwischen 1 und 9)
```

Die flags geben an, ob eine Formel in DNF oder in KNF generiert wird.
Die Anzahl am Ende gibt an, wie viele Variablen die Formel enthält.
Keine dieser Angaben ist optional.

Beispielhafter Programmaufruf:

```bash
main.py --dnf 4
```

$(\overline{A}B\overline{C}\overline{D}) + (AB\overline{C}D) + (ABCD) + (\overline{A}\overline{B}\overline{C}\overline{D}) + (\overline{A}B\overline{C}D) + (AB\overline{C}\overline{D}) + (ABC\overline{D})$
