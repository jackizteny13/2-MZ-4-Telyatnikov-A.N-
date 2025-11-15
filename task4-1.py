a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
if a<b:
    for n in range(a,b+1):
        print (n)
else:
    for n in range(-a,-b+1):
        print (-n)
