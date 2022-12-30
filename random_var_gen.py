import random
from latex_gen import make_inverse

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]


def random_boole() -> bool:
    return bool(random.randrange(0, 2))


def gen_var_list(var_num: int) -> list[str]:
    return LETTERS[:var_num]


def randomise_var_list(var_list: list[str]):
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
