import math

def trapez(a, b, n, f):
    """
    Trapez yontemiyle belirli integralin hesaplanmasi
    """
    if n <= 1 or a > b:
        print("Hatali veri!")

    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x = a + i * h
        s += f(x)

    return s * h

def f(x):
    """Analiz edebilmek için ornek bir fonksiyon"""
    return math.sin(x)

a = 0
b = 1
n = 1000

result = trapez(a, b, n, f)
print(f"{result:.6f}")
