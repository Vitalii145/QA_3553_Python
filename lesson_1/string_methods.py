name = 'Alice'
age = 22

form_string = f" Hello my name is {name} and  I am  {age} years old"
print(form_string)

d = 'Abrakadabra'
str = 'bra'
print(d.find(str))
print(d.rfind(str))
print(d.find('mmmmm'))

s = 'Hi!'
print(s.rjust(10,'*'))
print(s.ljust(10,'*'))

test = ["Login", "Cart", "API"]
for t in test:
    print(t.ljust(10), "OK")
