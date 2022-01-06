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
oxygen_generator_rating = -1
co2_scrubber_rating = -1


def getGammaEpsilonBinary(bits):
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


getGammaEpsilonBinary(bits)
gamma_int = int(gamma_rate_binary, 2)
epsilon_int = int(epsilon_rate_binary, 2)
power_consumption = gamma_int * epsilon_int
print(f'Gamma is {gamma_int}, Epsilon is {epsilon_int}')
print(power_consumption)

def findOxygenGenerator(bits):
    global oxygen_generator_rating

    oxygen_generator_options = bits
    zero = 0
    one = 0
    good_numbers = []

    for i in range(0, 12):
        zero = 0
        one = 0
        good_numbers = []
        for item in oxygen_generator_options:
            if item[i] == '0':
                zero += 1
            if item[i] == '1':
                one += 1
        if zero > one:
            for item in oxygen_generator_options:
                if item[i] == '0':
                    good_numbers.append(item)
        if one > zero:
            for item in oxygen_generator_options:
                if item[i] == '1':
                    good_numbers.append(item)
        if zero == one:
            for item in oxygen_generator_options:
                if item[i] == '1':
                    oxygen_generator_rating_binary = item
        oxygen_generator_options = good_numbers

    oxygen_generator_rating = int(oxygen_generator_rating_binary, 2)


findOxygenGenerator(bits)

def findCO2Rating(bits):
    global co2_scrubber_rating

    co2_scrubber_options = bits
    zero = 0
    one = 0
    good_numbers = []
    co2_scrubber_rating_binanary = []

    for i in range(0, 12):
        print(f'zeros = {zero}')
        print(f'ones = {one}')
        zero = 0
        one = 0
        good_numbers = []
        print('There are', len(co2_scrubber_options), 'items left.')
        if len(co2_scrubber_options) == 1:
            co2_scrubber_rating = int(co2_scrubber_options[0], 2)
        else:
            for item in co2_scrubber_options:
                if item[i] == '0':
                    zero += 1
                if item[i] == '1':
                    one += 1
            if zero < one:
                for item in co2_scrubber_options:
                    if item[i] == '0':
                        good_numbers.append(item)
            if one < zero:
                for item in co2_scrubber_options:
                    if item[i] == '1':
                        good_numbers.append(item)
            if zero == one:
                for item in co2_scrubber_options:
                    if item[i] == '0':
                        good_numbers.append(item)
            co2_scrubber_options = good_numbers

findCO2Rating(bits)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating


print(oxygen_generator_rating)
print(co2_scrubber_rating)
print(life_support_rating)
