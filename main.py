import sys
from knf import knf_gen
from dnf import dnf_gen
from random_var_gen import gen_var_list

"""
Dieses Programm generiert boolsche Ausdrücke in KNF oder
DNF mit einer spezifizierten Anzahl an Variablen.
"""


OPTIONS_LIST = ["-k", "--knf", "-d", "--dnf", "-h", "--help"]

HELP_TEXT = f"""
boolGen kann mit den folgenden Parametern aufgerufen werden:

main.py {OPTIONS_LIST!r} [Anzahl der Variablen (zwischen 1 und 9)]

Die flags geben an, ob eine Formel in DNF oder in KNF generiert wird.
Die Anzahl am Ende gibt an, wie viele Variablen die Formel enthält.
Keine dieser Angaben ist optional.
"""


def help_text():
    print(HELP_TEXT)
    exit()


options = sys.argv[1]

if options == "-h" or options == "--help":
    help_text()


num_of_vars = int(sys.argv[2])

if num_of_vars > 9 or num_of_vars < 1:
    help_text()

if options == "-k" or options == "--knf":
    print(knf_gen(gen_var_list(num_of_vars)))

elif options == "-d" or options == "--dnf":
    print(dnf_gen(gen_var_list(num_of_vars)))

else:
    help_text()
