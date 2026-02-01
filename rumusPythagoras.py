import math
print("     *Menghitung Garis Pytagoras* by Hekaa")
print("\n")
print("             /|")
print("            / |")
print("         c /  | b")
print("          /   |")
print("         /____|")
print("            a")
print("\n")

aInput = float(input('Masukan Nilai Garis "A" : '))
cInput = float(input('Masukan Nilai Garis "C" : '))
bInput = float(input('Masukan Nilai Garis "B" : '))

def menghitung(a,b,c):
    
    # menghitung Garis A
    if aInput == 0 and bInput > 0 and cInput > 0:
        aOutput = float(math.sqrt(c**2 - b**2))
        print(f"Nilai Garis A : {aOutput}" )
        
    # menghitung garis B
    elif bInput == 0 and aInput > 0 and cInput > 0:
        bOutput = float(math.sqrt(c**2 - a**2))
        print(f"Nilai Garis B : {bOutput}" )
        
    #Menghitung Garis C
    elif cInput == 0 and aInput > 0 and bInput > 0:
        cOutput = float(math.sqrt(a**2 + b**2))
        print(f"Nilai Garis C : {cOutput}" )


menghitung(aInput, bInput, cInput)
print('\n')