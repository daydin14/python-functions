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


# Challenge 4