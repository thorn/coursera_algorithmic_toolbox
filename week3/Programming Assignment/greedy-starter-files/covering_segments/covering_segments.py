# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    sorted_segments = sorted(segments, key=lambda segment:segment.end)
    for segment in sorted_segments:
      if not(len(points) > 0 and (segment.start <= points[-1]) and (points[-1] <= segment.end)):
        points.append(segment.end)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    # data = [4, 7, 1, 3, 2, 5, 5, 6]
    # data = [1, 3, 4, 5, 4, 6]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
