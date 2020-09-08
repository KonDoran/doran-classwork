import pdb
gallon = 4.546
print("Enter the car mileage from the last time your car was filled.")
mileage1 = int(input())
print("Enter the current car mileage.")
mileage2 = int(input())
milestravelled = mileage2 - mileage1
print("Please enter the total number of litres taken to fill the tank.")
litres = float(input())
gallonsmile = (litres*gallon)/milestravelled 
print("Your car consumes",gallonsmile,"gallons per mile.")