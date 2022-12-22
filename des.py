def chartobin(s):
  s1 = ''
  for i in range(len(s)):
    s1 += str(bin(ord(s[i]))).replace("b","")
  return s1

def expand(rpt):
  
  ans = []
  bits = []

  for i in range(8):
    ans.append(rpt[:4])
    bits.append([rpt[0],rpt[3]])
    rpt = rpt[4:]
  for i in range(1,7):
    ans[i] = bits[i-1][1]+ans[i]+bits[i+1][0]
  ans[0]=bits[-1][1]+ans[0]+bits[1][0]
  ans[7]=bits[-2][1]+ans[7]+bits[0][0]
  print(ans)
  return ans

def xor (rpt,key,n):
  print(len(rpt),len(key))
  ans = ''
  for i in range(48):
    ans += str(int(rpt[i])^int(key[i]))
  return ans

def compress(s):
  ans = ''
  for i in range(8):
    row = int(s[0]+s[5],2)
    col = int(s[1:5],2)
    val str(bin(box[row][col])).replace('0b','')
    while(len(val) < 4):
      val = '0'+ val
    ans += val
    s = s[6:]
  return ans

def encrypt():
  s = 'sharvari'
  s1 = chartobin(s)
  slpt = s1[:32]
  srpt = s1[:32]
  k = 'sharvarichaw'
  k1 = chartobin(k)
  klpt = k1[:48]
  krpt = k1[48:]

  rpt = expand(srpt)
  rpt = ''.join(rpt)
  print(rpt)
  rpt = xor(rpt,klpt,48)
  rpt = compress(rpt,box[0])
  rpt = xor(rpt,lpt,32)

  srpt,slpt = slpt,rpt
  rpt = expand(srpt)
  rpt = ''.join(rpt)
  print(rpt)
  rpt = xor(rpt,krpt,48)
  rpt = compress(rpt,box[1])
  rpt = xor(rpt,lpt,32)

  return slpt + rpt

encrypt()
