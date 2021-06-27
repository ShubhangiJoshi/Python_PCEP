my_tuples = (1,2,3,[4,5,6])

x,y,z = my_tuples[3]

print( "this is tuple %s",my_tuples)

print (my_tuples)

#my_tuples[1] = ([7,8,9])  cn not update tuple

print(my_tuples)

new_my_tuple = my_tuples + (1.0,2.0)

print (new_my_tuple)

#list in tuple
my_tuples[3].append([8.0,"Te",'a'])

print(my_tuples[3][3][2])

#tuple in list

my_list = ["1","wew",3,(3.0,4.14),10]

print(my_list[3][1])




