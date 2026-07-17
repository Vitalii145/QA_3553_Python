def print_config(**kwargs):
    print(type(kwargs), kwargs)

print(print_config(browser = "chrome",headless = True,timeout = 30))

def create_user(**data):
    return data

user = create_user(name ='John', role = 'user')
print(user)

def example(a,b=10,*args,**kwargs):
    print(a,b,args,kwargs)
example(1,2,3,45, name='Anna')


