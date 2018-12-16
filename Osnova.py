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
math.log1p()
[200, 23, 26, 39, 36, 38, 41, 43, 44, 45, 46, 47, 48, 48, 49]
[200, 35, 39, 44, 48, 52, 54, 56, 58, 59, 60, 61, 62, 62, 63]
[200, 28, 32, 36, 38, 42, 44, 46, 47, 49, 50, 51, 52, 52, 53]