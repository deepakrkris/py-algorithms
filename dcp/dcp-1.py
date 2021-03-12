# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

def targetSumListElements(target, list):

    diff = {}
    for i in range(len(list)):
        diff[list[i]] = i

    for i in range(len(list)):
        if target-list[i] in diff and diff[target-list[i]] is not i:
            return True

    return False

print(targetSumListElements(10, [3, 4, 5, 6]))
print(targetSumListElements(10, [3, 5, 5, 6]))
print(targetSumListElements(10, [3, 4, 4, 2, 1]))
