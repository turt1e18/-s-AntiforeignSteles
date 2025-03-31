from sys import stdin

result = []

while True:
    stack = []
    inputList = list(stdin.readline().rstrip())
    if len(inputList) == 1 and inputList[0] == ".":
        break
    for i in inputList:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if len(stack) == 0 and (i == ")" or i == "]"):
                stack.append("end")
                break
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == ")" and stack[-1] == "[":
                stack.append("end")
                break
            elif i == "]" and stack[-1] == "(":
                stack.append("end")
                break
        # print(i,", ",stack)
        
    if len(stack) == 0:
        result.append("yes")
    else:
        result.append("no")

for i in result: print(i)

# 무한반복 -> .(첫글자가 .)일때 종료 -> (스페이스바). 은 종료아님
# 1. 문장을 입력받음 (마지막은 무조건 .)
# 	1-1 리스트 첫번째가 .이고 길이가 1이면 무한반복 종료
# 		==== 리스트로 반복 ====
# 		2. ( 또는 [ 가 나오면 stack에 저장
# 			2-1 이전 스택이 나온 괄호에 대한 짝이 아닌경우 no로 
# 			2-2 아니면 stack에서 pop
# 	3. stack이 비어있다면 yes
# 		3-1 아니면 no