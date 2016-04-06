# Uses python3
import sys

def get_fibonacci_last_digit(n):
  if (n <= 1): return n

  res = [0, 1]
  for i in range(2, n + 1):
    res.append((res[i - 2] + res[i - 1]) % 10)

  return res[n]
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
