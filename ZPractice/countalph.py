def encode_string(str1):
    encoded = ""
    ctr = 1
    last_char = str1[0]   # A

    for i in range(1, len(str1)):    #13

        if last_char == str1[i]:
            ctr += 1
         
        else:
            encoded += str(ctr) + last_char  
            ctr = 0
            last_char = str1[i]
            ctr += 1
    encoded += str(ctr) + last_char
    return encoded
# print(encode_string("AAAABBBCCDAAA")) 
# print(encode_string("PHP"))  
# print(encode_string("AAAABBBCCCDAABDAAAAC"))



def wordcount(num):
    finalshow= " "
    count = 1
    last_num = num[0]

# SOLUTION 1

# s = input()
# r=""
# i=0
# while i<len(s):
#     if s[i].isdigit():
#         n=""
#         j=i
#         while j<len(s) and s[j].isdigit():
            
#             n+=s[j]
#             j+=1
#         i=j
#     else:
#         m=""
#         j=i
#         while j<len(s) and not s[j].isdigit():
            
#             m+=s[j]
#             j+=1
#         r+=m*int(n)
#         i=j
# print(r)


#Solution 2 
# s = input()
# cu = ''
# cus = ''
# s+='0'
# for i in range(len(s)):
#     if s[i] in "1234567890":
#         if cus != '':
#             print(cus*int(cu),end='')
#             cus=''
#             cu=s[i]
#         else:cu+=s[i]

#     else:cus+=s[i]


    for i in range( 1, len(num)):

        if last_num == num[i]:
            count += 1
        else:
            finalshow += str(count) + last_num

            count = 0
            last_num= num[i]
            count += 1 
        
    # finalshow += str(count) + last_num                # last ko dekhauna 

    print(count, last_num)

    return finalshow


print(wordcount("ABBBBBBBB!!!!!!!!!!CCCCCCCC"))




# Read the characters from the standard input and print them in the requested order. The order is given as a series of digits describing the position in the original input string of the next character to print.
# Input
# Line 1: n
# Line 2: n characters
# Line 3: n unique digits in the range 1..n
            

        