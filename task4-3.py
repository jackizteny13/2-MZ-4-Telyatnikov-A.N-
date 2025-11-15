h=int(input("Введите высоту елки: "))
s=str(input("Введите символ: "))
for i in range(1, h):
    l=s*(i-1)
    r=s*(i-1)
    sp=(' ')*(h-i)
    print(sp+l+'||'+r)
print((' ')*(h - 1)+'||')
