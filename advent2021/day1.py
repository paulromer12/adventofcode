#How many measurements are larger than the previous measurement?


file = open('day1data', 'r')
data = file.readlines()

list = []

for line in data:
    list.append(int(line.strip('\n')))

counter = 0
counter1 = 0

for i, num in enumerate(list):
    if i >= 0 and list[i] > list[(i - 1)]:
        counter += 1
    if i >= 3 and list[i]+list[i-1]+list[i-2] > list[i-1]+list[i-2]+list[i-3]:
        counter1 += 1

print(counter)
print(counter1)
