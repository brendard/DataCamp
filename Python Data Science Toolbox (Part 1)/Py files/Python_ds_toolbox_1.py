# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:12:15 2023

@author: Brenda Rojas Delgado

Course: Python Data Science Toolbox (Part 1)

In this course you will learn to:
    
    a) Define functions with no parameters
    b) Define functions with one parameter
    c) Define functions that return a value
    d) Later: multiple arguments, multiple return values
    
Basic ingredients of a function:
    
    a) Function header
    b) Function body

Types of functions:
    
    a) Scope function:
    
    In this type of function, not all objects are accessible everywhere in a 
    script. The types of scope are:
        - Global scope: defined in the main body of a script
        - Local scope: defined inside a function
        - Built-in scope: names in the pre-defined built-in models (e.g print)
    
    Global vs. local scope:
        
        new_value=10             <- Global scope
        
        def square(x):           
            new_value=x**2       
            return new_value     <- Local scope
                                 
       square(3)  
       [Out]=9
       
       new_value (if not defined globally before the function)
       NameError: name 'new_value' is not defined
       Not accessible because it is defined within the local scope of the function
       
       new_value (if defined globally before the function)
       10
       
       If global and local scopes are combined
       
       new_value=10              #<- Global scope
       
       def square(x):           
           global new_value     # <- Keyword for altering the value of a global
                                # call within a function
           new_value2=new_value**2       
           return new_value2     #<- Local scope
                                
      square(3)  
      [Out]=100

    b) User-defined function: 
    
Built-in functions' examples:
    
    a) str(), which accepts an object such as a number and returns a string object
    b) def square(), which is a user-defined function, starting with the keyword
    def and later accompanied by the name given to the function to be defined
    c) Docstrings(), what describes what your function does. The depicted 
    descriptions serve to document your function, and this command is placed
    in the immediate line after the function header in between triple-double 
    quotes 

A function is created with the next sequence:
    
    def square():            #<- Function header (in this case with no parameters)
        new_value=4**2       #<- Function body
        print(new_value)     # To call the function, simply write down square() 
                             either in the console or in the file
    square()    
    
If you want to write the same function with one parameter, you can simply assign
the parameter inside the parentheses of the same function.

    def square(x):           #<- Function header (in this case with one parameter)
        new_value=x**2       #<- Function body
        print(new_value)     # To call the function, simply write down square() 
                             either in the console or in the file
   square(x)   
   
If you want to add more than one parameter to the same function, simply do this:
    
    def square(x,y):         #<- Function header with parameters x and y
        new_value=x**y       #<- Function body
        print(new_value)     # To call the function, simply write down square() 
                             either in the console or in the file
    square(x,y)
    
You can also return values from a function. That is, you can return the square 
value and assign it to some variable:

    def square(base,exp):            
        new_value=base**exp       
        return new_value    
    
    base=4; exp=2; square(base,exp) 

    An alternative way to call square(base,exp) that works with the return keyword
    num=square(base,exp)
    print(num)
    
It is important to remember that assigning a variable y2 to a function that prints 
a value but does not return a value will result in that variable y2 being of a type 
NoneType.

Multiple function parameters:
    
    a) Accept more than one parameter (see square(x,y) and square(base,exp) 
    examples above)
    b) Call function: # arguments= # parameters
    c) Make functions return multiple values: tuples
                                       
A quick jump into tuples

Tuples are like a list and can contain multiple values. Tuples are inmutable: 
you cannot modify values once the tuple is constructed.

Tuples are constructed using parentheses, while lists are constructed using 
squared brackets and dictionaries using curly brackets.

A tuple is unpacked into several variables:
    
    even_nums=(2,4,6)
    a,b,c=even_nums

You can access tuple elements the same way you do with lists

    a) print(even_nums[1])
    b) second_num=even_nums[1], print(second_num)

Nested functions' structure:
    
    def outer(...):
        """ '...' """
        x=...
        
        def inner(...):
            """ '...' """
            y=x**2
        return...

