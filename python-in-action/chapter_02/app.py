# Temperature Converter

# Step 1: Get user input for the temperature and unit
temperature = float(input("Enter the temperature: "))
unit = input("Is this in Celsius or Fahrenheit? (C/F): ").upper()

# Step 2: Perform the conversion
if unit == "C":
    # Convert Celsius to Fahrenheit
    converted_temp = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temp}°F")
elif unit == "F":
    # Convert Fahrenheit to Celsius
    converted_temp = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temp}°C")
else:
    print("Invalid input! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
