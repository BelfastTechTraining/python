def add_up(num_list):
    x = 0
    for i in num_list:
        x += i
    return x


# our script starts running from here.
nums = [1, 2, 3, 4, 5, 6]
print('The sum of {0} is {1}'.format(nums, add_up(nums)))
