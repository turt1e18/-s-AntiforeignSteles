import sys

number = int(sys.stdin.readline().rstrip())
n = 2

while number != 1:
    if number % n != 0:
        n += 1
    else:
        # // -> 몫 계산 
        number //= n 
        sys.stdout.write(str(n) + '\n')

# 드럽게 느린데? 검사하는데 3분걸림