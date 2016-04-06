# Uses python3
import sys

def get_change(n):
  change_left = n
  coins = 0
  nominations = sorted([1, 5, 10])
  for nomination in reversed(nominations):
    if change_left == 0: return coins

    coin_count = change_left // nomination
    change_left -= nomination * coin_count
    coins += coin_count

  return coins

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))

