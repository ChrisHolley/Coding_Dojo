# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def bigSize(inputList):
    for x in range(0, len(inputList)):
        if inputList[x] > 0:
            inputList[x] = "big"
    return inputList
print(bigSize([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(fnInput):
    posCounter = 0
    for x in range(0, len(fnInput)):
        if fnInput[x] > 0:
            posCounter += 1
    fnInput[len(fnInput)-1] = posCounter
    print(len(fnInput)-1)
    return fnInput
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(fnInput):
    output = 0
    for x in range(0, len(fnInput)):
        output += fnInput[x]
    return output
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(fnInput):
    output = 0
    for x in range(0, len(fnInput)):
        output += fnInput[x]
    return output / len(fnInput)

print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(fnInput):
    return len(fnInput)
print(length([37,2,1,-9]))
print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(fnInput):
    if fnInput == []:
        return False
    else: 
        output = fnInput[0]
        for x in range(0, len(fnInput)):
            if output > fnInput[x]:
                output = fnInput[x]
    return output

print(minimum([37,2,1,-9]))
print(minimum([]))



# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(fnInput):
    if fnInput == []:
        return False
    else: 
        output = fnInput[0]
        for x in range(0, len(fnInput)):
            if output < fnInput[x]:
                output = fnInput[x]
    return output

print(maximum([37,2,1,-9]))
print(maximum([]))

print("UltAnalysis")

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(fnInput):
    output = {}
    output["sumTotal"] = sum_total(fnInput)
    output["average"] = sum_total(fnInput)
    output["minimum"] = sum_total(fnInput)
    output["maximum"] = sum_total(fnInput)
    output["length"] = sum_total(fnInput)
    return output
print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(fnInput):
    midIndex = int(len(fnInput) / 2)
    print(midIndex)
    temp = fnInput[0]
    for x in range (0, midIndex):
        temp = fnInput[len(fnInput) - 1 - x]
        fnInput[len(fnInput) - 1 - x] = fnInput[x]
        fnInput[x] = temp
    return fnInput
print(reverse_list([37,2,1,-9]))



