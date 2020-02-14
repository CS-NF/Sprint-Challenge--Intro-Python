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

class FlightVehicle:
    pass

class Starship:
    pass

# inheritance of Vehicle class

class GroundVehicle:
    pass

#  inheritance of FlightVehicle class

class Airplane:
    pass

# inheritance of GroundVehicle class

class Car:
    pass

class Motorcycle:
    pass


