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
<<<<<<< HEAD
c = my_pow("2", 3)
assert c == pow(2, 3)
=======
print("This is a test file!")
assert pow(1, 2)==my_pow(1, "2")
>>>>>>> 86a1654 (change actions & files)
