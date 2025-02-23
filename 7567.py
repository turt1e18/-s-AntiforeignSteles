import sys

plate = list(input())
p_length = 10

for i in range(len(plate)):
    if(i==len(plate)-1):
        break
    if(plate[i+1] == plate[i]):
        p_length += 5
    elif(plate[i+1] != plate[i]):
        p_length += 10
    
print(p_length)


# 입력 최소 3개 ~ 50개
# 입력될 문자는 '(' 또는 ')'
# 
# 조건
# 같은 문자가 연속되면 +5
# 문자가 같지않으면 +10
# 
# 출력
# 위에 계산한거 정수형으로 총합
# 
# 문자열 입력을 받음
# 계산하는 반복 횟수는 리스트의 길이로 설정
# 총합은 무조건 10부터 시작
# 리스트로 만든후 n번이랑 n-1이랑 비교해서 숫자를 계산