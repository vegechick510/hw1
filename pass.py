def my_pow(a, b):
    print("a: {}, b: {} \nCalculating a^b...".format(a, b))
    assert a!=0
    c = 1
    for i in range(b):
        c = c * a
    return c
def test():
    c = my_pow(2, 3)
<<<<<<< HEAD
    assert c == pow(2, 3)
test()
=======
    assert c == pow(2, 3)
>>>>>>> 84641c6 (change pytest)
