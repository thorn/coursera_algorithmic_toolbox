# Uses python3
import sys

def optimal_summands(n):
  summands = []
  amount_left = n
  last_used_number = 1

  for i in range(1, n + 1):
    if amount_left == 0:
      return summands

    if (i < ((amount_left) / 2)) or ((amount_left - i) == 0):
      amount_left -= i
      summands.append(i)

  return summands

if __name__ == '__main__':
  input = sys.stdin.read()
  n = int(input)
  summands = optimal_summands(n)
  print(len(summands))
  for x in summands:
      print(x, end=' ')
