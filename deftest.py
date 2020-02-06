def ifprime (numberToCheck) :
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0):
            return False
    return True

answer = ifprime(9999999967)

print(answer)