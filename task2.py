def function(a, b, h, d):
    x = a

    while x <= b:
        y = 0
        k = 1

        while True:
            sum = (1 / (4 * k + 3)) * (x ** (4 * k + 3))
            y += sum

            if abs(sum) < d:
                break
            
            k += 1

        print(f"{x:.2f}  | {y:.6f}")
        
        x += h

a = 0.2
b = 0.3
h = 0.01
d = 1e-6
function(a, b, h, d)