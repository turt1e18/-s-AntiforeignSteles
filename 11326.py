count = int(input())

result = []

for i in range(count):
    a,b = input().split()
    a = sorted(a)
    b = sorted(b)
    temp = ""
    
    # ..? 길이 가 다르면 이라는 조건은 필요없던거임???
    # if(len(a) != len(b)):
    #     temp = "Impossible"
    #     continue
    
    for k in range(len(a)):
        if a[k] != b[k]:
            temp = "Impossible"
            break
        else:
            temp = "Possible"
    
    result.append(temp)

for i in range(len(result)):
    print(result[i])

# 입력
# 입력 받을 줄
# 문자열 섞은문자열

# 출력
# possible -> 두 문자열이 같은 경우
# impossible -> 두 문자열이 다른 경우

# 조건
# 입력 받은 두 문자열의 구성원은 같아야한다.

# 1. 줄 입력받기
# ==== 반복 시작 ====
# 	2. 문자열과 임의배열 문자열 입력받기
# 	3. 알파벳 대로 솔트
# 	==== 반복 시작 ====
# 	4. 각 알파벳 비교
# 		조건-> 각자 똑같아야함
# 		아니라면 impossible 입력
# 		같다면 possible 입력
# 	==== 반복 끝 ====
# 5. 출력