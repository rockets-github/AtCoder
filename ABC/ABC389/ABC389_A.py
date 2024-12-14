import re
N, c, c2 = input().split()
print(re.sub(f"[^{c}]",c2, input()))