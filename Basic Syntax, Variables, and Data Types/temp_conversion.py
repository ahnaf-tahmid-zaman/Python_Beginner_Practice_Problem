# Convert a given temperature from Celsius to Fahrenheit and Vice-Versa



choice = int(input("------Which Conversion do you want?------\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\nEnter your preference (1 or 2): "))

if choice == 1:
    celsius_temp = float(input('Enter the temperature in Celsius: '))
    fahrenheit_temp = (celsius_temp * 9/5) + 32
    print(f'{celsius_temp} Celsius = {fahrenheit_temp:.4f} Fahrenheit')

elif choice == 2:
    fahrenheit_temp = float(input('Enter the temperature in Fahrenheit: '))
    celsius_temp = (fahrenheit_temp - 32) * 5/9
    print(f'{fahrenheit_temp} Fahrenheit = {celsius_temp:.4f} Celsius')

else:
    print("Invalid choice. Please enter 1 or 2.")
