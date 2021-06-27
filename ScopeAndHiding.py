y = 10


def NameHiding(y):
    x = y
   # global y    --> this line would thrwo error since passed parameter is with same name
    y = x
    print (y)

NameHiding(15)

print (y)


def NameGlobalHding(z):
    x = z
    global a
    global y
    y = x
    a = 7

print (y) # set at the start hence 10
NameGlobalHding(20)
print(y) #set above hence 20
print(a) # set in function but global hence 7