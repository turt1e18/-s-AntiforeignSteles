topList = []
caseCount = int(input())
for i in range(caseCount):
    topSchoolName = ""
    topCount = 0
    schoolCount = int(input())
    for j in range(schoolCount):
        tempList = list(map(str,input().split()))
        if(int(tempList[1]) > int(topCount)):
            topCount = tempList[1]
            topSchoolName = tempList[0]
    topList.append(topSchoolName)
for k in range(caseCount):
    print(topList[k])
# 입력
# 케이스 수
# -> 케이스 만큼 반복
# 학교 수
# 학교명 숫자

# 출력
# 케이스 별 술 많이 쳐 먹은 학교

# 조건
# 입력 받은 학교 명과 학교 술병 수를 비교

# 1. 케이스 수
# ---- 반복 ----
# 2. 학교 수 입력
# ---- 반복 ----
# 3. 학교 이름 + 술 병 숫자 입력
# 4. 학교 수 완료 시 -> 해당 케이스에서 제일 많이 먹은 학교 저장
# 조건 ->
# 1. 첫 조건 전역에 등록
# 2. 입력 받으면 이전 값이랑 비교
# 3. 이전 값이 높으면 무시 아니면 이름과 값 저장
# ---- 반복 완료 ----
# 마지막 전역 값을 배열에 등록
# --- 반복 완료 ---
# 5. 케이스 마다 탑인 학교 출력 엔터