import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
boxes = list(map(int, sys.stdin.readline().split()))
wants = list(map(int, sys.stdin.readline().split()))
boxes = [-entry for entry in boxes]
heapq.heapify(boxes)

flag = 1
for want in wants:
    current = -heapq.heappop(boxes)
    if current >= want:
        current -= want
        heapq.heappush(boxes, -current)
    else:
        flag = 0
        break
print(flag)

