
from functools import partial 
import functools
import functools as ftools 


# simple data types 
# int
a = 5      # 5 
b = 012    # 10 decimal
c = 0x1B   # 27 decimal 

# float
d = 10.3
e = 1e3 

# complex 
f = 1 + 3.5j

# string 
g = 'abc'
h = "abc"
i = """
   A multiline 
   "string" 
   ''"""

# list
j = [5,6,7]

# dictionary 
a_dict = { "abc" : "xyz" }

# tuple 
l = ( 5,6,7 )

# set 
m = { 5, 6, 7 }

# selections (if-then-else)
print "if statement"
a = 1
b = 2 
c = 3 
if a < b:
    print a
elif a < c:
    print b
else:
    print c 
print "-" * 20 

# conditional expression 
x = a if a < b else b

# loops
print "for-loop:"
for i in [5,6,7]: 
    print i 
print "-" * 40 

print "while-loop:"
i = 10 
while i > 0: 
    print i 
    i -= 1
print "-" * 40 

# functions
def func1(a, b, c):
    x = a + b + c 
    return x 

func2 = lambda a,b: a < b

# functional programming 
def square(a):
    return a*a

def five_times(f, x):
    return 5 * f(x)

print "Functions "
print five_times(square, 5)

curried_five = partial(five_times, square)
print curried_five(5)
print "-" * 40 

# comprehension 
print "Comprehension:"
a_list = [ x*5 for x in range(0, 10) ]
print a_list

a_set  = { x % 2 for x in range(100) }
print a_set

a_dict = { x : x * 3 for x in range(10) }
print a_dict 
print "-" * 40 

# iterators and generators
def mygenerator(n_elements):
    complete_list = range(n_elements)
    for i in complete_list:
        print "Before yield: %s" % i 
        yield i
        print "After yield: %s" % i 

for val in mygenerator(5):
    print "Received value in loop: %s" % val 

# classes 
print "Classes:"
class MyClass(object):
    def __init__(self, value):
        self.x = value 

    def print_val(self):
        print self.x 

    def get_val(self):
        return self.x

inst = MyClass(5)
inst.print_val()
f = inst.get_val
print f()
print "-" * 40 

# using the standard library 


# popular examples 

# parse a CSV file in one line 

# fibonaci 

# 
prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6 }
grocery_bill = sum(prices[fruit] * quantity
                   for fruit, quantity in my_purchase.iteritems())
print 'I owe the grocer $%.2f' % grocery_bill


