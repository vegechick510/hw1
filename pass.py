def my_pow(a, b):
    print("a: {}, b: {} \nCalculating a^b...".format(a, b))
    if a==0:
        return -1
    elif b==0:
        return 1
    else:
        c = 1
        for i in range(b):
            c = c * a
    return c
def test():
    assert my_pow(1, 2) == pow(1, 2)
test()