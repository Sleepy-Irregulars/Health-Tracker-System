class Vehicle:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start_engine(self):
        raise NotImplementedError("Subclasses must implement start_engine method")

    def accelerate(self):
        raise NotImplementedError("Subclasses must implement accelerate method")

    def brake(self):
        raise NotImplementedError("Subclasses must implement brake method")

# Now, let's create a subclass of Vehicle, such as Car

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started."

    def accelerate(self):
        return "Car is accelerating."

    def brake(self):
        return "Car is braking."

# Using the Vehicle and Car classes

my_car = Car(color="red", brand="Toyota")
print(f"My {my_car.color} {my_car.brand} is ready to go!")
print(my_car.start_engine())
print(my_car.accelerate())
print(my_car.brake())


print("GABUYO!!!!! ")
