import time                     #import time function

print(time.localtime().tm_yday)  #this will give an int value to todays date.

int_day = int(input("What date would you like to enter: "))  #need the int() otherwise it will be input as a string
int_month = input("What month would you like to enter: ")    #keeping this one as a string for now



def calculateTime():                                            #function to calculate time
    if int_month == '1':                                        #if statement for Januray
        print("Days since January," , int_day, " is...")        #opening statement
        print(time.localtime().tm_yday - (int_day + 31))        #print days
    elif int_month == '2':
        print("Days since February,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:                   #Inbedded if statement for leap years
            print(time.localtime().tm_yday - (int_day + 60))
        else:                                                   #Else statement for non-leap years
            print(time.localtime().tm_yday - (int_day + 59))
    elif int_month == '3':
        print("Days since March,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 91))
        else:
            print(time.localtime().tm_yday - (int_day + 90))
    elif int_month == '4':
        print("Days since April,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 90))
        else:
            print(time.localtime().tm_yday - (int_day + 89))
    elif int_month == '5':
        print("Days since May,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 121))
        else:
            print(time.localtime().tm_yday - (int_day + 120))
    elif int_month == '6':
        print("Days since June,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 151))
        else:
            print(time.localtime().tm_yday - (int_day + 150))
    elif int_month == '7':
        print("Days since July,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 182))
        else:
            print(time.localtime().tm_yday - (int_day + 181))
    elif int_month == '8':
        print("Days since August,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 213))
        else:
            print(time.localtime().tm_yday - (int_day + 212))
    elif int_month == '9':
        print("Days since September,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 243))
        else:
            print(time.localtime().tm_yday - (int_day + 242))
    elif int_month == '10':
        print("Days since October,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 274))
        else:
            print(time.localtime().tm_yday - (int_day + 273))
    elif int_month == '11':
        print("Days since November,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 304))
        else:
            print(time.localtime().tm_yday - (int_day + 303))
    elif int_month == '12':
        print("Days since December,", int_day, " is...")
        if time.localtime().tm_year % 4 == 0:
            print(time.localtime().tm_yday - (int_day + 335))
        else:
            print(time.localtime().tm_yday - (int_day + 334))
    else:
        print("Not the first 2 months")
        print(int_month)




calculateTime()
