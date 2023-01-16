import argparse
from classes import boolean_expression

"""
Dieses Programm generiert boolsche Ausdrücke in KNF oder
DNF mit einer spezifizierten Anzahl an Variablen.
"""


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-t",
        "--type",
        help="Set the type of the expression to cnf or dnf",
        required=True,
        choices=["c", "cnf", "d", "dnf"],
    )

    parser.add_argument(
        "-s",
        "--style",
        help="Set the style of the output. Should be either l (Latex) "
        "or p (plain text).",
        default="l",
        choices=["l", "latex", "p", "plain_text"],
    )

    parser.add_argument(
        "vars",
        metavar="VARS",
        type=int,
        choices=range(2, 10),
        help="Number of variables to be generated. Should be an integer "
        "between 2 and 9.",
    )

    args = parser.parse_args()
    func_type: str = args.type
    style: str = args.style
    var_num: int = args.vars

    print(boolean_expression(var_num, func_type, style))


if __name__ == "__main__":
    main()
