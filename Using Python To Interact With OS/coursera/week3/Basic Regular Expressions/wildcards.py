import re

'''
Character classes are written inside square brackets and let us list the characters we want to match inside of those brackets
'''
print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))

'''
Sometimes we may want to match any characters that aren't in a group. To do that, we use a circumflex inside the square brackets.
'''
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
# print(re.search(r"[^a-zA-Z  \.]", "This is a sentence with spaces."))

print(re.search(r"dog|cat", "I like cats"))
print(re.search(r"dog|cat", "I like dogs"))
print(re.findall(r"dog|cat", "I like both dogs and cats"))

# Repetition Qualifiers

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py[a-z]*n", "Python Programming"))


# The plus character matches one or more occurrences of the character that comes before it.
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))



