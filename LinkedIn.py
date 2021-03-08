sujan = [1, 2, 3]
print(any(sujan))   #
print(all(sujan))   #The all() function returns True if all items in the list evaluate to True. Otherwise, it returns False.

hel, bel, cel = (1, 2, 3) # both list & tuple can be unpacked               tuple unpacking
print(hel, bel, cel)




myset = {0, 1, 0}
x = any(myset)

#from sys import *         # Sys library provides access to Python's Library           to capture command-line arguments given at a file's runtime

# What is the runtime of accessing a value in a dictionary by using its key?         => O(1), also called constant time.


# class Game:              class Game(inherits from)

# doctest?
def sum(a, b):
    """
    >>> sum(4, 3)
    7

    >>> sum( 3,4)
    7

    >>> sum(-4, 5)
    1
    """
    return a + b

print(sum(4, 3))

#The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions
#  to verify that they work exactly as shown.


# What built-in Python data type is commonly used to represent a stack?    => List 

college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']  # List 
print( list((college_years, 2019)))   # [['Freshman', 'Sophomore', 'Junior', 'Senior'], 2019]
print(list(enumerate(college_years, 2019)))           # Ennumerate

# How does defaultdict work?   f you try to access a key in a dictionary that doesn't exist, defaultdict will create a new key for you instead of throwing a KeyError.

# setdefault lee chai navako 

dictionary1 = { "sujan": "hello"}

dictionary1.setdefault("5", 10)          # set default lee chai yo garxa

print(dictionary1)                        #{'sujan': 'hello', '5': 10}


# self refers to the instance whose method was called.

# characteristic of namedtuples?

# You can assign a name to each of the namedtuple members and refer to them that way, similarly to how you would access keys in dictionary.
#  Each member of a namedtuple object can be indexed to directly, just like in a regular tuple.
#  namedtuples are just as memory efficient as regular tuples.

from collections import namedtuple
nam_tup = namedtuple('human', 'Fname city country MiddleName'  )                  # declaring a namedtuple
                        #TYPE, FIELD 
obj = nam_tup(Fname="pranay", city="London", country="England", MiddleName= "Kumar")             # initializing 
print(obj)       # human(Fname='pranay', city='London', country='England', MiddleName='Kumar')

print(obj.Fname, obj.city) # accessing objects specific fields

print(obj[0],obj[2]) # accessing objects using indexes
print('-' * 35)
for x in obj: #  We can also get the value by looping
    print(x)

print(obj._asdict())             # converting namedtuple to a dictionary     => 'Fname': 'pranay', 'city': 'London', 'country': 'England', 'MiddleName': 'Kumar'}

nam_tup1=namedtuple('human', 'name city address class', rename=True) # class is python reserved name   ('name', 'city', 'address', '_3')
nam_tup2=namedtuple('human', 'name name addressss name' , rename=True) # city field has occured twice    ('name', '_1', 'address', 'city')
                    # First ko linxa, repeat vako index  linxa, tyo position ma repeat vako 
print(nam_tup1._fields)
print(nam_tup2._fields)


tup=(23,45,54, 'abc',20.3)
print(type(tup))                 #  return <class ‘tuple’>
print(len(tup))


# What is an instance method?    => Instance methods can modify the state of an instance or the state of its parent class.

#  Encapsulation
#  It protects the data from outside interference.
#  A parent class is encapsulated and no data from the parent class passes on to the child class.
#  It keeps data and the methods that can manipulate that data in one place.

# Stack/queue?   => list

#What is the correct syntax for instantiating a new object of the type Game?    #my_game = Game()

# What does the built-in map() function do?
# => It applies a function to each item in an iterable and returns the value of that function.

# Pass It is a null operation used mainly as a placeholder in functions, classes, etc.

def samy(samy, sujan):
    pass 

samy(4, 5)

class samikshya:
    pass
   

print(type(samy))            
print(type(samikshya))          #<class 'type'> 

#Assuming the node is in a singly linked list, what is the runtime complexity of searching for a specific node within a singly linked list?
#The runtime is O(n) because in the worst case, the node you are searching for is the last node, and every node in the linked list must be visited.


fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]

def desiredoutPut( fruits, quantities, prices):
    for fruit in fruits:
        for quantity in quantities:
            for price in prices:
                print( fruit, quantity, price)

print(desiredoutPut(fruits, quantities, prices))
# for x in (fruits,quantities, prices):
#     

# Desired output
[('Apples', 5, 1.50),
('Oranges', 3, 2.25),
('Bananas', 4, 0.89)]




# def out_put(fruits, quantities, prices):
    

#     i = 0
#     output = []
#     for fruit in fruits:
#         temp_qty = quantities[i]
#         temp_price = prices[i]
#         output.append((fruit, temp_qty, temp_price))
#         i += 1
#         print(output)
#         return output

# out_put(fruits, quantities, prices)
# print(out_put)

#ZIP
# groceries = zip(fruits, quantities, prices)
# return groceries


#What is the algorithmic paradigm of quick sort?  => divide and conquer

# What is runtime complexity of the list's built-in .append() method? O(1), also called constant time ( Just additon ho so (1))


# What is key difference between a set and a list?
# A set is an unordered collection unique items. A list is an ordered collection of non-unique items.

# What is the definition of abstraction as applied to object-oriented Python?
# Abstraction means the implementation is hidden from the user, and only the relevant data or information is shown.


def print_alpha_nums(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return

print(print_alpha_nums(['a', 'b', 'c'], [1, 2, 3]))

# Suppose a Game class inherits from two parent classes: BoardGame and LogicGame. Which statement is true about the methods of an object instantiated from the Game class?
# An instance of the Game class will inherit whatever methods the BoardGame and LogicGame classes have.

class BoardGame:
    def __init__(self, name, size):

        self.name= name
        self.size = size

    @classmethod
    def letprintName():
        print(f' the game name is {self.name}')


class LogicGame(BoardGame):
    def __init__(self,name, size, time):
        super.__init__(name, size)
        self.time = time


#space complexity => The amount of space taken up in memory as a function of the input size


fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}
fruit_names = [x for x in fruits.keys()]    #Print Lekhna pardaina arko [ ] lee list ma convert hunxa
print(fruit_names) # arko main kura, 


# Quick Sort => Divide & Conquer

#self refers to the instance whose method was called.

# A class method can modify the state of the class, but they can't directly modify the state of an instance that inherits from that class.

# What does it mean for a function to have linear runtime?
# The amount of time it takes the function to complete grows linearly as the input size increases.

#PEP 8 coding style guidelines for constnts
#in all caps with underscores separating words -- e.g. MAX_VALUE = 255
# for function name => get_max_num  ( all small number say)

     #Describe the functionality of a deque.
                # A deque adds items at either or both ends, and remove items at either or both ends.



#You use the decorator to alter the functionality of a function without the without having to modify the functions code.

#What would happen if you did not alter the state of the element that an algorithm is operating on recursively?
# You would get a RuntimeError: maximum recursion depth exceeded.


#What is the runtime complexity of searching for an item in a binary search tree?
# The runtime for searching in a binary search tree is generally O(h), where h is the height of the tree.


# Why would you use mixin?#
#if you have many classes that all need to have the same functionality, you'd use a mixin to define that functionality.

#What is the runtime complexity of adding an item to a stack and removing an item from a stack?
# Add items to a stack in O(1) time and remove items from a stack in O(1) time.

# What does calling namedtuple on a collection type return?
# a tuple subclass with iterable named fields






        





