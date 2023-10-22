class Student:
    noOfLeaves = 8

    # def __init__(self):
    #     self.name = name = input("Enter your name :")
    #     print("your name is :", name)
    #     self.salary = salary = input("Enter your Salary :")
    #     print("your name is :", salary)
    #     self.role = role = input("Enter your Role :")
    #     print("your Roll Number is :", role)
    #     return name,salary,role
        
    @classmethod
    def ChangeLeaves(cls,newLeaves):
        cls.noOfLeaves = newLeaves
sk = Student()
sk.ChangeLeaves(34)
print(sk.noOfLeaves)
# Aryan = Student()
# # print(sk)
# a = "sk aryan khan"
# print(Student.__dict__)
# print(a.capitalize())
# print(a.encode())
# print(a.isalpha())
# print(a.isalnum())
# print(a.isascii())
# print(a.lower())
