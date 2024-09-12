print(10>9)
print(10 == 9)
print(10<9)

a = 200
b = 33
if b > a:
    print("b is greater then a")
else:
    print("b is not greater then a")

print(bool("Hello"))
print(bool(15))


bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


x = bool(False)
x = bool(None)
x = bool(0)
x = bool("")
x = bool(())
x = bool([])
x = bool({})
print(x)



class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(myobj)

def myFunction():
    return True
print(myFunction())


def myFunction():
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")
    
x = 200
print(isinstance(x, int))