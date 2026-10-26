#inheritance
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return  f"{self.brand} {self.model}"

class EletricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = EletricCar("Tesal","Model s","85")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.battery_size)




