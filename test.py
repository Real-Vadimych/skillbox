import math
def summa(i):
    return sum(math.log(k) for k in range(1, i+1))

def multipl(i):
    p = 1
    for k in range(1, i+1):
        p *= k      
    return math.log(p)

for i in range(20):
    print(i, summa(i) == multipl(i))