a = input("enter vector1: ").split(' ')
for i in range(len(a)):
   a[i] = int(a[i])
b = input("enter vector2: ").split(' ')
for i in range(len(b)):
   b[i] = int(b[i])
sum = 0
for i in range(len(a)):
   sum += a[i]*b[i]
print(sum)
