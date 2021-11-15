a = input("Введіть масив : ").split(' ')
k=0
b=[]
for i in range(len(a)):
  a[i] = float(a[i])
for i in range(len(a)):
  if abs(a[i])<1 :
      k=k+1
  else :
      b.append(a[i])
for n in range(k):
  b.append(0)
print(b)
