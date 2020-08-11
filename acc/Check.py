def Check(num1, num2):
    value = False
    dict = {}
    for i in range(num1, num2):
        value = False
        l = list(bin(i))
        print(l)
        for k in range(2, len(l) - 1):
            if l[k] == '1' and l[k + 1] == '1':
                value = True

        dict[i] = value
    return dict