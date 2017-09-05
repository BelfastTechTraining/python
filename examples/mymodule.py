def sum_numeric_list(nums):
    """
    Accepts a list of numeric values.
    Returns the sum of the elements.
    """
    sum = 0
    for item in nums:
        sum += item
    return sum


def prune_dict(dict, keys_to_remove):
    """
    Accepts a dict to priune and a list of keys to remove.
    Matching keys are deleted and rmainders returned.
    """
    pruned_dict = {}
    for key in dict.keys():
        if key not in keys_to_remove:
            pruned_dict[key] = dict[key]

    return pruned_dict


if __name__ == '__main__':
    test_ints = [1, 2, 3, 4, 5]
    print('The sum of {0} is {1}'.format(test_ints, sum_numeric_list(test_ints)))

    test_dict = {'Tom': 'The First', 'Dick': 'The Second', 'Harry': 'The Third'}
    pruned_dict = prune_dict(test_dict, 'Tom')
    print('Stripping \'Tom\' from {0} gives us {1}'.format(test_dict, pruned_dict))
