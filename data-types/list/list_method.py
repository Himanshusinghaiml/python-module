l=[5,4,7,8,5,6,5,6]
# these are all the method of list 
'''
append
insert
sort - ascending
reverse=true - descending
reverse
len
copy
count
extend,pop, remove ,clear
'''
print(l.append(10))  # output None
print(l)
# print(l.insert(0,100))
l.insert(0,100)
print(l)


# sorting
l.sort()
print(l)
l.sort(reverse=True)
print(l)  # descending order the list 

l.reverse()
print(l)
l.remove(100)
print(' removing the list ',l)

l.clear()
print(l)