#Uses python3
import sys

def print_value(value):
  print("Value is " + str(len(value[0])) + "x" + str(len(value)) + " matrix")
  for i in range(0, len(value)):
    string = ""
    for j in range(0, len(value[i])):
      string += str(value[i][j]) + " "
    print(string)

def lcs3(str1, str2, str3):
  result = 0

  distance = [[[0 for k in range(len(str3) + 1)] for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

  for k in range(0, len(str3)):
    for j in range(0, len(str2)):
      for i in range(0, len(str1)):
        if str1[i] == str2[j] == str3[k]:
          print("setting distance[" + str(i + 1) + "][" + str(j + 1) + "][" + str(k + 1) + "] = " + str(distance[i][j][k] + 1), '  ', i, j, k)
          distance[i + 1][j + 1][k + 1] = distance[i][j][k] + 1
        else:
          print("choosing max between   ", distance[i][j + 1][k + 1], distance[i + 1][j][k + 1], distance[i + 1][j + 1][k], '  ', i, j, k)
          distance[i + 1][j + 1][k + 1] = max(
            distance[i][j + 1][k + 1],
            distance[i + 1][j][k + 1],
            distance[i + 1][j + 1][k],
          )
        print_value(distance)
  # print_value(distance)
  result = distance[len(str1)][len(str2)][len(str3)]
  return result

if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    data = [3, 1, 2, 3, 3, 2, 1, 3, 3, 1, 3, 5]
    # data = [5, 8, 3, 2, 1, 7, 7, 8, 2, 1, 3, 8, 10, 7, 6, 6, 8, 3, 1, 4, 7]
    # data = [5, 1, 1, 1, 2, 3, 5, 1, 1, 2, 3, 4, 5, 1, 1, 1, 1, 1]
    # data = [3, 1, 2, 4, 3, 1, 1, 4, 3, 1, 4, 6]
    # data = [3, 1, 2, 3, 3, 1, 3, 2, 3, 2, 1, 3]
    # data = [3, 1, 2, 3, 3, 1, 3, 2, 3, 1, 1, 3]
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
    # print(lcs3(a, b, c))

