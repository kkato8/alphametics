# Date: 06/23/20
# Author: Ken Kato
# Reference: https://github.com/diveintomark/diveintopython3/blob/master/examples/alphametics.py
# Description: solve a alphametrics
# Please provide arguments in the form below
# "[A-Z][A-Z]* [+,-,*,/] [A-Z][A-Z]* == [A-Z][A-Z]*

import re
import itertools

def solve(alphametics):
    print(alphametics)
    alist = re.findall("[A-Z]+", alphametics)
    words = [word for word in alist]
    first = set(word[0] for word in words) # first character of each word
    num = len(first) # number of unique first characters
    string = list("".join(words))
    unique = set(string)
    if len(unique) > 10: # checks if number of characters are more than the numbers [0,1,2,3,4,5,6,7,8,9]
        return "There are too many letters"
    order = "".join(first) + "".join(unique - first) # prevents from having a 0 at the begging of each number 
    for guess in itertools.permutations("0123456789", len(unique)):
        if "0" not in guess[:num]:
            guess = "".join(guess) 
            seed = str.maketrans(order, guess)
            arithmetic = alphametics.translate(seed) # replace each character with integers
            if eval(arithmetic):
                return arithmetic

if __name__=='__main__':
    import sys
    for alphametics in sys.argv[1:]:
        if isinstance(alphametics, str):
            solution = solve(alphametics)
            print(solution)
        else:
            print("Please provide arguments as string")
