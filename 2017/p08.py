f = open('assets/08.txt', 'r')
lines = [x.rstrip() for x in f.readlines()]

registers = {}
lens = []
largest = -float("inf")

for line in lines:
  expression = line.split(' ')
  register_a = expression[0]
  increase = 1 if expression[1] == "inc" else -1
  amount = int(expression[2])
  logic = expression[5]
  logic_val = int(expression[6])
  logic_register = expression[4]

  if register_a in registers:
    register_a_val = registers[register_a]
  else:
    registers[register_a] = 0
    register_a_val = registers[register_a]

  if logic_register in registers:
    logic_register_val = registers[logic_register]
  else:
    registers[logic_register] = 0
    logic_register_val = registers[logic_register]

  if eval("logic_register_val "+logic+" logic_val"):
    registers[register_a]+= increase * amount
    if registers[register_a] > largest:
      largest = registers[register_a]

print(registers)
max_reg = max(registers, key=registers.get)
print(max_reg + ": " + str(registers[max_reg]))
print("largest: " + str(largest))



