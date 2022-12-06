class Variable:
    def __init__(self,data):
        self.data = data

import numpy as np

data = np.array(1.0)
x = Variable(data)
print(x.data)

class Function:
    def __call__(self, input):
        x = input.data # 데이터를 꺼낸다.
        y = x ** 2 # 실제 계산
        output = Variable(y)
        return output

x = Variable(np.array(10))
f = Function()
y = f(x)

print(type(y))
print(y.data)