# 1) Create a function that prints/logs all the integers from 1 to 20.
def print1to20():
    for i in range(1, 21):
        print(i)

# 2) Create a function that prints/logs all the odd numbers from 3 to 20.
def printOdd3to20():
    for i in range(3,20, +2):
        print(i)
 
#  3) Create a function that prints/logs all the even numbers from 4 to 22.
def printEven4to22():
    for i in range(4, 23, +2):
        print(i)

# 4) Print/log all the multiples of 7 between the numbers 7 to 62.
def multiplesof7():
    for i in range (1, 62, +1):
        if i % 7 == 0:
            print(i)

# 5) Log positive numbers starting at 50, counting down by fives (exclude 0).
def countdownByFives():
    for i in range(50,1,-5):
        print(i)

#6)Given an array, print/log the sum of the first value in the array, plus the array’s length. Assume that the array is composed of numbers
def firstPlusLength(arr):
    sum = arr[0] + len(arr)
    print(sum)

#7) Create a function that prints/logs all the even numbers from 4 to 22. Have it also return the sum of all the numbers that were printed.
def printEven4to22():
    sum = 0
    for i in range(4, 24, +2):
        sum = sum + i
        print(i)
    return(sum)

#8) Add odd integers from -25,000 to 30,000 and have the function return its final sum. Is there a short cut?
def addOddInts():
    sum = 0
    for i in range(-25000, 30000,1):
        if i % 2 != 0:
            sum = sum + i
    return(sum)

#9) Given an array, write a function that prints/logs each number in the array.
def printArray(arr):
    for i in arr:
        print(i)

#10) Given an array, write a function that only prints/logs its positive value. For example printPositives([-1,3,-5, 10]) prints/logs 3, 10.
def printPositives(arr):
    for i in arr:
        if i > 0:
            print(i)

#11) Given an array, write a function that prints the index value of its positive values. For example printPositiveIndex([1, 3, -10]), have it print/log 0, 1 
# (as the 0th index had a positive value and index 1 also had a positive value). printPostiiveIndex([10, 5, -5, 15]) should print/log 0, 1, and 3. In other words, 
# it prints the index of each positive number in the array.
def printPositiveIndex(arr):
    for i in range(len(arr)):
    if arr[i] > 0:
        print(i)

#12) Given an array, write a function that returns a new array where each negative value was converted to a positive value. For example, bePositive([-1,-3,-5]) returns [1, 3, 5]. 
# A positive number in the original array should remain as positive, so that each number in the new array is all positive.
def bePositive(arr):
    for i in range(len(arr)):
        if i < 0:
            i = i*-1
            print(i)

#13) Given an array with multiple values, write a function that replaces each value in the array with the product of the original value multiplied by itself. 
# For example squareVal( [1, 3, 5] ) should return [1, 9, 25].
def squareVal(arr):
    new =[]
    for i in arr:
        new.append(i*i)
    return(new)