def f(i, values = []):
    values.append(i)
    return values
 
f(1)
f(2)
v = f(3)
print(v)'


shallow copy vs deeepcopy 
1. for 1D list shalow and deep copy are same 
2. if we create shallow copy only copies refrences not list of list objects so for this changes can be done 
##  deep copy case
1. totally different indenpendent copy even list of list objects -copies only objects of vlaues not memory location. 
