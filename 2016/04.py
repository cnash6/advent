f = open('assets/04.txt', 'r')
rooms = f.readlines()

# rooms = [
#   "aaaaa-bbb-z-y-x-123[abxyz]",
#   "a-b-c-d-e-f-g-h-987[abcde]",
#   "not-a-real-room-404[oarel]",
#   "totally-real-room-200[decoy]"
# ]

realNums = []
real = []

for r in rooms:
  room = {}
  room['room'] = r
  room['split'] = r.rstrip().split('-')
  room['name'] = "".join(room['split'][:-1])
  room['number'] = room['split'][-1].split('[')[0]
  room['checksum'] = room['split'][-1].split('[')[1][:-1]

  chars = {}
  for char in room['name']:
    if char in chars:
      chars[char]+=1
    else:
      chars[char] = 1

  chars_ordered = [{"char": x, "count": chars[x]} for x in chars]
  chars_ordered = sorted(chars_ordered ,key=lambda x: x["char"])
  chars_ordered = sorted(chars_ordered ,key=lambda x: x["count"], reverse=True)[:5]

  check = "".join([x["char"] for x in chars_ordered])

  if check == room["checksum"]:
    realNums.append(int(room["number"]))
    real.append(room)

# print(sum(realNums)) 

def shift_char(character, shift):
  alphabet = 'abcdefghijklmnopqrstuvwxyz' 
  if char == '-':
    return ' '
  else:
    return alphabet[((alphabet.index(character) + shift) % 26)]


for room in real:
  decrypted = []
  for character in room["name"]:
    decrypted.append(shift_char(character, int(room['number'])))
  room["decrypted"] = "".join(decrypted)
  print(room["decrypted"] + ": " + room["number"])
  



