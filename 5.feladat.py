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
        if nyerte(tabla)==True:
            print("Az X játékos győzött!")
            break
        print(ojon(tabla))
        if nyerte(tabla) == True:
            print("Az O játékos győzőtt!")
            break
def xjon(tabla):
     while True:
        x = input("X következik: ")
        x = x.split(' ')
        if x[0].isdigit() and x[1].isdigit():
            if int(x[0])>tabla.shape[0]-1 or int(x[1])>tabla.shape[1]-1:
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
            if int(o[0]) > tabla.shape[0]-1 or int(o[1]) > tabla.shape[1]-1:
                print("HIBA: ilyen pozíció nincs")
            elif tabla[int(o[0]), int(o[1])] == 'X' or tabla[int(o[0]), int(o[1])] == 'O':
                print("HIBA: a mező már meg lett jelölve")
            else:
                tabla[int(o[0]), int(o[1])] = 'O'
                return tabla
        else:
            print("HIBA: érvénytelen bemenet")

def nyerte(tabla):
    for i in range(tabla.shape[0]):
        csakazvan=0
        for j in range(tabla.shape[1]):
            if tabla[i,0]==tabla[i,j] and tabla[i,0]!='#':
                csakazvan+=1
        if csakazvan==tabla.shape[0]:
            return True

    for j in range(tabla.shape[1]):
        csakazvan=0
        for i in range(tabla.shape[0]):
            if tabla[0,j]==tabla[i,j] and tabla[0,j]!='#':
                csakazvan+=1
        if csakazvan==tabla.shape[0]:
            return True

    csakazvan = 0
    for i in range(tabla.shape[0]):
        if tabla[0,0]==tabla[i,i] and tabla[0,0]!="#":
            csakazvan+=1
        if csakazvan==tabla.shape[0]:
            return True

    csakazvan = 0
    for i in range(tabla.shape[0]-1,0,-1):
        for j in range(tabla.shape[1]):
            if tabla[tabla.shape[0]-1,0]==tabla[i,j] and tabla[tabla.shape[0]-1,0]!="#":
                csakazvan+=1
            if csakazvan==tabla.shape[0]-1:
                return True

try:
    meret=int(sys.argv[1])
    if meret>8 or meret<3:
        print("Ilyen méretű játéktáblán nem lehet játszani.")
        breakpoint()
    tabla=np.empty((meret,meret),dtype=object)
    jatektabla=feltoltes(tabla)
    print(jatektabla)
    jatek(jatektabla)
except ValueError:
    print("A megadott argumentum nem alakítható számmá.")
