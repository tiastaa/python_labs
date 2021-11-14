rozmirnisty = int(input("Введіть розмір матриці : "))
a = [[int(input("Введіть елемент [{0},{1}] матриці a: " .format(j+1,i+1))) for i in range(rozmirnisty)] for j in range(rozmirnisty)]
product = 1
k=0
for i in range(rozmirnisty):
   for j in range(rozmirnisty):
       if(a[i][j]>=0):
           k=k+1
           product = product*a[i][j]
       if(k==rozmirnisty):
           print("Добуток {0}-го рядка матриці = {1} ".format(i+1 ,product))
   k=0
   product=1
