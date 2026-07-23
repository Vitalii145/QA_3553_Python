# 1
# def get_list_elements(items,index):
#     try:
#         return items[index]
#     except IndexError:
#         return "Index out of range"
#
# numbers_2 = [1,2,3,4,5,6,7,8,9]
# print(get_list_elements(numbers_2,5))
# print(get_list_elements(numbers_2,1))
# print(get_list_elements(numbers_2,-1))

2
# def get_user_data(user,key):
#     try:
#         return user[key]
#     except KeyError:
#         return "Key was not found"
#
# user = {
#     "name" : "Anna",
#     "age" : 30
# }
# print(get_user_data(user,"name"))
# print(get_user_data(user,"age"))
# print(get_user_data(user,"email"))
# print(user.get("name"))

# 3
# def calculate_average(first_value, second_value):
#     try:
#         first_value = float(first_value)
#         second_value = float(second_value)
#         return (first_value + second_value) / 2
#     except ValueError:
#         return "Value must be a number"
#     except TypeError:
#         return "Invalid dara type"
#
# print(calculate_average(156, 289))
# print(calculate_average("Hello", 2))
# print(calculate_average(None, 20))
# 4
# def read_number():
#     try:
#         num = int(input("Enter a number: "))
#     except ValueError:
#         print("Invalid number")
#     else:
#         print("Number was entered successfully")
#     finally:
#         print("Program finished")
#
#
# read_number()

# 5
# def validate_age(age):
#     if age <0:
#         raise ValueError("Age cannot be negative")
#     if age > 120:
#         raise ValueError("Age cannot be greater than 120")
#     return age
# print(validate_age(20))
# print(validate_age(26))
# print(validate_age(-10))

