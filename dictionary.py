import json
from difflib import get_close_matches

def print_def(word):
    english_dictionary = json.load(open("english_dictionary.json"))

    if word in english_dictionary:
        return english_dictionary[word]
    elif word.title() in english_dictionary: 
        return english_dictionary[word.title()]
    elif word.lower() in english_dictionary:
        return english_dictionary[word.lower()]
    elif word.upper() in english_dictionary: 
        return english_dictionary[word.upper()]
    elif len(get_close_matches(word, english_dictionary.keys())) > 0:
        closest = input("Did you mean %s? Enter Y/N (yes/no)" % get_close_matches(word, english_dictionary.keys())[0])
        if closest == "Y":
            return english_dictionary[get_close_matches(word, english_dictionary.keys())[0]]
        elif closest == "N":
            return "The word you're looking for does not exist"
    else:
        return "The word you're looking for does not exist"


if __name__ == '__main__':
    word = input("Enter word: ")
    definition = print_def(word)
    print(definition)