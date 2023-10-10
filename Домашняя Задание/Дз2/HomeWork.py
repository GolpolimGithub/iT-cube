num = int(input())
num2 = num // 100 % 10
num1 = num // 1000
num4 = num % 10
num3 = num // 10 % 10
print('Цифра в позиции тысяч:', num1)
print('Цифра в позиции сотен:', num2)
print('Цифра в позиции десятков:', num3)
print('Цифра в позиции единиц:', num4)