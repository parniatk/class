# استفاده از کلاس ماشین برای نمایش اظلاعات برند مدل و سال ان است
class Car :
    def __init__(self , brand , model , year) :
        self.brand = brand
        self.model = model
        self.year = year

    def get_car_info(self) :
        info = f"car : {self.brand} \n model : {self.model} year {self.year}"
        return info
    
brand = input("Enter your brand : ")
model = input("Enter model : ")
year = eval(input("Enter the year : "))
car = Car (brand , model , year)
print(car.get_car_info())
