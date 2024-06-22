#Approach1: using Loop

mylist=[1,6,3,5,3,4]
ele=100
flag=0
for i in mylist:
    if(i==ele):
        print("Element found")
        flag=1
        break
if(flag==0):
    print("Element Not found")



#Approach2: using in operator

mylist=[1,6,3,5,3,4]
ele=5
if(ele in mylist):
    print("Element found")
else:
    print("Element not found")
    



