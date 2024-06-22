# Input : list1 =[3,2,4]
#Output : 24
# Explanation: 3*2*5=24

# Method1 : Traversal

mylist=[3,2,4]
result=1
for x in mylist:
    result=result * x  # 6
print(result)

#Method 2 : using numpy.prod() * Install numpy package
import numpy as np
mylist=[3,2,4]
result=np.prod(mylist)
print(result)



