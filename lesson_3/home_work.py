# 1.
# def create_profile(name,age=18,city='Unknown'):
#     return {'name':name,'age':age,'city':city}
# print(create_profile("Anna Bordo"))
# print(create_profile(name="Tom",age=18))
# print(create_profile(city="Berlin",name="Shurle"))
from calendar import month

# 2.
# def sum_even_numbers(*numbers):
#     total = 0
#     for n in numbers:
#         if n % 2 == 0:
#             total += n
#     return total
#
# print(sum_even_numbers(1,2,3,4,5))
# print(sum_even_numbers(7,9))
# print(sum_even_numbers())
#
# def sum_odd_numbers(*numbers):
#     return sum(filter(lambda n: n % 2 ==0, numbers))
# print(sum_odd_numbers(1,2,3,4,5,6))
# print(sum_even_numbers(7,9))
# print(sum_even_numbers())
# print()
#
# 3.
# def print_pet_info(name,**info):
#     print(f"Name:{name} ")
#     if not info:
#         print("No additional info")
#         return
#     for k,v in info.items():
#         print(f"{k}:{v}")
#
# print_pet_info(
#     "Lucky",
#     age = "5 month",
#     color = "black",
#     breed = "border-colly"
#          )
#
# def merge_lists(*lists):
#     result = []
#
#     for current_list in lists:
#         for item in current_list:
#             result.append(item)
#
#     return result
# print(merge_lists(
#     [1,25],
#     [47,87],
#     [123],
#     []
# ))

def build_message(*words,separator=' '):
    return separator.join(words)
print(build_message("Hello,world"))
print(build_message())
print(build_message("2026","07","16",separator="-"))