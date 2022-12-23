import hashlib

input_text = "I like shiny things. but i'll marry you with paper rings. aa ha. thats right. you are the one i want"
input_lines = input_text.split(". ")
input_lines = list(map(str.encode, input_lines))

hash_object = list(map(hashlib.sha1, input_lines))
hash_values = list(map(type(hash_object[0]).hexdigest, hash_object))

def merkel(hash_values):
  
  counter = 0
  root = ''
  
  for i in range(len(hash_values)):
    if i == counter**2:
      root += hash_values[i-1]
      counter += 1
    else:
      root += hash_values[i]
    return root

merkel(hash_values)
