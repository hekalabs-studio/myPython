import math 
print("\n      *Mencari Keliling & Luas Lingkaran* by Hekaa")

print('\n[Masukan nilai "0" jika salah satu nilai tidak diketahui!]')
iDiameter = int(input("Masukan nilai Diameter (cm) : "))
iJari2 = int(input("Masukan nilai Jari2 (cm) : "))

oDiameter = float(iJari2 * 2)
oJari2 = float(iDiameter / 2)



def Perhitungan():
   if iDiameter == 0:
      Keliling = int(2 * math.pi * iJari2)
      Luas = int(math.pi * iJari2**2)
      print(f"\nDiameternya adalah : {oDiameter} cm" )
      print(f'Keliling Lingkaran Adalah : {Keliling} cm' )
      print(f'Luas Lingkaran Adalah : {Luas} cm²' )
   elif iJari2 == 0:
      Keliling = int(2 * math.pi * iDiameter/2)
      Luas = int(math.pi * iDiameter/2 **2)
      print(f"\nJari-jarinya adalah : {oJari2} cm"  )
      print(f'Keliling Lingkaran Adalah : {Keliling} cm' )
      print(f'Luas Lingkaran Adalah : {Luas} cm²' )
   else:
      print('"Eror" jangan isi salah satu')
      

Perhitungan()
print("\n")


