import time
import math

# HEADER
print("=== KONVERSI SUHU By Heka ===")
konversi= ["1. Celcius", "2. Reamur", "3. Farenheit", "4. Kelvin"]

for i in range(len(konversi)):
    print(konversi[i])


# FUNGSI
def celcius_fungsi(nilai) :
    reamur = float(4/5 * nilai)
    farenheit = float(9/5 * nilai + 32)
    kelvin = float(5/5 * nilai +273)
    rumus = {"Reamur" : reamur,
            "Farenheit" : farenheit,
            "Kelvin" : kelvin}
    return rumus

def reamur_fungsi(nilai) :
    celcius = float(5/4 * nilai)
    farenheit = float(9/4 * nilai + 32)
    kelvin = float(5/4 * nilai +273)
    rumus = {"Celcius" : celcius,
            "Farenheit" : farenheit,
            "Kelvin" : kelvin}
    return rumus

def farenheit_fungsi(nilai) :
    reamur = float(4/9 * nilai)
    celcius = float(5/9 * nilai + 32)
    kelvin = float(5/9 * nilai +273)
    rumus = {"Reamur" : reamur,
            "Celcius" : celcius,
            "Kelvin" : kelvin}
    return rumus

def kelvin_fungsi(nilai) :
    reamur = float(4/5 * nilai)
    farenheit = float(9/5 * nilai + 32)
    celcius = float(5/5 * nilai + 273)
    rumus = {"Reamur" : reamur,
            "Farenheit" : farenheit,
            "Celcius" : celcius}
    return rumus



user_input = int(input("\nPilih Mode Konversi yang kalian inginkan : "))

match user_input:
    case 1:
        diket = float(input("Masukan Nilai Celcius yang diketahui : "))
        hasil = celcius_fungsi(diket)
        for key, value in hasil.items():
            print(f"{key} : {value}")

    case 2:
        diket = float(input("Masukan Nilai Reamur yang diketahui : "))
        hasil = reamur_fungsi(diket)
        for key, value in hasil.items():
            print(f"{key} : {value}")
    case 3:
        diket = float(input("Masukan Nilai Farenheit yang diketahui : "))
        hasil = farenheit_fungsi(diket)
        for key, value in hasil.items():
            print(f"{key} : {value}")
    case 4:
        diket = float(input("Masukan Nilai Kelvin yang diketahui : "))
        hasil = kelvin_fungsi(diket)
        for key, value in hasil.items():
            print(f"{key} : {value}")
    case _:
        print("pilihan tidak ada")

print("SUON SING AKEH")

