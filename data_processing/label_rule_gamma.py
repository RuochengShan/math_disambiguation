from util.search_equ import search_by_token, search_by_id
from util.alter_label_text import alter_label
from util.path import LABEL_LOG_GAMMA


def get_all_index_of_a_token(token_list, token):
    index_list = []
    for i in range(len(token_list)):
        if token_list[i] == token:
            index_list.append(i)
    return index_list


def multivariate_gamma(token_list, gamma_index):
    if token_list[gamma_index+1] == "_" and token_list[gamma_index+2] == "m":
        return True
    else:
        return False


def q_gamma(token_list, gamma_index):
    if token_list[gamma_index+1] == "_" and token_list[gamma_index+2] == "q":
        return True
    else:
        return False


def incomplete_gamma(tokens, gamma_index):
    if tokens[gamma_index+1] == "\left(":
        n = 2
        while True:
            if tokens[gamma_index+n] == ",":
                return True
            elif tokens[gamma_index+n] == r"\right)" or tokens[gamma_index+n] == r"\right )":
                return False
            else:
                n += 1


def write_log(eq_id, token_index, new_label):
    msg = "[Labeling] %s at index %d with %s " % (eq_id, token_index, new_label)
    print(msg)
    with open(LABEL_LOG_GAMMA, "a") as f:
        f.write(msg + "\n")


def label_gamma_function():
    # label gamma functions
    data_list = search_by_token("Gamma")
    for i in data_list:
        tokens, labels = search_by_id(i)
        index_list = get_all_index_of_a_token(tokens, "\Gamma")
        for j in index_list:
            is_m_gamma = multivariate_gamma(tokens, j)
            is_q_gamma = q_gamma(tokens, j)
            is_i_gamma = incomplete_gamma(tokens, j)

            if is_m_gamma:
                new_label = "multivariate_variable_gamma_function"
            elif is_q_gamma:
                new_label = "q_gamma_function"
            elif is_i_gamma:
                new_label = "incomplete_gamma_function"
            else:
                new_label = "gamma_function"

            alter_label(i, j, new_label)
            write_log(i, j, new_label)


if __name__ == '__main__':
    label_gamma_function()
