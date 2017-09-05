list_1        = [1, 2, 3, 4]
list_2        = ['a', 'b', 'c', 'd']
list_specials = [['a'], (1, 2, 3), False]

print('{0} is of length {1}'.format(list_1, len(list_1)))

list_1.append(5)
print('{0} is of length {1}'.format(list_1, len(list_1)))

list_1.extend(list_2)
print('{0} is of length {1}'.format(list_1, len(list_1)))

print('{0} is of length {1}'.format(list_specials, len(list_specials)))
