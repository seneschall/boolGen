# Readme

boolGen ist ein kleines Programm zur Zufallsgenerierung von boolschen Ausdrücken
in Konjunktiver Normalform (KNF) oder Disjunktiver Normalform (DNF). Das Ergebnis wird wahlweise als Latex-Mathe-Formel oder als Plain-Text ausgegeben.

boolGen kann mit den folgenden Parametern aufgerufen werden:

```bash
main.py --type [cnf, dnf] --style [optional: latex, plain_text] [Anzahl der Variablen (zwischen 2 und 9)
```

Mit `--type` oder `-t` wird spezifiziert, ob der generierte boolsche Ausdruck in KNF (`cnf`/`c`) oder DNF (`dnf`/`d`) ausgegeben wird.

Mit `--style` oder `-s` kann optional noch spezifiziert werden, ob die Formel als Plain-Text (`plain_text`/`p`) oder Latex (`latex`/`l`) ausgegeben werden soll. Standard ist Latex.

Abschließend muss angegeben werden, wie viele Variablen der Ausdrucken enthalten soll (Ganzzahl zwischen 2 und 9).

## Beispielhafter Programmaufruf (Latex)

```bash
main.py --type dnf 4
```

Ausgabe:

```
$(A\overline{B}\overline{C}D) + (\overline{A}BCD) + (ABCD) + (\overline{A}B\overline{C}D) + (AB\overline{C}\overline{D})$
```

Gerendert:

$(A\overline{B}\overline{C}D) + (\overline{A}BCD) + (ABCD) + (\overline{A}B\overline{C}D) + (AB\overline{C}\overline{D})$

## Beispielhafter Programmaufruf (Plain Text)

```bash
main.py --type cnf --style plain_text 5
```

Ausgabe:

```
(A' + B' + C + D + E')(A + B' + C + D' + E')(A + B' + C' + D' + E)(A + B + C + D + E')(A + B + C + D' + E')(A + B + C' + D + E)
```