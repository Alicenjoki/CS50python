class names():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

name = names("Alice", "Kamuyu")

print(f"My name is {name.firstName} {name.lastName}")

class flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity -len(self.passengers)

Flight = flight(3)

people = ["Alice", "Collins", "Stacy", "Milley", "Jane", "Mitchelle"]
for person in people:
    success = Flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight sucesfully")
    else:
        print(f"No available seat for {person}")
