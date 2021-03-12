def make_printer (msg):
    msg = "hi there"

    def printer():
        print(msg)

    return printer

#myprinter = make_printer("What the hell")

# myprinter()


# def outer_func(msg):
    
#     def inner_func(hello):
#         print(f'{msg} is {hello}')  
    
#     return inner_func

# # def add( a, b):
# #     return a + b


# Hello_1 = outer_func("H1")
# Hello_1("Bye" )
# Hello_1("You kidding me")


# def outer_func(func):
    
#     def inner_func(*args):
#         print( func(*args) )
      
    
#     return inner_func

# def add( a, b):
#     return a + b
 
# def substract(a, b, c):
#     return a-b -c

# add_1 = outer_func(add)
# add_1(4, 5)

# substract = outer_func(substract)               # 1) function pass garyo 1st        2) Call chai paxi
# print(substract.__name__)
# substract(4, 2, 1)                           # call jhailee ni yeha garnee ho!



# closure 

def outerfunc (func):


    def inner_func(*args):
        return ( func(*args))

    return  inner_func

def add (a, b):
    return a+b



name = (outerfunc(add))     
print(name(4, 5))


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method before {}'.format(self.original_function.__name__))
        self.original_function(*args, **kwargs)














