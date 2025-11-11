import math

def f(x):
    return math.sin(x)

a = 1.0
h = 0.1
print("h degeri          turev degeri    hata payi")
for i in range(14):
    f1 = (f(a + h) - f(a)) / h
    print(f"{h:.12f}\
    {f1:.10f}\
    {abs(math.cos(a) - f1):.10f}") # Hata payini mutlak degerini alarak gosterdim
    h = h / 10.0
