# python 3

class Worker():
 
 def __init__(self, index):
  self.next_free_time = 0
  self.number = index
  
 def addJob(self, job_time):
  self.next_free_time = self.next_free_time + job_time
  
def siftDown(arr, i):
 left = 2*i + 1
 right = 2*i + 2
 smaller = i
 l = len(arr)
 free_time = arr[i].next_free_time 
 if left < l:
  l_free_time = arr[left].next_free_time
  l_num = arr[left].number
  if l_free_time < free_time:
   smaller = left
  elif l_free_time == free_time and l_num < arr[i].number:
   smaller = left
  if right < l:
   r_free_time = arr[right].next_free_time
   r_num = arr[right].number
   if r_free_time < arr[smaller].next_free_time:
    smaller = right
   elif r_free_time == arr[smaller].next_free_time and r_num < arr[smaller].number:
    smaller = right
 if i != smaller:
  tmp = arr[i]
  arr[i] = arr[smaller]
  arr[smaller] = tmp
  siftDown(arr, smaller)
 
def main():
 n, m = map(int, input().split())
 jobs = list(map(int, input().split()))
 workers = [Worker(i) for i in range(n)]
 for j in jobs:
  worker = workers[0]
  print(worker.number, worker.next_free_time)
  worker.addJob(j)
  siftDown(workers, 0)
 
if __name__ == "__main__":
 main()
