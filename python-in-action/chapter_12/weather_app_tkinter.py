
import tkinter as tk

def show_weather():
    city = entry.get()
    label.config(text=f"Weather in {city}: Sunny, 25°C")  # Placeholder weather data

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Create a label for instructions
instruction_label = tk.Label(window, text="Enter city name:")
instruction_label.pack()

# Create an entry widget for city input
entry = tk.Entry(window)
entry.pack()

# Create a button to show weather data
button = tk.Button(window, text="Show Weather", command=show_weather)
button.pack()

# Create a label to display the weather information
label = tk.Label(window, text="")
label.pack()

# Start the event loop
window.mainloop()
