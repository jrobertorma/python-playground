# How to find the highest value in an array of int numbers?
# We can store the big number so far and compare it with the next values, and so on
# If the new value is bigger than the current we replace it, if it doesn't we don't do anything

def findHigherNumber(numbersList) :
    highestNumber = 0
    for number in numbersList :
        if highestNumber < number :
            highestNumber = number
    return highestNumber

# Notice the 'None' keyword, is used to indicate emptiness, so we can know if is the first iteration of the loop
# we also can use the 'is' operator, it's like an '==' operator but 'stronger' because checks for type and value
# 'is not' is also a logical operator, obviously, if you have a clean dataset '==' is good enough 
def findSmallestNumber(numbersList) :
    smallestNumber = None
    for number in numbersList :
        if smallestNumber is None or number < smallestNumber :
            smallestNumber = number
    return smallestNumber

numbers = [12, 22, 44, 77, 5, 6, 1, 33, 71, 11]
print ("Numbers list:",numbers)
print ("Highest number:",findHigherNumber(numbers))
print ("Smallest number:",findSmallestNumber(numbers))