# pick one random key from hiragana2.json
# pick three random keys from hiragana2.json
    # if current_key in all_keys:
        # choose another random key
# prompt user for answer
# if answer == correct["english]:
    # print("Thats pretty correct.")
# else:
    # print("Thats not right")
import random, json, time


def get_data(file_name):
    """Loads the data from a .json file

    The passed in .json file is used to load in all of the information from 
    said file and then cast into a list so that the information can be worked
    with in either it's raw form or in a form that asks for a list.

    Args:
        file_name: The .json file that contains the information that needs to 
            be loaded

    Returns:
        Returns a tuple containing the entire data that was loaded in from the
            .json file and the data from the .json file but cast into a list
            to work easily with other functions
    """

    data = {}
    with open(file_name, "r") as f:
        data = json.load(f)
        
    # turn the data into a list for later use
    list_data = list(data)
    return (data, list_data)


def get_random_character(all_characters, current_choices):
    """Chooses a random character from the character set that was passed in.

    A Japanese character set is passed in along with the choices tha have already
    been chosen in the past. The function will randomly choose a character from the
    set and if has already been chosen in the past then it will choose another 
    character at random. Once it has found a character that it has not seen before 
    then it will return that choice.

    Args:
        all_characers: A list of all the characters in the character set
        current_choices: A list of characters that have already been chosen

    Returns:
        A random character that was chosen from a list of Japanese characters
    """

    # choose random from the dictionary
    # if the choice is in the current_choices then pick another one
    choice = random.choice(all_characters)

    while(choice in current_choices):
        choice = random.choice(all_characters)
    
    return choice


def get_choices(list_data):
    """Gets the choices to fill a questions.

    A multiple choice question is created in this function. It will loop through
    four(4) times and call the get_random_character() function, it will then add
    that choice to the choices list. Once the four choices (A, B, C, D) have been
    chosen then it will return the list of potential answers.

    Args:
        list_data: The data of the entire character set that is being sed in list form
    
    Returns:
        This returns a list of all four of the choices that have been chosen for 
            the question.
    """

    choices = []
    for iteration in range(4):
        choice = get_random_character(list_data, choices)
        choices.append(choice)

    return choices


def format_question(data, choices, number_of_attempts):
    """Formats the questions to be presented to the user.

    Returns either True or False. True is the user got the answer correct, False is 
    the user got the answer wrong.

    Args:
        data: The data of the entire character set that is being used in dictionary form
        choices: The four choices that the user has to guess from
        number_of_attempts: The amount of attempts that the user has to get the questions
            right in integer form
    
    Returns:
        A boolean that says if the user has gotten the correct answer within the alotted
            amount of retries.
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
    """This creates a quiz for the user to take.

    You've only got one shot at getting these answers right. Good luck.

    Args:
        number_of_questions: The number of questions that the user will be answering
            in integer form
        data: The data of the entire character set that is being used in dictionary form
        list_data: The data of the entire character set that is being sed in list form

    Returns:
        None
    """

    total_score = 0
    for question in range(number_of_questions):
        all_choices = get_choices(list_data)
        result = format_question(data, all_choices, 1)

        if result:
            total_score = total_score + 1
    
    print("You've gotten {}/{}".format(total_score, number_of_questions))


def time_attack(total_time, data, list_data):
    """A time attack choice for the user to use.

    If the user would like to test their might and see how many questions that they 
    can complete correctly in a set amount of time then the user would choose this
    option.
    One shot at each question. You set the timer. We keep score. Ready. Set. Go.

    Args:
        total_time: The total amount of time in second that the user has to complete 
            the trial in integer form
        data: The data of the entire character set that is being used in dictionary form
        list_data: The data of the entire character set that is being sed in list form

    Returns:

    """

    total_score = 0
    number_of_questions = 0
    start = time.time()
    elapsed_time = 0
    while elapsed_time < total_time:
        all_choices = get_choices(list_data)
        result = format_question(data, all_choices, 1)

        if result:
            total_score = total_score + 1
        number_of_questions = number_of_questions + 1
        elapsed_time = time.time() - start
    
    print("Times up. You've gotten {}/{}".format(total_score, number_of_questions))


def questions_controller(character_set_choice):
    """The controller for the questions.py script

    This is the main controller for this script. It prompts the user of the functions 
    that this script is capable of and properly works with the user's response.

    Args:
        character_set_choice: The choice of which character set that was chosen in string
            form.
    
    Returns:
        None
    """

    # I need both the original dictionary and the list version
    # one is for input checking, the other is for random.choice
    print("Would you like to do a 20 questions quiz or a time attack for 30 seconds?")
    print("Enter 1 for quiz, 2 for time attack")
    test_type_choice = input()
    # print("Enter 1 for Hiragana, 2 for Katakana")
    # character_set_choice = input()
    if character_set_choice == "1":
        file_name = "character_sets/hiragana2.json"
    elif character_set_choice == "2":
        file_name = "character_sets/katakana2.json"
    else:
        file_name = ""
        print("Sorry. I do not recognize that file. Going to Main Menu.")

    if file_name:    
        data, list_data = get_data(file_name)

        if test_type_choice == "1":
            quiz(20, data, list_data)
        elif test_type_choice == "2":
            time_attack(30, data, list_data)

    print("Ending now.")


if __name__ == "__main__":
    questions_controller("1")
