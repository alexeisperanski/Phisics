import math
m = []
# m1 = input("Введите данные для hs в строчку через пробелы: ").split(" ")
# m2 = input("Введите данные для hs в строчку через пробелы: ").split(" ")
# m3 = input("Введите данные для hs в строчку через пробелы: ").split(" ")
# m.append(m1)
# m.append(m2)
# m.append(m3)
m1 = [200, 23, 26, 39, 36, 38, 41, 43, 44, 45, 46, 47, 48, 48, 49]
m2 = [200, 35, 39, 44, 48, 52, 54, 56, 58, 59, 60, 61, 62, 62, 63]
m3 = [200, 28, 32, 36, 38, 42, 44, 46, 47, 49, 50, 51, 52, 52, 53]
print(m)
val = 15
n = 3

sr = []
for i in range(val):
    sr.append((int(m1[i])+int(m2[i])+int(m3[i]))/n)
# print(sr)
for n in sr:
    print('{:2f}'.format(n), end = ' ')
print('\n')
dh = []
ht = 55
for i in range(val):
    dh.append(abs(ht - sr[i]))
for n in dh:
    print('{:2f}'.format(n), end = ' ')
# print(dh)
print('\n')
lnh = []
for i in range(val-1):
    v = dh[i]
    lnh.append(math.log(float(v)))
# print(lnh)
for n in lnh:
    print('{:2f}'.format(n), end = ' ')
print('\n')

