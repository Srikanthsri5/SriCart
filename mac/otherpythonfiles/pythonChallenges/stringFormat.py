def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        print("{} {} {} {}".format((str(i).rjust(width)), (str(oct(i)[2:]).rjust(width)),
                                   (str(hex(i)[2:]).upper().rjust(width)), (str(bin(i)[2:]).rjust(width))))

        print(i, "{0:o}".format(i), hex(i), "{0:b}".format(i))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)