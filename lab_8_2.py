def mul_vec(i, vec):
    for k in range(len(vec)):
        vec[k] = i*vec[k]
    return vec

def add_vec(vec1, vec2):
    vec3 = []
    for i in range(len(vec1)):
        vec3.append(vec1[i]+vec2[i])
    return vec3

length = int(input("vvedit dovzhynu masssyva: "))
a =[]
b =[]
c =[]
for i in range(length):
    a.append(int(input("vvedit {0}-iy element masszvu a: " .format(i+1))))
for i in range(length):
    b.append(int(input("vvedit {0}-iy element  masszvu b: " .format(i+1))))
for i in range(length):
    c.append(int(input("vvedit {0}-iy element  masszvu c: " .format(i+1))))

d = add_vec(add_vec(a, mul_vec(-3, b)), mul_vec(2, c))
print(d)
