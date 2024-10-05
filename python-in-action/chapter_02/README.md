## **Chapter 2: Variables, Data Types, and Operations**

### **How the Temperature Converter Works:**

1. **User Input:**
   - The program prompts the user to enter a temperature (as a floating-point number) and the unit of the temperature (`C` for Celsius or `F` for Fahrenheit).
   - The input for the unit is converted to uppercase using `.upper()` to ensure that both lowercase and uppercase letters are accepted.
2. **Conditional Statements:**
   - The program checks the unit of temperature entered by the user:
     - If the unit is `"C"`, it converts the Celsius temperature to Fahrenheit using the formula: Fahrenheit=(95×Celsius)+32\\text{Fahrenheit} \= \\left(\\frac{9}{5} \\times \\text{Celsius}\\right) \+ 32Fahrenheit=(59​×Celsius)+32
     - If the unit is `"F"`, it converts the Fahrenheit temperature to Celsius using the formula: Celsius=59×(Fahrenheit−32)\\text{Celsius} \= \\frac{5}{9} \\times (\\text{Fahrenheit} \- 32)Celsius=95​×(Fahrenheit−32)
3. **Invalid Input Handling:**
   - If the user enters an invalid unit (anything other than `"C"` or `"F"`), the program prints an error message indicating that the input is invalid.

### **Example Usage:**

`Enter the temperature: 25`  
`Is this in Celsius or Fahrenheit? (C/F): C`  
`25.0°C is equal to 77.0°F`

`Enter the temperature: 77`  
`Is this in Celsius or Fahrenheit? (C/F): F`  
`77.0°F is equal to 25.0°C`

This project helps reinforce concepts such as **user input**, **conditional logic**, **basic arithmetic operations**, and **type casting** between different data types in Python.
