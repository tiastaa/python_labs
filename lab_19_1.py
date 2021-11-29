#Дано текстовий файл, який містить цілі числа. Визначити кількість елементів більших за найменший елемент.
from functools import reduce
import random

a=[random.randint(-100,100) for i in range(20)]
with open('test.txt', 'w') as file:
    file.write( ' '.join( map(lambda el:str(el), a) ) )
with open('test.txt') as file:
    line = file.readline()
    numbers = list(map(lambda el: int(el), line.split(sep=' ')))
    min_x = min(numbers)
    k_bigger=reduce(lambda k ,i : k+1 if i > min_x else k , numbers , 0)
print(k_bigger)
