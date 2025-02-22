tryCount = int(input())
for i in range(tryCount):
    n,data = input().split()
    for word in data:
        print(word*int(n), end = "")   
    print("")