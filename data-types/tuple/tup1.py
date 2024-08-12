tup=(5,6,4,3,90)
print(tup) # priting all the elements 
print(tup[2])  #accessing the elements
# print(tup[2]=8)  # not able to modify due to inmutuble 

#everything same as list only diff inmutable , represents using parenthesis

x=()
print(x,type(x))  # empty tuple
y=(1,) # tuple 
z=(1) # integer
print(y,type(y))


# comprehension
print('tuple printing using comprehension')
ans=(i for i in range(101))
print(ans)
for i in ans:
    print (i)
    
#count and index method of tuple in python
