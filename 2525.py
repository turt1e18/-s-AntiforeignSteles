a,b = map(int, input().split())
c = int(input())

resultM = (b + c) % 60

addH = (b + c) / 60
resultH = a + addH

if resultH == 24:
    resultH = 0
elif resultH > 24:
    resultH -= 24
else:
    resultH
    
print(int(resultH),resultM)