# python 3

tables = []

class Table:
 def __init__(self, rows, parent):
  self.rank = 0
  self.parent = parent
  self.rows = rows
  
def merge(src, dest):
 src_indx = findParent(src)
 dest_indx = findParent(dest)
 if src_indx == dest_indx:
  return 0
 t_src = tables[src_indx]
 t_dest = tables[dest_indx]
 src_rank = t_src.rank
 dest_rank = t_dest.rank
 total_rows = t_src.rows + t_dest.rows

 if src_rank < dest_rank:
  t_src.parent = dest_indx
  t_dest.rows = total_rows
  t_src.rows = 0
 elif src_rank >= dest_rank:
   t_dest.parent = src_indx
   t_src.rows = total_rows  
   if src_rank == dest_rank:
    t_src.rank = src_rank + 1
   t_dest.rows = 0
 return total_rows

def findParent(indx):
 parent = tables[indx].parent
 if indx != parent:
  p = findParent(parent)
  tables[indx].parent = p # Path Compression
  return p
 else:
  return indx
   

def main():
 global tables
 
 n, opers = map(int, input().split())
 maxm = 0
 tables_data = list(map(int, input().split()))
 parents = list(range(n))

 assert len(tables_data) == n
 if n != 0: 
  maxm = max(tables_data)
 else: return
 
 tables = [Table(t, indx) for indx, t in enumerate(tables_data)]
 
 #for indx, t in enumerate(tables):
 # t[indx] = Table(t, indx)
 
 for op in range(opers):
  src, dest = map(int, input().split())
  final_rows = merge(src-1, dest-1)
  if final_rows > maxm:
   maxm = final_rows
  print(maxm)
  
if __name__ == "__main__":
 main()
