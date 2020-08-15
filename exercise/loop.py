# coding: utf_8
items = [1,2,3]
for i in items:
    print(f'変数iの値は{i}')

for j in range(3):
    print(f'{j}番目の処理')

chars = 'world'
for count, char in enumerate(chars):
    print(f'{count}番目の文字は{char}')

n = 0
while n < 3:
    print(f'変数nの値は{n}')
    n += 1
else:
    print('end')
