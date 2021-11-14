rozmirnisty = int(input("Введіть розмір матриці: "))
a = [[int(input("Введіть елемент [{0},{1}] матриці : " .format(j+1,i+1))) for i in range(rozmirnisty)] for j in range(rozmirnisty)]
product = 1
k=1
for i in range(rozmirnisty):
   for j in range(k,rozmirnisty):
       if(a[i][j]>0):
           product = product*a[i][j]
   k=k+1

print(product)
