pt = "aandu gondu"
k = "shari"

pt = pt.replace(" ","").upper()
k = k.replace(" ","").upper()

def generate_key(k,pt):
  key=''
  j = 0
  for i in range(len(pt)):
    if(j==len(k)):
      j=0
    key += k[j]
    j += 1
  return key

key = generate_key(k,pt)

def encryption(pt,key):
  ct = ''
  for i in range(len(pt)):
    x = (ord(pt[i])+ord(key[i]))%26
    x += ord('A')
    ct += chr(x)
  # print(ct)
  return ct

ct = encryption(pt,key)
print(ct)

def decryption(ct,key):
  pt1 = ''
  for i in range(len(ct)):
    x = (ord(ct[i]) - ord(key[i]))%26
    x += ord('A')
    pt1 += chr(x)
  return pt1

decryption(ct,key)
