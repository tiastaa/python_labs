a = int(input("Введіть число а : "))
min=a%10
a=a//10
while (a!=0):
   if min>(a%10) :
       min=a%10
   a=a//10
print(min)
