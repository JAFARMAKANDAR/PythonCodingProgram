# Method 1
# 1) Find reverse of string
# 2) Check if reverse and original are same or not

s=input ("Enter a string:")  #abcdef
print(s[:])
print(s[0:5])  #abcde
print(s[0:5:1])  #abcde



reverse=(s[::-1])    #edbca reverse string

if reverse==s:
    print("Palindrome")
else:
    print("Not Palindrome")

