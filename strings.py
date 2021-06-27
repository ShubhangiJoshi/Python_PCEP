#strings are immutable
my_str= "testing"
print ("testing ")

print(id(my_str))

if str(id(my_str)).__eq__(str(id('testing'))):
    print("This is same")
else:
    print (id("testing"))


#length

print(len(my_str))

#indexing

print(my_str[1])
print(my_str[-1]) # reverse way

#my_str [1] = "t"  since immutable string not working
#print(my_str)

print(my_str[1:6])
print(my_str[-1:-6]) # wont work blank op

print(my_str[1:-6]) # wont work blank op

# mystr[1:2:1] --> first index is start index, second index is end index and third index is step index

print(my_str[::-1])

#string encoding

#ord will help getting utf number for character/ hex number
print(ord("\u2125"))

#chr will help getting character related o the number inputted
print(chr(8482))


print(my_str.upper())

#capitalize first letter
print (my_str.capitalize())

#title ()
print ("This is multiline example".title())

#check format

print("hi there {} and {}".format("shubh","joshi"))

my_test = "this is text string bing one"

words = my_test.split()

print(",".join(words))


message = input()

print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title())

words = message.split()


print(",".join(words))

list1 = list(words)
print(list1)
print(sorted(list1)[0])

print(sorted(list1)[-1])




