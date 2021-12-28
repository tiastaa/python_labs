'''
Довідник покупця. База торгівельних підприємств міста: назва, адреса та телефон,
спеціалізація, час роботи. Організувати вибір магазину за довільним запитом.
Дані зберігаються в масиві.
'''
a=[['TEDIS_UKRAINA', 'vulicya_Slavi' , '+380990145966', 'Optova_torgivlya_tyutyunovimi_virobami', '8:00-15:00'],['DTEK_TREJDING', 'vulicya_Gvardijska' , '+380990145967', 'Optova_torgivlya_tverdim,_ridkim,_gazopodibnim_palivom_i_podibnimi_produktami', '6:00-23:00'],['MHP', 'vulicya_Lisova' , '+380509362439', 'Optova_torgivlya_myasom_i_myasnimi_produktami', '11:00-2:00'] ]
with open('test.txt', 'w') as file:
    for i in range(len(a)):
        file.write(' '.join(a[i]) + '\n')
info=str(input('Введіть запит : '))

f = open('test.txt')
for line in f:
    line1=line.split(sep=' ')
    if info in line1 or info+"\n" in line1:
        print(line1[0])
f.close()
