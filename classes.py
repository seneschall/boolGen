import random

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]


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
        result += f"{item} + "
    result = result[:-3]
    return result


def make_latex_math(formula: str, inline=True) -> str:
    if inline is True:
        return f"${formula}$"
    else:
        return f"$$\n{formula}\n$$"


def make_maxterm(var_list: list[str]) -> str:
    return f"({make_disjunction(var_list)})"


def make_minterm(var_list: list[str]) -> str:
    return f"({make_conjunction(var_list)})"


def random_boole() -> bool:
    return bool(random.randrange(0, 2))


def gen_var_list(var_num: int) -> list[str]:
    return LETTERS[:var_num]


def randomise_var_list(var_list: list[str]) -> list[str]:
    results = []
    for var in var_list:
        random_value = random_boole()
        if random_value is False:
            results.append(make_inverse(var))
        else:
            results.append(var)
    return results


def gen_num_of_terms(min_amount: int, max_amount: int) -> int:
    return random.randint(min_amount, max_amount)


class boolean_expression:
    def __init__(
        self, var_num: int, func_type: str, style: str, amount: int = 1
    ) -> None:

        self.var_list = gen_var_list(var_num)
        self.style = style
        self.func_type = func_type
        self.amount = amount

    def make_random_term(self, var_list: list[str]) -> str:
        if self.func_type == "c" or self.func_type == "cnf":
            return make_maxterm(randomise_var_list(var_list))
        elif self.func_type == "d" or self.func_type == "dnf":
            return make_minterm(randomise_var_list(var_list))
        else:
            raise ValueError("Illegal expression type. Should be 'c' or 'd'.")

    def make_boolean_expression(self) -> str:
        list_len = len(self.var_list)
        num_of_terms = gen_num_of_terms(list_len, list_len + 3)
        results_list: list[str] = []
        while len(results_list) < num_of_terms:
            new_term = self.make_random_term(self.var_list)
            if new_term not in results_list:
                results_list.append(new_term)
        if self.func_type == "d" or self.func_type == "dnf":
            result = make_disjunction(results_list)
        elif self.func_type == "c" or self.func_type == "cnf":
            result = make_conjunction(results_list)
        else:
            raise ValueError("Illegal expression type. Should be 'c' or 'd'.")
        return result

    def __str__(self) -> str:
        if self.amount == 1:
            return make_latex_math(self.make_boolean_expression())
        else:
            res_str = ""
            for i in range(self.amount):
                res_str += f"{self.make_boolean_expression()}\n"
            return make_latex_math(self.make_boolean_expression(), inline=False)
