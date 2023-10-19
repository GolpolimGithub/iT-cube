q, w, e, r = int(input()), int(input()), int(input()), int(input())
num1 = (q + w + e + r) % 2
if num1 == 0:
    print('Да')
else:
    print('Нет')

