

# print(1/0)


#arr = [1,2,3]
#print(arr[9])




try:
    x = 23/10
except:
    print("excetion occured")



try:
    x = 1/2
except ZeroDivisionError:
    print("zero divisio error occured")




try:
    x = 1/52
except EOFError:
    print("end of file occured")
except ImportError:
    print("import error exception occured")
except RuntimeError:
    print("zero didision error occured")
else:
    x = 20
    #print("control is inside else")
    #else will be execeuted after try when there is no exception occured


#This is a dummy comment


try:
    x = 1/8
except ZeroDivisionError as err:
    print(err)


#this is a dummy comment



try:
    x = 1/80
except ZeroDivisionError as err:
    print(err)
finally:
    print("finally will always gets executed")
    #finnalyy block will always gets executed


#this is a dummy coment



arr = [1,2,3]

try:
    if len(arr) >=4:
        raise ValueError("array length is greater or equal to 4")
    else:
        print("everything is fine")
except ValueError as err:
    print(err)


#how to define custom exceptions in python



class CustomException(Exception):
    "This is a custom exeption"
    pass

try:
    x = 20
    if x==20:
        raise CustomException
    else:
        print("x is not 20")
except CustomException as err:
    print("exception occured")













#this is a dummy comment















#this is a dummy comment
