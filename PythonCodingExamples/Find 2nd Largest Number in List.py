#Method 1

mylist = [10, 20, 4, 45, 99]
mylist.sort()
print(mylist)   #[4,10,20,45,99]

print("Largest number is:",mylist[-1])
print("Second largest number is:",mylist[-2])

#Method2
mylist = [10, 20, 4, 45, 99]

new_list= set (mylist)
print(new_list)

new_list.remove(max(new_list))
print(new_list)   # {4, 10, 45, 20}
print(max(new_list))