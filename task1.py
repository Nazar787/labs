import math

# Визначення початкових значень
x = 2
end = 4
step = 0.2

print(" x     |     y")
print("----------------")

# Цикл для табулювання
while x <= end:
    if x < 2.5:
        y = math.cos(math.log(x**2))
    elif 2.5 <= x <= 3.5:
        y = 1 / math.cos(x**4)  # sec(x) = 1 / cos(x)
    else:
        y = math.tan(math.sin(x))
    
    # Виведення результатів
    print(f"{x:.2f}  | {y:.4f}")
    
    # Збільшення x на 0.2
    x += step