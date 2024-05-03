#کلاسسی به نام محصول ایجاد کرده و اطلاعات یک محصول را مانند نام و قیمت و تعداد موجودی را نمایش دهد
class Product:
    def __init__(self , name , price , quantity) :
        self.name = name 
        self.price = price
        self.quantity = quantity

    def display_product_info(self) :
        print(f"name of product  is : {name}")
        print(f"price product: {price}")
        print(f"Number of product inventory {quantity}")

name = input("enter the name of product :")
price = eval(input("enter the price :"))
quantity = eval (input("enter Number of inventory : "))
product = Product (name , price , quantity)
print (product.display_product_info())