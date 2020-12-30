import os, json, pyperclip, time
from gtts import gTTS
from playsound import playsound


def play_sound(file):
    for i in range(3):
        playsound(file)
        time.sleep(.8)


def create_sound(character):
    """
    BOILERPLATE
    """
    # mytext="\u3048"
    mytext = character
    language = "ja"
    myobj = gTTS(text=mytext, lang=language, slow=True)
    file_name = "sounds/temporary_sound.mp3"
    myobj.save(file_name)

    return file_name


def delete_sound(file_name):
    print("Attempting to delete temporary .mp3")
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("File not found.")


def get_english_sound(character):
    file_name = create_sound(character)
    # if needed, go to google and paste character into google translate
    # for repeated sound
    pyperclip.copy(character)

    print(character)
    print("What sound does this character make? ")
    print("If you need to hear again, you can paste directly to google translate.")
    play_sound(file_name)
    input_character = input()
    delete_sound("sounds/temporary_sound.mp3")
    # print("This sounds like '{}'".format(input_character))

    return input_character


if __name__ == "__main__":
    # character_controller("\u3041")
    print("Which file would you like to use?")
    main(input())
    print("Thank you. Mata ne~")
