my_list = []
print(my_list)

my_list = [1,2,3,4,5]
print((my_list))

other_list = ["1", 2, 4.9, "thsi", "a", 4,0,-1]
print((other_list))

print(my_list[0])

print(my_list[-1])

print(len(other_list))

print(other_list[0::-1])

print(other_list[1:3:])

other_list[0]="new"

print(other_list[:3])

my_list[2:4] = ["this",9.0]

print(my_list[:5])

#del my_list[1]

#del my_list[2:]


my_list [2:4] = [7,9]

my_list[4:7] = [8,6,5]
print(my_list)


###list method

my_list.append(10)
print(my_list)

my_list.insert(0,11)
print(my_list)

print(my_list.index(1))

print( 4 not in my_list)

#print(sorted(other_list)) # wont work as this contain string and int

#print (reversed(other_list)) # wont work due to string and int values

print (list(reversed(my_list)))

print (list(reversed(sorted(my_list))))



########netset lists###########

my_matr = [[1,2,3],[4,5]]

row_count = len(my_matr)

print(row_count)

column_count = len(my_matr[0])

print(my_matr[0])

print(column_count)

print (my_matr[1][1])



list_exe = ["one","two","three"]


new_list = [color.upper() for color in list_exe]

print(new_list)

another_list = [color for color in list_exe if color in ["one", "four" ]]

print(another_list)