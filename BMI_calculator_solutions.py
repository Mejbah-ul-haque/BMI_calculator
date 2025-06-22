print("Welcome to BMI Calculator")

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in KG: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"You have a normal weight.")
elif bmi < 30:
    print(f"You are slightly overweight.")
elif bmi < 35:
    print(f"You are obese.")
else:
    print(f"You are clinically obese!")
    print(f"Please! Go to the doctor's Chamber!")