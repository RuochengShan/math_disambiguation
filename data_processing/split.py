from util.path import ALL_TOKEN, DATA_FOLDER
import os
with open(ALL_TOKEN, "r", encoding="utf-8") as f:
    data = f.readlines()
    for i in data:
        id_ = i.split("  ")[0]
        chapter = id_.split(".")[0]
        chapter_dir = DATA_FOLDER + '/' + chapter
        if not os.path.isdir(chapter_dir):
            os.makedirs(chapter_dir)

        # last char is ",\n", remove from tokens
        eq_token = i.split("  ")[1].split("。")[:-1]
        if len(eq_token) >= 15:
            tokens, labels = [], []
            for j in eq_token:
                tokens.append(j)
                labels.append("O")

            new_file = open(chapter_dir + "/" + id_ + ".txt", "w")
            for index in range(len(tokens)):
                new_file.write(tokens[index] + "  " + labels[index] + "\n")
            new_file.close()

