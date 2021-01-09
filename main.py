from questions import questions_controller
from kanji import kanji_controller


def get_input():
    """Gets user's input

    Asks for user input and makes sure that the input is within the 
    available choices.

    Args:
        None
    
    Returns:
        A string of what the user has entered, even when it is only a 
            int.
    """

    print("""Press 'q' to quit. Otherwise we will show your input.
    1) Katakana
    2) Hiragana
    3) Kanji-A-Day
    q) Quit
    """)
    user_input = input().lower()
    available_choices = ["1", "2", "3", "q", "quit"]

    while user_input not in available_choices:
        print("Please only answer with '1', '2', '3', or 'q'")
        user_input = input().lower()

    return user_input


def game():
    """The main menu for the program

    The main controller for the entire program.

    Args:
        None

    Returns:
        None
    """

    choice = get_input()

    while choice != "q" and choice !="quit":
        if choice == "3":
            kanji_controller()
        else:
            questions_controller(choice)

        choice = get_input()

    print("Thank you for playing. Mata ne~")


if __name__ == "__main__":
    game()