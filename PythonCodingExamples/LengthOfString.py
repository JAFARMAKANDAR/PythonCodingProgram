# Input : welcome
#Output :7

# Method1: Using for loop
str="welcome"
counter=0
for i in str:
    counter=counter+1

print(counter)

# Method2: Using while loop and slicing
str="welcome"
counter=0
while str[counter:]:  # 0:6
    counter=counter+1
print(counter)


# Method3: Using built-in function len()
str="welcome"
print(len(str))

# Method4: Using join and count
str="welcome"
random_str = "X"

print((random_str).join(str))   #wXeXlXcXoXmXe
print((random_str).join(str).count(random_str))      #6  X added show
print((random_str).join(str).count(random_str)+1)    #length of string
