#Ввести необхідні дані
a=float(input("a : "))
b=float(input("b : "))
c=float(input("c : "))
# Перевірка умови
if(a<b<c) :
   print("y=1")
elif(a==b==c) :
   print("y=2")
elif(b<a<c) :
   print("y=3 \ny=4")
else :
   print("y=0")
