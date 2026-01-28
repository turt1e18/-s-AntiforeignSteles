from sys import stdin

input = stdin.readline

n = int(input().rstrip())
num_list = list(map(int, input().rstrip().split(" ")))

now = 0
num_list.sort()

for i in num_list:
    if i > now+1:
        break
    now += i

print(now + 1)

# while True:
#     count = num_list[index]
#     for i in range(index+1,n):
#         temp = num_list[index] + num_list[i]
#         count += num_list[i]
#         # print(num_list[index], num_list[i], "temp : ", temp,"count : " ,count )
#         result.append(temp)
#         result.append(count)

#     index += 1
#     if index > n: break

# count = list(set(result))[0]
# for i in list(set(result)):
#     if i != count:
#         print(count)
#         break
#     else: count += 1

# 받고 0번부터 끝번까지 더하고
# 1번부터 끝번까지 더하고
# 0 1 0 2 0 3
# 1 2 1 3
# 2 3
# 그럼 근데 1 2 3은 못만드는데?

# 1 2 2 7 -> 1 ,3 , 5, 12, 3, 3, 8
# 2 2 7 -> 2 4 11 4 9
# 2 7 -> 2 9 
# 7 -> 7