# Input : mylist = [20, 100, 20, 1, 10]
# Output :
# samllest is 1
# Largest is 100

#Method 1 : Sort the list in ascending order and print the first & last element in the list
mylist=[20, 100, 20, 1, 10]
mylist.sort()  #sorting
print(mylist)   # [1, 10, 20, 20, 100]
print("smallest element is :",mylist[0]) #1
print("largest element is :",mylist[-1])  #100


#Methd 2: Using min() & max() methods
mylist=[20, 100, 20, 1, 10]
print("smallest element is:",min(mylist))
print("largest element is:",max(mylist))