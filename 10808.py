import sys

text = list(sys.stdin.readline().rstrip())
alp = [0] * 26

for i in range(len(text)):
    if(text[i] == "a"):
        alp[0] += 1
    elif(text[i] == "b"):
        alp[1] += 1
    elif(text[i] == "c"):
        alp[2] += 1
    elif(text[i] == "d"):
        alp[3] += 1
    elif(text[i] == "e"):
        alp[4] += 1
    elif(text[i] == "f"):
        alp[5] += 1
    elif(text[i] == "g"):
        alp[6] += 1
    elif(text[i] == "h"):
        alp[7] += 1
    elif(text[i] == "i"):
        alp[8] += 1
    elif(text[i] == "j"):
        alp[9] += 1
    elif(text[i] == "k"):
        alp[10] += 1
    elif(text[i] == "l"):
        alp[11] += 1
    elif(text[i] == "m"):
        alp[12] += 1
    elif(text[i] == "n"):
        alp[13] += 1
    elif(text[i] == "o"):
        alp[14] += 1
    elif(text[i] == "p"):
        alp[15] += 1
    elif(text[i] == "q"):
        alp[16] += 1
    elif(text[i] == "r"):
        alp[17] += 1
    elif(text[i] == "s"):
        alp[18] += 1
    elif(text[i] == "t"):
        alp[19] += 1
    elif(text[i] == "u"):
        alp[20] += 1
    elif(text[i] == "v"):
        alp[21] += 1
    elif(text[i] == "w"):
        alp[22] += 1
    elif(text[i] == "x"):
        alp[23] += 1
    elif(text[i] == "y"):
        alp[24] += 1
    elif(text[i] == "z"):
        alp[25] += 1
    
addStr = "" 

for i in range(len(alp)):
    addStr = addStr + str(alp[i]) + " "

print(addStr)

# text1 = input()
# alp = [0] * 26
# for i in range(text1):
# 	alp[ord(i)-97] = text1.count(i)
# for i in alp:
# 	print(i, end=" ")