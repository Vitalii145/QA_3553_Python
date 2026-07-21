with open("users.txt","w+",encoding="utf-8") as file:
    file.write("tony\n")
    file.write("ivan\n")
    file.write("jack\n")

# with open("users.txt","r",encoding="utf-8") as file:
#     content = file.read()
# print(content)


with open("users.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
print(lines)


for line in lines:
    print(line.strip())
