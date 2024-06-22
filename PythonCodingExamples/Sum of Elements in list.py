# Input : [5, 10, 15, 20]
# Output : 50

#Method1: using for Loop with range()

mylist=[5,10,15,20]
total=0

for i in range(0,len(mylist)):
    total=total+mylist[i]

print("sum of all elements in given list: ", total)

# Method 2 : using sum() method
mylist=[5,10,15,20]
total=sum(mylist)
print("sum of all elements in given list: ", total)
