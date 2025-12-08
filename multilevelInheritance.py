
# multi Level Inheritance
class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b

class C(B):
    def __init__(self, a, b, c):
        # A.__init__(self, a)
        B.__init__(self, a, b)
        self.c = c


obj = C(10, 20, 30)
print(obj.a, obj.b, obj.c)


# multiple Inheritance

class ma:
    def __init__(self, m):
        self.m = m

class mb:
    def __init__(self, n):
        self.n = n

class mc(ma, mb):
    def __init__(self, m, n, o):
        ma.__init__(self, m)
        mb.__init__(self, n)
        self.o = o

objMul = mc(40, 50, 60)
print(objMul.m, objMul.n, objMul.o)


