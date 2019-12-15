'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word: str):
    if len(word) < 2: # if word is less than 2 characters, return 0 occurrences
        return 0
    elif word.find('th') != -1: # if occurrence of 'th' found, grab the index, set count to 1 and recall function passing in the remaining characters of word to be checked
        index_of_occurrence = word.find('th')
        count = 1
        return count + count_th(word[index_of_occurrence + 2:]) # +2 because .find() finds inital index of substring and 'th' is two characters long
    else: # No occurrences were found
        return 0






