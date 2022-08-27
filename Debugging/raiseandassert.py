def printBox(symbol, height, width):
    print(symbol * width)

    if len(symbol) != 1:
        raise Exception('"Symbol" needs to be a string of length 1.')

    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater than 2 or equal to 2. ')

    for i in range(height-2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

print(printBox('o', 10, 20))