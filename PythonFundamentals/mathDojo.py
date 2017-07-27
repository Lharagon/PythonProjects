class MathDojo(object):

    def __init__(self):
        self.total = 0

    def add(self, *num):
        for number in range(len(num)):
            if type(num[number]) == list or type(num[number]) == tuple:
                for index in num[number]:
                    self.total += index
                     
            else:
                self.total += num[number]
        return self

    def subtract(self, *num):
        for number in range(len(num)):
            if type(num[number]) == list or type(num[number]) == tuple:
                for index in num[number]:
                    self.total -= index
            else:
                self.total -= num[number]
        return self

md = MathDojo()

print md.add(2).add(2,5).subtract(3,2).total

print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).total