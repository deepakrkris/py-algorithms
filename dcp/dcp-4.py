# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

# ex: [  -1, 2, 0, -2 , 1 , 4, -3 ]
# ex: [   3, 2, 0, -2 , 1 , 4, -3 ]
#
#
#


def firstMissingPositiveInteger_linearspace(list):
    s = set(list)
    i = 1
    while i in s:
        i += 1
    return i

print(firstMissingPositiveInteger_linearspace([3, 4, -1, 1]))
print(firstMissingPositiveInteger_linearspace([1, 2, 0]))
print(firstMissingPositiveInteger_linearspace([-1, 2, 0, -2 , 1 , 4, -3]))
print(firstMissingPositiveInteger_linearspace([3, 2, 0, -2 , 1 , 4, -3]))


def firstMissingPositiveInteger(list):

    for index, value in enumerate(list):
        while list[index] != index + 1 and 0 < list[index] < len(list):
            v = list[index]
            list[index], list[v - 1] = list[v - 1], list[index]
            if list[index] == list[v-1]:
                break
    missingNumber = 0
    for index, value in enumerate(list):
        if index + 1 != value:
            return missingNumber + 1
        missingNumber = index + 1
    return missingNumber

print(firstMissingPositiveInteger([3, 4, -1, 1]))
print(firstMissingPositiveInteger([1, 2, 0]))
print(firstMissingPositiveInteger([-1, 2, 0, -2 , 1 , 4, -3]))
print(firstMissingPositiveInteger([3, 2, 0, -2 , 1 , 4, -3]))
print(firstMissingPositiveInteger([3, 2, 3, -2 , 1 , 4, -3]))

