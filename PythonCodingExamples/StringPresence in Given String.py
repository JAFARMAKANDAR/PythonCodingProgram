# The find() method find the first occurance of specified value.
# The find() method returns -1 if the value is not found.

str="welcome to python programming"
sub_str="python"
print( str.find(sub_str))  #11 present at 11 position

if( str.find(sub_str) == -1):
    print("Not found")
else:
    print("Found")