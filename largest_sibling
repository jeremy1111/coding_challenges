#This function returns the largest sibling of an integer. For example,
#if 3947 is given, it will return 9743.

def find_largest_sibling(N):
    if N < 0 or type(N) != int:
        print('Number cannot be negative and must be an integer')
    else:
        listOfDigits = [int(digits) for digits in str(N)]
        sortedListOfDigits = sorted(listOfDigits, key=int, reverse=True)
        largestSibling = int(''.join(str(digits) for digits in sortedListOfDigits))
        return largestSibling
