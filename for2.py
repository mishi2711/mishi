#numbers using list

numbers = [30, 50, 120, 200, 300, 550, 600]

for number in numbers:
    if number > 500:
        break 
    if number > 150:
        continue  
    if number % 5 == 0:
        print(number)
