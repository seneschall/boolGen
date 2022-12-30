def make_inverse(variable: str) -> str:
    return r"\overline{" + variable + r"}"


def make_conjunction(items: list[str]) -> str:
    result = ""
    for item in items:
        result += item
    return result


def make_disjunction(items: list[str]) -> str:
    result = ""
    for item in items:
        result += item + " + "
    result = result[:-3]
    return result


def make_latex_math(formula: str, inline=True) -> str:
    if inline is True:
        return f"${formula}$"
    else:
        return f"$$\n{formula}\n$$"
