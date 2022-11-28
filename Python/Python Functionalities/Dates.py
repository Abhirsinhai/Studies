from datetime import date #Import date

now = date.today() #Check todays date
date3 = now.strftime("%B %d, %Y") #Format in strftime and put the formatted date into a variable
print("The date today is", date3) #Print out the date