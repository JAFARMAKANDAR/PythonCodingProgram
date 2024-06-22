# num1=10
# num2=20
num1=input("Enter num1 value:")
num2=input("Enter num2 value:")


print("value of num1 before sawpping:",num1)
print("value of num2 before sawpping:",num2)
#Approach 1 ; using temp variable
temp=num1 #10
num1=num2 #20
num2=temp #20

print("value of num1 after sawpping:",num1)
print("value of num2 after sawpping:",num2)

#Approach2 :
num1,num2=num2,num1

print("value of num1 after sawpping:",num1)
print("value of num2 after sawpping:",num2)