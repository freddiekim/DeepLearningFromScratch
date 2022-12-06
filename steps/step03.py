import numpy as np

class Variable:
    def __init__(self,data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x) # 구체적인 계산은 forward 메서드에서 한다.
        output = Variable(y)
        return output
    def forward(self, x):
        raise NotImplementedError()


class Square(Function):
    def forward(self, x):
        return x ** 2

class Exp(Function):
    def forward(self, x):
        return np.exp(x)

x = Variable(np.array(0.5))
A = Square()
B = Exp()
C = Square()
a = A(x)
b = B(a)
y = C(b)
print(y.data)