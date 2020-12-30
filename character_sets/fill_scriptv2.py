import json, pyperclip

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


def printing(file_name):
    fo = open(file_name, "r", encoding="utf8").read()
    pyperclip.copy(fo)
    pasted = pyperclip.paste()
    my_arr = pasted.replace("\r", "").split("\n")

    dictionary = Convert(my_arr)
    json_object = json.dumps(dictionary, indent = 4)
    w_file_name = file_name.replace("_dump.txt", ".json")
    with open(w_file_name, "w") as outfile:
        outfile.write(json_object)
    


if __name__ == "__main__":
    print("What is the file_path")
    printing(input())