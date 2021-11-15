import math
'''
сторона ab float side_ab
сторона bc float side_bc
сторона ca float side_ca
'''
#Ввести необхідні дані
x1=float(input("x1 : "))
y1=float(input("y1 : "))
x2=float(input("x2 : "))
y2=float(input("y2 : "))
x3=float(input("x3 : "))
y3=float(input("y3 : "))
# Перевірка умови
side_ab=math.sqrt((x2-x1)**2+(y2-y1)**2)
side_bc=math.sqrt((x3-x2)**2+(y3-y2)**2)
side_ca=math.sqrt((x1-x3)**2+(y1-y3)**2)
if((((side_ab)**2+(side_bc)**2)<((side_ca)**2)) or (((side_bc)**2+(side_ca)**2)<((side_ab)**2)) or (((side_ca)**2+(side_ab)**2)<((side_bc)**2))):
   print("Трикутник тупокутній")
else:
   print("Трикутник не тупокутній")
