filled_dict = {
    "one": 1,
    "one": 2,
    "one": "three"
}  # 3 ota nai aautai nai value ma 6 vani last ko lido raixa

print(filled_dict["one"])
print(filled_dict.get("two"))
filled_dict.update({"six": 6})
print(filled_dict)

print({'a': 1, **{'b': 2}})
print(filled_dict)

print({'a': 1, **{'a': 2}})

if (2 > 5):
    print("this is sth")
elif (5 > 2):
    print("we have to do ")

else:
    print("what can I do then??")

for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a {}".format(animal, animal))

animals = ["dog", "cat", "mouse"]
for value, i in enumerate(animals):
    print(value, i)

try:
    raise IndentationError("tjis i somth")
except (IndentationError, NameError):
    pass
else:
    print("ALl good")
finally:
    print("We can clean up resources here")

try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass  # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass  # Multiple exceptions can be handled together, if required.
else:  # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")  # Runs only if the code in try raises no exceptions
finally:  #  Execute under all circumstances
    print("We can clean up resources here")

# with open("myfile.txt", "mode") as file:
#     for line in f:
#         print(line)

filled_dict1 = {"one": 1, "two": 2, "three": 3}
our_iterable = list(filled_dict1.keys())
our_iterable1 = filled_dict1.keys()
print(our_iterable)
print(our_iterable1)


def vargs(**arguments):
    print(arguments)


vargs(name="sujan")


def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)


all_the_args(1, 2, a=3, b=4, c=10)

from functools import wraps


def sujanInIf(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@sujanInIf
def say(say_please=False):
    msg = "Can you consider me?"
    return msg, say_please


print(say())  # Can you buy me a beer?
print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(

x = "sujan"


def changeglobal(someth):
    global x
    print(x)
    x = someth
    print(x)


changeglobal("hello")

print((lambda x: x > 3)(3))

print((lambda x, y: x + y)(2, 3))


def create_adder(x):
    def adder(y):
        print(x)
        print(y)
        return x + y

    return adder


add_10 = create_adder(10)
print(add_10)  # <function create_adder.<locals>.adder at 0x108514940>

print(add_10(3))  # => 13


def sujan(x):
    def samy(y):
        return x + y

    return samy  # name of the fuction


trying = [x for x in [1, 2, 3, 4, 5] if x > 2]
print(trying)

sth = list(map(max, [
    5,
    2,
    3,
], [4, 2, 10]))  # => [4, 2, 3]
print(sth)

samy = {x: x**2 for x in range(4)}
print(samy)

from math import sqrt, ceil, floor
print(floor(sqrt(14)))

import math
dir(math)
print(dir(math))


class Human:
    species = "H. sapiens"

    def __init__(self, name):

        self.name = name
        self._age = 0

    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    def sing(self):
        print ('yo... yo... microphone check... one two... one two...')

    @classmethod
    def get_species(cls):
        print( cls.species )

    @staticmethod
    def grunt():            
       print( "*grunt*")

    @property                  
    def age(self):             # get 
        print( self._age)

    @age.setter               # set
    def age(self, age):
        self._age = age

    @age.deleter             # delete
    def age(self):
        del self._age


if __name__ == '__main__':

    Sujan = Human(name="Sujan") 
    Sujan.say("hi")  # "Sujan: hi"        self, message      say( self, message)

    Samikshya = Human("Samikshya")
    Samikshya.say("hello")  # "Samikshya: hello"
    Samikshya.sing()
  


    Sujan.say(Sujan.get_species())  # "Sujan: H. sapiens"

    Human.species = "H. neanderthalensis"
    Sujan.say(Sujan.get_species())  # => "Sujan": H. neanderthalensis"
    Samikshya.say(Samikshya.get_species())  # => "Samikshya: H. neanderthalensis"

    Human.grunt() # => "*grunt*"

    Samikshya.grunt()  # => "*grunt*"

    Sujan.age = 42
    # Get the property
    Sujan.say(Sujan.age)  # => "Sujan: 42"
    Samikshya.say(Samikshya.age)  # => "Samikshya: 0"

    # Delete the property
    del Sujan.age
    # i.age                         # => this would raise an AttributeError



    sujan = [ { 'posts': "sujan",
     'what':"what is that"}]

    whatthehell = {
        posts: sujan
    }

    

    print(sujan.posts)