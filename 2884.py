hour,minute = map(int,input().split())

minute = minute - 45
if(minute < 0):
    minute = minute + 60
    hour = hour - 1
if(hour < 0):
    hour = 23

print(hour,minute)

# 입력
# h시간 m분
# 
# 출력
# h시간 m분
# 
# 조건
# 입력으로 받은 시간이랑 분을 - 45분한 시간이 결과로 출력해야한다
# 
# 1. 입력받기
# 2. m에서 -45한 후 결과 저장
# 	만약 해당 결과에서 - 이면 (60 - 결과) 후 m에 저장
# 		위 조건이 발동되면 h에서 -1후 저장
# 	만약 h가 음수이면 23 저장