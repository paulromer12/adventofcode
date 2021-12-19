file = open('day3data', 'r')
data = file.readlines()

list = []
bits1 = []

for line in data:
    list.append(line.strip('\n'))

#each has 12 bits
#create a list with the 1st charater of each item
for i in list:
    bits1.append(i[0])

zero = 0
one = 0
for i in bits1:
    if int(i) == 0:
        zero += 1
    if int(i) == 1:
        one += 1

if zero > one:
    print("There are more zeros. " + str(zero))
else:
    print("There are more ones. " + str(one))


gamma_rate = 0
epsilon_rate = 0
power_consumption = gamma_rate * epsilon_rate

binary = '10110'
integer = int(binary, 2)
