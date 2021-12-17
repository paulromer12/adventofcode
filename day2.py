#get data

file = open('day2data', 'r')
data = file.readlines()

list = []
list1 = []

for line in data:
    list.append(line.strip('\n'))
for line in list:
   list1.append(line.split())


#driver code
# forward
# down is +
# up is -

horizontal = 0
depth = 0

for line in list1:
    if line[0] == 'forward':
        horizontal += int(line[1])
    if line[0] == 'down':
        depth = depth + int(line[1])
    if line[0] == 'up':
        depth = depth - int(line[1])

final = horizontal * depth

print(horizontal, depth, final)
