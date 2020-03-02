# # Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# # Example: countdown(5) should return [5,4,3,2,1,0]

# def countdown(num):
#     mylist = []
#     for x in range(num, -1, -1):
#         mylist.append(x)
#     return mylist
# print(countdown(5))

# # Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# # Example: print_and_return([1,2]) should print 1 and return 2
# def PNC(b):
#     print(b[0])
#     return b[1]
# print(PNC([1,2]))

# # First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# # Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
# def initNlength(somelist):
#     x = somelist[0] + len(somelist)
#     return x
# print(initNlength([1,2,3,4,5]))

# # Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# # Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# # Example: values_greater_than_second([3]) should return False
def grThanSecond(somelist):
    newlist = []
    if len(somelist) < 2:
        return False
    for x in range(0, len(somelist)):
        if somelist[x] > somelist[1]:
            newlist.append(somelist[x])
    print(len(newlist))
    return newlist

# print(grThanSecond([5,2,3,2,1,4]))
# print(grThanSecond([9]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def thisThat(size, value):
    out = []
    for x in range(0, size, 1):
        out.append(value)
    return out

print(thisThat(4,7))
print(thisThat(6,2))