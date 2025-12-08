
class calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        try:
            return self.x / self.y
        except ZeroDivisionError:
            print("Please divide by other number instead of zero")



num = calc(2, 0)

print(num.sum())
print(num.mul())
print(num.div())


# add items in the lis

class numbers:
    def __init__(self):
        self.lis = []

    def add_items(self, num):
        self.lis.append(num)


odd = numbers()

odd.add_items(1)
odd.add_items(3)
odd.add_items(5)
print(odd.lis)

even = numbers()
even.add_items(2)
even.add_items(4)
even.add_items(6)
print(even.lis)







