def test1():
    print('himanshu singh')
    return 'himanshu singh '
    
# test1()+'from varanasi ' print return Nonetype 
print(test1()+'from varanasi ')

#---------------------------------------#

#function with argument/ withoutargument 

def test2(a=50,b=90):
    # this is docstring  - good approach to write the code 
    ''' this function takes two argu and print just value '''
    print(a,b)
test2(b=100)
#python automatically understand what the value to be going to return so we do not need define return type 


# python *args - args is  not keyword 
#** keywords args - takes keys value pair 
# without define parameters and we can pass multiple argu what ever we want 

def args(*args,name):
    print(args,name)
    return args,name
store=args([5,4,7,8,9,5,6,],555,6778,345,name='himanshu singh')
print(store,type(store))

# function by defaults return tuple()

# ** kwargs -key values pairs

def kwargs(**himanhsu):  # it takes multiple argument as key value pairs
    print(himanhsu,type(himanhsu))
kwargs(name='himanshu singh ',age=21,location='varansai') 