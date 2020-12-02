import numpy as np
from time import time


with open('/Users/mike/git/advent-of-code-2020/day_01/input.txt', 'r') as f:
    nums = np.array([int(line.replace('\n', '')) for line in f])
    start = time()
    nums = np.sort(nums)
    sort_time = time() - start
print(sort_time)

# PART 1
start = time()
for n in nums:
    if 2020 - n in nums:
        print(n*(2020 - n))
        break
end = time()
print(end - start)

# PART 2
start = time()
for i, n in enumerate(nums):
    for j, m in enumerate(nums):
        if 2020 - n - m in nums:
            print(n*m*(2020 - n - m))
            break
    else:
        continue
    break
end = time()
print(end - start)