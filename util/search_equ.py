from util.path import DATA_FOLDER
import os


def search_by_id(equ_id):
    """

    :param equ_id: str - 1.1.2
    :return: list of tokens - ["a", "+", "b", "=", "c"]
    """
    chapter = equ_id.split(".")[0]
    eq_path = DATA_FOLDER + chapter + "/" + equ_id + ".txt"

    with open(eq_path, "r", encoding="utf-8") as f:
        token_list, label_list = [], []
        lines = f.readlines()
        for i in lines:
            token = i.split("  ")[0]
            label = i.split("  ")[1].rstrip()
            token_list.append(token)
            label_list.append(label)

    return token_list, label_list


def search_by_token(token, mode):
    """

    :param token: str - gamma
    :return: list - equation_ids
    """
    eq_id_list = []

    for roots, dirs, files in os.walk(DATA_FOLDER):
        # skip the math root
        if roots.split("/")[-1].isnumeric():
            for file in files:
                file_path = roots + "/" + file
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for i in lines:
                        token_i = i.split("  ")[0]
                        if mode == 1:
                            if token in token_i:
                                eq_id_list.append(file.split(".txt")[0])
                                break
                        else:
                            if token == token_i:
                                eq_id_list.append(file.split(".txt")[0])
                                break

    return eq_id_list


def search_all_label(label):
    num = 0
    eq_list = []
    for roots, dirs, files in os.walk(DATA_FOLDER):
        # skip the math root
        if roots.split("/")[-1].isnumeric():
            for file in files:
                file_path = roots + "/" + file
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for i in lines:
                        label_i = i.split("  ")[1].rstrip()
                        if label_i == label:
                            num += 1
                            eq_list.append((file.split(".txt")[0], label_i))
    return num, eq_list


def if_equation_labelled():
    num = 0
    for roots, dirs, files in os.walk(DATA_FOLDER):
        # skip the math root
        if roots.split("/")[-1].isnumeric():
            for file in files:
                file_path = roots + "/" + file
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for i in lines:
                        label_i = i.split("  ")[1].rstrip()
                        if label_i != "O":
                            num += 1
                            break
    return num


def multi_label_single_label():

    m = 0
    s = 0
    for roots, dirs, files in os.walk(DATA_FOLDER):
        # skip the math root
        if roots.split("/")[-1].isnumeric():
            for file in files:
                label_list = []
                file_path = roots + "/" + file

                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for i in lines:
                        label_i = i.split("  ")[1].rstrip()
                        if label_i != "O":
                            label_list.append(label_i)

                if len(list(set(label_list))) > 1:
                    m += 1
                elif len(list(set(label_list))) == 1:
                    s += 1
    return m, s

def get_labelled_data_set(token):
    eq_list = search_by_token(token, 1)

    token_list_all = []
    label_list_all = []
    for i in eq_list:
        token_list = []
        label_list = []
        chapter = i.split(".")[0]
        with open(DATA_FOLDER + chapter + "/" + i + ".txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                token1 = line.split("  ")[0]
                label = line.split("  ")[1].rstrip()
                token_list.append(token1)
                label_list.append(label)
            if list(set(label_list)) == ["O"]:
                continue
        token_list_all.append(token_list)
        label_list_all.append(label_list)
    return token_list_all, label_list_all


if __name__ == '__main__':

    from pprint import pprint
    label = "multivariate_variable_gamma_function"
    n, eq = search_all_label(label)
    # print(label, n)
    pprint(eq)

    # en = if_equation_labelled()
    # print(en)
    #
    # m, s = multi_label_single_label()
    # print(m, s)
