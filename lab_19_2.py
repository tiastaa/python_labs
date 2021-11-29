#Дано типізований файл, який містить квадратну матрицю  (матриця зберігається поелементно, кількість елементів визначити за допомогою функції FileSize). Визначити найменший елемент серед додатних використовуючи динамічно створений двовимірний масив. Від’ємні елементи зберегти у окремому файлі дійсних чисел «V.dat».

from functools import reduce
import random
n=int(input("Введіть кількість рядків матриці : "))
a=[[random.randint(-100,100) for i in range(n)] for j in range(n)]
with open('test.txt', 'w') as file:
    for i in range(n):
        file.write(' '.join(map(lambda el: str(el), a[i])))
        if(i==n-1):
            break
        file.write(' ')
with open('V.dat.txt', 'w') as file:
    for row in a:
        for el in row:
            if el < 0 :
                file.write(str(el))
                file.write(' ')
with open('test.txt') as file:
    line = file.readline()
    numbers = list(filter(lambda el: el>0 ,map(lambda el:  int(el),line.split(sep=' ')) ))
    min_x = min(numbers)
print(min_x)



