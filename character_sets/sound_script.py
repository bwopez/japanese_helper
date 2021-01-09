import os, json, pyperclip, time
from gtts import gTTS
from playsound import playsound


def play_sound(file):
    """Plays an audio file.

    Plays the audio file that is passed in.

    Args:
        file: The audio file that should be played
    
    Returns:
        None
    """

    for i in range(3):
        playsound(file)
        time.sleep(.8)


def create_sound(character, directory):
    """Creates an .mp3 file

    Japanese characters are passed into the function and are sent through
    Google Text to Speech and an .mp3 file is created.

    Args:
        character: The japanese characters written in utf-8
        directory: The directory where the temporary sound file will be 
            saved

    Returns:
        The relative file name of the temporary sound file
    """

    # mytext="\u3048"
    mytext = character
    language = "ja"
    myobj = gTTS(text=mytext, lang=language, slow=True)
    file_name = os.path.join(directory, "sounds/temporary_sound.mp3")
    # file_name = "{}\\sounds\\temporary_sound.mp3".format(directory)
    myobj.save(file_name)

    return file_name


def delete_sound(file_name):
    """Delete the sound file that was passed in

    Deletes the temporary sound file.

    Args:
        file_name: The file name of the file that you want to delete

    Returns:
        None
    """

    print("Attempting to delete temporary .mp3")
    # added a little something so that you can't just delete any random file
    if os.path.exists(file_name) and "temporary_sound.mp3" in file_name:
        print("Found file. Deleting temporary .mp3")
        os.remove(file_name)
    else:
        print("File not found.")


def get_english_sound(character):
    """A function that helped with getting the pronunciation of Japanese characters

    This function was created so that it would loop through every character that was in 
    a .json file and ask the user what sound it was making and spell it out in english.

    Args:
        character: The current Japanese character to work with
    
    Returns:
        The english phonetical spelling of the sound that was just heard
    """

    directory = os.path.dirname(os.path.realpath(__file__))
    file_name = create_sound(character, directory)
    # if needed, go to google and paste character into google translate
    # for repeated sound
    pyperclip.copy(character)

    print(character)
    print("What sound does this character make? ")
    print("If you need to hear again, you can paste directly to google translate.")
    play_sound(file_name)
    input_character = input()
    # delete_sound("sounds\\temporary_sound.mp3")
    delete_sound(file_name)
    # print("This sounds like '{}'".format(input_character))

    return input_character


if __name__ == "__main__":
    # character_controller("\u3041")
    print("Which file would you like to use?")
    main(input())
    print("Thank you. Mata ne~")
