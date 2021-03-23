from util.path import ALL_EQU


def select(x):
    with open(ALL_EQU, "r", encoding="utf-8") as f:
        data = f.readlines()
        n = 0
        id_list = []
        for i in data:
            id_ = i.split("   ")[0]
            eq = i.split("   ")[1]
            if x in eq:
                print(id_)
                id_list.append(id_)
                n += 1
        return id_list


## prime
# x = "'"
# x1 = "prime"
# result = select(x)
# result1 = select(x1)
#
# result2 = list(set(result + result1))
# result2.sort()
# new_file = open("prime" + ".txt", "w")
# for index in range(len(result2)):
#     new_file.write(result2[index] + "\n")
# new_file.close()

## superscript
x = "^"
result = select(x)
new_file = open("superscript" + ".txt", "w")
for index in range(len(result)):
    new_file.write(result[index] + "\n")
new_file.close()