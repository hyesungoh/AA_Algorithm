# import sys
# sys.setrecursionlimit(10**9)
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = self.right = None
#
#     def __str__(self):
#         return str(self.data)
#
# class Binary:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         self.root = self.insert_req(self.root, data)
#
#     def insert_req(self, node, data):
#         if node == None:
#             node = Node(data)
#         else:
#             if node.data < data:
#                 node.right = self.insert_req(node.right, data)
#             else:
#                 node.left = self.insert_req(node.left, data)
#         return node
#
#     def postorder(self, node):
#         if node != None:
#             self.postorder(node.left)
#             self.postorder(node.right)
#             print(node)
#
#
# l = list(map(int, sys.stdin.readlines()))
# b = Binary()
# for i in l:
#     b.insert(i)
# b.postorder(b.root)

import sys
sys.setrecursionlimit(10**9)

def postorder(start, end):
    if start > end:
        return

    division = end + 1  # 나눌위치
    for i in range(start + 1, end + 1):
        if l[start] < l[i]:
            division = i
            break

    postorder(start + 1, division - 1)  # 분할 왼쪽
    postorder(division, end)  # 분할 오른쪽
    print(l[start])

l = list(map(int, sys.stdin.readlines()))
postorder(0,len(l)-1)
