def recursive_list_sum(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):                    # Recursive kati khera garne??  ( type aautai nai vayo vani, list ko jsto)
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total
#print( recursive_list_sum([1, 2, 3,4,[5,6]]))

def recur( list_arr):
    total = 0
    for element in list_arr:
        if type(element)== type([]):
            total = total + recur(element)
        else:
            total = total + element
    

    return total

#print( recur([1, 2, 3,4,[5,6]]))

# 0, 1, 2, 3,5, 7
#     x, y
#         x 

#          x+y

def fibo(num):
    x = 0
    y = 1
    series = y
    
    while (num < 50):
        fibo(num)
        x=y
        y=x+y

    return series

#fibo( 10)


def fibon():
    x= 0
    y = 1

    no_of = int(input("how many numbers "))
    count = 0

    fibon_series = [] 

    while(count <= no_of):
        print(x, end = '')
        fibon_series.append(x)
        nth = x+y                           # print x, paxi  yo n-th vanera= x+y garnee ani 
        x=y 
        y= nth
        
        count += 1
    return fibon_series

print(fibon())


# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))

# # first two terms
# n1, n2 = 0, 1
# count = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
       
#        count += 1


    



    



