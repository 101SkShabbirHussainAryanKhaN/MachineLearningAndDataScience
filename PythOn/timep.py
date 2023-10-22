import time
sk ="this is aryan khan"
k = 0
initial = time.time()

while(k<44):
    
    print(sk.title())
    k+=1

print("this is while Loop", time.time() - initial," Seconds")

initial2 = time.time()
for m in range(44):
    print(sk.title())
print("this is For Loop", time.time() - initial2," Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)    
           