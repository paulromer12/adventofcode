file = open('day3data', 'r')
data = file.readlines()

list = []
bits1 = []
bits2 = []
bits3 = []
bits4 = []
bits5 = []
bits6 = []
bits7 = []
bits8 = []
bits9 = []
bits10 = []
bits11 = []
bits12 = []


for line in data:
    list.append(line.strip('\n'))

#each has 12 bits
#create a list with the 1st charater of each item
for i in list:
    bits1.append(i[0])
for i in list:
    bits2.append(i[1])
for i in list:
    bits3.append(i[2])
for i in list:
    bits4.append(i[3])
for i in list:
    bits5.append(i[4])
for i in list:
    bits6.append(i[5])
for i in list:
    bits7.append(i[6])
for i in list:
    bits8.append(i[7])
for i in list:
    bits9.append(i[8])
for i in list:
    bits10.append(i[9])
for i in list:
    bits11.append(i[10])
for i in list:
    bits12.append(i[11])

zero = 0
one = 0
zero1 = 0
one1 = 0
zero2 = 0
one2 = 0
zero3 = 0
one3 = 0
zero4 = 0
one4 = 0
zero5 = 0
one5 = 0
zero6 = 0
one6 = 0
zero7 = 0
one7 = 0
zero8 = 0
one8 = 0
zero9 = 0
one9 = 0
zero10 = 0
one10 = 0
zero11 = 0
one11 = 0


for i in bits1:
    if int(i) == 0:
        zero += 1
    if int(i) == 1:
        one += 1
for i in bits2:
    if int(i) == 0:
        zero1 += 1
    if int(i) == 1:
        one1 += 1
for i in bits3:
    if int(i) == 0:
        zero2 += 1
    if int(i) == 1:
        one2 += 1
for i in bits4:
    if int(i) == 0:
        zero3 += 1
    if int(i) == 1:
        one3 += 1
for i in bits5:
    if int(i) == 0:
        zero4 += 1
    if int(i) == 1:
        one4 += 1
for i in bits6:
    if int(i) == 0:
        zero5 += 1
    if int(i) == 1:
        one5 += 1
for i in bits7:
    if int(i) == 0:
        zero6 += 1
    if int(i) == 1:
        one6 += 1
for i in bits8:
    if int(i) == 0:
        zero7 += 1
    if int(i) == 1:
        one7 += 1
for i in bits9:
    if int(i) == 0:
        zero8 += 1
    if int(i) == 1:
        one8 += 1
for i in bits10:
    if int(i) == 0:
        zero9 += 1
    if int(i) == 1:
        one9 += 1
for i in bits11:
    if int(i) == 0:
        zero10 += 1
    if int(i) == 1:
        one10 += 1
for i in bits12:
    if int(i) == 0:
        zero11 += 1
    if int(i) == 1:
        one11 += 1

print(zero)
print(one)
print("")
print(zero1)
print(one1)
print("")
print(zero2)
print(one2)
print("")
print(zero3)
print(one3)
print("")
print(zero4)
print(one4)
print("")
print(zero5)
print(one5)
print("")
print(zero6)
print(one6)
print("")
print(zero7)
print(one7)
print("")
print(zero8)
print(one8)
print("")
print(zero9)
print(one9)
print("")
print(zero10)
print(one10)
print("")
print(zero11)
print(one11)

gamma_rate = '100111100011'
epsilon_rate = '011000011100'
gamma_int = int(gamma_rate, 2)
epsilon_int = int(epsilon_rate, 2)
power_consumption = gamma_int * epsilon_int
print(gamma_int, epsilon_int)
print(power_consumption)

binary = '10110'
integer = int(binary, 2)
