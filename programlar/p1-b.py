from decimal import Decimal

toplam_default = 1.0
toplam_decimal = Decimal('1.0')

for i in range(10000):
    toplam_default += 0.00001 # Kitabın gösterdiği Python 3 itibarıyla hatalı olan yöntem
    toplam_decimal += Decimal('0.00001') # Decimal ile istenen sonucun eldesi

print(f"Toplam(Dahili)= {toplam_default} \nToplam(Decimal)= {toplam_decimal}")
