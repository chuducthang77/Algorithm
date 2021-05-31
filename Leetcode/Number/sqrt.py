def mySqrt(x):
    i = 0
    while True:
        if i*i == x:
            return i
        elif i*i > x:
            return i - 1
        i += 1
    return i 

print(mySqrt(0))
print(mySqrt(1))
print(mySqrt(10))