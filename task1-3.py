abcd = int(input('Введите четырехзначное число abcd: '))
m = str(abcd) 
ab = int(m[:2])
cd = int(m[2:])
s = ab + cd
print(f'сумма ab+cd равнв: {s}')