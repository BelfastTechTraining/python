title: Python Exercises
theme: ../styles/cleaver-dark
author:
  name: Matt Mulhern
  email: mattmulhern01@gmail.com
output: python_exercises.html

--

###ex1-1.py
Write a program that inputs a 4 digit year and then calculates whether or not it is a leap year.

--

###ex1-2.py
Using a variation of the above program, calculate the number of days in the inclusive date range '1st January 2000' to '31st December 2999'.

--

###ex1-3.py
Write a program that prints out the square, cubes and fourth power of the first 20 integers.

--

###ex1-4.py
Write a program that prints out the first 20 Fibonacci numbers.  You can use the web to find out the definition of the Fibonacci sequence.

--

###ex1-5.py
Write a program that calculates the ratio of successive pairs of the first 20 Fibonacci numbers.
Does the ratio appear to converge to a number?

--

###ex2-1.py
Write a program that prints out the sum, difference, product and dividend of two numbers.

--

###ex2-2.py
Use the split() function to split a fullname such as `Julius Caesar` into two strings called firstName and lastName.

--

###ex2-3.py
Use the range function to generate two separate tuples containing the list of integers from 10 to 19 and from 30 to 39.

Tuples are immutable, so how can you form a tuple that has all the elements of the other two tuples?

--

###ex2-4.py
int(x[,radix]) converts a string to an int using the supplied radix.

Use this function to compute the decimal value of the binary number `101010101010101010101`

--

###ex2-5.py
Create a dictionary consisting of people's names and salaries.

Initialise the dictionary with at least 5 pairs of names and salaries. Now print the dictionary.

Why is the printed order different from the order you used to initialise the dictionary?

--

###ex3-1.py
Write a function that calculates the area of a rectangle.
Decide how many input parameters your function needs.

The area should be returned from the function.

Write a test program that calls your function with different sets of test data.

--

###ex3-2.py
Write a function that rotates the values of 3 variables.  For example:

```
    x = 100
    y = 200
    z = 300
    Rotate( ... )
    # x is now 200
    # y is now 300
    # z is now 100
```
--

###ex3-3.py
Write a function to calculate Factorials.  

A Factorial number is the product of all positive integers less than n, e.g.

factorial(5) = 1 x 2 x 3 x 4 x 5

Try out:

```
    factorial(1)
    factorial(10)
    factorial(40)
    factorial(100)
```
--

###ex3-4.py
Write a function that takes a string and capitalises the first character of the string and ensures the remaining characters are converted to lower case.

Use the following test data:

```
    UpperFirst("test1")
    UpperFirst("mIxEdCaSe")
    UpperFirst("UPPER")
    UpperFirst("lower")
    UpperFirst("oPPOSITE")
```

--

###ex3-5.py
How do you find the intersection of 2 lists (i.e. those elements common to both lists)?

--
###ex3-6.py
Write a function that takes an integer list as a parameter and doubles the value of each element of the array.

--

###ex3-7.py
Write a function that takes two int arrays (same size) as parameters and adds the arrays together, element by element.

Print out the array as part of the function.

--

###ex3-8.py
Modify the previous example to return the sum of the two input arrays instead of printing the result.

--

###ex4-1.py
Write a program that calculates the factorial of an integer in the range 2 to 10.

Add exception handling code to prevent calculating a result where the input number is larger than 10, or any negative integer.

Make sure you can handle the case where the input is not an integer.

--

###ex5-1.py
Write a program that counts the number of lines in a file.

--

###ex5-2.py
Write a file copy program

--

###ex5-3.py
Create a file call TestData.txt with test data consisting of one number per line using your favourite editor.
Your job is to read the entire file into memory so that you can compute the sum of all the numbers.

--

###ex5-4.py
Try the previous example with other test files that may contain non integral data.
Use exception handling to filter out lines that don't contain integers.

--

###ex5-5.py
Write a program that concatenates three files into a new file.

--

###ex5-6.py
Write a program that reads a file, reverses the order of lines in the file and then saves the changes in a new file.

--

###ex6-1.py
Create two subroutines that convert a decimal number in the range 1 to 4000 to Roman numerals, and back.

Warning: This question is rather more difficult than it looks!

Don't spend too much time on it.

*Hints:*
* Use two dicts to map:
    * letters to numbers
    * 1-9,10's, 100's and 1000's to letters
* Use a toRoman() and toDecimal() function for clarity.
* Typical algo for toDecimal():
    * Break letters into an array and iterate through:
        * If a symbol is less than it's sucessor then negative so flip it's sign (apending converted decimal to new array.
    * Summing your new array should give you the decimal number.

--

###ex6-2.py
Words prefixes are also called stems.

e.g. of the words 'dog', 'doable' and 'dodecahedron' the stem is 'do'.

Write a program that reads a file with one word per input line and finds the most popular stems of size 2 to 6.

--
