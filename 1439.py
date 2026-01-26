from sys import stdin

input = stdin.readline

turn_one = 0
turn_zero = 0
last_num = -1

num_list = list(map(int,input().rstrip()))

for i in num_list:
# print("i: ",i, "last : ", last_num, "turn_one : ", turn_one, "turn_zero : ", turn_zero)
    if last_num != i and i == 0:
        last_num = 0
        turn_zero += 1
    elif last_num != i and i == 1:
        last_num = 1
        turn_one += 1

# print("last turn_one : ", turn_one, "turn_zero : ", turn_zero)
print(min(turn_zero, turn_one))
