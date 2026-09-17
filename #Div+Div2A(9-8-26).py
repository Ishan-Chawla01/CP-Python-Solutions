import sys

t = int(sys.stdin.readline())
for x in range(t):
    a, b, c = map(int, sys.stdin.readline().split())
    initial_range = max(a, b, c) - min(a, b, c)
    mid = a + b + c - max(a, b, c) - min(a, b, c)

    if a + b > min(a, b, c):
        ans = min(initial_range, mid)
    elif a + b < max(a, b, c):
        ans = min(initial_range, mid)
    elif b + c > min(a, b, c):
        ans = min(initial_range, mid)
    elif b + c < max(a, b, c):
        ans = min(initial_range, mid)
    elif a + c > min(a, b, c):
        ans = min(initial_range, mid)
    elif a + c < max(a, b, c):
        ans = min(initial_range, mid)
    else:
        ans = min(initial_range, mid)

    print(ans)