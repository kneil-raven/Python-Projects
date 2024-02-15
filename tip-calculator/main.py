'''
1. if bill is $150.00, split between 5 people, with 12% tip.
2. each person should pay (150.00 / 5) * 1.12 = 33.6
3. round to 2 decimal places
4. add percentage of bill you would like to give, 10, 12
'''

print('Welcome to tip calculator!')
bill = float(input('How much is your bill? $'))
tip = int(input('How much tip do you want to give? 10% or 12%? '))
numPersons = int(input('How many persons are paying? '))

billWithTip = (tip / 100) * bill + bill


billPerPerson = (billWithTip / numPersons)

print(f"Each person should pay ${round(billPerPerson, 2)}")