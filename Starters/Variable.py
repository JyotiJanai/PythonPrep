# Variable declaring in Python
mystring = "hello"
myfloat = 10.0
myint = 20

print("mystring: %s" % mystring)
print("Myfloat: %f" % myfloat)
print("My integer: % d" % myint)


def dummy():
    global x
    x = "Easy"
    print("Python is " + x)


dummy()
print("Python is " + x)
