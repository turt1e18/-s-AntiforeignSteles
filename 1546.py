count = int(input())
list = sorted(list(map(int, input().split())))
sum = 0

def newCalc(value,max):
    return value / max * 100

for i in range(count): sum += newCalc(list[i],max(list))

print(sum / count)