''' Lists are great for storing items we may want to change throughout the life of a program.  We can also modify lists, they are mutable!  However, there are situations where we may want a data structure that cannot be modified. 
An immutable data structure!  Hello tuples.'''

# here's a basic tuple that we might use for coordinates

coordinate = (7,4)

# we use parentheses to declare a tuple, however we can use the familiar
# brackets to access the tuple values at their index.
  
print(coordinate[0])
print(coordinate[1])

# if we attempt this:

# coordinate[0] = 9

# we will most definitely receive a "tuple" object does not support item assignment error.

# to circumvent this, you can declare a new tuple.

coordinate = (10,12)

# let's create a quick exotic car rental program that exemplifies tuples, and use a for loop, just as we can with a list, to iterate over these tuples.

exotic_cars = ('Ferrari', 'Lotus', 'Aston Martin', 'Maserati', 'Porsche')
car_rental_cost = (120, 70, 120, 70, 90)

for car in exotic_cars:
	print(car)

print ("A " + exotic_cars[0] + " is $" + str(car_rental_cost[0]) + " per day")

# we decide that we are no longer going to rent Maseratis

exotic_cars = ('Ferrari', 'Lotus', 'Aston Marton', 'Porsche')
car_rental_cost = (120, 70, 120, 90)

for car in exotic_cars:
	print(car)


