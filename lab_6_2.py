import math
'''
a1 знаменник
а2 чисельник
sum_positive  сума додатніх
sum_negative  сума від'ємних
'''
element_number=int(input("Введіть кількість елементів: "))
a1=[]
a2=[]
a=[]
a1.append(math.cos(1))
a2.append(1)
a.append(a1[0]/a2[0])
sum_positive=0
sum_negative=0
for i in range(1 , element_number) :
   a1.append(a1[i-1]*(2*i-1)*math.cos(i))
   a2.append(a2[i-1]+i*i)
   a.append(a1[i]/a2[i])
   if a[i]<0 :
       sum_negative=sum_negative+a[i]
   else:
       sum_positive=sum_positive+a[i]
if sum_positive>sum_negative:
   print("-1")
else :
   print("1")
