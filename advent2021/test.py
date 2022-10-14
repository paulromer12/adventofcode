bits = ['10', '01', '10']

def findOxygenGenerator(bits):
    global oxygen_generator_rating

    oxygen_generator_options = bits
    zero = 0
    one = 0
    good_numbers = []


    while len(oxygen_generator_options) > 1:
        for i in range(0, 12):
            print(f'zeros = {zero}')
            print(f'ones = {one}')
            zero = 0
            one = 0
            print('There are', len(oxygen_generator_options), 'items left.')
            if len(oxygen_generator_options) == 1:
                oxygen_generator_rating = oxygen_generator_options[0]
            else:
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

    print(oxygen_generator_rating)




findOxygenGenerator(bits)
