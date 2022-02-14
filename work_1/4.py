digit = (input('введите целое положительное число '))
i = 0
last_digit = 0
while i < len(digit):
    current_digit = int(digit[i])
    if current_digit > last_digit:
        bigest_digit = current_digit
    last_digit = current_digit
    i += 1
print ('наибольшая цифра в числе = ', bigest_digit)
