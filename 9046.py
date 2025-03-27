import sys

lineCount = int(sys.stdin.readline().rstrip())

for i in range(lineCount):
    alp= [0] * 26
    listInput = input().replace(" ","")

    for i in listInput:
        alp[ord(i) - 97] += 1

    if alp.count(max(alp)) > 1:
        print("?")
    else:
        print(chr(97 + alp.index(max(alp))))