Returning functions:
    
    def raise_val(n):
        """ 'Returns the inner function' """
            
        def inner(x):
            """'Raises x to the power of n' """
            raised=x**n
            return raised
        return inner

Using nonlocal:
    
    The nonlocal keyword is used to create and change names in an enclosing 
scope

def outer():
    """ 'Prints the value of n' """
    n=1
    
    def inner():
        nonlocal n
        n=2
        print(n)
        
    inner()
    print(n)

Functions with default and flexible arguments:
    
    a) Add a default argument
                                       
    def power(number,pow=1):
        """ 'Raise a number to the power of pow.' """
        new_value=number**pow
        return new_value

    power(9,2)
    
Functions with flexible arguments are used when writing a function, there are
uncertainties about how many arguments to pass through, or when you want to
process compatible data types (e.g., floats with ints)

    def all_args(*args):
        """ 'Sum all values in *args together' """
        
        # Initialize sum
        sum_all=0
        
        # Accumulate the sum
        for num in args:
            sum_all+=num
        
        return sum_all    
    
    all_args(arg1,arg2,..,argn)
    
You can also use a double star to pass an arbitrary number of keyword arguments
called kwargs, that is, arguments preceded by identifiers. 

    def print_all(**kwargs):
        """ 'Print out key-value pairs in kwargs' """
        
        # Print out the key-value pairs
        for key, value in kwargs.items():
            print(key+":"+value)
    
    print_all(name="Brenda Rojas Delgado", course="DataCamp")
    
Generalized functions:
    
    a) Count occurrences for any column
    b) Count occurrences for an arbitrary number of columns
                                       
Lambda functions are functions written with the keyword lambda. With this type
of functions, you can write the function body in the function header

    raise_to_power=lambda x,y:x**y
    
    raise_to_power(2,3)

Although it is not advised to use lambda functions all the time, they come in 
very handy when dealing with other types of functions, such as anonymous 
functions. In such cases, we can pass lambda functions to another one without
naming them. That is why these are called anonymous functions. 

    nums=[48,6,9,21,1]
    
    square_all=map(lambda num:num**2,nums) #<-map(function,sequence)
    
    print(square_all)  # It prints a map object

    print(list(square_all)) # It prints what is contained in the map object

The function filter() offers a way to filter out elements from a list that 
don't satisfy certain criteria.

The reduce() function is useful for performing some computation on a list and, 
unlike map() and filter(), returns a single value as a result. To use reduce(),
you must import it from the functools module.

Errors and exceptions:
    
    a) Exceptions - caught during execution
    b) Catch exceptions with a try-except clause
       - Runs the code following the try
       - If there is an exception, run the code following except
                    
"""

" Import the necessary libraries "
# Import pandas
import pandas as pd

# Import reduce from functools
from functools import reduce 

" User-defined functions "

# Write a function square that gives the square value of a number and print it out
# Type it with no parameters

def square():     
    """Return the square of a value."""       
    new_value=4**2       
    print(new_value)    
square() 

print(square.__doc__)  # This command line returns the function description

# Type the same function with the parameter base. Print it out
# Type it with no parameters

def square(base):            
    new_value=base**2       
    print(new_value)    

base=4; square(base) 

# Type the same function with base and exponent as parameters. Print it out
# Type it with no parameters

def square(base,exp):            
    new_value=base**exp       
    print(new_value)    

base=4; exp=2; square(base,exp) 

# Return a value from the last function using the return keyword instead of print

def square(base,exp):           
    """Return the square of a value."""
    new_value=base**exp       
    return new_value    

base=4; exp=2; square(base,exp) 

# Alternative way to call square(base,exp) that works with return keyword
num=square(base,exp)
print(num)

# print(square(base,exp).__doc__)

# Define the function shout
def shout():
    """ Print a string with three exclamation marks"""
    # Concatenate the strings 'congratulations'+'!!!': shout_word
    shout_word='congratulations'+'!!!'

    # Print shout_word
    print(shout_word)

# Call shout
shout()

# Define shout with the parameter, word
def shout(word):
    """ Print a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word = word + '!!!'

    # Print shout_word
    print(shout_word)

