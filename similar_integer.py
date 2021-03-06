#This function finds the number of similar integers given an integer as parameter

from collections import Counter

def no_of_similar_integers(N):
    if N < 0 or type(N) != int:
        print('Number cannot be negative and must be an integer')
    elif N == 0 and type(N) == int:
        return 1
    else:
        listOfDigits = [int(digits) for digits in str(N)]
        noOfNonzeros = sum(elements > 0 for elements in listOfDigits)
        dictOccurrences = dict(Counter(listOfDigits))
        listOccurrences = list(dictOccurrences.values())
        facts = 1
        for noOfOccurrences in listOccurrences:
            if noOfOccurrences > 1:
                facts = facts * factorial(noOfOccurrences)
        noOfSimilarInts = noOfNonzeros * factorial(len(listOfDigits) - 1) / facts
        return int(noOfSimilarInts)

#This is a recursive helper function to calculate the factorial
def factorial(N):
    if N > 0:   
        N = N * factorial(N - 1)
    else:
        N = 1
    return N
