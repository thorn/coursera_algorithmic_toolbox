a = 357
b = 234

def euclid_gcd(a, b):
  if(b == 0): return a

  tmp = a % b

  return euclid_gcd(b, tmp)

print(euclid_gcd(a, b))
