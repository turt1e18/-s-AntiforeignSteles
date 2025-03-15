import sys

data = list(input())

if "".join(data)  == "".join(list(reversed(data))):
    print(1)
else:
    print(0)
