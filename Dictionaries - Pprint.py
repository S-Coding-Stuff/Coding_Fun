import pprint

# This program shows how many of each character appear in a message
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
#print(count)
#print(pprint.pformat(count))

# pprint is extremely useful for dictionaries with nested lists or dictionaires
# You can display this text as a string value with pprint.pformat()
# Or also pprint.pprint(someDictionaryValue)
# print(pprint.pformat(someDictionaryValue))