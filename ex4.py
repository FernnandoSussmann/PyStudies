cars = 100
space_in_a_car = 4.0 #4.0 because it's float
drivers = 30
passengers = 90
cars_not_driven = cars - drivers # set the number of cars that are unused
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car #Sees the number of people able to be transported with the number of drivers we set before
average_passengers_per_car = passengers / cars_driven

#prints sentences using everything we created
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
