#Created by: Binod Gurung
#Date Created: 27 Sep 2021
#Date last modified: 27 Sep 2021

#LAB 4.3.1.6: Utilising parameterized funcitons and return statement to test leap year.

def is_year_leap(year):
#   
    if(year % 4 == 0):
        return True
      
#

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