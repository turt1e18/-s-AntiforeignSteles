import sys

def selectPrimeNum(n):
    isPrime = [True] * (n + 1)
    result = []
    for i in range(2, n+1):
        if isPrime[i]:
            result.append(i)
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return result

n = int(sys.stdin.readline().rstrip())
inputNum = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

maxValue = max(inputNum)
primeList = selectPrimeNum(maxValue)

result = []

for i in inputNum:
    index = 0
    while i > 1 and index < len(primeList):
        count = 0
        while i % primeList[index] == 0:
            i //= primeList[index]
            count += 1
        if count > 0:
            result.append(str(primeList[index]) + " " + str(count))
        index += 1

sys.stdout.write("\n".join(result)+ "\n")


    # 1. 소수 판단
    # 2. 소수 리스트로 들어온 애들 판단

    # 1차 시도
    # index = 0
    # count = 0
    # while True:
        
    #     if inputNum == 1 or inputNum % primeList[index] != 0:
    #         a = str(primeList[index]) + " " + str(count)
    #         result.append(a)
    #         index += 1
    #         count = 0
    #         if inputNum == 1:
    #             break
            
    #     else:
    #         inputNum = int(inputNum) / int(primeList[index])
    #         count += 1