earnings = int(input('введите выручку фирмы '))
cost = int(input('введите издержки фирмы '))
if earnings > cost:
    print('фирма работает в прибыль')
elif cost > earnings:
    print('фирма работает в убыток')
else:
    print('доходы и расходы одинаковы')
