# Uses python3
import sys
import math

def binary_search_recursive(array, low, high, key):
  if high < low: return(-1)

  mid = (math.floor(low + (high - low) / 2))
  if key == array[mid]:
    return(mid)
  elif key < array[mid]:
    return binary_search_recursive(array, low, mid - 1, key)
  else:
    return binary_search_recursive(array, mid + 1, high, key)

def binary_search(a, x):
  left, right = 0, len(a) - 1
  res = binary_search_recursive(a, left, right, x)
  return(res)

def linear_search(a, x):
  for i in range(len(a)):
    if a[i] == x:
      return i
  return -1

if __name__ == '__main__':
  input = sys.stdin.read()
  data = list(map(int, input.split()))
  n = data[0]
  m = data[n + 1]
  a = data[1 : n + 1]
  for x in data[n + 2:]:
    # replace with the call to binary_search when implemented
    # print(linear_search(a, x), end = ' ')
    print(binary_search(a, x), end = ' ')
