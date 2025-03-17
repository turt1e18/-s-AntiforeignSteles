inputCount = int(input())

primeList = list(map(int, input().split()))
count = 0
for i in primeList:
    if i == 1:
        continue

    for j in range(2, i + 1):
        if j == i: 
            count += 1 
            break
        if i % j == 0:
            break
        
       
print(count)