import re
from time import time


start = time()
with open('/Users/mike/git/advent-of-code-2020/day_02/input.txt', 'r') as f:
    data = [[int(re.findall(r'\d*-', line)[0][:-1]), int(re.findall(r'-\d*', line)[0][1:]), re.findall(r'\s[\w*|\.]*:', line)[0][1:-1], re.findall(r'\s\w*$', line)[0][1:]] for line in f]
print(f'Part 1: {sum([data[i][0] <= data[i][3].count(data[i][2]) <= data[i][1] for i in range(len(data))])}')
print(f'Part 2: {sum([(data[i][3][data[i][0]-1] == data[i][2]) != (data[i][3][data[i][1]-1] == data[i][2]) for i in range(len(data))])}')
end = time()
print(end - start)