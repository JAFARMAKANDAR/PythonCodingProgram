#Approach1: Using slicing technique
mylist=[4,8,2,10,15,18]
mylist_copy=mylist[:]
print(mylist_copy)

#Approach2: Using extend() method
mylist=[4,8,2,10,15,18]
mylist_copy=[]   #add value  in list if have mylist_copy=[10,34,37]
mylist_copy.extend(mylist)
print(mylist_copy)

#Approach3: Using extend() method
mylist=[4,8,2,10,15,18]
mylist_copy=list(mylist)
print(mylist_copy)

#Approach4 : using the copy()
mylist=[4,8,2,10,15,18]
mylist_copy=mylist.copy()
print(mylist_copy)

#Approach5 : using  list comprehension
mylist=[4,8,2,10,15,18]
mlist_copy=[i for i in mylist]
print(mylist_copy)

