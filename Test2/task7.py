q, w, e, r = int(input()), int(input()), int(input()), int(input())
num1 = q + w
num2 = e + r
if num1 + 3 == num2 or num2 + 3 == num2 or num1 + 1 == num2 or num2 + 1 == num1:
    print('Да')
else:
    print('Нет')