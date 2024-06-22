#Input : List = [10,11,12,13,14,15]
# Output : List = [15,14,13,12,11,10]

#Approach1 : using reverse() method
mylist = [10,11,12,13,14,15]
print("mylist before reverse:",mylist)
mylist.reverse()
print("mylist after reverse:",mylist)


#Approach2: Using the slicing techinique
mylist = [10,11,12,13,14,15]
print("mylist before reverse:",mylist)
mylist2=mylist[::-1]
print("mylist after reverse:",mylist2)
