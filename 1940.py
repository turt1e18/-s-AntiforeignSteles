from sys import stdin

input = stdin.readline

countIngredient = int(input().rstrip())
armor = int(input().rstrip())
ingredient = list(map(int,input().split(" ")))
count = 0
front,back = 0,len(ingredient) - 1
ingredient = sorted(ingredient)


while(front != back):
    result = ingredient[front] + ingredient[back]
    if armor < result:
        back -= 1
    elif armor == result:
        count += 1
        front += 1
    elif armor > result:
        front += 1

# print(countIngredient,armor,ingredient,front,back)
print(count)


# 무조건 정렬 후

# if 목표치보다 낮다 -> front + 1
# if 목표치다 ->  카운트 + 1, front + 1
# if 목표치보다 높다 -> back -1

# front back 이 같아지면 종료