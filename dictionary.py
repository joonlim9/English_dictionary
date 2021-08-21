import json

def print_def(word):
    english_dictionary = json.load(open("english_dictionary.json"))

    if word in english_dictionary:
        return english_dictionary[word]
    else:
        return "The word you're looking for does not exist"


if __name__ == '__main__':
    word = input("Enter word: ")
    definition = print_def(word)
    print(definition)