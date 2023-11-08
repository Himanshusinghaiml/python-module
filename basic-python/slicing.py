# placement preparation of Slicing 

# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.
a="himanshu,singh"
j=0
for i in a:
    print(j,i)
    j+=1
print() # above we can directly print the string 
print()  # below we define range and print index and character of the strings
for i in range(len(a)):
    print(i,a[i])
    
print(a[2:5]) #Get the characters from position 2 to position 5 (not included position 5 ):
print(a[:5])# print the starting index
w=a[:2]  # we cam alos assign in varaible and access
print(w)