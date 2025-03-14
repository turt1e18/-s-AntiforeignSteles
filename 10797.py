import sys

ban = int(sys.stdin.readline().rstrip())
list = map(int, sys.stdin.readline().split())
count = 0
for i in list:
    if i == ban: count += 1

sys.stdout.write(str(count))