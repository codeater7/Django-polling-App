#Fizz, Buzz and FizzBuzz
def fizzbuzz():
    for fizzbuzz in range(51):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print(
                "fizzbuzz"
            )  # very much remember about the continue, as instead of Number, we are doing Fizz,Buzz
            continue
        elif fizzbuzz % 3 == 0:
            print("fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("buzz")
            continue
        print(fizzbuzz)  # Also have to print the number


# Splat operator
def test(p, q, r):
    print(p, q, r)


test_Dict = {
    'p': 2,
    'q': 4,
    'r': 6
}  # dictionary ko 2 **  ho ? after  ** must be a mapping, not list
test_List = [20, 40, 60]
sujan_test = (100, 200, 300)

test(**test_Dict)
test(*test_List)
test(*sujan_test)

#                                  <listcomp>    --->        range_iterator instance


def iterator_sth():
    row_num = int(input("Input number of rows: "))
    col_num = int(input("Input number of columns: "))
    multi_list = [[2 for col in range(col_num)] for row in range(row_num)]

    for row in range(row_num):
        for col in range(col_num):
            multi_list[row][col] = row * col

    print(multi_list)

    # "a".isdigit() => True                   isdigit()
    # "10".isalpha() => True                   isalpha()  pass

    #int(str(1101), 2) => 13


#num = [x for x in input("write sth =>").split(' ')]
#print(num)

# Very special Notification, While True ma always always must be some clause to exit; or keep break


def reading_input_and_UpperCasing():
    lines = []
    while True:
        l = input()
        if l:
            lines.append(l.upper())
        else:
            break

    for l in lines:
        print(l)


#reading_input_and_UpperCasing()


def printonly_even_letter_only():

    items = []


    for i in range(100, 401):
        s = str(i)               #convert to string 2 0 2
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0): #convert to int and check if divisible by 2
            items.append(s)
    print(",".join(items))             # join vitra chai items
    #['200', '202', '204', '206', '208', '220', '222', '224', '226', '228', '240', '242', '244', '246', '248', '260', '262', '264', '266', '268', '280', '282', '284', '286', '288', '400']
    # 200,202,204,206,208,220,222,224,226,228,240,242,244,246,248,260,262,264,266,268,280,282,284,286,288,400 ( last ko change lee)

#printonly_even()

def number_pattern():
    for i in range(10):
        print (str(i)*i )

#number_pattern()

def multiplication_table(num):
    for i in range(1,11):
        print (f' {num} * {i} = {int(num) * i }' )





#multiplication_table(110)


# Median vanako 3; kun middle ho 3 jana ma vankao





def median():


    a = float(input("Input first number: "))
    b = float(input("Input second number: "))
    c = float(input("Input third number: "))

    if a > b:                # idea 
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c

print("The median is", median)

    
# Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

def sum_average_print():
    
    
    sum1= 0
    count = 0
    
    
    while(True ):                   # user lee hali rahanee ho, until num is not, so loop
        a = int(input("Write some numbers from please to find the number"))
        sum1  = sum1 + a
        count += 1 

        
        if a == 0:
            break
        
    print(f"The sum is {sum1} and the average is { sum1 / (count-1) }")  # count garna parxa,coz, tyo loop ma pani count increase hunxa
        
#sum_average_print()

#print("Input some integers to calculate their sum and average. Input 0 to exit.")

def count_Number_andloop():
    count = 0
    sum = 0.0
    number = 1

    while number != 0:
        number = int(input(""))
        sum = sum + number
        count += 1

    if count == 0:
        print("Input some numbers")
    else:
        print("Average and Sum of the above numbers are: ", sum / (count-1), sum)

def find_if_scalent_Equilateral():
    print("Input lengths of the triangle sides: ")
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))

    if x == y == z:
        print("Equilateral triangle")
    elif x==y or y==z or z==x:
        print("isosceles triangle")
    else:
        print("Scalene triangle")


# month = input("Input the month (e.g. January, February etc.): ")
# day = int(input("Input the day: "))

# if month in ('January', 'February', 'March'):
# 	season = 'winter'
# elif month in ('April', 'May', 'June'):
# 	season = 'spring'
# elif month in ('July', 'August', 'September'):
# 	season = 'summer'
# else:
# 	season = 'autumn'

# if (month == 'March') and (day > 19):
# 	season = 'spring'
# elif (month == 'June') and (day > 20):
# 	season = 'summer'
# elif (month == 'September') and (day > 21):
# 	season = 'autumn'
# elif (month == 'December') and (day > 20):
# 	season = 'winter'

# print("Season is",season)


# day = int(input("Input birthday: "))
# month = input("Input month of birth (e.g. march, july etc): ")
# if month == 'december':
# 	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'        # yeha main concept asto_sign = '' else ko ni tehi maa nai janxa
# elif month == 'january':
# 	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'

# elif month == 'november':
# 	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
# print("Your Astrological sign is :",astro_sign)


def zebra_z():
    result_str="";    
    for row in range(0,7):    
        for column in range(0,7):     
            if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row+column==6):  
                result_str=result_str+"*"   
                
            else:      
                result_str=result_str+" "    
        result_str= result_str+"\n"    
    print(result_str);

zebra_z()
