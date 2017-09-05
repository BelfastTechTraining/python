# if
x = [1, 2, 3]
if len(x) > 0:
    print('IF:{0}'.format(x))

# for
for item in x:
    print('FOR:{0}'.format(item))

# while
y = []
i = 0
while len(y) < len(x):
    i += 1
    y.append(i)
print('WHILE:{0}'.format(y))
