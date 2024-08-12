# method in python
'''
- clear,copy ,keys,values
- items
- update
- pop '''
dict = {'name': 'himanshu singh ', 'age': 22, 'place': 'varanasi'}
# print(dict)
store_key = []
for key, value in dict.items():
    # print(key)
    store_key.append(key)
    store_key.append(value)
print(store_key) 
# dict.clear()
# print(dict)
dict['himanshu'] = 'rajpoot'  # here we can add items in dictionaries
print(dict)
