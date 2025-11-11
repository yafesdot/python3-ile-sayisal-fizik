import math

def simpson(a, b, n, f):
    """
    Simpson yontemiyle belirli integralin hesaplanmasi
    """
    if n <= 1 or a > b:
        print("Hatali veri!")

    if n % 2 == 1:
        print("N sayisi cift degil.")

    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        coeff = 2 if i % 2 == 0 else 4 # ternary for fun
        s += coeff * f(x)

    return s * h / 3

def f(x):
    """Analiz edebilmek için ornek bir fonksiyon"""
    return math.sin(x)

a = 0
b = 1
n = 1000

result = simpson(a, b, n, f)
print(f"{result:.6f}")
