from sys import stdin

input = stdin.readline

word = input().rstrip()
alp = [-1] * 26

for i, ch in enumerate(word):
    idx = ord(ch) - ord('a')
    if alp[idx] == -1:
        alp[idx] = i
        
print(" ".join(map(str,alp)))