# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#base class 
class Vehicle:
    pass

# inheritance of Vehicle class

class FlightVehicle(Vehicle):
    pass

# inheritance of FlightVehicle class

class Starship(FlightVehicle):
    pass

# inheritance of Vehicle class

class GroundVehicle(Vehicle):
    pass

#  inheritance of FlightVehicle class

class Airplane(FlightVehicle):
    pass

# inheritance of GroundVehicle class

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass


