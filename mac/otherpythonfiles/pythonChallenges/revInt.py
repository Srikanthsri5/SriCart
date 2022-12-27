n = int(input("enter an integer: "))
n1 = n
rev = 0
while n > 0:
    n1 = n % 10
    rev = rev*10+n1
    n //= 10
print("reversed is ", rev)