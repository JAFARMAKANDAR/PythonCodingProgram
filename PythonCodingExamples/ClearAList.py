#Approach1: using clear () method

mylist=[6, 0, 4, 1]
print("mylist before clear:",mylist)
mylist.clear()
print("mylist after clear:",mylist)

#Approach2: initializes the list with no value
mylist = [6, 0, 4, 1]
print("mylist before clear:",mylist)
mylist=[]
print("mylist after clear:",mylist)

#Approach3: using "*=0"   this method removes all element of the list and makes it empty.
mylist = [6, 0, 4, 1]
print("mylist before clear:",mylist)
mylist *=0  #delets List
print("mylist after clear:",mylist)


#Approach 4 :  using del method
mylist= [6, 0, 4, 1]
print("mylist before clear:",mylist)
del mylist[:]    #   delets all the elements
print("mylist after clear:",mylist)

