def DVO(a):
  return bin(a)[2:]

a = int(input('Введите число в десятиричной виде: '))
m = DVO(a)
print (f'Исходное число {a}, полученное число - {m}')