import math
def sko(allTabl):
    sumTabl = sum(allTabl)/len(allTabl)
    #поиск среднего
    for ic in allTabl:
        sumQr += (ic - sumMas)**2
    #сумма квадратов разницы
    otv = math.sqrt(sumQr/(len(allTabl) - 1))
    #окончательный ответ (корень из суммы квадратов делённой на кол-во элементов - 1)
    return otv
sumQr = 0

#alltabl = []
# while True:
#     inf = input("Введите число. Для выхода вводите 'stop': ")
#     if inf == 'stop':
#         break
#     else:
#         mass.append(float(inf))
# #полное заполнение массива
