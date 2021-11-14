rozmirnisty = int(input("Введіть розмір матриці : "))
a = [[int(input("Введіть елемент [{0},{1}] матриці a: " .format(j+1,i+1))) for i in range(rozmirnisty)] for j in range(rozmirnisty)]
max = 0
sum=0
i=0
j1=0
j=0
for k in range(rozmirnisty):
   while(0<=i<rozmirnisty and 0<=j<rozmirnisty):
       sum=sum+a[i][j]
       i=i+1
       j=j+1
   j1=j1+1
   j = j1
   i=0
   if(sum>max):
       max=sum
   sum=0
a = [list(i) for i in zip(*a)]
i=0
j=0
j1=0
for k in range(rozmirnisty):
   while(0<=i<rozmirnisty and 0<=j<rozmirnisty):
       sum=sum+a[i][j]
       i=i+1
       j=j+1
   j1=j1+1
   j = j1
   i=0
   if(sum>max):
       max=sum
   sum=0
print(max)
