def my_pow(a, b):
    if a==0 and b==0:
        return -1
    elif b==0:
        return 1
    c = 1
    for i in range(b):
        c = c * a
    return c
ans = my_pow(2, "4")