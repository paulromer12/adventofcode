# Get data and remove new line from each item, save data in array bits
file = open('day3data', 'r')
data = file.readlines()

bits = []

for line in data:
    bits.append(line.strip('\n'))

#convert binary to decimal -> int(variable, 2)
#output variables needed
gamma_rate_binary = ''
epsilon_rate_binary = ''


def getGammaBinary(bits):
    global gamma_rate_binary
    global epsilon_rate_binary
    zero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    one = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


    for item in bits:
        k = 0
        for i in item:
            if i == '0':
                zero[k] += 1
            elif i == '1':
                one[k] += 1
            k += 1

    for i in range(0, 12):
        if zero[i] > one[i]:
            gamma_rate_binary = gamma_rate_binary + '0'
        elif one[i] > zero[i]:
            gamma_rate_binary = gamma_rate_binary + '1'

    for i, v in enumerate(gamma_rate_binary):
        if v == '0':
            epsilon_rate_binary = epsilon_rate_binary + '1'
        if v == '1':
            epsilon_rate_binary = epsilon_rate_binary + '0'

    print(gamma_rate_binary)
    print(epsilon_rate_binary)

getGammaBinary(bits)


gamma_int = int(gamma_rate_binary, 2)
epsilon_int = int(epsilon_rate_binary, 2)
power_consumption = gamma_int * epsilon_int
print('Gamma is ',gamma_int, 'Epsilon is ',epsilon_int)
print(power_consumption)
