# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
# count the number of ways it can be decoded.
#
# For example, the message '111' would give 3,
# since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable.
# For example, '001' is not allowed.

def decode(encoded, index=0):

    if index == len(encoded):
        return 1
    elif index > len(encoded):
        return 0

    firstTwoCars = int(encoded[index:index+2])
    #print(index , firstTwoCars)
    return decode(encoded, index + 1) + (decode(encoded, index + 2) if firstTwoCars <= 26 else 0)

# print(decode('111'))
# print(decode('12626'))


from collections import defaultdict

def num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    # empty char - single char can be done in 1 ways
    cache[len(s)] = 1

    for i in range(len(s) - 1, -1, -1):
        currentInt = int(s[i])
        if currentInt == 0:
            return 0
        elif currentInt < 3:
            cache[i] = cache[i + 1] + cache[i + 2]
        else:
            cache[i] = cache[i + 1]
            
    return cache[0]

print(num_encodings('111'))
print(num_encodings('12626'))
