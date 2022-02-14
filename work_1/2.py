time= input('введите время в секундах ')
hour = int(time)//3600
minute = (int(time) - hour*3600)//60
sec = (int(time) - hour*3600 - minute*60)

result = f"{hour}:{minute}:{sec}"
print(result)
