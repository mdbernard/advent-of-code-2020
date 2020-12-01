import numpy as np
from time import time


with open('/Users/mike/git/advent-of-code-2020/day_01/input.txt', 'r') as f:
    nums = np.array([int(line.replace('\n', '')) for line in f])
    start = time()
    nums = np.sort(nums)
    sort_time = time() - start
print(sort_time)

# PART 1
def find_prod_of_pair(nums, target=2020):
    pairs = target - nums
    for i, pair in enumerate(pairs):
        if pair in nums:
            print(nums[i]*pair)
            break


start = time()
find_prod_of_pair(nums)
end = time()
print(end - start)

# PART 2
start = time()
for i, n in enumerate(nums):
    for j, m in enumerate(nums):
        for k, l in enumerate(nums):
            if i != j and j != k and n + m + l == 2020:
                print(n*m*l)
                break
        else:
            continue
        break
    else:
        continue
    break
end = time()
print(end - start)