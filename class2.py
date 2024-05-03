#کلاسسی به نام شخص ایجاد کرده و اطلاعات فرد را مانند نام و سن و شغل ذخیره کند
class Person :
    def __init__(self , name , age , job) :
        self.name = name
        self.age = age
        self.job = job

    def introduce_self (self) :
        return print(f"my name is {name} , my age is {a} and my job is {job}")

name = input("Enter your name : ")
a = eval(input("Enter your age : "))
job = input("Enter your job : ")

person = Person ( name , a , job)
print (person.introduce_self())