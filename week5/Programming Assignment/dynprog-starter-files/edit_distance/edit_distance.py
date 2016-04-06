# Uses python3
def edit_distance(str1, str2):
  result = 0

  value = []
  for i in range(0, (len(str1) + 1)):
    value.append(list((0 for j in range((len(str2) + 1)))))

  for i in range(0, len(value)): value[i][0] = i
  for i in range(0, len(value[0])): value[0][i] = i

  for j in range(1, len(str2) + 1):
    for i in range(1, len(str1) + 1):
      insertion = value[i][j - 1] + 1
      deletion = value[i - 1][j] + 1
      match = value[i - 1][j - 1]
      mismatch = value[i - 1][j - 1] + 1

      if str1[i - 1] == str2[j - 1]:
        value[i][j] = min(insertion, deletion, match)
      else:
        value[i][j] = min(insertion, deletion, mismatch)

  result = value[len(str1)][len(str2)]
  return result

def print_value(value):
  print("Value is " + str(len(value[0])) + "x" + str(len(value)) + " matrix")
  for i in range(0, len(value)):
    string = ""
    for j in range(0, len(value[i])):
      string += "{:>3}".format(value[i][j]) + " "
    print(string)

if __name__ == "__main__":
  # print(edit_distance("editing", "distance"))
  print(edit_distance(input(), input()))
