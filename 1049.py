from sys import stdin

input = stdin.readline

lost, brand = map(int, input().rstrip().split(" "))
setprice , oneprice = 0,0
result = 0

for _ in range(brand):
    bset, bone = map(int, input().rstrip().split(" "))
    
    if setprice == 0 and oneprice == 0:
        setprice = bset
        oneprice = bone

    if bset < setprice:
        setprice = bset
    if bone < oneprice:
        oneprice = bone

if lost <= 6:
    if setprice < oneprice * lost:
        result = setprice
    else:
        result = oneprice * lost
else:
    index = 0
    afterLost = 0
    if lost % 6 != 0:
        afterLost = lost % 6
        index = lost // 6
    else:
        index = lost // 6

    if setprice <= oneprice:
        if afterLost > 0:
            result = setprice * (index+1)
        else:
            result = setprice * index
        # print("세트 가격이 개당 가격 이하일때", setprice * index)

    else:
        onlyset = 0
        if afterLost > 0:
            onlyset = setprice * (index+1)
        else:
            onlyset = setprice * index
        onlyone = oneprice * lost
        mixprice = setprice * index + oneprice * afterLost
        # print(onlyone, onlyset, mixprice)
        result = min(onlyone, onlyset, mixprice)
        
print(result)


# 입력

# 첫째 줄
# 끊어진 기타 줄 숫자 + 기타 줄 브랜드 수(입력 반복수)

# 둘째 줄 - n째 줄
# 6개 세트 값 + 1개당 값

# 세트를 사거나 1개 또는 여러개를 낱개로 구매가능
# 최소값을 구하라

# 0. 최소값 구하기
# 	set, one = 0 으로 선언
# 	현재 값보다 작으면 저장

# 1. 세트의 최소값과 낱개의 최소값을 구함
# 2. 개수에 대한 최소값을 구해봄
# 	2-1 6개 이하라면
# 		n 개까지 낱개 vs 1세트 값
# 	2-2 아니라면	
# 		세트만으로 n개 도달 값 vs 낱개만으로 n개 도달 값 vs 세트 먼저 까고 낱개 값 에서 제일 작은거
		