max = int(input())
list = sorted(list(map(int, input().split())))
targetNum = int(input())

count = 0

left,right = 0 , max - 1

while left < right:
    temp = list[left] + list[right]
    if(temp == targetNum):
        count += 1
        left += 1
    elif(temp < targetNum):
        left +=1
    else:
        right -= 1

print(count)

# 입력
# 배열 크기
# 배열(띄워쓰기)
# 두합의 숫자

# 출력
# 두합의 숫자가 나온 횟수

# 조건
# 배열 A에서
# n + m 번째 애들이 두합의 숫자와 같아야 한다

# 1. 배열 크기 지정
# 2. 배열 숫자들 받기
# 3. 찾고자 하는 두 숫자의 합
# ==== 반복 ====
# 	4. 0 -> n 까지 더하기
# 		조건 -> 합이 같으면 카운트 +
# 	5. 끝나면 1 -> n 까지 더하기
# ==== 반복 종료 ====
# 6. 출력



# 0 1 -> 0 2 -> 0 3 -> ...
# 1 2 -> 1 3 -> ...
# 2 3 -> 2 4 -> ...
# 3 4 -> 3 5 -> ...
# ...
# 6 7 -> 6 8
# 7 8

# 투 포인터를 쓰래...

# 0 + n-1 => 같으면 카운트
# 작으면 end + 1
# 높으면 start + 1

# 1 2 3 5 7 9 10 11 12
# 1 12 13
# 2 12 14
# 2 11 13
# 3 11 14
# 3 10 13
# 5 10 15
# 5 9  14
# 5 7  12