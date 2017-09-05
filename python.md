title: Python
theme: ./styles/cleaver-dark
author:
  name: Matt Mulhern
  email: mattmulhern01@gmail.com
output: index.html

--

# Python Basics
## A quick primer on the scripting language.


_Generated using [cleaver](https://github.com/jdan/cleaver)_
--

* Introduction to Python
* Control Structures
* Basic Data Types
* Advanced Data Types
* Dictionaries
* Functions
* Exception Handling
* Classes
* Files
* Larger Programs
* Pattern Matching

--

###  Introduction to Python
* General purpose high level scripting language:
* Emphasis placed on
    * Human Readability.
    * Self describing code.

*from PEP-20 - The Zen of Python*:
```
 Beautiful is better than ugly
 Explicit is better than implicit
 Simple is better than complex
 Complex is better than complicated
 Readability counts
```

--

###  Introduction to Python - *Hello World*
Python can be run in two ways, either in **The Python Interpreter**:

*hello.py*:
```python
print('Hello World!')
```
```bash
> python hello.py
Hello World!
```
or in an *Interactive shell*:
```bash
> python
Python 2.7.9 (default, May  1 2015, 19:04:44)
[GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.49)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World!")
Hello World!
>>> exit()
```
** Try doing the following in an interactive shell**:
```python
import this
```


--

###  Basic Data Types
* Everything is an object.
    * Interpreter can be left to decide what a variable is.
    * Explicit casts are available (int(), str() etc) but are not recommended.

*variables.py*
```python
i = 2
f = 0.33
s = "This is a string"

print(s)
print(f * i)
```

```bash
> python variables.py
This is a string
0.66
```

--

###  Basic Data Types - *String Ms = 'Since everything\'s an object, strings have methods for manipiulation'anipulation*
Since everything is an object, strings have builtin methods for modification.

*strings.py*
``` python
s = 'Since everything\'s an object, strings have methods for manipiulation'
print(s)
print(s.rstrip('manipiulation'))
print(s.upper())
print(s.lower())
print(s.swapcase())
```
```
> python strings.py
Since everything's an object, strings have methods for manipiulation
Since everything's an object, strings have methods for
SINCE EVERYTHING'S AN OBJECT, STRINGS HAVE METHODS FOR MANIPIULATION
since everything's an object, strings have methods for manipiulation
sINCE EVERYTHING'S AN OBJECT, STRINGS HAVE METHODS FOR MANIPIULATION
```

--

###  Sequence Data Types - *Lists*
* As described, lists are a collection of objects.
* Behave in the same way as c arrays, but with the benifits of being an object in themselves!
* Lists are **mutable**.
* Can be added to with .append() and concanated with .extend()

*list.py*
```python
list_1        = [1, 2, 3, 4]
list_2        = ['a', 'b', 'c', 'd']
list_specials = [['a'], (1, 2, 3), False]

print('{0} is of length {1}'.format(list_1, len(list_1)))

list_1.append(5)
print('{0} is of length {1}'.format(list_1, len(list_1)))

list_1.extend(list_2)
print('{0} is of length {1}'.format(list_1, len(list_1)))

print('{0} is of length {1}'.format(list_specials, len(list_specials)))
```
```
> python list.py
[1, 2, 3, 4] is of length 4
[1, 2, 3, 4, 5] is of length 5
[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd'] is of length 9
[['a'], (1, 2, 3), False] is of length 3
```

--

###  Sequence Data Types - *Tuples*
* Similar to lists except that they are **immutable**!
* Cannot be modified once created.
* Useful when returning more than one thing from *functions* (see later).

*tuple.py*
```python
x1 = ()
x2 = (1,)
x3 = (1, 2, 3)
x4 = (1, "mixed", 2, "tuple")
x5 = ((1, 2), (3, 4))

print('{0} is of length {1}'.format(x1, len(x1)))
print('{0} is of length {1}'.format(x2, len(x2)))
print('{0} is of length {1}'.format(x3, len(x3)))
print('{0} is of length {1}'.format(x4, len(x4)))
print('{0} is of length {1}'.format(x5, len(x5)))
```
```
> python tuple.py
()  is of length  0
(1,)  is of length  1
(1, 2, 3)  is of length  3
(1, 'mixed', 2, 'tuple')  is of length  4
((1, 2), (3, 4))  is of length  2
```

--

###  Sequence Data Types - **Dictionaries**
* Used to store **key value pairs**.
* Not stored in any particular order, left up to interpreter to order when inserting/accessing.
* Values can be accessed/updated by refering to dictionary's key.

*dict.py*
```python
d = {}
d['name'] = 'Matt'
d['job'] = 'something or other'

print(d)
print(d.keys())
print('my name is{0}'.format(d['name']))
print('and i do {0}'.format(d['job']))
```
```
> python dict.py
{'job': 'something or other', 'name': 'Matt'}
['job', 'name']
my name is Matt
and i do something or other
```

--

###  Control Structures
#### IF
Only execute statement(s) if condtion is met.

```python
x = [1, 2, 3]
if len(x) > 0:
    print('IF:{0}'.format(x))
```

#### FOR
Iterates through items in collection (set, list, tuple etc...)

```python
for item in x:
    print('FOR:{0}'.format(item))
```

#### WHILE
Keep executing statement(s) until condition is not met.

```python
y = []
i = 0
while len(y) < len(x):
    i += 1
    y.append(i)
print('WHILE:{0}'.format(y))
```

```
IF:[1, 2, 3]
FOR:1
FOR:2
FOR:3
WHILE:[1]
WHILE:[1, 2]
WHILE:[1, 2, 3]
```
--

###  Functions
* Used to logically seperate off common code.
* Can return value(s) to calling function.

```python
def add_up(num_list):
    x = 0
    for i in num_list:
        x += i
    return x


# our script starts running from here.
nums = [1, 2, 3, 4, 5, 6]
print('The sum of {0} is {1}'.format(nums, add_up(nums)))
```

```
The sum of [1, 2, 3, 4, 5, 6] is 21
```
--

###  Exception Handling
* Gracefully handle problems occuring in execution.
* exceptions are signals sent from interpreter at time of problem.
* Unless handled, they will cause a program to crash, displaying the exception.

```python
x = 3
print(x / 0)
```

```
> python exception.py
Traceback (most recent call last):
  File "exception.py", line 2, in <module>
    print(x / 0)
ZeroDivisionError: integer division or modulo by zero
```
* Exceptions can be used by wrapping code in try / except statements.

```python
x = 3
try:
    print(x / 0)
except ZeroDivisionError:
    print("You're trying to print by zero, this isnt allowed!")
```

```
> python exception.py
You're trying to print by zero, this isnt allowed!
```

--

###  Classes
* Used to group together variables/classes logically (usually into a model of something).
* All the types we have been using are classes!

*class.py*
```python
class TrainingGroup:
    # class members
    date = ''
    participants = []

    # class methods
    def __init__(self, date, participants):
        self.date = date
        self.participants = participants

    def __str__(self):
        return '{0} participants on {1}'.format(len(self.participants), self.date)

    def kick_member(self, idiot):
        new_members = []
        for member in self.participants:
            if idiot != member:
                new_members.append(member)
            else:
                print('kicking {0}'.format(idiot))
        self.participants = new_members


group = TrainingGroup('2015-08-10', ['Tom', 'Dick', 'Harry'])
print(group)
print(group.participants)
group.kick_member('Dick')
print(group)
print(group.participants)
```

```
> python class.py
3 participants on 2015-08-10
['Tom', 'Dick', 'Harry']
kicking Dick
2 participants on 2015-08-10
['Tom', 'Harry']
```

--

###  Files
*file.py*
```python
infile  = open('testfile.txt', 'r')       # opened for reading only
outfile = open('file.output.txt', 'w')    # opened for writing
for line in infile.readlines():
    outfile.write(line)
```

```
> python file.py

> cat file.output.txt
this
is
is
a
test
file
```

Files can be opened in different *modes*:

|||
|:--|:-------------------------------------------------------------------------------------------------------------------|
|r  |Open text file for reading. The stream is positioned at the beginning of the file.                                  |
|r+ |Open for reading and writing. The stream is positioned at the beginning of the file.                                |
|w  |Truncate file to zero length or create text file for writing. The stream is positioned at the beginning of the file.|
|w+ |Open for reading and writing.  The file is created if it does not exist, otherwise it is truncated.  The stream is  |
|   |positioned at the beginning of the file.                                                                            |
|a  |Open for writing.  The file is created if it does not exist. The stream is positioned at the end of the file.       |
|   |Subsequent writes to the file will always end up at the then current end of file.                                   |
|a+ |Open for reading and writing. The file is created if it does not exist.  The stream is positioned at the end of the |
|   |file.  Subsequent writes to the file will always end up at the then current end of file.                            |

--

###  Larger Programs - *Using Modules*
* Large codebases can be broken up into seperate files.
* *Calling* functions calling functions from another file need to have **imported** them before use.
* Good practice to cut down on *code replication*.
* Importing a file causes **all code in the file to be executed**.
    * Need to be wary of code not within a function
    * Can *guard* against this code by wrapping it in `if __name__ == '__main__':`

*mymodule.py*
```python
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
```

```
> python mymodule.py
The sum of [1, 2, 3, 4, 5] is 15
Stripping 'Tom' from {'Harry': 'The Third', 'Dick': 'The Second', 'Tom': 'The First'} gives us {'Dick': 'The Second', 'Harry': 'The Third'}
```

Notice how just importing the module doesn't execute the test code:

```
> python
Python 2.7.9 (default, May  1 2015, 19:04:44)
[GCC 4.2.1 Compatible Apple LLVM 6.1.0 (clang-602.0.49)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mymodule
>>> dir(mymodule)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'prune_dict', 'sum_numeric_list']
```

--

###  Larger Programs - *Using Modules*
After importing the module, you can now use it's functions without the test code being called:

*import py:*
```python
import mymodule

from mymodule import prune_dict

nums = [6, 7, 8, 9]
print('SUM:{0}'.format(mymodule.sum_numeric_list(nums)))

dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = prune_dict(dict, 'b')

print('dict:     {0}'.format(dict))
print('new_dict: {0}'.format(new_dict))
```

```
> python import.py
SUM:30
dict:{'a': 1, 'c': 3, 'b': 2}
new_dict:{'a': 1, 'c': 3}
```
--

###  Pattern Matching
* Regex matching is done via built in `re` module.
* re.search - *look for pattern anywhere within string*
* re.match  - *look for exact pattern match in string*
* regex's can be pre-compiled for optimisation *see example*


*regex cheat sheet*:

|||
|------:|:--------------------------------------------------------------------------|
|^      |start of string                                                            |
|$      |end of string                                                              |
|[abc]  |Any one character from list (a OR b OR c)                                  |
|[a-m]  |Any one character from range (a OR b OR ... OR m)                          |
|[^abc] |Any one character not in list (NOT a NOR b NOR c)                          |
|.      |Any one character                                                          |
|\s     |Any white space character                                                  |
|\S     |Any NON white space character                                              |
|\d     |Any digit                                                                  |
|\D     |Any NON digit                                                              |
|\w     |Any alphanumeric                                                           |
|\W     |Any NON alphanumeric                                                       |
|()     |Group together matches within parentheses (use with re.search().group()).  |

--

###  Pattern Matching
*matching.py*

```python
import re
string = 'The quick brown fox jumps over the laxy dog.'

print('search:      {0}'.format(re.search('The quick brown fox', string)))
print('search_gr0:  {0}'.format(re.search('The quick brown fox', string).group(0)))

print('match:       {0}'.format(re.match('quick (brown) fox', string)))
print('match_gr0:   {0}'.format(re.match('\S* quick (brown) fox', string).group(0)))
print('match_gr1:   {0}'.format(re.match('\S* quick (brown) fox', string).group(1)))

regex = re.compile('^[\S\s]*(over) (the)[\s\S]*')
print('compiled_match_gr0:  {0}'.format(regex.match(string).group(0)))
print('compiled_match_gr1:  {0}'.format(regex.match(string).group(1)))
print('compiled_match_gr2:  {0}'.format(regex.match(string).group(2)))
```

```
> python matching.py
search: <_sre.SRE_Match object at 0x10938acc8>
search_gr0: The quick brown fox
match: None
match_gr0: The quick brown fox
match_gr1: brown
compiled_match_gr0 The quick brown fox jumps over the laxy dog.
compiled_match_gr1 over
compiled_match_gr2 the
```

--

###  Debugging - PDB
* Drops script into interactive console either when:
    * Interpreter hit `pdb.set_trace()` function.
    * Interpreter hits an *unhandled* exception (if script called with `python -m pdb <script.py>`
* Same as an interactive python shell any commands/functions you like can be called manually to test.

*basic controls:*

|||
|------:|:------------------------------|
|l      | show code at current frame    |
|c      | continue code execution       |
|bob    | prints variable 'bob'         |
|Ctrl-c | quit script as usual          |

--
### What Now?
Have a go at the [exercises](https://belfasttechtraining.github.io/python-intro/exercises).
 --
