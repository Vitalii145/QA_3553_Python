# 1
# def save_shopping_list(items):
#     with open("shopping.txt", "w", encoding="utf-8") as file:
#         for item in items:
#             file.write(item + "\n")
# save_shopping_list(["Milk", "Bread", "Apple", "Coffee"])
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
from pathlib import Path


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
def create_reports_folder():
    reports_dir = Path("reports_1")
    reports_dir.mkdir(exist_ok=True)
    result_file = reports_dir/"result.txt"
    with open(result_file, "w",encoding="utf-8") as file:
        file.write("Homework completed successfully!")

create_reports_folder()