# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    all_points = []
    for start in starts:
        all_points.append({"point_type": 0, "value": start })
    for end in ends:
        all_points.append({"point_type": 2, "value": end })
    for index, point in enumerate(points):
        all_points.append({"point_type": 1, "value": point, "index": index })

    all_points = sorted(all_points, key = lambda point: (point["value"], point["point_type"]))

    starts_found = 0
    for point in all_points:
        if point["point_type"] == 0:
            starts_found += 1
        elif point["point_type"] == 2:
            starts_found -= 1
        elif point["point_type"] == 1:
            cnt[point["index"]] = starts_found

    #
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [2, 3, 4, 10, 2, 6, 5, 8, 3]
    # data = [2, 3, 0, 5, 7, 10, 1, 6, 11]
    # data =[1, 3, -10, 10, -100, 100, 0]
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    # cnt1 = naive_count_segments(starts, ends, points)
    # res = ([index, count] for index, count in enumerate(cnt1) if count != cnt[index])
    cnt = fast_count_segments(starts, ends, points)

    for x in cnt:
        print(x, end=' ')
