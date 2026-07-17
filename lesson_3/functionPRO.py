# def create_user(name,role="user"):
#     return {"name":name,"role":role}
# print(create_user("Bob"))
# print(create_user("John","admin"))
#
#
# def calculate_discount(price,discount_percent=10):
#     return price - (price * discount_percent/100)
# print(calculate_discount(568,25))


def add_test_result(name,results=None):
    if results is None:
        results = []
    results.append(name)
    return results
print(add_test_result("test login"))
print(add_test_result("test_logout"))
print(add_test_result("test_tractor"))


def create_user_22(username,email,role):
    return f"User {username},({email}) with role - {role}"
print(create_user_22("Vitalii","lev@gmail.com","admin"))
print(create_user_22(role="admin",username="Vitalii",email="lev@gmail.com"))