# LAB 1

# 1.1 Part A

temperature_F = float(input("Please enter the temperature in Fahrenheit: "))

temperature_C = (temperature_F - 32) * 5/9

print("The temperature in Celsius is", temperature_C)


# 1.2 Part B

height = float(input("Please enter the height of the trapezoid: "))
bottom = float(input("Please enter the length of the bottom base of the trapezoid: "))
top = float(input("Please enter the length of the top base of the trapezoid: "))

area = 0.5*(bottom+top)*height

print("The area of the trapezoid is", area)

# 1.3 Part C

distance = input("Please insert the total number of KMs traveled: ")
distance = float(distance)
time_min = float(input("Please insert the total number of minutes traveled: "))
hours = time_min/60

speed = int(distance / hours)

print("You were traveling at an average speed of", speed, "km//h.")