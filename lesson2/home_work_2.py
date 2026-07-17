1
def print_list_reverse(lst):
    if lst is None or not isinstance(lst, list) or lst == []:
        print("Wrong list")
    else:
        print(lst[::-1])

print_list_reverse([1, 2, 3, 4, 5])
2
def is_valid_point(point):
    if point is None or point ==():
        return None
    if not isinstance(point, tuple):
        return False
    if len(point) != 2:
        return False
    if not isinstance(point[0], (int, float)):
        return False
    if not isinstance(point[1], (int, float)):
        return False
    return True
print(is_valid_point((2, 5)))
print(is_valid_point((3, "5")))
print(is_valid_point([3, 5]))
print(is_valid_point((1, 2, 3)))
print(is_valid_point(()))
print(is_valid_point(None))
3
def print_sublist_reverse(lst, start, finish):
    if lst is None or lst == []:
        print("Wrong args")
    elif not isinstance(lst, list):
        print("Wrong args")
    elif not isinstance(start, int) or not isinstance(finish, int):
        print("Wrong args")
    elif start < 0 or finish >= len(lst) or start > finish:
        print("Wrong args")
    else:
        lst[start:finish + 1] = lst[start:finish + 1][::-1]
        print(lst)

print_sublist_reverse([10, 20, 30, 40, 50, 60], 1, 3)
print_sublist_reverse([10, 20, 30, 40, 50, 60], 3, 5)

4
def get_students_by_grade(students):
    if students is None or students == [] or not isinstance(students, dict):
        return {}

    results = {}
    for name in students:
        grade = students[name]
        if grade not in results:
            results[grade] = []
        results[grade].append(name)
    return results

students = {
    "Alice": 90,
    "Bob": 85,
    "Diana": 90,
    "Charlie": 85
}

print(get_students_by_grade(students))

