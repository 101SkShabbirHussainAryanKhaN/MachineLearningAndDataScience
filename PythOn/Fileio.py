"""
File handLing in Python

"Read Mode "r" " : Open File for Reading Purpose - Default mode 
"Read Mode "w" " : Open File for Writing Purpose 
"Exclusive Creation Mode "x" " : Open File for Creation Purpose if not exist
"Append Mode "a" " : Open File for adding more materail to file
"Text Mode "t" " : Open File in a text mode - Default mode
"Binary Mode "b" " : Open File to perform binary function mode 
"Plus Mode "+" " : Open File for updation purpose/Read and write 

"""
s = open("sk.txt", "rt")
# content = s.read()
# print(content)
# print("This will give output as List :",s.readlines())
print(s.readline(), end="")
print(s.readline(), end="")
# for line in s:
#     print(line , end="")
s.close()