import math

def sko(allTabl, sumTabl, ks):
    sumQr = 0
    N = len(allTabl)
    for ic in allTabl:  #сумма квадратов разницы
        sumQr += (ic - sumTabl)**2
    otv = ks*math.sqrt(sumQr/((N-1)*N))
    return otv

def tablIn(kol): #заполнение столбца массива
    tabl = []
    for i in range(kol):
        inf = input("Введите значение замера №{}: ".format(i+1))
        tabl.append(float(inf))
    return tabl

def averValue(allTabl):
    return sum(allTabl)/len(allTabl)


dtv = 0.01
Ks = input("Введите коэфициент Стъюдента: ")
massTruck11 = input("Введите массу тележки №1: ")
massTruck12 = input("Введите массу тележки №2: ")
massTruck13 = input("Введите массу тележки №2 с утежелителем: ")
massTruck21 = input("Введите массу тележки №1: ")
massTruck22 = input("Введите массу тележки №2: ")
massTruck23 = input("Введите массу тележки №2 с утежелителем: ")
# massSusp = input()
# massWasher = input("Введите массу 1 шайбы: ")

N = int(input("Сколько опытов проводилось? "))
print("Заполнение таблицы 1.1 \n")
print("Все значения v10x\n")
v10x = tablIn(N)
print("Все значения v1x\n")
v1x = tablIn(N)
print("Все значения v2x\n")
v2x = tablIn(N)

print("Заполнение таблицы 2.1 \n")
#N = int(input("Сколько опытов проводилось? "))
print("Все значения v10\n")
v10 = tablIn(N)
print("Все значения v\n")
v = tablIn(N)

print("Заполнение таблицы 3.1 \n")
N = int(input("Сколько опытов проводилось? "))
print("Массы тел таблицы 3.1\n")
massSusp = tablIn(N)
print("Все значения v1\n")
v1 = tablIn(N)
print("Все значения v2\n")
v2 = tablIn(N)

for i in range(N):
    p10x = []
sigp = (p1+p2)/p10 - 1


