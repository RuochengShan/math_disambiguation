from util.search_equ import search_by_token, search_by_id
from util.alter_label_text import alter_label
from util.useful_functions import neighbor, get_all_index_of_a_token, neighbor_in_range

normal_v_list = ["x", "z", "t", "n", "e", "R"]


# tier1
def left_to_prime(token_list, token_index):
    if neighbor(token_list, token_index, "\prime", 1):
        return True
    else:
        return False


def right_to_sum(token_list, token_index):
    if neighbor(token_list, token_index, "\sum", -1):
        return True
    elif neighbor(token_list, token_index, "\prod", -1):
        return True
    else:
        return False


def right_to_variable(token_list, token_index):
    for v in normal_v_list:
        if neighbor(token_list, token_index, v, -1):
            return True
    return False


# tier 2
def is_new_variable(token_list, token_index):
    if token_index + 1 == len(token_list):
        return False

    if token_list[token_index+1] == "(" and token_list[token_index-1] != "f":
        return True
    else:
        return False


def is_integral(token_list, token_index):
    if neighbor_in_range(token_list, token_index, "\int", -3) and neighbor_in_range(token_list, token_index, "_", -3):
        return True
    elif neighbor_in_range(token_list, token_index, "\int", -3) and neighbor_in_range(token_list, token_index, "_", 3):
        return True
    elif neighbor(token_list, token_index, "I", -1):
        return True
    else:
        return False


def is_power(token_list, token_index):
    if right_to_variable(token_list, token_index):
        return True
    elif token_list[-1].isnumeric():
        return True
    else:
        return False


def is_derivative(token_list, token_index):
    if neighbor(token_list, token_index, "f", -1):
        return True
    elif neighbor(token_list, token_index, "D", -1):
        return True
    else:
        return False

def label_superscript():

    data_list = search_by_token("^", mode=1)

    jintegal, jpower, jsum_, jnew, jprime, jder = [], [], [], [], [], []
    all_no = []
    for i in data_list:
        tokens, labels = search_by_id(i)
        index_list = get_all_index_of_a_token(tokens, "^")

        for j in index_list:

            is_n = is_integral(tokens, j)
            is_p = is_power(tokens, j)
            is_s = right_to_sum(tokens, j)
            is_new = is_new_variable(tokens, j)
            is_pri = left_to_prime(tokens, j)
            is_der = is_derivative(tokens, j)

            if is_n:
                jintegal.append((i, j))
            if is_p:
                jpower.append((i, j))
            if is_s:
                jsum_.append((i, j))
            if is_new:
                jnew.append((i, j))
            if is_pri:
                jprime.append((i, j))
            if is_der:
                jder.append((i, j))
            if not is_n and not is_p and not is_s and not is_new and not is_pri and not is_der:
                all_no.append((i, j))

    only_integal = [i for i in jintegal if i not in jsum_ and i not in jnew and i not in jpower and i not in jprime and i not in jder]
    only_sum = [i for i in jsum_ if i not in jintegal and i not in jnew and i not in jpower and i not in jprime and i not in jder]
    only_new = [i for i in jnew if i not in jintegal and i not in jsum_ and i not in jpower and i not in jprime and i not in jder]
    only_prime = [i for i in jprime if i not in jintegal and i not in jsum_ and i not in jpower and i not in jnew and i not in jder]
    only_power = [i for i in jpower if i not in jintegal and i not in jsum_ and i not in jprime and i not in jnew and i not in jder]
    only_der = [i for i in jder if i not in jintegal and i not in jsum_ and i not in jprime and i not in jnew and i not in jpower]

    for t in only_integal:
        eq_id = t[0]
        token_index = t[1]
        new_label = "integral_upper_bond"
        alter_label(eq_id, token_index, new_label)
        print(eq_id, token_index, new_label)

    for t in only_sum:
        eq_id = t[0]
        token_index = t[1]
        new_label = "summation_upper_bond"
        alter_label(eq_id, token_index, new_label)
        print(eq_id, token_index, new_label)

    for t in only_new:
        eq_id = t[0]
        token_index = t[1]
        new_label = "new_function_variable"
        alter_label(eq_id, token_index, new_label)
        print(eq_id, token_index, new_label)

    for t in only_prime:
        eq_id = t[0]
        token_index = t[1]
        new_label = "derivative"
        alter_label(eq_id, token_index, new_label)
        print(eq_id, token_index, new_label)

    for t in only_der:
        eq_id = t[0]
        token_index = t[1]
        new_label = "derivative"
        alter_label(eq_id, token_index, new_label)
        print(eq_id, token_index, new_label)

    for t in only_power:
        eq_id = t[0]
        token_index = t[1]
        new_label = "power"
        alter_label(eq_id, token_index, new_label)
        print(eq_id, token_index, new_label)


if __name__ == '__main__':
    label_superscript()
