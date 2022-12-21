pt = input("Enter plain text: ")
k = int(input("Enter key: "))

def encryption(pt,k):
  pt = pt.upper()
  ct = ''
  for i in pt:
    if(i==' '):
      ct += ' '
    ind = ord(i)
    ind1 = ((ind+k-65)%26)+65
    ct += chr(ind1)
  return ct
  
  def decryption(pt,k):
  pt = pt.upper()
  ct = ''
  for i in pt:
    if(i==' '):
      ct += ' '
    ind = ord(i)
    ind1 = ((ind-k-65)%26)+65
    ct += chr(ind1)
  return ct

ct = encryption(pt,k)
print(ct)
pt1 = decryption(ct,k)
print(pt1)
