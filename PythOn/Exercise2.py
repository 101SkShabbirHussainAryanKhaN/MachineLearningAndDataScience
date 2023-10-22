n = 18
nbrOfGuess = 1
limit = 7 
while (nbrOfGuess <= limit) :
   userInput  = int(input("Guess a number :"))
   if userInput > n :
         print("This is your Guess No:",nbrOfGuess)
         print("you Guessed too High! Try Again")
         
   elif userInput < n:
        print("you Guessed too Low! Try Again")
        print("This is your Guess No:",nbrOfGuess)

   else:
       print("Congratulations! you are winner",n)
       print("This is your Guess No:",nbrOfGuess)
       
   nbrOfGuess = nbrOfGuess + 1
   
if nbrOfGuess > limit :
   print("\n\tGame OvEr! \n    OOps you are Loser! :")