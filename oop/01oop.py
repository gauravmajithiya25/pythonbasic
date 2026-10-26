#oop
class Car:
    # brand = "TATA"
    # model = "Punch"
    def __init__(self, userbrand,usermodel):
        self.brand = userbrand
        self.model = usermodel

mycar = Car("TATA","punch")
print(mycar.brand)
print(mycar.model)
my_new_car = Car("safari","abc")
print(my_new_car.brand)
print(my_new_car.model)


#print(mycar.model)
