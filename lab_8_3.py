def rekursia(x_i):
    if x_i==0 or x_i==1:
        return 1
    else:
        return rekursia(x_i-1)+2*rekursia(x_i-2)
print(rekursia(int(input('vvedit i: '))))
