from functools import reduce

def add(x, y):
    return x + y

def new_list(x, y):
    x.append(y ** y)
    return x

print(reduce(add, [2, 4, 7, 3]))
print(reduce(new_list, [2, 4, 7, 3], []))
