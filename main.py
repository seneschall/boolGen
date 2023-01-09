import argparse
from knf import knf_gen
from dnf import dnf_gen
from random_var_gen import gen_var_list

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
        help="Set the style of the output. Should be either l (Latex) or p (plain text).",
        default="l",
        choices=["l", "p"],
    )

    parser.add_argument(
        "vars",
        metavar="VARS",
        type=int,
        choices=range(1, 10),
        help="Number of variables to be generated. Should be integer between 1 and 9.",
    )

    # args = vars(parser.parse_args())
    args = parser.parse_args()
    type: str = args.type
    style: str = args.style
    vars: int = args.vars

    print(f"Die Variablen sind type: {type}, style: {style}, vars {vars}.")

    # if mode[0] in KNF_FLAGS:
    #     print(
    #         knf_gen(gen_var_list(NUM_OF_VARS))
    #     )  # These functions should get the style as input

    # elif mode[0] in DNF_FLAGS:
    #     print(
    #         dnf_gen(gen_var_list(NUM_OF_VARS))
    #     )  # These functions should get the style as input

    # else:
    #     raise SyntaxError(f"Modus wurde nicht erkannt!\n{HELP_TEXT}")


if __name__ == "__main__":
    main()
