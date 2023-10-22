l1 =["bhindi ", "Achar ", "Chowmein","Tinda"]

i = 1
for item in l1:
    if i%2!=0:
        print(f"jarvis please Buy this :{item}")
    i+=1

# By using enumerate function
print("By using enumerate function")
for index, item in enumerate(l1):
    if index%2==1:
         print(f"jarvis please Buy this :{item}")
