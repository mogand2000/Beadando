import random
import numpy as np
#csapatszam=int(input("A bajnokság csapatainak száma: "))
csapat=[]
#for i in range(csapatszam):
#    csapat.append(input(f"{i+1}. csapat: "))
print(csapat)
csapatszam=4
csapat=["a","b","c","d"]
csapatpont=np.zeros(csapatszam)
rugottgol=np.zeros(csapatszam)
kapottgol=np.zeros(csapatszam)
for i in range(csapatszam):
    for j in range(i+1,csapatszam):
        hazai=random.randint(0,4)
        vendeg=random.randint(0,4)
        print(f"{csapat[i]} - {csapat[j]} {hazai}:{vendeg}")
        if hazai>vendeg:
            csapatpont[i]+=3
        elif hazai<vendeg:
            csapatpont[j] += 3
        elif hazai==vendeg:
            csapatpont[i]+=1
            csapatpont[j]+=1
        rugottgol[i]+=hazai
        kapottgol[i]+=vendeg
        rugottgol[j]+=vendeg
        kapottgol[j]+=hazai
matrix=np.empty((csapatszam,4),dtype=object)
for i in range(csapatszam):
    matrix[i,0]=csapat[i]
    matrix[i,1]=int(csapatpont[i])
    matrix[i,2]=int(rugottgol[i])
    matrix[i,3]=int(kapottgol[i])
#Rendezni kell
helyezes=1
print("Pontállás:")
for i in range(matrix.shape[0]):
    print('{0:<15}{1:20}{2:10}{3:15}{4:15}'.format(helyezes,matrix[i,0],matrix[i,1],matrix[i,2],matrix[i,3]))
    helyezes+=1
print(matrix)
print(csapatpont)
print(rugottgol,kapottgol)
