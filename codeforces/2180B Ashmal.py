from collections import deque
import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    arr = input().split()

    dq = deque()
    dq.append(arr[0])  # first string

    for i in range(1, n):
        current = "".join(dq)
        a = arr[i]

        # Compare both possibilities
        if a + current < current + a:
            dq.appendleft(a)
        else:
            dq.append(a)

    print("".join(dq))