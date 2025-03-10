result = []
while True:
    a,b,c = map(int,input().split())
    if(a == 0 and b == 0 and c == 0):
        break
    if pow(c,2) == pow(a,2) + pow(b,2) or pow(a,2) == pow(c,2) + pow(b,2) or pow(b,2) == pow(a,2) + pow(c,2):
        result.append("right")
    else:
        result.append("wrong")

for i in range(len(result)):
    print(result[i])


#..? 삼각형 완성 조건식 중에 세 개 다 조건을 만족해야한다는게 어디있는데요