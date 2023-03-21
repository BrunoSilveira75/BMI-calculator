welcome_alert = print("Welcome to the BMI Calculator 2.0.\n")

name = input("Type your name: ")
weight = float(input("Type your weight in kgs: "))
height = float(input("Type your height in meters: "))

result = round(weight / (height * 2))

if result < 18.5:
    print(f"{name} you are underweight and your BMI is {result}")
elif result == 18.5 and result < 25:
    print(f"{name} you have a normal weight and your BMI is {result}")
elif result >= 25 and result < 30:
    print(f"{name} you are overweight and your BMI is {result}")
elif result >= 30 and result < 35:
    print(f"{name} you are obese and your BMI is {result}")
else:
    print(f"{name} you are clinically obese and your BMI is {result}")