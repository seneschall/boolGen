import random

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]


def make_inverse(variable: str, style: str) -> str:
    if style == "l" or style == "latex":
        return r"\overline{" + variable + r"}"
    else:
        return f"{variable}'"


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

    def randomise_var_list(self, var_list: list[str]) -> list[str]:
        results = []
        for var in var_list:
            random_value = random_boole()
            if random_value is False:
                results.append(make_inverse(var, self.style))
            else:
                results.append(var)
        return results

    def make_random_term(self, var_list: list[str]) -> str:
        randomise_var_list = self.randomise_var_list
        if self.func_type == "c" or self.func_type == "cnf":
            return make_maxterm(randomise_var_list(var_list))
        elif self.func_type == "d" or self.func_type == "dnf":
            return make_minterm(randomise_var_list(var_list))
        else:
            raise ValueError("Illegal expression type. Should be 'c' or 'd'.")

    def make_boolean_expression(self) -> str:
        list_len = len(self.var_list)
        num_of_terms = (
            gen_num_of_terms(list_len, list_len + 3)
            if list_len > 2
            else gen_num_of_terms(list_len, list_len + 2)
        )
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
        style = self.style
        if self.amount == 1 and (style == "l" or style == "latex"):
            return make_latex_math(self.make_boolean_expression())
        elif self.amount > 1 and (style == "l" or style == "latex"):
            res_str = ""
            for i in range(self.amount):
                res_str += f"{self.make_boolean_expression()}\n"
            return make_latex_math(res_str, inline=False)
        elif self.amount == 1 and (style == "p" or style == "plain_text"):
            return self.make_boolean_expression()
        elif self.amount > 1 and (style == "p" or style == "plain_text"):
            res_str = ""
            for i in range(self.amount):
                res_str += f"{self.make_boolean_expression()}\n"
            return res_str
        else:
            raise ValueError("self.amount less than 1.")
