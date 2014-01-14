#Hardway page 4
#Setting variables and names

#Define initial variables
#Number of cars
cars = 100
#Number of seats in each car
space_in_a_car = 4.0
#Number of drivers
drivers = 30
#Number of passengers
passengers = 90

#Calculate new variables from initial variables
#Calculates number of cars without drivers
cars_not_driven = cars - drivers
#Creates a variable for the number of driven cars
cars_driven = drivers
#Calculates the maximum capacity of the carpool
carpool_capacity = cars_driven * space_in_a_car
#Calculates the average number of passengers per car
average_passengers_per_car = passengers / cars_driven

#Creates output to screen
print 'There are', cars, 'cars available.'
print 'There are only', drivers, 'drivers available.'
print 'There will be', cars_not_driven, 'empty cars today.'
print 'We can transport', carpool_capacity, 'people today.'
print 'We have', passengers, 'to carpool today.'
print "We need to put about", average_passengers_per_car, "in each car."
