import time  # import time function

int_year = int(input("What year would you like to enter: "))    #get integer value of year required

year_Value = time.localtime().tm_year - int_year                #subtract year entered from current year
year_in_days = year_Value * 365                                 #multiply result by 365

for x in range(int_year, time.localtime().tm_year):             #for loop with range of year selected and current year
    if x % 4 == 0:                                              #if its a leap year...
        year_in_days += 1                                       #add an extra year


month_list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #starting at 0 so that 1 is Jan, 2 is Feb, etc

int_month = int(input("Enter a number for the month: "))        #Take in int value for month


month_in_days = 0
for x in range(1, int_month):                                   #prints off the months from January and the month prior. The current month is left out.
    month_in_days += month_list[x]                              #adds value of months to month_in_days


current_day = time.localtime().tm_yday                          #Current number of days per Julian Calendar. Days since Jan 1st.


int_day = int(input("Enter a day value: "))                     #Get an int value for day in the month

total_value = time.localtime().tm_yday - month_in_days - int_day + year_in_days
                                                                #Current day minus previous months (in days) minus day selected add years total

print("Total number of days is: ", total_value)                        #Output of all days

