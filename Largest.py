
def List_func(myList):
    return sorted(myList)[-1]


#print(List_func([1, -28, 88, 200 , 7]))

def my_list( my_param):
    heaviest = 0
    num_index = 0
    for index, item in enumerate(my_param):
        if item > heaviest:
            heaviest = item
            num_index = index
            
    return  num_index


print(my_list([1, 4, 50, 24, 45]))





lst = [237, 72, -18, 237, 236, 237, 60, -158, -273, -78, 492, 243]
print(min((abs(x), x) for x in lst)[1])

def ISBULKY (width, height, length, mass):

    volume = width * height* length

    bulky = volume >= 1000000 or max(width, height, length)>= 150

    isheavy = mass>= 20


    if isheavy and bulky:
        return "REJECTED"
    if  not isheavy and not bulky:
        return "STANDARD"
    else:
        return "SPECIAL"

print(ISBULKY( 12, 12 , 1 , 2))




