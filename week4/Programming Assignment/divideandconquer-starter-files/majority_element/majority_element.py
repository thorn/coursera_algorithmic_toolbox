# Uses python3
import sys
from functools import reduce

def get_majority_element(a, left, right):
    if (right == left):
        return(a[right])
    if (right - left == 1):
        if a[right] == a[left]:
            return(a[left])
        else:
            return(-1)

    mid = left + ((right - left) // 2)
    l_elem = get_majority_element(a, left, mid)
    r_elem = get_majority_element(a, mid + 1, right)

    # if r_elem != -1: print('right_elem_count = ' + str(a[left:right+1].count(r_elem)) + ' right = ' + str(right) + ' left = ' + str(left) + ' ' + str(a[left:right+1]))
    # if l_elem != -1: print('left elem count  = ' + str(a[left:right+1].count(l_elem)) + ' right = ' + str(right) + ' left = ' + str(left) + ' ' + str(a[left:right+1]))

    if (l_elem != -1) and (a[left:right + 1].count(l_elem) > ((right + 1 - left) // 2)):
        return(l_elem)
    elif (r_elem != -1) and (a[left:right + 1].count(r_elem) > ((right + 1 - left) // 2)):
        return(r_elem)

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n, a = 5, [2, 3, 9, 2, 2]
    # n, a = 10, [767899817, 67202753, 395437752, 5, 901806735, 5, 5, 5, 5, 729234271]
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)
