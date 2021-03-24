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


def search_by_token(token):
    """

    :param token: str - gamma
    :return: list - equation_ids
    """
    eq_list = []
    for roots, dirs, files in os.walk(DATA_FOLDER):
        # skip the math root
        if roots.split("/")[-1].isnumeric():
            for file in files:
                file_path = roots + "/" + file
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for i in lines:
                        token_i = i.split("  ")[0]
                        if token in token_i:
                            eq_list.append(file.split(".txt")[0])
                            break

    return eq_list
