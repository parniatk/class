# کلاسی به نام حسابگر برای انجام عملیات پایه ریاضی مانند جمع، تفریق، ضرب و تقسیم ایجاد می کنیم. 
class Calculator :
    def __init__(self , num1 , num2 ):
        self.num1 = num1
        self.num2 = num2
#متودی برای جمع دو عدد
    def total (self) :
        sum = self.num1 + self.num2 
        return sum
#متودی برای تفریق دو عدد
    def subtraction (self) :
        sub = self.num1 - self.num2
        return sub
#متودی برای ضرب دو عدد
    def multiply (self) :
        mul = self.num1 * self.num2
        return mul
#متودی برای تقسیم دو عدد
    def divide (self) :
        div = self.num1 / self.num2
        return div
# دریافت ورودی از کاربر
num1 = eval(input("Enter the first number :"))
num2 = eval(input("enter the second number "))

calculator = Calculator (num1 , num2)

print(f"sum of numbers : {calculator.total()}")
print(f"sub of numbers : {calculator.subtraction()}")
print(f"mul of numbers : {calculator.multiply()}")
print(f"div of numbers : {calculator.divide()}")
