# Uses python3
def calc_fib(n):
  if (n <= 1): return n
  res = [0, 1]
  for i in range(2, n + 1):
    res.append(res[i - 2] + res[i - 1])

  return res[n]

n = int(input())
print(calc_fib(n))
