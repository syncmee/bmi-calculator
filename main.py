#BMI Calculator
# Formula = BMI = Weight / Height*Height

print("Welcome to BMI Calculator")
weight = int(input("Please Type Your Weight in kg\n"))
height = float(input("Please Type Your Height in m\n"))
bmi = weight / height**2
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
