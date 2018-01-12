from copy import deepcopy

def add(x, y):
    """Basic addition operator."""
    return x+y

def sub(x, y):
    """Basic subtraction operator."""
    return x-y

def mult(x, y):
    """Basic addition operator."""
    return x*y

def div(x, y):
    """Divide-by-zero safe division operator."""
    if y==0: # Defaults to addition/subtraction, since division is illegal
        return x # Might need to edit of an actual solution is desired
    return x/y

def isSolvable(nums):
    """Determines if an input list of numbers can be used to make 24."""
    length = len(nums)
    if length < 1:
        return False # This should not
    if length == 1:
        return nums[0] == 24 # Base case
    # Will only continue if there are 2 or more numbers
    funcs = [add, sub, mult, div]
    for i in range(length):
        for j in range(i+1,length):
            firstNum = nums[i]
            secondNum = nums[j]
            # Create a copy of the available numbers with two missing
            numsCopy = nums[:i] + nums[i+1:j] + nums[j+1:]
            # Permute the result
            for f in funcs:
                optionA = f(firstNum, secondNum)
                optionB = f(secondNum, firstNum)
                resultA = isSolvable(numsCopy + [optionA])
                resultB = isSolvable(numsCopy + [optionB])
                if resultA or resultB:
                    return True
    # Will only continue if no solution was found
    return False