# Call shout with the string 'congratulations'
shout('congratulations')

# Define shout with the parameter, word
def shout(word):
    """Return a string with three exclamation marks"""
    # Concatenate the strings: shout_word
    shout_word=word+'!!!'

    # Replace print with the return
    return(shout_word)

# Pass 'congratulations' to shout: yell
yell=shout('congratulations')

# Print yell
print(yell)

" Multiple function parameters - Part 1 "

# Define the same square function with the raise power specification

def raise_power(base,exp):
    """ Raise base value to its exponent."""
    raise_power=base**exp            
    return raise_power     # The function header and body can be named the same

base=2; exp=6; raise_power(base,exp) #or 
result=raise_power(base,exp); print(result)

# Modify the raise_power function to return a tuple

def raise_both(value1,value2):
    """ Raise value1 to the power of value2 and viceversa."""
    new_value1=value1**value2   
    new_value2=value2**value1 
    
    new_tuple=(new_value1,new_value2)
    
    return  new_tuple    

value1=2; value2=6; raise_both(value1,value2) #or 
result=raise_both(value1,value2); print(result)

" Functions with multiple parameters - Part 2 "

# Define shout with parameters word1 and word2
def shout(word1, word2):
    """ Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1=word1+'!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2=word2+'!!!'
    
    # Concatenate shout1 with shout2: new_shout
    new_shout=shout1=shout1+shout2

    # Return new_shout
    return new_shout

# Pass 'congratulations' and 'you' to shout(): yell
yell=shout('congratulations','you')

# Print yell
print(yell)

" Unpacking tuples "

# Unpack nums into num1, num2, and num3
num1=3; num2=4; num3=6
nums=[num1,num2,num3]
num1,num2,num3=nums

# Try to assign the number 2 to the first element of the tuple nums
#nums[0]=2 #makes mutable the first tuple created, but not the second one
#new_num=nums[0]=2 # makes changes on both tuples
new_num=2 # makes changes on the second tuple, but not in the first one

# TypeError: 'tuple' object does not support item assignment (on DataCamp)
# However, in Spyder console does not throw an error. Are tuples mutable here?

# Construct even_nums

#even_nums=[num1,num2,num3]
even_nums=[new_num,num2,num3]

" Functions that return multiple values (using tuples) "

# Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    
    # Concatenate word1 with '!!!': shout1
    shout1=word1+'!!!'
    
    # Concatenate word2 with '!!!': shout2
    shout2=word2+'!!!'
    
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words=(shout1,shout2)

    # Return shout_words
    return shout_words

# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = shout_all('congratulations', 'you')

# Print yell1 and yell2
#print(yell1)
#print(yell2) # or

print(yell1,yell2)

" Bringing it all together - Part 1 "

# Open tweets CSV file

tweets=pd.read_csv(r"C:\Users\LENOVO\OneDrive - Universidad Carlos III de Madrid\DataCamp courses\Python Data Science Toolbox (Part 1)\Datasets\tweets.csv",decimal=',')

# Initialize an empty dictionary: langs_count
langs_count = {}

# Extract column from DataFrame: col
col = tweets['lang']

# Complete the bodies of the if-else statements in the for loop: if the key is 
# In the dictionary langs_count, add 1 to the value corresponding to this key 
# In the dictionary, else add the key to langs_count and set the corresponding 
# value to 1. Use the loop variable entry in your code.

# Iterate over the lang column in DataFrame
for entry in col:

    # If the language is in langs_count, add 1 
    if entry in langs_count.keys():
         langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
         langs_count[entry] =1

# Print the populated dictionary
print(langs_count)

" Bringing it all together - Part 2 "

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry]+=1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry]=1

    # Return the langs_count dictionary
    return langs_count

# Call count_entries(): result
result=count_entries(tweets, 'lang')

# Print the result
print(result)

" Global and local scope combined within a function "

new_value=10              #<- Global scope
 
def square(x):           
     new_value2=new_value**2       
     return new_value2     #<- Local scope
                          
square(3) 

# If new_val is re-assigned with the number 20
new_value=20; square(new_value)

" Global keyword within a function call "

new_value=10              #<- Global scope
 
def square(value):           
     global new_value
     new_value=new_value**2       
     return new_value     #<- Local scope
                          
new_value=30; square(3) # With global keyword, having or not a parameter is 
                        # indifferent, as well as assigning or not the function
                        # with the same name as the global scope variable (input)
                        
" Changing the global variable inside the local scope "

## Example 1
num=5

def func1():
    num = 3
    print(num)
    
func1()

def func2():
    global num
    double_num = num * 2
    num = 6            # <- If enabled, changes the variable num globally
    print(double_num)
    
func2(); print(num)                 

## Example 2
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in the global scope
    global team

    # Change the value of the team globally: team
    team="justice league"

# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)

" Nested functions - Part 1 "

# Write mod2plus as a non-nested function

def mod2plus5(x1,x2,x3):
    """ Returns the remainder plus 5 of three values. """
    
    new_x1=x1%2+5
    new_x2=x2%2+5
    new_x3=x3%2+5
    
    return (new_x1,new_x2,new_x3)

new_x1=2; new_x2=3; new_x3=4; mod2plus5(new_x1,new_x2,new_x3)

# Re-write mod2plus as a nested function

def mod2plus5(x1,x2,x3):
    """ Returns the remainder plus 5 of three values. """
    def inner(x):
        """ Returns the remainder plus 5 of a value. """
        return x%2+5
    return (inner(x1),inner(x2),inner(x3))

# Choose one of the options to print out the result of the nested function
x1=2; x2=3; x3=4; mod2plus5(x1,x2,x3) # or
print(mod2plus5(2,3,4)) # or
result=mod2plus5(x1,x2,x3); print(result) # or
result=mod2plus5(2,3,4); print(result) 

" Returning functions "

# Define raise_val
def raise_val(n):
    """ Returns the inner function."""

    # Define inner
    def inner(x):
        """ Raises x to the power of n."""
        raised=x**n
        return raised

    # Return inner
    return inner

square=raise_val(2)
cube=raise_val(3)
print(square(2),cube(4))


# Define echo
def echo(n):
    "Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """ Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

