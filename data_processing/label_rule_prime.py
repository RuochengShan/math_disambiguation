from util.search_equ import search_by_token, search_by_id
from util.alter_label_text import alter_label

data_list = search_by_token("\prime", mode=0)
#data_list2 = search_by_token("'", mode= 0)

# check if prime following "^"
def get_all_index_of_a_token(token_list, token):
    index_list = []
    for i in range(len(token_list)):
        if token_list[i] == token:
            index_list.append(i)
    return index_list


def following_caret(token_list, token_index):
    if token_list[token_index-1] == "^":
        return True


f = []
for i in data_list:
    tokens, labels = search_by_id(i)
    index_list = get_all_index_of_a_token(tokens, "\prime")
    for j in index_list:
        if following_caret(tokens, j):
            f.append(i)
            break

pass
