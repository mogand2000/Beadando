from itertools import permutations
def jolista(perm):
    jolista=[]
    for item in perm:
        if joelem(item)==True:
            jolista.append(item)
    jolista=egyszer(jolista)
    return jolista

def joelem(elem):
    balance=0
    for jel in elem:
        if jel=='(':
            balance+=1
        if jel==')':
            balance-=1
        if balance<0:
            return False
    return True

def egyszer(lista):
    permegyszer=[]
    for item in  lista:
        if item not in permegyszer:
            permegyszer.append(item)
    return permegyszer

try:
    szam=int(input("Adjon meg egy pozitív egész számot: "))
    list1=[]
    for i in range(szam):
        list1.append('(')
        list1.append(')')
    perm=list(permutations(list1))
    keszlista=(jolista(perm))
    szepalak=[]
    for item in keszlista:
        sz=""
        for k in item:
            sz+=k
        szepalak.append(sz)
    print("Lehetséges kombinációk:",szepalak)
    print("Lehetséges kombinációk száma:",len(szepalak))

except ValueError:
    print("A megadott bemenet nem alakítható szám formátummá.")