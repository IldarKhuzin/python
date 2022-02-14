first = int(input('введите количество пройденных километров в первый день '))
target = int(input('введите целевое значение километров в день '))
count = 1
while first < target:
    first *= 1.1
    count += 1
    print(first)
print('спортсмен достиг результата не менее ',  target,' километров на ', count , ' день' )
