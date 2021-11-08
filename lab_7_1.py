import math
def func(x):
    if x>3 :
        f=math.sin(x)+math.sin(x**2)+math.sin(x**3)+math.sin(x**4)+math.sin(x**5)+math.sin(x**6)
    else:
        f=-math.cos(x)+math.cos(math.cos(x))-math.cos(math.cos(math.cos(x)))+math.cos(math.cos(math.cos(math.cos(x))))-math.cos(math.cos(math.cos(math.cos(math.cos(x)))))
    return f

print(min(func(int(input())),func(int(input()))))
