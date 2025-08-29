class Vehicle:
    def move(self):
        return "The vehicle is moving"
# class Plane
class Plane(Vehicle):
    def move(self):
        return "The  plane is flying in the sky ✈️"

# class Car
class Car(Vehicle):
    def move(self):
        return "The car is driving on the road 🚗"

# displaying result
for vehicle in (Plane(), Car()):
    move = vehicle.move()
    print(move)