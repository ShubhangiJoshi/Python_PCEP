count =1
while count<4:
    print(count)
    count+=1

for i in range(10):
    print(1)

strings = "This is string "

for i in strings:
    if i.isspace():
        pass
    else:
        print(i)


list1 = ['1','2',"(3,4,5)","q","string"]

for color in list1:
    if color.isdecimal():
        print("decimal ", color)
    elif color.isalpha():
        print("alpha ",color)
    else:
        print("type not know ", color)



tuple1 = (1,2,[3,4],{"kel":"fruit"})

for ite in tuple1:
    print(ite)

# dicct cn be coded later
dict1= {'key': 'values','[kel,jambhul]':'fruit','3':"WHY"}

#while(dict1.items()!='3'):
#    print("wwew")
#else:
 #   print("no wayy")


my_range = range(1,10,2)

for _ in my_range:
    print(_)

for its in dict1:
    for tes in dict.keys(dict1):
        if tes == "keys":
            print("keys present")
        else:
            print("anything else willbe printed here:", tes)
    else:
        print("no other option")




# loop excersz

for i in range(1,100):
    if (i%3==0 and i%5==0):
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print("other number : ",i)







