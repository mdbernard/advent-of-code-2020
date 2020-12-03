valid_part_1 = valid_part_2 = 0
for line in open('/Users/mike/git/advent-of-code-2020/day_02/input.txt', 'r'):
    mini, maxi, char, pwrd = int(line[0:line.find('-')]), int(line[line.find('-')+1:line.find(' ')]), line[line.find(' ')+1:line.find(':')], line.strip()[line.find(':')+2:]
    valid_part_1 += mini <= pwrd.count(char) <= maxi
    valid_part_2 += (pwrd[mini-1] == char) != (pwrd[maxi-1] == char)
print(valid_part_1, valid_part_2)