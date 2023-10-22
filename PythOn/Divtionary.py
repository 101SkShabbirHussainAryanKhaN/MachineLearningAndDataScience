#Dictionary is the key value of words pairs
d1 = {}
print(type(d1))
d2 = {"Shabbir ":"Pitza", "Aryan" : "SandWich", "Khurram":"Bhindi",
"Shakir" :{"Break Fast" : "Chai parathy", "Launch" : "Daal Roti" , "Dinner" : "Beef Biryani"}}

# by using this method we addd in dictionary
d2 ["Agha Shehzad"] = "Chicken KArahi"
d2 ["Mukarram Jaffari"] = "KabaB"
#delete command in dictionary
del d2["Mukarram Jaffari"]
print(d2)
print(d2["Aryan"])
print(d2["Shakir"] , "Dinner")
print(d2["Shabbir"])