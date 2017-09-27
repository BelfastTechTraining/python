#!/usr/bin/env python3
"""
###ex3-5.py
How do you find the intersection of 2 lists (i.e. those elements common to both lists)?

Use the following test data:
```
list_a = ["a", "b", "1", [1, 2, 4], ["a", "b"], [1, 2, 4], "foo", "bar", ("this", 1, 4)]
list_b = ["a", "1", [1, 2, 4], "foo", ("this", 1, 4)]
```
"""


def find_intersection(lista, listb):
    common = []

    for item in lista:
        if item in listb and item not in common:  # 'not in common' is to avoid duplicate entries in common[]
            common.append(item)
    return common


if __name__ == '__main__':  # 'main' function
    list_a = ["a", "b", "1", [1, 2, 4], ["a", "b"], [1, 2, 4], "foo", "bar", ("this", 1, 4)]
    list_b = ["a", "1", [1, 2, 4], "foo", ("this", 1, 4)]
    print("list_a = {0}".format(list_a))
    print("list_b = {0}".format(list_b))
    common_elements = find_intersection(list_a, list_b)
    print("common_elements = {0}".format(common_elements))
