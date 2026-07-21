import json
#
# user = {"username":"Egor", "age":30, "is_admin":True}
#
# string_json = json.dumps(user)
# print(string_json)
#
test_cofig={
  "base_url":"https://api.github.com/",
   "timeout":10,
    "retries":5
 }

with open("config.json","w", encoding="utf-8") as file:
    json.dump(test_cofig,file,indent=4,ensure_ascii=False)

with open("config.json","r", encoding="utf-8") as file:
    loaded_config = json.load(file)
    print(loaded_config)
    print(loaded_config["base_url"])