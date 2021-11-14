rozmirnisty = int(input("Введіть розмір матриці : "))
a = [[int(input("Введіть елемент [{0},{1}] матриці a: " .format(j+1,i+1))) for i in range(rozmirnisty)] for j in range(rozmirnisty)]
a_t = [list(i) for i in zip(*a)]
for i in range(rozmirnisty):
   if(i%2==0):
       a_t[i].sort()
a = [list(i) for i in zip(*a_t)]
print(a)
