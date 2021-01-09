"""
Kanji-A-Day.com scraper
DONE - use beautifulsoup to scrape the website page
DONE - get 'todays Kanji' with an element of glyph
- get reading too? I'm not sure
DONE - maybe put the glyph into gTTS to get the sound of it if you're freaky
- if you're really freaky then open the stroke order diagram in a dialogue box
- maybe somewhere down the line add this to a calendar thing
"""
import requests, os
from bs4 import BeautifulSoup as bs
from character_sets.sound_script import create_sound, play_sound, delete_sound


def print_path():
    """Prints the current path

    Prints the current location of the current file.

    Args:
        None
    Returns:
        None
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)


def kanji_controller():
    """This is the controller function for the kanji.py file

    The function gets the 'soup' from http://www.kanji-a-day.com/ and extracts 
    today's glyph, plays what it sounds like, and prints what it looks like.

    Args:
        None

    Returns:
        None
    """

    page = requests.get("http://www.kanji-a-day.com/")
    soup = bs(page.content, 'html.parser')

    # grabbing the "glyph" of today's kanji
    glyphs = soup.findAll("div", {"class": "glyph"})
    todays_glyph = glyphs[0]
    todays_glyph_cleaned = todays_glyph.text.strip()
    print("Today's kanji is {}".format(todays_glyph_cleaned))

    # putting glyph into gTTS
    print("Getting pronunciation.")
    directory = os.path.dirname(os.path.realpath(__file__)) + "\\character_sets\\"
    file_name = create_sound(todays_glyph_cleaned, directory)
    play_sound(file_name)
    delete_sound(file_name)

    # getting on-reading

    # getting kun-reading


if __name__ == "__main__":
    print_path()
    kanji_controller()
