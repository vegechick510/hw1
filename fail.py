def my_pow(a, b):
    print("a: {}, b: {} \nCalculating a^b...".format(a, b))
    if a==0 and b==0:
        # return print("Nonsense!")
        return -1
    c = 1
    for i in range(b):
        c = c * a
    # print("Output of a^b: {}^{} = {}".format(a, b, c))
    return c


print("This is a test file!")
c = my_pow("2", 3)
assert c == pow(2, 3)

# c = my_pow(0, 0)
# assert c == 0