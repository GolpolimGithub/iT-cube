q, w, e, r = int(input()), int(input()), int(input()), int(input())
if q + w == e + r or q - w == e - r or  q == e or w == r:
    print('Да')
else:
    print('Нет')