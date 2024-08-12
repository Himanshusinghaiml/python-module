'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.

''' 
try:
    x=int (input('enter the string value'))  
except:
    print('this is  invalid input ')
else:
    print('this is also printing ')
finally:
    print('this block is executing regardless of try and except block ')

x=-1
if x<0:
    raise Exception('integer value less than zero')