import json
"""with open('data.json') as data_file:
    data_item = json.load(data_file)"""

data_item = json.load(open("data.json"))

def find(word):
    words = data_item.keys()
    word = word.lower()           #case sensitive word eliminate
    if word in words:
        return data_item[word]
    else:
        return "Word you enter does not exist please recheck"

word = input("Please enter a word : ")
print(find(word))
