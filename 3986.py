from sys import stdin

cmdLine = int(stdin.readline().rstrip())
resultStack = 0

for i in range(cmdLine):
    stack = []
    aType = 0
    bType = 0

    inputData = list(stdin.readline().rstrip())
    
    for j in inputData:
        if len(stack) != 0 and stack[-1] == j:
            if j == "A":
                aType += 1
            else:
                bType += 1
            stack.pop()
        else:    
            if j == "A":
                aType += 1
            else:
                bType += 1
            stack.append(j)
    if len(stack) == 0:
        resultStack += 1
    # print(stack)
print(resultStack)

# 예시 
# aabb abba abbbab

# 1. 입력받기
# 2. 입력 받은걸 list화 하기
# ==== 끝까지 돌리기 ====
# 	3. a or b 들어가는거 확인 -> stack에 추가하고 type에 1씩 추가
		
# 		4-1. 배열의 -1이 추가된 글자와 같은 경우 pop
# 			4-1-1. 여기서 a이면 atype 1추가
# 			4-1-2. 아니면 btype 1추가
# 		4-2. 아니면 추가
# 			4-2-0. 예를 들어 추가되는 것이 b라면 a의 type을 확인하고 type홀수 인 경우 종료
# 			4-2-1. 여기서 a이면 atype 1추가
# 			4-2-2. 아니면 btype 1추가

# 	5. stack이 비어있으면 결과에 1추가