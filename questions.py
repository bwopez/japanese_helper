# pick one random key from hiragana2.json
# pick three random keys from hiragana2.json
    # if current_key in all_keys:
        # choose another random key
# prompt user for answer
# if answer == correct["english]:
    # print("Thats pretty correct.")
# else:
    # print("Thats not right")
import random, json


def get_data(file_name):
    data = {}
    with open(file_name, "r") as f:
        data = json.load(f)
        
    # turn the data into a list for later use
    list_data = list(data)
    return (data, list_data)


def get_random_character(all_characters, current_choices):
    # choose random from the dictionary
    # if the choice is in the current_choices then pick another one
    choice = random.choice(all_characters)

    while(choice in current_choices):
        choice = random.choice(all_characters)
    
    return choice


def get_choices(list_data):
    choices = []
    for iteration in range(4):
        choice = get_random_character(list_data, choices)
        choices.append(choice)

    return choices


def format_questions(data, choices):
    """
    Returns either True or False. True is the user got the answer correct, False is the user got the answer wrong.
    """
    correct_answer = random.choice(choices)
    print("The correct choice is {}".format(data[correct_answer]["english"]))
    print("What noise does this character make: {}".format(correct_answer))
    print("""
  A. {}
  B. {}
  C. {}
  D. {}
    """.format(data[choices[0]]["english"], data[choices[1]]["english"], data[choices[2]]["english"], data[choices[3]]["english"])
    )

    user_input = ""
    for attempts in range(3):
        user_input = input()
        if user_input.lower() == data[correct_answer]["english"].lower():
            print("That is the correct answer")
            return True
        else:
            print("That is the wrong answer. Please try again.")

    return False



def main():
    # I need both the original dictionary and the list version
    # one is for input checking, the other is for random.choice
    data, list_data = get_data("character_sets/hiragana2.json")

    all_choices = get_choices(list_data)
    ending_statement = format_questions(data, all_choices)
    
    print(ending_statement)


if __name__ == "__main__":
    main()
