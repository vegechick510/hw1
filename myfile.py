def my_pow(a, b):
    if a==0 and b==0:
        return -1
    c = 1
    for i in range(b):
        c = c * a
    return c
assert my_pow(0, 0) == -1
assert my_pow(2, 4) == 16
my_pow(2, "4")