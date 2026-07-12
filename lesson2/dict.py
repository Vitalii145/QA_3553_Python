student = {
    "name": "Alex",
    "age": 25
}

import random

d = {
    f"key{i}": random.randint(1, 100)
    for i in range(5)
}

for key, value in d.items():
    print(key, value)