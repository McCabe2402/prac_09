from unreliable_car import UnreliableCar

# Create an UnreliableCar object
unreliable_car = UnreliableCar("Unreliable", 100, 50)  # 50% reliability

# Drive the unreliable car
distance_driven = unreliable_car.drive(30)

# Print the details and distance driven
print(f"Car details: {unreliable_car}")
print(f"Distance driven: {distance_driven} km")
