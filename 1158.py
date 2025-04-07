# import sys

# class Node:
#     def __init__(self,  data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.length = 0
    
#     def __len__(self):
#         return self.length

#     def add(self, preNode, data):
#         node = Node(data)
#         self.length += 1

#         if preNode:
#             node.next = preNode.next
#             preNode.next = node
#         else:
#             node.next = node
#             self.head = node

#     def delete(self, preNode):
#         self.length -= 1

#         if preNode.next != self.head:
#             preNode.next = preNode.next.next
#         else:
#             if preNode != self.head:
#                 self.head = self.head.next
#                 preNode.next = self.head
#             else:
#                 self.head = None
    
#     def search(self):
#         cur = self.head
#         while True:
#             yield cur.data
#             if cur.next == self.head:
#                 break
#             else:
#                 cur = cur.next




# josephus = LinkedList()
# n, k = map(int, sys.stdin.readline().split())

from sys import stdin
from collections import deque
input = stdin.readline

cmdList = list(map(int,input().split(" ")))

# print(cmdList)
dq = deque(range(1, cmdList[0]+1))
newList = []

for _ in range(cmdList[0] - 1):
    dq.rotate(-(cmdList[1]-1))
    newList.append(str(dq.popleft()))
newList.append(str(dq.pop()))
# print(newList)
print("<"+", ".join(newList)+">")




# 1 2 3 4 5 6 7 
# 1 2 4 5 6 7 	3
# 1 2 4 5 7 	6
# 1 4 5 7 		2
# 1 4 5 		7
# 1 4 		5
# 4		1
# 4  