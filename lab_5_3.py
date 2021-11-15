import math
'''
f знаменник
d числьник
'''
a = int(input("Введіть число а : "))
x = int(input("Введіть число x : "))
n = int(input("Введіть число n : "))
E = int(input("Введіть число E : "))
f=1
z=1
d=x*math.log(a)
sum=0
while ((z/f)>E) :
   sum=sum+(z/f)
   f=f*(+1)
   z=z*d
if a**x==sum:
   print ("Тотожність вірна")
else:
   print("Тотожність не вірна")
