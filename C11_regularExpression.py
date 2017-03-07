import re
handle = open('regex_sum_332502.txt')
sum = 0
for line in handle:
    line = line.rstrip()
    num_list = re.findall('[0-9]+',line)
    for num in num_list:
        sum = sum+int(num)

print sum


