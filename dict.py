import json
import difflib
"""with open('data.json') as data_file:
    data_item = json.load(data_file)"""

data_item = json.load(open("data.json"))

def find(word):
    words = data_item.keys()
    word = word.lower()           #case sensitive word eliminate
    if word in words:             #if word in data_item: can also be used
        return data_item[word]
    elif len(difflib.get_close_matches(word,words,cutoff=0.8))>0:
        return "Did you mean %s"%difflib.get_close_matches(word,words,cutoff=0.8)[0]
    else:
        return "Word you enter does not exist please recheck"

word = input("Please enter a word : ")
print(find(word))