" Using nonlocal - Example 1 "

def outer():
    """ 'Prints the value of n' """
    n=1
    
    def inner():
        nonlocal n
        n=2
        print(n)
        
    inner()
    print(n)

outer()

" Nested functions - Part 2 "

# Define three_shouts
def three_shouts(word1, word2, word3):
    """ Returns a tuple of strings
    concatenated with '!!!'."""

    # Define inner
    def inner(word):
        """ Returns a string concatenated with '!!!'."""
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

" Nested functions - Part 3 \
The keyword nonlocal and nested functions"

# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    
    # Concatenate word with itself: echo_word
    echo_word=word*2
    
    # Print echo_word
    print(echo_word)
    
    # Define inner function shout()
    def shout():
        """ Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word+'!!!'
    
    # Call function shout()
    shout()
    
    # Print echo_word
    print(echo_word)

# Call function echo_shout() with argument 'hello'
echo_shout('hello')

" Default arguments "

def power(number,pow=1):          # number and pow are the function arguments
                                  # pow is the default argument
    """ 'Raise a number to the power of pow.' """
    new_value=number**pow
    return new_value

power(9,2) # Here the default argument can be changed, although being predefined
power(9)

" Flexible arguments - *args - Option 1 "

def all_args(*args):
    """ 'Sum all values in *args together' """
    
    # Initialize sum
    sum_all=0
    
    # Accumulate the sum
    for num in args:
        sum_all+=num
           
    return sum_all 

result=all_args(7,4.2,3,8.85); print(result)

" Flexible arguments - *args - Option 2  (passes a list as multiple arguments"

def all_args(*args):
    """ 'Sum all values in *args together' """
    
    # Initialize sum
    sum_all=0
    
    # Accumulate the sum
    for num in args:
        sum_all+=sum(num)
    
    return sum_all 

arg=[7,4.2,3,8.85]
result=all_args(arg); print(result)

" Flexible arguments - **kwargs "

def print_all(**kwargs):
    """ 'Print out key-value pairs in kwargs' """
    
    # Print out the key-value pairs
    for key, value in kwargs.items():
        print(key+":"+value)

# Option 1 to print out the results - Passing a dict as flexible arguments
dict={'name':'Brenda Rojas Delgado','course':'DataCamp'}
print_all(**dict)

# Option 2 to print out the results - Assign directly multiple variables
print_all(name="Brenda Rojas Delgado", course="DataCamp")
print_all(name="dumbledore", job="headmaster")

" Functions with one default argument "

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1*echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey",5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)

" Functions with multiple default arguments "

# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'

    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo("Hey",echo=5,intense=True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo("Hey",intense=True)

# Print values
print(with_big_echo)
print(big_no_echo)

" Functions with variable-length arguments (*args) "

# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge= ''

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word

    # Return hodgepodge
    return hodgepodge
# Call gibberish() with one string: one_word

one_word = gibberish("luke")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)

" Functions with variable-length keyword arguments (**kwargs) "

# Define report_status
def report_status(**kwargs):
    """ Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)

    print("\nEND REPORT")

