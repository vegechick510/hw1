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
    assert my_pow(2, "3") == pow(2, 3)
test()