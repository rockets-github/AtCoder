import numpy as np

N = int(input()) - 1
num = int(np.base_repr(N, base=5)) * 2
print(num)



