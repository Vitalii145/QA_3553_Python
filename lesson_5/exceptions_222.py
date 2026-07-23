# with open("user.json","r",encoding="utf-8") as file:
#     print(file.read())
#
# def div_int(a,b):
#     return a/b
#
# print("Start program")
# rss= div_int(10,0)
# print(rss)
# print("End program")

print("Start program")
try:
    result = 10 / 4
    print(result)

except ZeroDivisionError as e:
    print("An error occurred:" ,e)

print("End program")