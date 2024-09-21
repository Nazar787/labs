import math

x = float(2.361)
y = float(1.149)

expression = (13*x*y) + math.log(x/y) - 17*math.sin(x**2- y)
print(round(expression))