from sys import stdin

a = list(map(str,stdin.readline().rstrip()))
b = list(map(str,stdin.readline().rstrip()))
c = list(map(str,stdin.readline().rstrip()))
d = list(map(str,stdin.readline().rstrip()))
e = list(map(str,stdin.readline().rstrip()))
maxLen = max(len(a),len(b),len(c),len(d),len(e))

result = ""

# print( a,b,c,d,e)
for i in range(maxLen):
    if(i < len(a)):
        result = result + str(a[i])
    
    if(i < len(b)):
        result = result + str(b[i])
    
    if(i < len(c)):
        result = result + str(c[i])
    
    if(i < len(d)):
        result = result + str(d[i])
    
    if(i < len(e)):
        result = result + str(e[i])
    
print(result)

# 한줄에 15개 -> 띄워쓰기 없이
# 줄은 5개

# 각 배열 1번부터 n번 까지 출력
# 없으면 통과

# 1. 5줄 입력받기
# === 반복문 ===
# 2. 각 줄의 1번부터 출력
# 	여기서 i(반복문)가 리스트의 길이보다 클 경우에 해당 배열 무시
# 유툽 자동재생에서 이상한 노래나와 살려줘