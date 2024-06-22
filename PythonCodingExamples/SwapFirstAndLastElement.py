#Approach1: Temporary Variable

mylist=[12,35,9,56,24]  #index starts from 0
size=len(mylist) #5

temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp

print("list after swapping:",mylist)

#Approach2:

mylist=[12,35,9,56,24]  #index starts from 0
mylist[0],mylist[-1]=mylist[-1],mylist[0]

print("list after swapping:",mylist)


#Approach3: Using tuple
mylist=[12,35,9,56,24]  #index starts from 0
get=(mylist[-1],mylist[0])  #Packing 24  12

mylist[0],mylist[-1]=get
print("list after swapping:",mylist)

#Approach4: *append
mylist=[12,34,9,56,24]
start,*middle,end=mylist
mylist=[end,*middle,start]
print("list after swapping:",mylist)

#Approach5:using pop()
mylist=[12,34,9,56,24]
first=mylist.pop(0)  #12
last=mylist.pop(-1)  #24

mylist.insert(0,last)
mylist.append(first)

print("list after swapping:",mylist)



