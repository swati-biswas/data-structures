# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
  def __init__(self, key, left, right, parent):
   self.key = key
   self.left = left
   self.right = right
   self.parent = parent

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.treeNodes = [0 for i in range(self.n)]
    tn = self.treeNodes
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      if tn[i] == 0:
       tn[i] = Node(a, b, c, -1)
      else:
       node = tn[i]
       node.key = a
       node.left = b
       node.right = c
      if b != -1: #set parent for left node     
       if tn[b] == 0:
        tn[b] = Node(-1, -1, -1, i)
       else:
        node = tn[b]
        node.parent = i
      if c != -1: #set parent for right node
       if tn[c] == 0:
        tn[c] = Node(-1, -1, -1, i)
       else:
        node = tn[c]
        node.parent = i
    
  def isBinary(self, n):
    if len(self.treeNodes) == 0:
     return [0,0]
    n = self.treeNodes[n]
    l_node = n.left
    r_node = n.right
    #print(n.key + " " + n.left + " " + n.right)
    if l_node == -1 and r_node == -1:
     return [n.key, n.key] 
    minm = n.key
    maxm = n.key
    if l_node != -1:     
     mm = self.isBinary(l_node)
     if mm[0] == -1 or mm[1] > n.key:
      return [-1, -1]
     minm = mm[0]
    if r_node != -1:
     mm = self.isBinary(r_node)
     if mm[0] == -1 or mm[0] < n.key:
      return [-1, -1]
     maxm = mm[1]
    return [minm, maxm] 

def main():
 tree = TreeOrders()
 tree.read()
 mm = tree.isBinary(0)
 if mm[0] != -1 and mm[1] != -1:
  print('CORRECT')
 else:
  print('INCORRECT')

threading.Thread(target=main).start()
