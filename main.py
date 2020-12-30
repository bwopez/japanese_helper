from game_modes import katakana, hiragana


def get_input():
    print("""Press 'q' to quit. Otherwise we will show your input.
    1) Katakana
    2) Hiragana
    """)
    user_input = input()

    while len(user_input) > 1:
        print("Please only use one(1) character.")
        user_input = input()

    return user_input


def game():
    choice = get_input()

    while choice != "q":
        print("Your input was: " + choice)
        if choice == "1":
            katakana()
        elif choice == "2":
            hiragana()

        choice = get_input()

    print("Thank you for playing. Mata ne~")


if __name__ == "__main__":
    game()