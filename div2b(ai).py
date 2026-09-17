import sys

t = int(sys.stdin.readline())
ans = []

for x in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = sorted(list(map(int, sys.stdin.readline().split())))
    b = sorted(list(map(int, sys.stdin.readline().split())))

    used_indices = []  # Tracks used indices of array a
    matched_count = 0  # Counts how many elements of b were matched

    # Process b backwards (from largest element to smallest element)
    for j in range(len(b) - 1, -1, -1):
        found_match = False
        target = b[j]

        # Expand gap starting from adjacent elements (gap = 1, 2, 3...)
        gap = 1
        while gap < len(a):
            i = 0
            while i < len(a) - gap:
                # Skip if index i or i + gap is already used
                if i in used_indices or (i + gap) in used_indices:
                    i += 1
                    continue

                # Check if target fits strictly between a[i] and a[i + gap]
                if a[i] < target and target < a[i + gap]:
                    used_indices.append(i)
                    used_indices.append(i + gap)
                    found_match = True
                    break

                i += 1

            if found_match:
                break
            gap += 1

        if found_match:
            matched_count += 1
        else:
            break

    # If all elements of b found a valid pair in a
    if matched_count == len(b):
        ans.append("yes")
    else:
        ans.append("no")

print(ans)