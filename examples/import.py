import mymodule

from mymodule import prune_dict

nums = [6, 7, 8, 9]
print('SUM:{0}'.format(mymodule.sum_numeric_list(nums)))

dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = prune_dict(dict, 'b')

print('dict:     {0}'.format(dict))
print('new_dict: {0}'.format(new_dict))
