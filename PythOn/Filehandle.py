# f = open("parwana.txt","w")
# f.write("\n\tSK Aryan Khan is best boy")
# f.close()

# f = open("parwana.txt","a")
# a = f.write("\n\tSK Aryan Khan is best boy")
# print(a)
# f.close()

# Handle read and write both
# r+ for read and write mode

f = open("parwana.txt","r+")
print(f.tell())
f.write("thank you for Choosing our Brand")
print(f.read())
f.seek(10)
f.close()
