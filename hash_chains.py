# python 3

class StringStore():
 def __init__(self, cardinality):
  self.p = 1000000007
  self.x = 263
  self.m = cardinality
  self.strChain = [None]* self.m
  
 def doHash(self, string):
  i = 0
  sum = 0
  x = self.x
  for s in string:
   asci = ord(s)
   sum = sum + asci*(x**i)
   i = i + 1
  h = (sum%self.p)%self.m
  #print(h)
  return h
  
 def findString(self, string):
  h = self.doHash(string)
  if (self.strChain[h] != None):
   c = self.strChain[h]
   if string in c:
    return 'yes'
   else:
    return "no"
  else:
   return "no"
  
 def checkString(self, index):
  if (self.strChain[index] != None):
   string = ""
   for s in reversed(self.strChain[index]):
    #print(s)
    string = string + " " + s
   return string
  else:
   return ""
   
 def addString(self, string):
  h = self.doHash(string)
  if (self.strChain[h] != None):
   c = self.strChain[h]
   if string not in c: c.append(string)
  else:
   self.strChain[h] = [string]
   
 def delString(self, string):
  h = self.doHash(string)
  if (self.strChain[h] != None):
   c = self.strChain[h]
   if string in c: c.remove(string)
   if not c: self.strChain[h] = None
  
def main():
 result = []
 m = int(input())
 ss = StringStore(m)
 n = int(input())
 for i in range(n):
  q = input().split()
  if q[0] == 'add':
   ss.addString(q[1])
  elif q[0] == 'find':
   result.append(ss.findString(q[1]))
  elif q[0] == 'del':
   ss.delString(q[1])
  elif q[0] =='check':
   result.append(ss.checkString(int(q[1])))
 for i in result:
  print(i)
 
if __name__ == "__main__":
 main()
