numbers_tuple = (1, 2, 3, 4, 5)
print(numbers_tuple)

tuple1 = (1,2,3,4,5)
tuple2 = (6,7,8,9,10)
print(tuple1)
print(tuple2)
print(tuple1==tuple2)


my_tuple = (1,2,3,4,5)
my_list = list(my_tuple)
my_list[2] = 10
updated_tuple = tuple(my_list)
print("Original tuple: ", my_tuple)
print("Updated tuple: ", updated_tuple)

