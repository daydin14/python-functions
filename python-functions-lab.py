# Challenge 1
print('\n Challenge 1: \n')
def sum_to(n):
    sum = 0
    while (n > 0):
        sum += n
        n -= 1
    return sum
print(sum_to(6))
print(sum_to(10))


# Challenge 2
print('\n Challenge 2: \n')
def largest(list):
    if len(list) == 0:
        return 'You entered an emtpy list :('
    else:
        max = 0
        for num in list:
            if num > max:
                max = num
        return max
print(largest([1,2,3,4,0]))
print(largest([10,4,2,231,91,54]))


# Challenge 3
print('\n Challenge 3: \n')
# First attempt:
# def occurances(str1, str2):
#     if(len(str1) == 0 or len(str2) == 0):
#         return 'You entered at least 1 empty string, please try again.'
#     else:
#         count = 0
#         for idx in enumerate(str1):
#             if str2 in str1:
#                 count += 1
#     return count
def occurances(str1, str2):
    return str1.count(str2)
print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))


# Challenge 4
print('\n Challenge 4: \n')
def product(*args):
    numbers = []
    product = 1
    for number in args:
        numbers.append(number)
        product *= number
    
    return product
print(product(-1,4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))