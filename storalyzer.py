import string
from pprint import pprint

from story_sama import gen_story
import re
from collections import Counter

while True:
    start = input("Are yo sure yo wanna do this? Type yosh to proceed, no is not an option but yo can try 😒:")

    if start.lower() == "yosh":
        print("okie, here we goooo~ 🐱‍🏍")


        topic = input("Give topic, get cool story 👻->")


        story = gen_story(topic)

        word_count = len(re.findall("[a-zA-Z_]+", story))


        occurrences = Counter(story)


        alphabet = string.ascii_lowercase
        alphabet_occurrences = {letter: story.lower().count(letter) for letter in alphabet}


        info_dump = {
            "yo story": story,
            "word count": word_count,
            "being a bit extra and counting evewything": occurrences,
            "alphabet occurrences": alphabet_occurrences
        }

        pprint(info_dump, width=100, depth=5)

        print("AAAAAAAAAND, THE SHOW IS OVAH! 🥳🙀")

        break
    else:
        print("Yo can't escape write yosh 🐱🔫")

