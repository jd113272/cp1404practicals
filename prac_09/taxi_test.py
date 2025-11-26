from taxi import Taxi

# 1. Create a new taxi object named my_taxi
my_taxi = Taxi("Prius 1", 100)
# 2. Drive taxi
my_taxi.drive(40)
# 3. Print details and current fare
print(my_taxi)
# 4. Restart meter and drive car 100km
my_taxi.start_fare()
my_taxi.drive(100)
# 5. Print details and current fare
print(my_taxi)
