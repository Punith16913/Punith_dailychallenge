import re

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Step 1: Read column-wise into a single string
decoded_script = ''
for col in range(m):
    for row in range(n):
        decoded_script += matrix[row][col]

# Step 2: Replace symbol-runs sandwiched between alphanumerics with a single space
final_string = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', decoded_script)

print(final_string)