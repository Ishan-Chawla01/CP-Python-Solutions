import sys

input = sys.stdin.readline
test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    values = list(map(int, input().split()))
    triad_loves = [
        values[start] + values[start + 2] - values[start + 4]
        for start in range(n - 4)
    ]

    frequencies = {}
    for love in triad_loves:
        frequencies[love] = frequencies.get(love, 0) + 1

    answer = sum(count * (count - 1) // 2 for count in frequencies.values())

    for start, love in enumerate(triad_loves):
        if start + 2 < len(triad_loves) and triad_loves[start + 2] == love:
            answer -= 1
        if start + 4 < len(triad_loves) and triad_loves[start + 4] == love:
            answer -= 1

    print(answer)