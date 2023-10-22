
# def showName(a,b,c,d):
#     print(a,b,c,d)

# showName("Sk aryan" ,"Noor alam" , "Khan Baba" , "Drama COmpany")

def funargs(normal, *args, **kwargs):
    print(normal)
    for items in args :
        print(items)

    for key, value in kwargs.items():
        print("\nThese are Some Greatest people of the world")
        print(f"{key} is a {value}")
    # print(args[1])
    print("it will tell us type of data :-",type(args))
    # print(args[2])
    # print(args[3])
    # print(args[4])
normal = "i am normal "
# skjan =["Sk aryan" ,"Noor alam" , "Khan Baba" , "Drama COmpany"]
skjan =("Sk aryan" ,"Noor alam" , "Khan Baba" , "Drama COmpany")

skj = {"Aryan" :"King", "sk Shabbir" : "Emperor","shakir" : "wazir"}
funargs(normal , *skjan ,**skj)