x = "awesone"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is "+ x)


def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)