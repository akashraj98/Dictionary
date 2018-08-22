import json
import difflib            #this library is used to compare strings
"""with open('data.json') as data_file:
    data_item = json.load(data_file)"""

data_item = json.load(open("data.json"))  #json file containing data of dictionary.

def find(word):
    words = data_item.keys()
    word = word.lower()           #case sensitive word eliminate
    if word in words:             #if word in data_item: can also be used
        return data_item[word]
    elif len(difflib.get_close_matches(word,words,cutoff=0.8))>0:
        yn = input("Did you mean %s(y or n) : "%difflib.get_close_matches(word,words,cutoff=0.8)[0])
        if yn.lower()=='y' or 'yes':
            return data_item[difflib.get_close_matches(word,words,cutoff=0.8)[0]]
        elif yn.lower()== 'n' or 'no':
            return "I cann't find the word, please recheck"
        else:
            return "Sorry,I didn't get you"
    else:
        return "I cann't find the word, please recheck"

word = input("Please enter a word : ")
result = find(word)
if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
