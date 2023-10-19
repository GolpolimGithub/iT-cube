q = int(input())
if q % 2 == 1:
    print('Да')
else:
    print('Нет')
if q == 2 or q == 4:
    print('Нет')
else:
    print('Да')
if q == 6 or q == 8 or q == 10 or q == 12 or q == 14 or q == 16 or q == 18 or q == 20:
    print('Да')
else:
    print('Нет')
if q % 2 == 0 and 20 < q:
    print('Нет')
else:
    print('Да')