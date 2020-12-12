# python3
A = []
size = -1
braces = {"}":"{", "]":"[", ")":"("}
mismatch_open = None

def matchbraces(close_brace, i):
 global A, size, mismatch_open
# print(close_brace)
 if size == -1 or A[size] != braces[close_brace]:
 # print('no closing brace match found')
  return False
 else:
 # print('match found')
  size = size - 1
  if size == -1:
   mismatch_open = None 
  return True

def main():
 global A, size, mismatch_open
# print('hello')
 i = 0
 
 str = input()
# print(str)
# print(braces.values())
# print(braces.keys())
 A = [None] * len(str)
 for char in str:
  i = i+1
 # print(char)
  if char in braces.values():
 #  print('opening brace found')
   # If opening brace found
   size = size + 1
   A[size] = char
   if mismatch_open == None:
    mismatch_open = i
  elif char in braces.keys():
   # If closing brace found
 #  print('closing brace found')
   if not matchbraces(char, i):
    print(i)
    return
 if mismatch_open != None:
  print(mismatch_open)
  return
 else:
  print('Success')
  return

if __name__ == "__main__":
    main()

   
 
