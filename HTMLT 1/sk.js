alert("Hi ,Aryan Khan")
let age = prompt("Enter your age? ")
document.write("your age is :",age,"\n")
let hasVoterId = Boolean(prompt("Do you have Voter Id Card? "))
if(age>=18){
    if(hasVoterId==true){
        document.write("Congratulations!",<br></br>)
    }else{
        document.write("Sorry, for now get your ID card for next time.")
    }
    document.write("you can vote")        
}
else{
    document.write("Sorry, you are not eligible under aged!")
}