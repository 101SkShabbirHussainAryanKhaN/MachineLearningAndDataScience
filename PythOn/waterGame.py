import random
NoOfChance = 0
systemScore = 0
UserScore = 0
lisst = ["Snack","Water", "Gun"]
while(NoOfChance<10):
    NoOfChance = NoOfChance + 1
    # userInput = userInput + 1
    userInput = int(input("Choose \n1: for Snack\n2: for Water\n3: for Gun : "))
    choice = random.choice(lisst)
    print(f"The random Choice generated by system is :{choice} and userInput is: {userInput}")

if userInput==1 :
    print("you Choosed Snack")
elif userInput==2 :
        print("you Choosed Water")
else:
        print("you Choosed Gun")

    

if userInput==choice :
    print("Match Draw")
# elif(userInput)