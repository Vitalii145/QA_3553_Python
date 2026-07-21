# 1
# def save_shopping_list(items):
#     with open("shopping.txt", "w", encoding="utf-8") as file:
#         for item in items:
#             file.write(item + "\n")
# save_shopping_list(["Milk", "Bread"])
# 2
# import csv
#
# def read_students(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         reader = csv.DictReader(file)
#
#         for row in reader:
#             print(f"Users: {row['name']} ({row['email']}){row['role']} ")
#
# read_students("users.csv")

# 3
# import json
#
# def save_profile(name, age, city):
#     profile = {
#         "name": name,
#         "age": age,
#         "city": city
#     }
#
#     with open("profile.json", "w", encoding="utf-8") as file:
#         json.dump(profile, file, indent=4)
#
# save_profile("Maria", 30, "Haifa")

# 4