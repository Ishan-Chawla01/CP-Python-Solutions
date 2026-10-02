import sys
from collections import defaultdict

input_data = sys.stdin.read().split()
if input_data:
    t = int(input_data[0])
    vowels = {"a", "e", "i", "o", "u"}

    for i in range(1, t + 1):
        s = list(input_data[i])
        n = len(s)

        if n == 2:
            if s[0] != s[-1]:
                print("NO")
            else:
                print("YES")
            continue

        d = defaultdict(int)
        for char in s:
            d[char] += 1

        odd_count = 0
        odd_char = ""
        for key, value in d.items():
            if value % 2 != 0:
                odd_count += 1
                odd_char = key

        if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count > 1):
            print("NO")
            continue

        orig_vowels = [c for c in s if c in vowels]
        orig_consonants = [c for c in s if c not in vowels]

        left_half = []
        counts = d.copy()
        if odd_char:
            counts[odd_char] -= 1

        for char in sorted(counts.keys()):
            left_half.extend([char] * (counts[char] // 2))

        target_s = left_half + ([odd_char] if odd_char else []) + left_half[::-1]

        target_vowels = [c for c in target_s if c in vowels]
        target_consonants = [c for c in target_s if c not in vowels]

        if target_vowels == orig_vowels and target_consonants == orig_consonants:
            print("YES")
        else:
            print("NO")