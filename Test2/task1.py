num = int(input())
num1 = num % 10
num2 = num // 10 % 10
if num1 == 0 and num2 == 0:
    print('Да')
else:
    print('Нет')