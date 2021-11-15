import math
'''
side_1 float Перша сторона
side_2 float Друга сторона
angle float Кут між цими сторонами в радіанах
'''
#Ввести необхідні дані
side_1=float(input("Перша сторона : "))
side_2=float(input("Друга сторона : "))
angle=float(input("Кут між цими сторонами : "))
#Обчислення площі
s=0.5*side_1*side_2*math.sin(angle)
print ("Площа трикутника : {0}".format(s))  
