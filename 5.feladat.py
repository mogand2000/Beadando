import sys
import numpy as np
def feltoltes(tabla):
    for i in range(tabla.shape[0]):
        for j in range(tabla.shape[1]):
            tabla[i,j]='#'
    return tabla
def jatek(tabla):
    while (True):
        x = input("X következik: ")
        x = x.split(' ')
        for i in range(tabla.shape[0]):
            for j in range(tabla.shape[1]):
                if i == int(x[0]) and j == int(x[1]):
                    tabla[i, j] = 'X'
        print(tabla)
        if tabla[0, 0] == "b'X'":  # NEM MUKODIK
            print("NYERT")
        o = input("O következik: ")
        o = o.split(' ')
        for i in range(tabla.shape[0]):
            for j in range(tabla.shape[1]):
                if i == int(o[0]) and j == int(o[1]):
                    tabla[i, j] = 'O'
        print(tabla)
        if int(x[0]) == 5:
            print(tabla[0, 0])
            break
    print(tabla)
try:
    meret=int(sys.argv[1])
    if meret>8 or meret<3:
        print("Ilyen méretű játéktáblán nem lehet játszani.")
        breakpoint()                       #??
    tabla=np.chararray((meret,meret))
    jatektabla=feltoltes(tabla)
    jatek(jatektabla)
except ValueError:
    print("A megadott argumentum nem alakítható számmá.")
