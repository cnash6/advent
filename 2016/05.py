import hashlib

room = "cxdnnyjw"

password = "________"
n = 0
while "_" in (password):
  hashed = hashlib.md5(str.encode(room + str(n))).hexdigest() 
  if hashed[:5] == "00000":
    try: 
      i = int(hashed[5])
      if password[i] == '_':
        password = password[:i] + hashed[6] + password[i+1:]
        print(password)
    except:
      pass
  n+=1

print(password)