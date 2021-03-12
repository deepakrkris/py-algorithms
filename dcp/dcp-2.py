# Given an array of integers,
# return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

def listOfProducts_exclude_currentIndex(list):
    totalProduct = 1
    for x in list:
        totalProduct *= x

    result = []
    for x in list:
        result.append(int(totalProduct/x))

    return result

print(listOfProducts_exclude_currentIndex([1, 2, 3, 4, 5]))
print(listOfProducts_exclude_currentIndex([3, 2, 1]))
