#get data

file = open('day2data', 'r')
data = file.readlines()

list = []
list1 = []

for line in data:
    list.append(line.strip('\n'))
for line in list:
    list1.append(cmd,amt = line.split())


#driver code
# forward
# down is +
# up is -

horizontal = 0
depth = 0
final = horizontal * depth

for i, j in enumerate(list1):
    i, j = list1.split()
    j = int(j)
    if list1[i] == 'forward':
        horizontal += list1[j]
    if list1[i] == 'down':
        depth = depth + list[j]
    if list1[i] == 'up':
        depth = depth - list[j]

print(horizontal, depth, final)
