class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self,km):
        if km > 0:
            self.mileage += km
            print(f"Drove {km} km. Total: {self.mileage} km")
        else:
            print("Distance must be positive!")

    def age(self, current_year):
        return current_year - self.year

    def ___str___(self):
        return f"{self.brand} {self.model} {self.year} - Wheels: {self.wheels}"

if __name__=="__main__":
    car1 = Car("Suzuki", "Jimny", 1970)
    car2 = Car("Suzuki", "Fronx", 2025)
    car3 = Car("Suzuki", "Vitara", 1988)

    print(car1)
    car1.drive(50)
    car1.drive(-10)
    print (f"Age: {car1.age(2025)} years")

    print()
    print(car2)
    print(car3)