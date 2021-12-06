#How many measurements are larger than the previous measurement?


file = open('day1data', 'r')
data = file.readlines()

list = []

for line in data:
    list.append(int(line.strip('\n')))

counter = 0

for i in range(0, 2000):
    if list[i] > list[(i - 1)]:
        counter += 1
        print(counter)

print(counter)
