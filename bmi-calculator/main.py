'''
Write a program that interprets the Body Mass Index (BMI) based on
a user's weight and height.

It should tell them the interpretation of their BMI based on the
BMI value.

Conditions:
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.

Formula for BMI:
BMI = weight / (height ^2)
'''

print('Welcome to BMI Calculator!!')
weight = float(input('Enter your weight in kilograms(kg): '))
height = float(input('Enter your height in meters(m): '))

# round to 2 decimal places
roundedWeight = round(weight, 2)
roundedHeight = round(height, 2)
heightSquared = roundedHeight ** 2

# calculate bmi
bmi = round(roundedWeight / heightSquared, 2)
print(bmi)

# flow controls
if bmi < 18.5:
    print(f'Your BMI is {bmi}. you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}. you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}. you are slightly overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}. you are obese.')
else:
    print(f'Your BMI is {bmi}. you are clinically obese.')
