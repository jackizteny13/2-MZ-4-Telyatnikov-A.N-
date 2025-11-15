def create_christmas_tree(h,s):
 for i in range(1, h):
        l=s*(i-1)
        r=s*(i-1)
        sp=(' ')*(h-i)
        print(sp+l+'||'+r)
 print((' ')*(h - 1)+'||')

a = str(input('Хотите нарисовать Ёлку?: '))
if a=='Да' or a=='да':
    h=int(input("Введите высоту елки: "))
    s=str(input("Введите символ: "))
    y = create_christmas_tree(h,s)
    print(y)
