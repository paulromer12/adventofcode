def addToLists():
    x = ['1', '2', '1', '2', '1', '2', '1', '2', '1', '2', '1', '2', ]
    zero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    one = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    length = len(zero)
    k = 0

    for i in x:
        if i == '1':
            zero[k] += 1
        else:
            one[k] += 1
        k += 1
        # for i in item:
        #     index = index + 1
        #     if i == '0':
        #         zero[index] += 1
        #     if i == '1':
        #         one[index] += 1

    print(zero)
    print(one)

addToLists()
