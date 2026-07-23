# #low level- it only performs calculations/ it doesn't interact  with user
# def calculate(a:int,b:int,op:str):
#     if op == '+':
#         return a+b
#     elif op == '-':
#         return a-b
#     elif op == '*':
#         return a*b
#     elif op == '/':
#         return a/b
#     else:
#         return 0
#
# # middle level - parsing. Convert string into numbers
# def pars_and_calc(a_str:str,b_str:str,op:str):
#     a = float(a_str)# value error.
#     b = float(b_str)# ValueError if nor a number
#     return calculate(a,b,op)
#
# # TOP level - dialogue If captures everything and explains it to the user
#
# def run_calculator():
#     try:
#         a = int(input("Enter first number: "))
#         b = int(input("Enter second number: "))
#         op = input("Enter operation: (+,-,*,/:")
#         result = pars_and_calc(a,b,op)
#         print(f"Result: {result}")
#     except ValueError as e:
#         print(f"Invalid data:{e}")
#     except ZeroDivisionError as e:
#         print("You can't divide by zero!")
#
# run_calculator()
#



# def is_number(text):
#     try:
#         float(text)
#         return True
#     except (ValueError, TypeError):
#         return False
#
# print(is_number("wbdlkbV"))
# print(is_number("123d"))
# print(is_number("123"))
# print(is_number("12.3"))

# try:
#     value = int("69")
# except ValueError:
#     print("An error occurred")
# else:
#     print("The transformation was successful: ",value)
# finally:
#     print("This block is always executed")