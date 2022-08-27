def sqaure_digits(num):
    words = list(str(num))
    for word in words:
        print(int(word)**2, end="")

sqaure_digits(9119)
