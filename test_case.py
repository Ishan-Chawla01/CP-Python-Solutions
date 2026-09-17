# Run this locally to create input04.txt and output04.txt
import random
import string

# Generate 99,999 'a's and 1 'b' (Valid odd-length palindrome)
large_input = "a" * 99999 + "b"

with open("input04.txt", "w") as f_in:
    f_in.write(large_input)

with open("output04.txt", "w") as f_out:
    f_out.write("YES")

print("Files input04.txt and output04.txt created successfully!")