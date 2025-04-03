from sys import stdin

# a시간당 얻는 피로도 b진행도  c시간당 줄어드는 피로도 m최대 피로도
a,b,c,m = map(int, stdin.readline().split(" "))

time = 24
farigue = 0
work = 0

for _ in range(time):
    if farigue + a <= m:
        farigue += a
        work += b
    else:
        farigue = max(0, farigue - c)

print(work)
# while time > 0:

#     if cmdLine[0] > cmdLine[3]:
#         break

#     worktime = cmdLine[3] // cmdLine[0]
#     time -= worktime
#     work = cmdLine[1] * worktime + work

#     # print("log work : ",time,work)

#     resttime = cmdLine[3] // cmdLine[2]
#     if cmdLine[3] % cmdLine[2] != 0:
#         resttime += 1
#     time -= resttime

#     # print("log rest : ",time,work)

# 초기
#   
# 하루 24 시간
# 초기는 0 피로도
# 일한다면 : 시간당 A 만큼 피로도 B 만큼 처리
# 쉰다면  : 시간당 C 만큼 피로도 저하
# 최대피로도는 M

# 전체 24시간 초과 안하게 처리
# 0. A한번 돌릴때 M이 넘거나 시간이 0이면 종료
	
# 1. A를 M초과 안하게 피로도 입력
# 	이때 B 를 a 돌린 만큼 곱해서 저장
# 	이때 A 한번 돌릴때 마다 1 시간 감소
# 2. 피로도가 0이 될때 까지 C 반복
# 	이때 c 한번 돌릴때 마다 1 시간 감소

# 2 일하고 6
# 5 쉬고
# 2 일하고 6
# 5 쉬고
# 2 일하고 6
# 5 쉬고
# 2 일하고 6

# 후기
# 아니 그럼 그냥 1시간마다 돌리면 되는거 아닌가? 
# 어차피 하루는 24번이니까 24번만 돌리면 되잖아
