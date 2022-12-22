pt = input("Enter plain text: ")
key = input("Enter the key: ")

def encryption(pt,key):
  ind = []
  key = list(key)
  sort = sorted(key)
  for i in range(len(key)):
    ind.append(key.index(sort[i]))
    key[key.index(sort[i])] ="#"
  
  table = []
  i = 0

  while (i<len(pt)):
    temp = []
    for j in range(len(key)):
      if i<len(pt):
        temp.append(pt[i])
      else:
        temp.append('0')
      i += 1
    table.append(temp)

  ans = ""
  for i in range(len(key)):
    col = ind[i]
    for j in range(len(table)):
      ans += table[j][col]
  
  return ans

ct = encryption(pt,key)
print(ct)

def decryption(ct,k):
  ind = []
  sortd = sorted(k)
  k = list(k)
  ct = list(ct)
  for i in range(len(k)):
    ind.append(k.index(sortd[i]))
    k[k.index(sortd[i])]="#"
  
  cols = len(k)
  rows = len(ct) // len(k)
  table = []

  for i in range(rows):
    table.append(['0']*cols)
  
  for i in range(cols):
    currid = ind[i]
    for j in range(rows):
      table[j][currid] = ct.pop(0)
  ans = ""
  for i in table:
    ans += "".join(i)
  
  print(ans)

decryption(ct,key)
