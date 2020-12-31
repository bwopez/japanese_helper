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


def format_question(data, choices, number_of_attempts):
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
    for attempts in range(number_of_attempts):
        user_input = input()
        if user_input.lower() == data[correct_answer]["english"].lower():
            # print("That is the correct answer")
            return True
        else:
            print("That is the wrong answer. Please try again.")

    return False


def quiz(number_of_questions, data, list_data):
    """
    You've only got one shot at getting these answers right. Good luck.
    """
    total_score = 0
    for question in range(number_of_questions):
        all_choices = get_choices(list_data)
        result = format_question(data, all_choices, 1)

        if result:
            total_score = total_score + 1
    
    print("You've gotten {}/{}".format(total_score, number_of_questions))


def main():
    # I need both the original dictionary and the list version
    # one is for input checking, the other is for random.choice
    print("Enter 1 for Hiragana, 2 for Katakana")
    user_choice = input()
    if user_choice == "1":
        file_name = "character_sets/hiragana2.json"
    elif user_choice == "2":
        file_name = "character_sets/katakana2.json"
    else:
        file_name = ""
        print("Sorry. I do not recognize that file. Closing program.")

    if file_name:
        data, list_data = get_data(file_name)
        quiz(20, data, list_data)


if __name__ == "__main__":
    main()
