#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 
 
def solution1():
    number = [ ]
    for i in range(1500, 2700):
        if( i% 5 ==0) & (i% 7 ==0):         # & or we can keep and
            number.append(i)
    
    print(number)   #[1505, 1540, 1575, 1610, 1645, 1680, 1715, 1750, 1785, 1820, 1855, 1890, 1925, 1960, 1995, 2030, 2065, 2100, 2135, 2170, 2205, 2240, 2275, 2310, 2345, 2380, 2415, 2450, 2485, 2520, 2555, 2590, 2625, 2660, 2695]

#Write a Python program to convert temperatures to and from celsius, fahrenheit.

# c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
#Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : 104f                                     
#The temperature in Celsius is 40 degrees. 

def solution2():
    input_string_var = input("Input the number you like to convert  =>")
    lets_trim_until_LastNumber = int(input_string_var[:-1])          # Last ko F falxa   // very very important
    to_know_last_letter = input_string_var[-1]      # Last ko Digit Lina                 // Last ko digit matra lina


    if (to_know_last_letter.upper() == 'F'):
        celsius = round(((lets_trim_until_LastNumber - 32)/9) * 5)
        print(f'The temperature of {input_string_var} is {celsius} degree')

    elif( to_know_last_letter.upper() == 'C') :


        farenheit = (lets_trim_until_LastNumber* 9/5) + 32
        print(f'The temperature in {input_string_var} is {farenheit} Fahrenheit')

    else:
        print("Please specify the number")


# Write a Python program to guess a number between 1 to 9.
import random
def solution_random():
    my_num = random.randint(1,10)
    print(my_num)
    user_number = int(input("Enter the number between 1, 10"))

    while(my_num !=user_number):
        user_number = int(input("Not Right, Enter Again"))
    if(my_num == user_number):
        print("Mission Completed")


def samySolution_random():
    my_num = random.randint(1,10)
    gues_number = 0
    while( my_num != gues_number):
        gues_number = int(input("Enter the number again"))       #suru ko global scope ma init garyo ani check garyo vitra
    print("Hyvvaa")


def construct():
    num = 5
    for i in range(num):
        for j in range(i):
            print("*", end='')                 # end= 'Tehi ma rakhnee 

        print(' ')                              # new line ma leraija
    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end='')

        print(' ')
    
#construct()

#word_reverse
def word_reverse():
    word = input("Input a word to reverse: ")      ## Sakvar index ko tira laijaidai 6am, len -1 , -1 (samma), -1 lee 
    for char in range(len(word)- 1, -1, -1):    # len- 1
        print(word[char], end='')
    print('\n')



def count_odd_even():
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    oddCount = 0
    Evencount = 0

    for num in numbers:
        if (num%2 == 0):
            Evencount += 1
        else:
            oddCount += 1

    print(oddCount, Evencount)

# datalist = [1452, 11.23, 1+2j,  True,  'w3resource',  (0, -1),   [5, 12],  {"class":'V', "section":'A'}]
# for item in datalist:
#    print ("Type of ",item, " is ", type(item))      # Just remember type

# Prints all the numbers from 0 to 6 except 3 and 6
def conti():
    for x in range(6):
        if (x == 3 or x==6):
            continue
        print(x)    # aauxa; end = '' aautai line ma rakhna       new line ma jana ( print(\n))


# Fibonacci series between 0 to 50
def Fibonacci():
    x, y = 0, 1
    while(y< 50):
        print("x",x)
        print(y)
        y= x+y
        x= y
        

Fibonacci()


        











    
    

        
        


    

 




