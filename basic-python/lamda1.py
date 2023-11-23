#lambda function in python
x=lambda a:a+10
print(x(5))
y=lambda b,c:b*c
print(y(5,10))
from collections import Counter
#dictnaries in python
list1=[5,4,5,6,4,1,2,3,4,]
check_store={}
print()
# check_store=dict(Counter(list1))
for num in list1:
    check_store[num]=check_store.get(num,0)+1  # we can use manually or counter function for occurence 
# print(check_store)
for value in check_store.values():  # we can only traverse over the only values 
    print(value)
# both traverse over the key and value 
for key ,value in check_store.items():
    print(f"{key}:{value}")

print(list1) # same as or list1[:]