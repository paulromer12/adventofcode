file = open('day3data', 'r')
data = file.readlines()

list = []
bits1 = []

for line in data:
    list.append(line.strip('\n'))

#each has 12 bits

for i in list:
    bits1.append(list[0])

gamma_rate = 0
epsilon_rate = 0
power_consumption = gamma_rate * epsilon_rate

binary = '10110'
integer = int(binary, 2)

print(bits1)
