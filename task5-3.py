def rectangle(x,y):
  return x*y

def triangle(a,h):
  return a*h*0.5

def circle(r):
  return r*r*3.14

m = str(input('Площадь какой фигуры вы хотите расчиать: '))
if ((m == 'Прямоугольник') or (m == 'прямоугольник')):
    x = int(input('Введите длину: '))
    y = int(input('Введите ширину: '))
    i = rectangle(x,y)
    print(i)
if ((m == 'Треугольник') or (m == 'треугольник')) :
    a = int(input('Введите длину основания: '))
    h = int(input('Введите высоту: '))
    i = triangle(a,h)
    print(i)
if ((m == 'окружность') or (m == 'Окружность')) :
    r = int(input('Введите радиус: '))
    i = circle(r)
    print(i)