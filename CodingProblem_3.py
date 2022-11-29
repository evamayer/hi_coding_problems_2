import re

def split_words(text):
    result = re.split("\.|\?|\,|\-|\'|\"|\!|\:|\;|\ ", text)
    return list(filter(None, result))
    
text = str(input("Please enter some text: "))

print("List of words:", split_words(text))
