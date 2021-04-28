import sys
import numpy as np
def feltoltes(tabla):
    for i in range(tabla.shape[0]):
        for j in range(tabla.shape[1]):
            tabla[i,j]='#'
    return tabla
def jatek(tabla):
    while (True):
        print(xjon(tabla))
        print(ojon(tabla))
def xjon(tabla):
     while True:
        x = input("X következik: ")
        x = x.split(' ')
        if x[0].isdigit() and x[1].isdigit():
            if int(x[0])>tabla.shape[0] or int(x[1])>tabla.shape[1]:
                print("HIBA: ilyen pozíció nincs")
            elif tabla[int(x[0]),int(x[1])]=='X' or tabla[int(x[0]),int(x[1])]=='O':
                print("HIBA: a mező már meg lett jelölve")
            else:
                tabla[int(x[0]), int(x[1])] = 'X'
                return tabla
        else:
            print("HIBA: érvénytelen bemenet")

def ojon(tabla):
    while True:
        o = input("O következik: ")
        o = o.split(' ')
        if o[0].isdigit() and o[1].isdigit():
            if int(o[0]) > tabla.shape[0] or int(o[1]) > tabla.shape[1]:
                print("HIBA: ilyen pozíció nincs")
            elif tabla[int(o[0]), int(o[1])] == 'X' or tabla[int(o[0]), int(o[1])] == 'O':
                print("HIBA: a mező már meg lett jelölve")
            else:
                tabla[int(o[0]), int(o[1])] = 'O'
                return tabla
        else:
            print("HIBA: érvénytelen bemenet")

try:
    meret=int(sys.argv[1])
    if meret>8 or meret<3:
        print("Ilyen méretű játéktáblán nem lehet játszani.")
    tabla=np.empty((meret,meret),dtype=object)
    jatektabla=feltoltes(tabla)
    print(jatektabla)
    jatek(jatektabla)
except ValueError and meret>8:
    print("A megadott argumentum nem alakítható számmá.")
