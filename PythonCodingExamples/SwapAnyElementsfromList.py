#Approach simple swap
mylist=[23,65,19,90]  #index starts from0
print(mylist)
pos1,pos2=1,3
mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
print(mylist)

#Approach2 :  using inbuild list.pop() function

mylist=[23,65,19,90]  #index starts from0
pos1,pos2=1,3

first_ele=mylist.pop(pos1)  #65
sec_ele=mylist.pop(pos2-1)   #23,19,90

mylist.insert(pos1,sec_ele)
mylist.insert(pos2,first_ele)
print(mylist)

#Approach3: using tuple
mylist=[23,65,19,90]  #index starts from0
pos1,pos2=1,3

get=(mylist[pos1],mylist[pos2])
mylist[pos2],mylist[pos1]=get
print(mylist)
