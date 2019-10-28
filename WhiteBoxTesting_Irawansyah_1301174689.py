import math
input1 = (float(input("Masukkan sisi segitiga : ")))
input2 = (float(input("Masukkan sisi segitiga : ")))
input3 = (float(input("Masukkan sisi segitiga : ")))
a = round(input1)
b = round(input2)
c = round(input3)
if (a<=0 or a==0 or b<=0 or b==0 or c<=0 or c==0):
	print("segitiga tidak bisa dibuat")
elif (a==b and b==c):
	print("segitiga sama sisi")
elif (a==b or b==c or a==c):
 	print("segitiga sama kaki")
elif (a>=b+c or b>=a+c or c>=a+b):
	print("segitiga tidak bisa dibuat")
elif (a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2):
	print("segitiga siku siku")
elif (a<b+c or b<a+c or c<a+b):
	print("segitiga bebas")