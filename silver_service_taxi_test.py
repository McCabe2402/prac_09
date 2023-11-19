from silver_service_taxi import SilverServiceTaxi

# Create a SilverServiceTaxi object
silver_taxi = SilverServiceTaxi("Hummer", 200, 4)

# Drive the silver service taxi
silver_taxi.drive(18)

# Print the details and fare
print(f"SilverServiceTaxi details: {silver_taxi}")
print(f"Fare for the trip: ${silver_taxi.get_fare():.2f}")
