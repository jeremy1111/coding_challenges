#This function finds out if an integer is a prime number

def PrimeTime(num):
    if type(num) != int or num <= 0:
        return 'number must be positive integer'
    elif num == 1:
        return 'false'
    elif num == 2 or num == 3:
        return 'true'
    else:
        for x in range(2, num - 1):
            if num%x == 0:
                isPrimeNumber = 'false'
                break
            else:
                isPrimeNumber = 'true'
        return isPrimeNumber
