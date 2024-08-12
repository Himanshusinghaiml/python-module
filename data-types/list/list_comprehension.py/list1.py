# list comprehension is used for to make a code in a elegant way
# sort code and fastest  using list comprehension

''' lets take example where we need list comprehension'''
ans=[]
# have to store 1 to 100 numbers
for i in range(1,101):
    ans.append(i)
print(ans)  # here we need to write four lines of code but we can compress with the help of coprehension



# using comprehension
print('using list comprehension')
store=[i for i in range(1,101)]
print(store)
for i in store:
    print(i)