a= int(input())
b= int(input())
c= int(input())

result = a * b * c

count = [0] * 10

for i in str(result):
    count[int(i)] += 1

for i in range(len(count)):
    print(count[i])