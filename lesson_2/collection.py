shoppinig_cart = ['orange', 'apple','lemon']
mixed = [2,'orange',None,True,4.58]
print(shoppinig_cart[0])

shoppinig_cart[1] = 'blueberry'
print(shoppinig_cart)

fruits = ['apple','orange','lemon','peach']
first,second,third,fourth = fruits
print(first)
print(second)
print(third)
print(fourth)

print(len(fruits))

numbers = [1,2,3,4,5]
print(sorted(numbers,reverse=True))
print(sorted(fruits,reverse=True))


fruits = ['apple','orange','lemon','peach']
fruits.append('watermelon')
print(fruits)

fruits.insert(1,'pupa')
print(fruits)
first_fruits_index = fruits.index('apple')
print(f"The index of 'apple' is {first_fruits_index}")


deleted = fruits.pop(2)
print(deleted)
print(fruits)