# First call to report_status()
dict={'name':'luke','affiliation':'jedi','status':'missing'}
report_status(**dict)
#report_status(name="luke", affiliation="jedi", status="missing")

# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")

" Bringing it all together (1) \
    In this exercise, we will generalize the Twitter language analysis that \
you did in the previous chapter. You will do that by including a default \
argument that takes a column name."

# Define count_entries()
def count_entries(df,col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets)

# Call count_entries(): result2
result2 = count_entries(tweets,'source')

# Print result1 and result2
print(result1)
print(result2)

" Bringing it all together (2) \
    You're now going to generalize this function one step further by allowing \
the user to pass it a flexible argument, that is, in this case, as many columns \
names as the user would like!"

# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1 = count_entries(tweets, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)

" Lambda functions " 

# Rewrite the raise to power function as a lambda function
raise_to_power=lambda x,y:x**y

raise_to_power(2,3)

" Anonymous functions (using lambda function) "

nums=[48,6,9,21,1]

square_all=map(lambda num:num**2,nums) #<-map(function,sequence)

print(square_all)  # It prints a map object

print(list(square_all)) # it prints the output of the function 
                        # It prints what is contained in the map object

## Write an add_bangs function that adds three exclamations signs to a word

# Option 1
add_bangs=lambda a,b:a+b; print(add_bangs('hello','!!!'))

# Option 2 (with default argument)
add_bangs=lambda a:a+'!!!'; print(add_bangs('hello'))

" Writing a lambda function you already know\
    def echo_word(word1, echo):\
    """' Concatenate echo copies of word1.'"""\
    words = word1 * echo\
    return words"""

# Define echo_word as a lambda function: echo_word
echo_word = (lambda word1,echo:word1*echo) # + sign cannot concatenate str&int

# Call echo_word: result
result = echo_word('hey',5)

# Print result
print(result)

" Map() and lambda functions\
    Recall from the video that map() applies a function over an object, such as \
as a list. Here, you can use lambda functions to define the function that map()\
will use to process the object. For example:\
    \
    nums=[48,6,9,21,1]\
    square_all=map(lambda num:num**2,nums) \
    print(square_all) \
    print(list(square_all)) "
    
# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item:item+'!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list=list(shout_spells)

# Print the result
print(shout_spells_list)

