#Created by: Binod Gurung
#Date Created: 27 Sep 2021
#Date last modified: 27 Sep 2021

#LAB 4.3.1.6: Utilising parameterized funcitons and return statement to test leap year.

def is_year_leap(year):
#
    if year % 4 != 0:       #If the year divided by 4 doesn't give the remainder 0, it isn't a leap year.
        return False
    if year % 100 != 0:     #For some early Gregorian years, the leap years are found it the year is divisible by 100 but not divisible by 400.
        return True
    if year % 400 != 0:     #For some early Gregorian years, the leap years are found it the year is divisible by 100 but not divisible by 400.
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
#
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    if year % 4 == 0:
        return True
#

def days_in_month(year, month):
#
    No_of_days_Non_Leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #List of days for Non-leap years.
    No_of_days_Leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]      #List of days for leap years.
    if is_year_leap(year) and month == 2:                                   #Checking if the month is February of a leap year.
        return No_of_days_Leap
    else:                                                                   #For any conditions that isn't the months of February of a leap year.    
        return No_of_days_Non_Leap
#

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

#MODULE 4.3.1.8