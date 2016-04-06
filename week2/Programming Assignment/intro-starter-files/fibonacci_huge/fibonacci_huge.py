# Uses python3
import sys

def get_fibonaccihuge(n, m):
  fibPrev = 0
  fib = 1
  cached = [fibPrev, fib]

  for curr in range(1, n):
      fibOld = fib
      fib = (fib + fibPrev) % m
      fibPrev = fibOld
      print(cached)
      if fibPrev == 0 and fib == 1:
          cached.pop()
          break
      else:
          cached.append(fib)

  offset = n % len(cached)
  return cached[offset]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
