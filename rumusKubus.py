print("\n")
print('      "Menghitung Luas dan Volume Kubus" by Hekaa')
print("\n")
print("Tulis sisi yang diketahui")

sisi = int(input("ketik sisinya :"))
volume = sisi**3
luasP = 6 * sisi**2     

def myFunction():
    
    if(sisi > 0):
        print(f"Volume kubus adalah : {volume} cm^3")
        print(f"Luas Permukaan Kubus adalah : {luasP} cm^3")
    elif(sisi == 0):
        print("masukan kode dengan benar")
    elif(sisi < 0):
        print(f"Volume kubus adalah : {volume} cm^3")
        print(f"Luas Permukaan Kubus adalah : {luasP} cm^3")
    
myFunction()