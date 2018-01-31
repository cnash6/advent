gen_a = 591
gen_b = 393

# Testing
# gen_a = 65
# gen_b = 8921

FACTOR_A = 16807
FACTOR_B = 48271
DIVISOR = 2147483647

N = 5 * (10**6)
# N = 5

def gen(val, factor, div):
  while True:
    val = (val * factor) % DIVISOR
    if val % div == 0:
      return val

total = 0
for i in range(N):
  if i % (N//100) == 0:
    print("..." + str(i // (N//100)) + "%", end="\r")
  gen_a = gen(gen_a, FACTOR_A, 4)
  gen_b = gen(gen_b, FACTOR_B, 8)
  # print(str(gen_a) + "      " + str(gen_b))
  if (gen_a & 0xffff) == (gen_b & 0xffff):
    total+=1

print()
print(total)
