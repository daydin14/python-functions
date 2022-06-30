# minimal functions
def fahr_to_kelvin(temp):
    return ((temp-32) * (5/9)) + 273.15
print(fahr_to_kelvin(70))


def first_function():
    pass
result = first_function()
print(result)

# key differences between python and js
# refer to markdown to see js version 
nums = [1,3,2,6,5]
odds = list( filter(lambda num: num % 2, nums) )
print(odds)

# parameters and arguments
def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def compute (a, b, op):
    return op(a,b)

print( compute(1,2, add))

# accepting a varying number of arguemnts
def f(*args):
    print( type(args) )
    for arg in args:
        print(arg)
f(1,2,'SEI')

def dev_skills(dev_name, *args):
    # args originally stores data as a tuple
    # print(args)
    dev = {'name': dev_name, 'skills': []}
    for skill in args:
        dev['skills'].append(skill)
    return dev
print(dev_skills('David', 'HTML', 'CSS', 'Javascript', 'Python'))

def dev_skills2(dev_name, **kwargs):
    # kwargs = looking for key:value pairs, 
    dev = {'name': dev_name, 'skills': {}}
    # unpackingn the tuples returned by the items function
    for skill, rating in kwargs.items():
        dev['skills'][skill] = rating
    return dev
print(dev_skills2('David', HTML=5, CSS=3, JavaScript=4, Python=2))

def arg_demo(pos1, pos2, *args, **kwargs):
    print(f'Positional params: {pos1}, {pos2}')
    print('*args')
    for arg in args:
        print(' ', arg)
    print('**kwargs:')
    for keyword, value in kwargs.items():
        print(f' {keyword}: {value}')
arg_demo('A', 'B', 1,2,3, color='purple', shape='circle')