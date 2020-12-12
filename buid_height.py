# python 3

swaps = []

def siftDown(arr, i):
 left = 2*i + 1
 right = 2*i + 2
 smaller = i
 l = len(arr)
 if left < l and arr[left] < arr[smaller]: smaller = left
 if right < l and arr[right] < arr[smaller]: smaller = right
 if i != smaller:
  swaps.append((i, smaller))
  tmp = arr[i]
  arr[i] = arr[smaller]
  arr[smaller] = tmp
  siftDown(arr, smaller)
 else:
  return

def main():
 n = int(input())
 arr = list(map(int, input().split()))
 #print(len(arr))
 assert len(arr) == n
 
 for i in reversed(range(n//2)):
  #print(i)
  siftDown(arr, i)
 print(len(swaps))
 for i, j in swaps: print(i, j)
  
if __name__ == "__main__":
 main()
