from sys import stdin

input = stdin.readline

hour, min, sec = map(int, input().rsplit(" "))
timer = int(input().rstrip())

add_sec = int(timer % 60)
add_min = timer // 60
add_hour = 0

if add_min >= 60:
    add_hour = add_min // 60
    add_min = add_min - (60 * add_hour)

re_sec = add_sec + sec
re_min = add_min + min
re_hour = add_hour + hour

if re_sec >= 60 :   
    re_sec = re_sec - 60
    re_min = re_min + 1

if re_min >= 60 :   
    re_min = re_min - 60
    re_hour =  re_hour + 1

if re_hour >= 24:
    re_hour = re_hour % 24  

print(re_hour, re_min, re_sec)


# print(re_hour,re_min, re_sec)

# print("결과 : ",add_hour,add_min,add_sec)

# 입력 받고 -> 초를 분으로 나누고 -> 분을 시간으로 나누기
# 그 다음 현재 시간에서 시 + 분 + 초를 각각 더하기 
# 
# 마지막에 만약 hour 부분이 24 보다 넘으면 결과 - 24 하기
# 1 min  = 60sec
# 1 hour = 60 min
# 23 : 59 : 59 뒤 1초는 0 : 0 : 0