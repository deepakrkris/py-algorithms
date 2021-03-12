

class DutchFlag:

    def __init__(self, list):
        self.list = list

    def order(self, pivot):

        smaller = 0
        for i in range(len(self.list)):
            if self.list[i] < pivot:
                self.list[smaller], self.list[i] = self.list[i], self.list[smaller]
                smaller += 1
        larger = len(self.list) - 1
        for i in range(len(self.list) - 1, 0, -1):
            if self.list[i] > pivot:
                self.list[larger], self.list[i] = self.list[i], self.list[larger]
                larger -= 1

    def orderSinglePass(self, pivot):

        smaller = 0
        larger = len(self.list) - 1
        index = 0

        while index < larger:
            if self.list[index] < pivot:
                self.list[smaller], self.list[index] = self.list[index], self.list[smaller]
                smaller += 1
                index += 1
            elif self.list[index] > pivot:
                self.list[larger], self.list[index] = self.list[index], self.list[larger]
                larger -= 1
            else:
                index += 1
            #print(index, self.list)


d = DutchFlag([1, 1, 0, 2, 1, 0, 2, 1])
d.orderSinglePass(1)
print(d.list)

d = DutchFlag([0, 2, 1, 0, 2, 1])
d.orderSinglePass(1)
print(d.list)

d = DutchFlag([1, 2, 1, 0])
d.orderSinglePass(1)
print(d.list)