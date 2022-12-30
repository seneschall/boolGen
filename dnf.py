from random_var_gen import gen_num_of_terms, randomise_var_list
from latex_gen import make_conjunction, make_disjunction, make_latex_math


def make_minterm(var_list: list[str]):
    return f"({make_conjunction(var_list)})"


def make_random_term(var_list: list[str]):
    return make_minterm(randomise_var_list(var_list))


def dnf_gen(var_list: list[str]):
    list_len = len(var_list)
    num_of_terms = gen_num_of_terms(list_len, list_len + 3)
    results_list: list[str] = []
    while len(results_list) < num_of_terms:
        new_term = make_random_term(var_list)
        if new_term not in results_list:
            results_list.append(new_term)
    result = make_latex_math(make_disjunction(results_list))
    return result
