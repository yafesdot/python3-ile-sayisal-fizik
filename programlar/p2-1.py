import math

def f(x):
    return math.tan(x)

def f1(x):
    """Birinci Tam Turev"""
    return 1.0 / (math.cos(x) ** 2)

h = 0.001

# tablo basliklari
print(f"{'x':<5}{'İleri Fark':<20}{'Geri Fark':<19}{'Simetrik Fark':<16}{'Tam Türev'}")

for i in range(3):
    x = float(i+1)

    f1_fw = f(x + h) - f(x) / h # ileri fark
    f1_bw = f(x) - f(x - h) / h # geri fark
    f1_cd = f(x + h) - f(x - h) / (2 * h) # simetrik fark

    f1_exact = f1(x) # tam turev

    print(f"{i}\
    {f1_fw:.12f}\
    {f1_bw:.10f}\
    {f1_cd:.10f}\
    {f1_exact:.10f}")