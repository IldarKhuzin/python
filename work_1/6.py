earnings = int(input('введите выручку фирмы '))
cost = int(input('введите издержки фирмы '))
if earnings > cost:
    profit = earnings - cost
    print('фирма работает в прибыль')
    print('рентабельность фирмы = ', profit/earnings)
    worker = int(input('введите количество сотрудников '))
    print('прибыль фирмы в расчете на одного сотрудника = ', profit/worker)
elif cost > earnings:
    print('фирма работает в убыток')
else:
    print('доходы и расходы одинаковы')
