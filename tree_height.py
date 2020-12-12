# python3

import sys
import threading

parents = []

class Node:
 def __init__(self, p):
  self.parent = p
  self.children = []

 def addChild(self, x):
  self.children.append(x)

def createTree(nodes):
 root = None
 for i in range(0, len(nodes)):
  node = None
  current = nodes[i]
#  print(current)
  if isinstance(current, int):
   current = Node(current)
   nodes[i] = current 
  
  if current.parent == -1:
   root = current
  else:
   parent_to_current = current.parent
   if isinstance(nodes[parent_to_current], int):
    parent_node = Node(nodes[parent_to_current])
    nodes[parent_to_current] = parent_node
   else:
    parent_node = nodes[parent_to_current]
   parent_node.addChild(i)

 #print(nodes)
 #print(root)
 return root
 
  
  
def getHeight(node):
 global parents
# print(node)
 children = node.children
 if len(children) == 0:
  return 1
 else:
  children_ht = []
  for x in children:
   child_ht = 1 + getHeight(parents[x])
   children_ht.append(child_ht)
  return max(children_ht)
   
def main():
    global parents
    n = int(input())
 #   print(n)
    parents = list(map(int, input().split()))
 #   print(parents)
    root = createTree(parents)
  #  print(parents)
  #  print(root)
  #  for a in parents:
  #   print(a.parent)
  #   print(a.children)
    print(getHeight(root))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
