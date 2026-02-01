import math

print("\n")
print('  *Menghitung Volume dan Luas Permukaan Tabung/Cylinder* by Hekaa')
print ("\n")
print('"Jika ada nilai yang tidak diketahui ketik dengan "0"')

iDiameter = float(input("Diketahui Diameter : "))
iJari2 = float(input("Diket Jari-jari : "))
iTinggi = float(input("Diket Tinggi :"))
print("\n")

oDiameter = iDiameter /2 
oJari2 = iJari2 * 2


def myFunction():
    if(iDiameter > 0):
        volumeTb = int(math.pi * (iDiameter/2) **2 * iTinggi) 
        luasPTb = int(2 * math.pi * (iDiameter/2) * ((iDiameter/2) + iTinggi))
        print(f"Jari-jarinya : {oDiameter}")
        print(f"Volume tabung adalah : {volumeTb} cm^3")
        print(f"Luas Permukaan tabung adalah : {luasPTb} cm²")
    elif(iJari2 > 0):
        volumeTb = int(math.pi * iJari2 **2 * iTinggi) 
        luasPTb = int(2 * math.pi * iJari2 * (iJari2 + iTinggi))
        print(f"Diamter : {oJari2}")
        print(f"Volume tabung adalah : {volumeTb} cm^3")
        print(f"Luas Permukaan tabung adalah : {luasPTb} cm²")
    else :
        print("kode eror")
        
myFunction()
print("\n")
