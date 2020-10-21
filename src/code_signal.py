"""PROBLEM#5
"""


# your given two strings (a,b)
# want to map every char in string a to to every char in b so that a becomes b

# plan
# iterate over a and somehow conver the chars to b -> save char a as keys into a hash map
# this hash map will has values of b
# once a key has been saved then we can no longer update the hash map
# iterate over a, and replace every char in in a to its value ,based on our dict
# check if  a == b
def csIsomorphicStrings(a, b):
    dictionary = {key: value for key, value in zip(a, b)}
    temp = list(a)
    if len(a) > len(b) or len(b) > len(a):
        print(len(a), len(b))
        return False
    for index, char in enumerate(temp):
        temp[index] = dictionary[char]
    if temp != list(b):
        return False
    else:
        return True


# were given a pattern
# we want to check if a emulates that pattern
# plan
# split the string  by spacing so we get all the words in the sentence a
# create hash map/dictionar1 that keeps that assigns every char in pattern to every word
# create another hashmap/dictionary2 that assigns every word to one char
# iterate over all the words(list a) get the value associated to each word based on dict(second one)
# if the word at index i is not equal to pattern[i] then return False

"""PROBLEM# 5"""


def csWordPattern(pattern, a):
    words = a.split()
    check = {}
    if len(a.split()) < len(list(pattern)):
        return False
    for key, value in zip(words, pattern):
        # this makes sure that every letter in pattern is only associated with one word
        if value not in check:
            check[value] = key
    dictionary = {key: value for key, value in zip(words, pattern) if check[value] == key}
    # makes sure that every word is associated with only one letter in the patter
    for index, word in enumerate(words):
        if word in dictionary and dictionary[word] == pattern[index]:
            # whenever we have a word that is not mapped to any letter in the pattern we will return false
            continue
        else:
            return False
    return True


pattern = "abba"
a = "lambda school school lambda"
csWordPattern("abba", a)

"""PROBLEM#6"""


# were given an array of strings
# want to group anagrams together
# we also want these groups to be sorted by greatest to least

# plan
# create a dicitonary with keys associated to the strings
# check words/strings if they pertain to a key in a dicitonary then
# update the dicitonary by appending the value(a list) with the string
# this dicitonary key will correspond to the a sorted list version of every string for the given array
# I can do this by splitting the string, sorting and treating it as a key
# when a is in the dict true, update the dict

def csGroupAnagrams(strs):
    dictionary = {}
    srt = []
    for word in strs:
        dictionary[''.join(sorted(word))] = []
        print(dictionary)
    for word in strs:
        organized = ''.join(sorted(word))
        if organized in dictionary:
            dictionary[organized].append(word)

    for key, value in dictionary.items():
        srt.append(value)
    return sorted(srt, reverse=True)


# Input:
# strs = ["apt","pat","ear","tap","are","arm"]
#
# Output:
# [["apt","pat","tap"],["ear","are"],["arm"]]

strs = ["ear", "tap", "are", "arm", "apt", "pat"]
print(csGroupAnagrams(strs))
