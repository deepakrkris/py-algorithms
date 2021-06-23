#
#  4 - 1 = 3
#  4 - 2 = 2
#  3 - 1 = 2
#  3 - 2 = 1
#  2 - 1 = 1
#  2 - 2 = 0
#  1 - 1 = 0

# O(2^N)
def staircase(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    return staircase(n-1) + staircase(n-2)

print(staircase(4))

def staircaseDyn(n):
    cache = [0 for _ in range(n + 1)]
    cache[1] = 1
    cache[0] = 1

    for i in range(2, n+1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n]

print(staircaseDyn(4))

def staircaseGeneric(n, X):
    if n==0:
        return 1
    elif n < 0:
        return 0
    return sum([staircaseGeneric(n-x, X) for x in X])

print(staircaseGeneric(4, [1, 2, 3]))

def staircaseGenericDyn(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[1] = 1
    cache[0] = 1

    for i in range(2, n+1):
        cache[i] = sum([cache[i - x] for x in X if i - x >= 0])

    return cache[n]

print(staircaseGenericDyn(4, [1, 2, 3]))