# Input : list = [15,6, 7, 10, 12, 20, 10, 28, 10]
# x=10
#Output : 3
# 10 appears three times in given list

#Approach 1 :using loop
mylist = [15,6, 7, 10, 12, 20, 10, 28, 10,15]
x=15
count=0

for ele in mylist:
    if(ele==x):
        count=count+1
print("{} has occured {} times". format(x,count))

#Approach2 : using count()
mylist=[5,6,7,10,12,20,10,28,10]
x=10
print("{} has occured {} times". format(x,mylist.count(x)))


#Approach3 : using Counter ()
from collections import Counter
mylist=[5,6,7,10,12,20,10,28,10]
x=10
dic=Counter(mylist)   #{5:1, 6:1, 7:1, 10:3........ }
print("{} has occured {} times". format(x,dic[x]))

