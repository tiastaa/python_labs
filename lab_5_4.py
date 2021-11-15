n = int(input("Введіть число n : "))
x_i_2=9
x_i_1=0
x=0
for i in range(1 ,n) :
   x=3*x_i_2+2*x_i_1
   x_i_2=x_i_1
   x_i_1=x 
print (x)
