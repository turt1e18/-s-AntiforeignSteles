import sys

facto = int(sys.stdin.readline().rstrip())
result = 1

for i in range(facto):
    result *= (i+1)

count = 0

temp = list(reversed(list(str(result))))

for i in temp:
    if(i != "0"): break
    else: count += 1

sys.stdout.write(str(count))