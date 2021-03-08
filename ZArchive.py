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


def printonly_even():

    items = []


    for i in range(100, 401):
        s = str(i)               #convert to string 2 0 2
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0): #convert to int and check if divisible by 2
            items.append(s)
    print(",".join(items))             # join vitra chai items


printonly_even()