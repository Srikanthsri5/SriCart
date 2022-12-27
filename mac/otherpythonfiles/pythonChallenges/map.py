# li = [1,2,3,4,5,6,7,8,9]
#
# cubedli = list(map(lambda x: x*x*x,li))
# print(cubedli)
li = [1,2,3,4,5,6,7,8]
def evenn(n):
    if n%2==0:
        return n
    else:
        pass

def oddn(n):
    if n%2!=0:
        return n

vari = [evenn, oddn]
for i in li:
    evodd = list(map(lambda x : x(i),vari))
    print(evodd)