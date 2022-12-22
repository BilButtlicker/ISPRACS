pt = 'sharvari is very awesome'
k = 5

n = len(pt)
pt = list(pt)
for i in range(n):
  if(pt[i] == ' '):
    pt[i] = '_'

if(n%16):
  for i in range(16 - n%16):
    pt.append("_")


groups = []
for i in range((len(pt)//16)):
  temp = ''
  for j in range(16):
    ch = str(pt.pop(0))
    temp += ch
  groups.append(temp)

print(groups)
ans = []

for group in groups:
  t=''
  for c in group:
    t += str(bin(ord(c))).replace('b','')
  ans.append(t)

print(ans)

for i in range(len(ans)):
  rev = ans[i][::-1]
  a = rev[:k]
  b = rev[k:]
  ans[i] = a[::-1]+b[::-1]

print(ans)