" Filter() and lambda functions\
In the previous exercise, you used lambda functions to anonymously embed an\
operation within a map(). You will practice this again in this exercise by using \
a lambda function with filter() may be new to you! The function filter()\
offers a way to filter out elements from a list that don't satisfy certain \
criteria. "

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir',\
              'legolas', 'gimli', 'gandalf']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member:len(member)>6, fellowship)


# Convert the result to a list: result_list
result_list=list(result)

# Print result_list
print(result_list)

" Reduce() and lambda functions "

# In this exercise, the same functionality of gibberish() is replicated with
# another function and data sequence by using lambda.

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1,item2:item1+item2, stark)

# Print the result
print(result)

" Error handling - Passing valid arguments "

def sqrt(x):
    """ 'Returns the square root of a number.' """
    return x**(0.5)
tup_sqrt=(sqrt(4), sqrt(10))
#sqrt('hello') #throws an error

" Errors and exception - Use the sqrt function and modify it"

# This function also includes raise keyword to pinpoint complex numbers as err
def sqrt(x):
    """ 'Returns the square root of a number.' """
    if x<0:
        raise ValueError('x must be non-negative')
    try:
        return x**(0.5)
    except TypeError:
        print('x must be an int or float')

#sqrt(-9)     # Throws ValueError: x must be non-negative
sqrt(4)      # Throws a positive float number (either if the input is int or float)
#sqrt('hello')   # Throws TypeError: '<' not supported between instances of 'str'
                # and 'int'
                
" Error handling with try-except "

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Initialize empty strings: echo_word, shout_words
    echo_word=''
    shout_words=''    

    # Add exception handling with try-except
    try:
        # Concatenate echo copies of word1 using *: echo_word
        echo_word = word1*echo

        # Concatenate '!!!' to echo_word: shout_words
        shout_words = echo_word+'!!!'
    except:
        # Print error message
        print("word1 must be a string and echo must be an integer.")

    # Return shout_words
    return shout_words

# Call shout_echo
shout_echo("particle", echo="accelerator")
shout_echo("hey", echo="5")
shout_echo("particle", echo="accelerator")
shout_echo("hey")

" Error handling by raising an error "

# Define shout_echo
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with the raise
    if echo<0:
        raise ValueError('echo must be greater than or equal to 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo
shout_echo("particle", echo=5)
#shout_echo("particle", echo=-5)

" Bringing all together - Part 1 \
    The lambda function should check if the first 2 characters in a tweet x \
are 'RT'. Assign the resulting filter object to the result. To get the first 2 \
characters in a tweet x, use x[0:2]. "

# Select retweets from the Twitter DataFrame: result
result = filter(lambda x: x[0:2] == 'RT', tweets['text'])

# Create a list from filter object result: res_list
res_list=list(result)

# Print all retweets in res_list
for tweet in res_list:
    print(tweet)

" Bringing all together - Part 2 \
    In this exercise, you will improve on your previous work with the \
count_entries() function in the last chapter by adding a try-except block \
to it. This will allow your function to provide a helpful message when the\
user calls your count_entries() function but provides a column name that isn't\
in the DataFrame."

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Add try block
    try:
        # Extract column from DataFrame: col
        col = df[col_name]
        
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    
        # Return the cols_count dictionary
        return cols_count

    # Add except block
    except:
        print('The DataFrame does not have a ' + col_name + ' column.')

# Call count_entries(): result1
result1 = count_entries(tweets, 'lang')

# Print result1
print(result1)

" Bringing all together - Part 3 \
    In this exercise, you'll instead raise a ValueError in the case that the \
the user provides a column name that isn't in the DataFrame."

# Define count_entries()
def count_entries(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Raise a ValueError if col_name is NOT in DataFrame
    if col_name not in df.columns:
        raise ValueError('The DataFrame does not have a ' + col_name + ' column.')

    # Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
            # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
        
        # Return the cols_count dictionary
    return cols_count

# Call count_entries(): result1
result1=count_entries(tweets,'lang')

# Print result1
print(result1)

#count_entries(tweets, 'lang1')
# ValueError: The DataFrame does not have a lang1 column.