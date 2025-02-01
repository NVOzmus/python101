#NV Ozmus
#Input
##request to enter number between 1-7
## if number is 1, enter monday, 2 enter tuesday, 3 enter wednesday, 4 enter thursday, 5 enter friday, 6 enter saturday, 7 enter sunday
#Output print the day and number

day = int(print("Enter a number 1 through 7 to calculate the corresponding day of the week"))
if day is 1: dayofweek = "Monday"
elif day is 2: dayofweek = "Tuesday"
elif day is 3: dayofweek = "Wednesday"
elif day is 4: dayofweek = "Thursday"
elif day is 5: dayofweek = "Friday"
elif day is 6: dayofweek = "Saturday"
elif day is 7: dayofweek = "Sunday"
else: dayofweek = "not a valid entry"

print("The day of the week you have entered is", dayofweek)