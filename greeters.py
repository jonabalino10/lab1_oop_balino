class Car:
    wheels = 4
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand}{self.model}{self.year} - wheels: {self.wheels}"

car1= Car("Suzuki", "Jimny", "2020")
car2= Car("Suzuki", "Espresso", "2021")
car3= Car("Suzuki", "Vitara", "2022")

print(car1)
print(car2)
print(car3)