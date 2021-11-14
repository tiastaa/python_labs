rozmirnisty = int(input("Введіть розмір матриці: "))
a = [[int(input("Введіть елемент [{0},{1}] матриці : " .format(j+1,i+1))) for i in range(rozmirnisty)] for j in range(rozmirnisty)]
i1=int(input("Введіть номер рядка матриці : "))
j1=int(input("Введіть номер стовпця матриці : "))
product = 0
for i in range(rozmirnisty):
   product=product+a[i1-1][i]*a[i][j1-1]
print(product)
