number = list(map(int, input().split()))
price = 0

if(number[0]== number[1] and number[1] == number[2]):
    price = 10000 + number[0] * 1000
elif(number[0]== number[1] or number[0] == number[2]):
    price = 1000 + number[0] * 100
elif(number[1] == number[2]):
    price = 1000 + number[1] * 100
else:
    if(number[0]> number[1] and number[0] > number[2]):
        price = number[0] * 100
    elif(number[0] < number[1] and number[1] > number[2]):
        price = number[1] * 100
    elif(number[0] < number[2] and number[1] < number[2]):
        price = number[2] * 100
print(price)