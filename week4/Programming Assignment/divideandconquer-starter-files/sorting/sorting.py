# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    x_start = l
    x_end = l + 1
    for i in range(l + 1, r + 1):
        if a[i] == x:
            if a[x_end] != a[i]:
                a[x_end], a[i] = a[i], a[x_end]
            x_end += 1

    for i in range(x_end, r + 1):
        if a[i] < x:
            a[x_end], a[i] = a[i], a[x_end]
            a[x_start], a[x_end] = a[x_end], a[x_start]
            x_start += 1
            x_end += 1

    return(x_start, x_end - 1)

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);

    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # n, a = 5, [2, 3, 9, 2, 2]
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
