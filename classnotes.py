def fahr_to_kelvin(temp):
    return ((temp-32) * (5/9)) + 273.15
print(fahr_to_kelvin(70))


def first_function():
    pass
result = first_function()
print(result)


nums = [1,3,2,6,5]
odds = list( filter(lambda num: num % 2, nums) )
print(odds)


def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def compute (a, b, op):
    return op(a,b)

print( compute(1,2, add))


def f(*args):
    print( type(args) )
    for arg in args:
        print(arg)
f(1,2,'SEI')