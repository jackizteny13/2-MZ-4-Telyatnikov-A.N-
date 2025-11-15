import random
a = random.randint(0,10)
n=1
b=int(input('Попробуйте угадать число от 0 до 10: '))
while n < 3:
    while b>a:
        print('Неверно! Загаданное число меньше вашего')
        b=int(input('Попробуйте снова угадать число: '))
        n=n+1
        break
    while b<a:
        print('Неверно! Загаданное число больше вашего')
        b=int(input('Попробуйте снова угадать число: '))
        n=n+1
        break
    while b == a:
        print('Поздравляю! Вы угадали число')
        n=n+3
        break
while n==3: 
    print ('Неверно! Ваши попытки закончились')
    break