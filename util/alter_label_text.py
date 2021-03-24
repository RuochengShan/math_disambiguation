from util.path import DATA_FOLDER


def alter_label(eq_id, token_index, new_label):
    # get eq file path
    chapter = eq_id.split(".")[0]
    file_path = DATA_FOLDER + chapter + "/" + eq_id + ".txt"

    # read old file, clear old file
    with open(file_path, "r+", encoding="utf-8") as f:
        tokens = []
        labels = []
        lines = f.readlines()
        for line in lines:
            tokens.append(line.split("  ")[0])
            labels.append(line.split("  ")[1].strip())

        f.truncate(0)

    # open same file
    new_file = open(file_path, "w")

    # replace label
    labels[token_index] = new_label

    # write file
    for i in range(len(tokens)):
        new_file.write(tokens[i] + "  " + labels[i] + "\n")
    new_file.close()
