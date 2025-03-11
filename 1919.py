from collections import Counter
str1 = Counter(input())
str2 = Counter(input())

print(sum((str1-str2).values()) + sum((str2-str1).values()))