def fahr_to_kelvin(temp):
    return ((temp-32) * (5/9)) + 273.15
print(fahr_to_kelvin(70))


def first_function():
    pass
result = first_function()
print(result)


nums = [1,3,2,6,5]
odds = list( filter(lambda num: num % 2, nums) )
