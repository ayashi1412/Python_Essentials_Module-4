#Created by: Binod Gurung
#Date Created: 27 Sep 2021
#Date last modified: 27 Sep 2021

#LAB 4.3.1.6: Utilising parameterized funcitons and return statement to test leap year.

def is_year_leap(year):
    if year % 4 != 0:       #If the year divided by 4 doesn't give the remainder 0, it isn't a leap year.
        return False
    if year % 100 != 0:     #For some early Gregorian years, the leap years are found if the year is divisible by 100 but not divisible by 400.
        return True
    if year % 400 != 0:     #For some early Gregorian years, the leap years are found if the year is divisible by 100 but not divisible by 400.
        return False
    if year % 4 == 0:       #If the year divided by 4 gives the remainder 0, it is a leap year after Gregorian year
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

#MODULE 4.3.1.7: Finding the number of days in a month in a year.

def is_year_leap(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    if year % 4 == 0:
        return True

def days_in_month(year, month):
    No_of_days_Non_Leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #List of days for Non-leap years.
    No_of_days_Leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]      #List of days for leap years.
    if is_year_leap(year) and month == 2:                                   #Checking if the month is February of a leap year.
        return No_of_days_Leap
    else:                                                                   #For any conditions that isn't the months of February of a leap year.    
        return No_of_days_Non_Leap

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

#MODULE 4.3.1.8 How to find Prime Numbers

def is_prime(num):
    if num == 2:                    #Taking a single argument to check.
        return True
    for i in range(2, num):         #If the given number is divided by 2 to itself and the remainder is 0, its not prime therefore, False. 
        if num % i == 0:
            return False
        else:
            return True             #Else, it is prime number.
    
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()

#MODULE 4.3.1.10 LAB: Converting Fuel Consumption

# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

def liters_100km_to_miles_gallon(litres): 
    gallons = litres / 3.785411784          #Converting litre to gallon which is small to big therefore, division.
    miles = (100 * 1000) / 1609.344         #Converting km to mile which is small to bigh therefore divide (100 * 1000 to convert from km to m.)
    return miles / gallons              

def miles_gallon_to_liters_100km(miles):    
    km_100 = miles * 1609.344 / (1000 * 100)  #Converting mile to m which is big to small therefore, multiplication (1000 * 100 converting km to m.)
    litres = 3.785411784                      #Converting gallon to litres; 1 gallon = 3.785411784 as given.
    return litres / km_100  

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

#END OF LAB