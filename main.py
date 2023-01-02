import sys
from knf import knf_gen
from dnf import dnf_gen
from random_var_gen import gen_var_list

"""
Dieses Programm generiert boolsche Ausdrücke in KNF oder
DNF mit einer spezifizierten Anzahl an Variablen.
"""


KNF_FLAGS = ["-k", "--knf"]
DNF_FLAGS = ["-d", "--dnf"]
MODES_LIST = [*KNF_FLAGS, *DNF_FLAGS]
HELP_LIST = ["-h", "--help"]
STYLE_FLAG_LIST = ["-s", "--style"]
STYLES_LIST = ["l", "latex", "p", "plain-text"]
ALL_FLAGS = [*MODES_LIST, *HELP_LIST, *STYLE_FLAG_LIST, *STYLES_LIST]

HELP_TEXT = f"""
boolGen kann mit den folgenden Parametern aufgerufen werden:

main.py {MODES_LIST!r} [Anzahl der Variablen (zwischen 1 und 9)]

Die flags geben an, ob eine Formel in DNF oder in KNF generiert wird.
Die Anzahl am Ende gibt an, wie viele Variablen die Formel enthält.
Keine dieser Angaben ist optional.
"""


def help_text():
    print(HELP_TEXT)
    exit()


def error_text():
    print("ERROR: Eingabe nicht erkannt!")
    help_text()


arguments = sys.argv[1:]

help_true = bool([x for x in HELP_LIST if x in arguments])

if help_true:
    help_text()

try:
    NUM_OF_VARS = int(arguments[-1])
except TypeError:
    error_text()

mode = [x for x in arguments if x in MODES_LIST]

mode_is_valid = bool(mode) and len(mode) == 1

if not mode_is_valid:
    raise SyntaxError(f"Modus wurde nicht erkannt!\n{HELP_TEXT}")

style_flag_list = [x for x in arguments if x in STYLE_FLAG_LIST]

style_is_specified = bool(style_flag_list)

style_flag = style_flag_list[0]
style_index = arguments.index(style_flag) + 1

if style_is_specified:
    style: str = arguments[style_index]
    if len(style) > 1:
        style = style[:1]  # so that we can treat style as a single letter
    if style not in STYLES_LIST:
        raise SyntaxError("Style wurde nicht erkannt.")
    else:
        print("Hurra!")
else:
    style = "l"  # Latex is default

if mode[0] in KNF_FLAGS:
    print(
        knf_gen(gen_var_list(NUM_OF_VARS))
    )  # These functions should get the style as input

elif mode[0] in DNF_FLAGS:
    print(
        dnf_gen(gen_var_list(NUM_OF_VARS))
    )  # These functions should get the style as input

else:
    raise SyntaxError(f"Modus wurde nicht erkannt!\n{HELP_TEXT}")
