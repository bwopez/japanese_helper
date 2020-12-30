import json
from sound_script import get_english_sound


def format_json():
    """
    from this
    {
        ...
        "\u30a5": "30a5",
        ...
    }
    to this
    {
        "Character": "hiragana/katakana",
        "unicode": "\u3048", (example)
        "english": "he" (example)
    }

    - make a new list of dictionaries
    - read the json into memory
    - iterate through each line of json
    - create new dictionary 
        - 
        [enter key of old dictionary]: {
            "unicode": [enter value of old dictionary],
            "english": [ask user for english sound]
        }
    """
    # get json from input file and format
    print("What will be your input file: ")
    input_file = input()
    with open(input_file, "r") as f:
        data = json.load(f)
        dictionary = {}
        # 'i' represents every key in the old dictionary. A japanese character
        for i in data:
            # get the english sound
            english_sound = get_english_sound(i)
            # if there is no sound then throw it away
            if english_sound == "":
                continue
            dictionary[i] = {
                "unicode": data[i],
                "english": english_sound
            }

    json_object = json.dumps(dictionary, indent = 4)

    # write the json to output file
    print("What will be your output file: ")
    output_file = input()
    with open(output_file, "w") as outfile:
        outfile.write(json_object)


if __name__ == "__main__":
    print("Hello again")
    format_json()