import sys

n = int(sys.stdin.readline())  # Number of test cases
for _ in range(n):
    m = int(sys.stdin.readline())  # The number of books available
    result = []
    for _ in range(m):
        parts = sys.stdin.readline().strip().split()
        if not parts:
            continue
        result.append([int(parts[0]), parts[1]])

    min_time_first = 9999999
    min_time_second = 9999999
    min_common = 9999999
    for i in range(m):
        if (result[i][1] == '01' or result[i][1] == '11') and min_time_first > result[i][0]:
            min_time_first = result[i][0]
        if (result[i][1] == '10' or result[i][1] == '11') and min_time_second > result[i][0]:
            min_time_second = result[i][0]
        if result[i][1] == '11' and min_common > result[i][0]:
            min_common = result[i][0]
    if min_time_first == 9999999 or min_time_second == 9999999:
        if min_common == 9999999:
            print(-1)
    if min_common > min_time_first + min_time_second:
        print(min_time_second + min_time_first)
    elif min_common != 9999999:
        print(min_common)
