a = []
for i in range(9):
    a.append(int(input()))

a.sort()
b, c = 0, 0

for i in range(9):
    for j in range(9):
        if sum(a)-a[i]-a[j] == 100 and i != j:
            b, c = i, j

for i in range(9):
    if i != b and i != c:
        print(a[i])