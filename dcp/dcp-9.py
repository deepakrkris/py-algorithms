# Given a list of integers,
# write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
#
# For example,
# [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?

def largestSumNumbers(list, sum=0, index=0):
    if index >= len(list):
        return sum

    return max(largestSumNumbers(list, sum, index + 1),
                    largestSumNumbers(list, sum + list[index], index + 2))


def largestSumWithCache(list):
    maxSum = [list[0]]
    maxSum.append(max(maxSum[0], list[1]))

    for i in range(2, len(list)):
        maxSum.append(max(maxSum[i-1], (maxSum[i-2] + list[i]), list[i]))

    return maxSum[len(list) - 1]

print(largestSumNumbers([2, 4, 6, 2, 5]))
print(largestSumNumbers([5, 1, 1, 5]))
print(largestSumNumbers([-1, -1, 1, -1, -1, 5]))

print(largestSumWithCache([2, 4, 6, 2, 5]))
print(largestSumWithCache([5, 1, 1, 5]))
print(largestSumWithCache([-1, -1, 1, -1, -1, 5]))

