num =int(input())
num1 = num // 100000
num2 = num // 10000 % 10
num3 = num // 1000 % 10
num4 = num // 100 % 10
num5 = num //10 % 10
num6 = num % 10
print(num1,'+', num2, '+', num3, '+', num4, '+', num5, '=', num1 + num2 + num3 + num4 + num5 + num6)
