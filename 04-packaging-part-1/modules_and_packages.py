{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "# Packaging\n",
    "\n",
    "In this lesson we'll learn about\n",
    "* Modules\n",
    "* Packages\n",
    "* Sub packages\n",
    "* What directory structure to use for your packages\n",
    "* How to write a setup.py file\n",
    "* How to install packages\n",
    "* Adding exectuables to your packages"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Modules\n",
    "\n",
    "### What?\n",
    "\n",
    "Packages and modules are used in python to facilitate modular programming. \n",
    "\n",
    "Modular programming is a software design technique that emphasizes separating the functionality of a program into independent, interchangeable modules, such that each contains everything necessary to execute only one aspect of the desired functionality. [Wikipedia](https://en.wikipedia.org/wiki/Modular_programming)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Why?\n",
    "\n",
    "This brings several advantages:\n",
    "\n",
    "1. Simplicity: It's much easier to focus on one small part of a problem rather than the whole program at once. You just need to understand how the section you are looking at works rather than the entire code base.\n",
    "\n",
    "2. Maintainability: When you break up a problem into many smaller problems, typically each piece of code is logically separated from the others. This means making changes to one module is less likely to impact the operations of the others. Meaning many people can work on a project without effecting each other, it's even possible that you have no idea how the rest of the application works, but can understand the module you are working on.\n",
    "\n",
    "3. Reusability: Smaller pieces of code that do one (or a small number of) thing can easily be reused elsewhere. This allows you to reuse the code in the application, or even outside of the application in other solutions that are being developed.\n",
    "\n",
    "4. Scoping: We can resuse variable and function names by using separate namespaces. This means that we have less chance of having name collisions in our application."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### How can we use them?\n",
    "\n",
    "There are 3 different types of module that can be used in python, normally when creating your own, it will be the first. \n",
    "\n",
    "1. A pure python module\n",
    "2. A C/C++ module that is compiled and loaded at run time. (e.g. numpy)\n",
    "3. A built-in module that is part of the interpretter. (asyncio)\n",
    "\n",
    "The implementation is abstracted from us when we use them in python. They are all brought in using the same keyword `import`.\n",
    "\n",
    "To create a pure python module all we need to do is create a file with some python code in it and name it with the `.py` extension."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "quotes.py\n",
    "\n",
    "```python\n",
    "single_quote = \"Easy things make life harder, hard things make life easier\"\n",
    "multi_quote = [\"Collect underpants\", \"?\", \"Profit\"]\n",
    "\n",
    "def foo():\n",
    "    print(\"bar\")\n",
    "    \n",
    "class Bar():\n",
    "    pass\n",
    "```\n",
    "\n",
    "In the quotes module we have defined a string, a list, a function and a class.\n",
    "\n",
    "We can then use these later (assuming your setup is correct, which we'll come to)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Easy things make life harder, hard things make life easier\n",
      "['Collect underpants', '?', 'Profit']\n",
      "bar\n",
      "<quotes.Bar object at 0x7f6db82c09b0>\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import quotes\n",
    "\n",
    "print(quotes.single_quote)\n",
    "\n",
    "print(quotes.multi_quote)\n",
    "\n",
    "quotes.foo()\n",
    "\n",
    "my_class = quotes.Bar()\n",
    "print(my_class)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### sys.path\n",
    "\n",
    "When you run the command\n",
    "\n",
    "```python\n",
    "import quotes\n",
    "```\n",
    "\n",
    "The interpreter will search for a file called `quotes.py` in\n",
    "\n",
    "1. The current directory (or directory in which the script resides).\n",
    "2. If set, a list of directories in the environment variable `PYTHONPATH`.\n",
    "3. A list of directories configured at installation time for your python environment. Installation time includes when a new virtual environment is created."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "The list of directories can be seen in python using the sys module\n",
    "\n",
    "```python\n",
    "import sys\n",
    "print(sys.path)\n",
    "```\n",
    "```bash\n",
    "['', '/Users/mrobinson/source/work/training/python/venv/lib/python37.zip', '/Users/mrobinson/source/work/training/python/venv/lib/python3.7', '/Users/mrobinson/source/work/training/python/venv/lib/python3.7/lib-dynload', '/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Users/mrobinson/source/work/training/python/venv/lib/python3.7/site-packages']\n",
    "```\n",
    "\n",
    "So the easiest way to get your module recognised is to put it in the same directory as the script you are running.\n",
    "\n",
    "You *can* modify your sys.path, but it's generally not recommended."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Using import (and namespaces)\n",
    "#### Simplest form\n",
    "\n",
    "There are many ways we can use import, the simplest is \n",
    "```python\n",
    "import some_module\n",
    "```\n",
    "\n",
    "When importing in this fashion, the symbol table (the list of functions, variables, class) are not loaded into our namespace. This means to reference any of the symbols from the module we must prefix with the module name and a `.`, this is called *dot notation*.\n",
    "\n",
    "```python\n",
    "import some_module\n",
    "\n",
    "some_module.some_function()\n",
    "print(some_module.some_variable)\n",
    "```\n",
    "\n",
    "If you don't do this you will see a `NameError: name 'something' is not defined` error.\n",
    "\n",
    "It is possible, though *not* recommended to load several modules on the same line by using commas\n",
    "\n",
    "```python\n",
    "import re, sys, requests, pandas\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### Using the from keyword\n",
    "This allows us to import specific parts of a module and adds it directly to our namespace, if we go back to our quotes example."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Collect underpants', '?', 'Profit']\n",
      "Work is the curse of the drinking classes.\n"
     ]
    }
   ],
   "source": [
    "from quotes import multi_quote\n",
    "print(multi_quote)\n",
    "print(single_quote)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can see here, we have not used the *dot notation* when referencing multi_quote. But also, we have not been able to print the single_quote as it's not been imported.\n",
    "\n",
    "It is fine to import multiple things from a single module using commas while using from\n",
    "\n",
    "```python\n",
    "from my_lib import some_function, function_some, funct_some_oin\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "When importing modules this way, because we're adding to the global namespace, things can be overwritten. Take this next example."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Easy things make life harder, hard things make life easier\n"
     ]
    }
   ],
   "source": [
    "single_quote = \"Work is the curse of the drinking classes.\"\n",
    "\n",
    "from quotes import single_quote\n",
    "\n",
    "print(single_quote)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This would not be the case if we had just `import quotes`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Work is the curse of the drinking classes.\n",
      "Easy things make life harder, hard things make life easier\n"
     ]
    }
   ],
   "source": [
    "single_quote = \"Work is the curse of the drinking classes.\"\n",
    "\n",
    "import quotes\n",
    "\n",
    "print(single_quote)\n",
    "print(quotes.single_quote)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "You can also import everything from a module by using a `*`, however this is *very bad* idea. You can see from the above example that if we imported everything from a module, it would be very easy to overwrite something we already have defined. \n",
    "\n",
    "There are other reasons you shouldn't `from blah import *`, such as readability and traceability. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### Using the as keyword\n",
    "\n",
    "There are two ways this can be used. In both ways you are importing somethings `as` another name, such as the name suggests. \n",
    "\n",
    "This allows you to change the name it is reference by in your namespace. \n",
    "\n",
    "This can be useful for packages with long names or if you already have something in the namespace with the same name. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Easy things make life harder, hard things make life easier \n",
      " ['Collect underpants', '?', 'Profit']\n",
      "<quotes.Bar object at 0x7f6db82c0dd8>\n"
     ]
    }
   ],
   "source": [
    "from quotes import single_quote as single, multi_quote as multi, Bar as Foo\n",
    "\n",
    "print(f\"{single} \\n {multi}\")\n",
    "print(Foo())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bar\n"
     ]
    }
   ],
   "source": [
    "import quotes as things_someone_else_said\n",
    "\n",
    "things_someone_else_said.foo()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### dir()\n",
    "\n",
    "This is a very useful built in function that can show the current symbol table. It can be exectuted on an object by passing it in, or executed on the current namespace by running it with no arguments."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Foo',\n",
       " 'In',\n",
       " 'Out',\n",
       " '_',\n",
       " '__',\n",
       " '___',\n",
       " '__builtin__',\n",
       " '__builtins__',\n",
       " '__doc__',\n",
       " '__loader__',\n",
       " '__name__',\n",
       " '__package__',\n",
       " '__spec__',\n",
       " '_dh',\n",
       " '_i',\n",
       " '_i1',\n",
       " '_i10',\n",
       " '_i11',\n",
       " '_i12',\n",
       " '_i13',\n",
       " '_i2',\n",
       " '_i3',\n",
       " '_i4',\n",
       " '_i5',\n",
       " '_i6',\n",
       " '_i7',\n",
       " '_i8',\n",
       " '_i9',\n",
       " '_ih',\n",
       " '_ii',\n",
       " '_iii',\n",
       " '_oh',\n",
       " 'exit',\n",
       " 'get_ipython',\n",
       " 'less_eggs',\n",
       " 'module4',\n",
       " 'multi',\n",
       " 'multi_quote',\n",
       " 'my_class',\n",
       " 'package',\n",
       " 'quit',\n",
       " 'quotes',\n",
       " 'single',\n",
       " 'single_quote',\n",
       " 'things_someone_else_said']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dir()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Bar',\n",
       " '__builtins__',\n",
       " '__cached__',\n",
       " '__doc__',\n",
       " '__file__',\n",
       " '__loader__',\n",
       " '__name__',\n",
       " '__package__',\n",
       " '__spec__',\n",
       " 'foo',\n",
       " 'multi_quote',\n",
       " 'single_quote']"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import quotes\n",
    "dir(quotes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### Scripts\n",
    "\n",
    "Any file that ends in a .py can also be a script. The problem with this is that when we import a module, all the python code inside that module is executed at run time.\n",
    "\n",
    "So if we had a script like this:\n",
    "\n",
    "```python\n",
    "local_zealot = 'Wizard'\n",
    "\n",
    "def main():\n",
    "    print(f\" We're off to see the {local_zealot}\")\n",
    "    \n",
    "main()\n",
    "```\n",
    "\n",
    "and we wanted to import it in another application so we could reuse the `local_zealot` variable, we'd get this printed to screen once it was imported:\n",
    "\n",
    "```\n",
    "We're off to see the Wizard\n",
    "```\n",
    "\n",
    "You may have see the following code in places\n",
    "\n",
    "```python\n",
    "if __name__ == '__main__':\n",
    "    main()\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "This is to prevent against code running when we don't want it to. So in this case, we could import the module to get the `local_zealot` variable in one app. But we could still run the module (script) to use it's orginal functionality. The finished script would look like this :\n",
    "\n",
    "```python\n",
    "local_zealot = 'Wizard'\n",
    "\n",
    "def main():\n",
    "    print(f\" We're off to see the {local_zealot}\")\n",
    "    \n",
    "if __name__ == '__main__':\n",
    "    main()\n",
    "```\n",
    "\n",
    "This is of course a trivial example, but if you had a large set of functions and classes in the file you can see how this could be useful. \n",
    "\n",
    "Often this is used for unit testing, where the part that is run via the if statement, executes the tests. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "## Packages\n",
    "\n",
    "Once the number of modules in project grows, it can become a bit messy if they're all in one directory. This is where packages come in. \n",
    "\n",
    "Packages are a way to organise modules and namespaces. For all intents and purposes, a package is a file system directory that contains a number of modules. \n",
    "\n",
    "They allow hierarchical structure using *dot notation*. If we have the following: \n",
    "\n",
    "```bash\n",
    "package/\n",
    "├── module1.py\n",
    "└── module2.py\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "module1.py\n",
    "```python\n",
    "def eggs():\n",
    "    print('[module1] eggs()')\n",
    "\n",
    "class Egg:\n",
    "    pass\n",
    "```\n",
    "module2.py\n",
    "```python\n",
    "def spam():\n",
    "    print('[module2] spam()')\n",
    "\n",
    "class Spam:\n",
    "    pass\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "This means we can use the import in the same way we have before"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[module1] eggs()\n",
      "[module2] spam()\n"
     ]
    }
   ],
   "source": [
    "import package.module1, package.module2\n",
    "\n",
    "package.module1.eggs()\n",
    "package.module2.spam()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[module1] eggs()\n"
     ]
    }
   ],
   "source": [
    "from package.module1 import eggs\n",
    "eggs()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'package.module2.Spam'>\n"
     ]
    }
   ],
   "source": [
    "from package.module2 import Spam as lunch\n",
    "\n",
    "print(lunch)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "You can import the whole package, but this doesn't really do anything. This is because it *does not add the modules in the package to the local namespace*."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'package' has no attribute 'module1'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-6-4b75c994a3cd>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpackage\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mpackage\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmodule1\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0meggs\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: module 'package' has no attribute 'module1'"
     ]
    }
   ],
   "source": [
    "import package\n",
    "\n",
    "package.module1.eggs()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There is a way around this though, which we'll talk about next. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### __init__.py\n",
    "\n",
    "This is a special file that you may have sometimes seen in a python project. When you import a package, this file is run before anything else happens, i.e. initialisation.\n",
    "\n",
    "Let have a look at a new package, called imaginatively, new_package.\n",
    "\n",
    "```bash\n",
    "new_package/\n",
    "├── __init__.py\n",
    "├── module1.py\n",
    "└── module2.py\n",
    "```\n",
    "\n",
    "The two modules are the same, but inside the `__init__.py` we have\n",
    "\n",
    "```python\n",
    "print(f\"Running __init__.py from {__name__}\")\n",
    "import new_package.module1, new_package.module2\n",
    "```\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "So now when we import it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Running __init__.py from new_package\n",
      "[module1] eggs()\n"
     ]
    }
   ],
   "source": [
    "import new_package\n",
    "\n",
    "new_package.module1.eggs()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can see that it runs the code in `__init__`, meaning our two modules have been imported. \n",
    "\n",
    "Any arbitrary code can be placed inside this file, though it's generally not recommended to put too much in there. Definitely don't put any application logic in there."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "-"
    }
   },
   "source": [
    "Prior to python 3.3 it was a requirement to have a `__init__.py` in any package, this is no longer the case. \n",
    "\n",
    "Now we have the concept of [Implicit Namespace Packages](https://www.python.org/dev/peps/pep-0420/).\n",
    "\n",
    "You can still include them, and of course if you need to do some actual initialisation you need to include it.\n",
    "\n",
    "Most of the time I still include them anyway."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Subpackages\n",
    "\n",
    "We can create a nested structure to any depth using sub packages. If we look at another package, this time with four modules in it:\n",
    "\n",
    "```bash\n",
    "final_package/\n",
    "├── sub_package1\n",
    "│   ├── module1.py\n",
    "│   └── module2.py\n",
    "└── sub_package2\n",
    "    ├── module3.py\n",
    "    └── module4.py\n",
    "```\n",
    "\n",
    "we can import in the same manner as before, using the *dot notation*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[module3] more_eggs()\n",
      "<final_package.sub_package2.module4.CanOSpam object at 0x7f6db8272668>\n"
     ]
    }
   ],
   "source": [
    "import final_package.sub_package2.module3\n",
    "from final_package.sub_package2.moule4 import CanOSpam\n",
    "\n",
    "final_package.sub_package2.module3.more_eggs()\n",
    "print(CanOSpam())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "#### Relative and absolute imports\n",
    "\n",
    "If you need to reference something in module 1 from module 3 you can use an absolute import\n",
    "\n",
    "module3.py\n",
    "```python\n",
    "from final_package.sub_package1.module1 import eggs\n",
    "def more_eggs():\n",
    "    print('[module3] more_eggs()')\n",
    "\n",
    "class BigEgg:\n",
    "    pass\n",
    "\n",
    "def less_eggs():\n",
    "    eggs()\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[module1] eggs()\n"
     ]
    }
   ],
   "source": [
    "from final_package.sub_package2.module3 import less_eggs\n",
    "\n",
    "less_eggs()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "You can also use relative imports to do the same thing, this time we reference module 2 from module 4\n",
    "\n",
    "module4.py\n",
    "```python\n",
    "from ..sub_package1.module2 import spam\n",
    "def more_spam():\n",
    "    print('[module4] more_spam()')\n",
    "\n",
    "class CanOSpam:\n",
    "    pass\n",
    "\n",
    "def one_spam():\n",
    "    spam()\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[module2] spam()\n"
     ]
    }
   ],
   "source": [
    "from final_package.sub_package2 import module4\n",
    "\n",
    "module4.one_spam()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "### Creating your own package\n",
    "\n",
    "\n",
    "So, the first thing to do when you want to make your own package is more likely than not come up with a name for it. \n",
    "\n",
    "This is not in the interests of vanity, but you're going to have to name the repository after it and some of the directories, so you should probably come up with it first. \n",
    "\n",
    "There are a few things to consider though, python module/package names should generally follow the following constraints:\n",
    "\n",
    "* All lowercase\n",
    "* Unique on pypi, even if you don’t want to make your package publicly available (you might want to specify it privately as a dependency later)\n",
    "* Unique on internal repos (artifactory)\n",
    "* Underscore-separated or no word separators at all (don’t use hyphens)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "The next thing your probably going to do is to set out your directory structure. Here is an example of the CMDB library we looked at in a previous lesson:\n",
    "\n",
    "```bash\n",
    "essentials_cmdb\n",
    "├── CHANGELOG.md\n",
    "├── README.md\n",
    "├── credentials.example\n",
    "├── essentials_cmdb\n",
    "│   ├── __init__.py\n",
    "│   ├── core.py\n",
    "│   ├── genders.py\n",
    "│   ├── hosts.py\n",
    "│   └── i2csshrc.py\n",
    "```\n",
    "```bash\n",
    "├── other\n",
    "│   ├── make_defs.sh\n",
    "│   └── resources.py\n",
    "├── releaseNotes.sh\n",
    "├── requirements.txt\n",
    "├── setup.py\n",
    "├── tests\n",
    "│   └── test_core.py\n",
    "└── tools\n",
    "    ├── README.md\n",
    "    ├── change_roles.py\n",
    "    ├── cmdb-gen-localfiles.py\n",
    "    ├── cmdb-tk-requirements.txt\n",
    "    └── cmdb-tk.py\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "subslide"
    }
   },
   "source": [
    "This example is probably overkill, but lets have a quick look at it\n",
    "\n",
    "* The top level `essentials_cmdb` is the root of our git repo\n",
    "* It has a subdir `essentials_cmdb` which is the actual python module.\n",
    "* The README is in the top level\n",
    "* The requirements are in the top level\n",
    "* It has separate tools, tests and other directories."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "fragment"
    }
   },
   "source": [
    "So lets say we wanted the least amount of setup we could get away with. We only have one file that we want to publish. We could have\n",
    "\n",
    "```bash\n",
    "my_project\n",
    "├── my_project\n",
    "│   ├── __init__.py\n",
    "│   └── cmdb.py\n",
    "└── setup.py\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Now we have our layout, we need a way to tell python how to install the package. This is done using the setup.py. Here's a simple one we could use to install the above package:\n",
    "\n",
    "```python\n",
    "from setuptools import setup\n",
    "\n",
    "setup(name='my_project',\n",
    "      version='0.1',\n",
    "      description='The best project ever',\n",
    "      url='http://github.com/fakeuser/my_project',\n",
    "      author='Mr. Bean',\n",
    "      author_email='doc@who.com',\n",
    "      license='MIT',\n",
    "      packages=['my_project'],\n",
    "      zip_safe=False)\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "slideshow": {
     "slide_type": "slide"
    }
   },
   "source": [
    "Now you should be able to install it to your system with\n",
    "\n",
    "```bash\n",
    "pip install .\n",
    "```\n",
    "\n",
    "or as I mentioned in the last lesson, you can install it in editable mode. (creates symlinks so you can still edit the installed version)\n",
    "\n",
    "```bash\n",
    "pip install -e .\n",
    "```\n",
    "\n",
    "You should probaly be installing these in a virtual environment at this stage. You're going to iterate over the install of this package a lot. If it's done inside a virtual env, you can easily delete the dir and not leave a lot of mess lying around you OS. "
   ]
  }
 ],
 "metadata": {
  "celltoolbar": "Slideshow",
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
