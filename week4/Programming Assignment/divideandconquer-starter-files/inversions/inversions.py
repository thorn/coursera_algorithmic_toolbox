# Uses python3
import sys
import collections

def merge(left, right):
    result = []
    inv_count = 0
    i = 0
    j = 0
    left_size = len(left)
    right_size = len(right)
    while i < left_size and j < right_size:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv_count += left_size - i

    for i in range(i, left_size):
        result.append(left[i])
    for i in range(j, right_size):
        result.append(right[i])

    return(result, inv_count)

def merge_sort(a, left, right):
    if (right - left) == 1:
        return(a[left:right], 0)

    mid = left + (right - left) // 2

    sorted_left, inv_count_left = merge_sort(a, left, mid)
    sorted_right, inv_count_right = merge_sort(a, mid, right)

    sorted_array, inversions_count = merge(sorted_left, sorted_right)

    inv_count_total = inversions_count + inv_count_left + inv_count_right

    return(sorted_array, inv_count_total)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    print(merge_sort(a, 0, len(a))[1])
