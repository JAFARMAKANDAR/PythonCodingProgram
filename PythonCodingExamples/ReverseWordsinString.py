str="welcome to python programming"

words=str.split(" ")
print(words)  #['welcome', 'to', 'python', 'programming']
words=words[-1::-1]
print(words)   #['programming', 'pythonn', 'to', 'welcome']
outputstr=" ".join(words)
print(outputstr)
