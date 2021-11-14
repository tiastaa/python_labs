rozmirnisty = int(input("Введіть розмір матриці : "))
a = [[int(input("Введіть елемент [{0},{1}] матриці a: " .format(j+1,i+1))) for i in range(rozmirnisty)] for j in range(rozmirnisty)]
b = [[int(input("Введіть елемент [{0},{1}] матриці b: " .format(j+1,i+1))) for i in range(rozmirnisty)] for j in range(rozmirnisty)]
sum = 0
c=[]
for i in range(rozmirnisty):
   for j in range(rozmirnisty):
       c=[[a[i][j]*b[i][j] for i in range(rozmirnisty)] for j in range(rozmirnisty) ]
print(c)
