import sys

def checkPrime(n):
    isPrime = [True] * (n+1)
    result = []
    for i in range(2, n+1):
        if isPrime[i]:
            if(i > n/2 and i <= n):
                result.append(i)
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    
    return result

while True:

    n = int(sys.stdin.readline().rstrip())
    if n == 0: break
    print(len(checkPrime(2*n)))
