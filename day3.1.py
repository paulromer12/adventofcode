# Get data and remove new line from each item, save data in array bits
file = open('day3data', 'r')
data = file.readlines()

bits = []

for line in data:
    bits.append(line.strip('\n'))

gamma_rate_binary = ''
epsilon_rate_binary = ''

#convert binary to decimal -> int(variable, 2)
