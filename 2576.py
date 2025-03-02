numbers = []
odd = []
oddAdd = 0
for i in range(7):
    numbers.append(int(input()))
for j in range(7):
    if(numbers[j] % 2 == 1):
        odd.append(numbers[j])
if(len(odd)==0):
    print(-1)
else:
    for k in range(len(odd)):
        oddAdd += odd[k]
    odd.sort()
    print(oddAdd)
    print(odd[0])