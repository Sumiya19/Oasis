import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())  # Get weight from the user
        height = float(height_entry.get())  # Get height from the user
        
        # Check if values are within reasonable limits
        if weight <= 0 or height <= 0:
            raise ValueError("Height and weight must be positive numbers.")
        
        # Calculate BMI
        bmi = weight / (height ** 2)
        
        # Classify BMI into categories
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        
        # Display the result
        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for weight and height.")

# Function to clear input and result
def clear():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")

# Setup the GUI
root = tk.Tk()
root.title("BMI Calculator")

# Input for weight
weight_label = tk.Label(root, text="Enter your weight (in kg):")
weight_label.pack(pady=10)

weight_entry = tk.Entry(root, width=20)
weight_entry.pack(pady=5)

# Input for height
height_label = tk.Label(root, text="Enter your height (in meters):")
height_label.pack(pady=10)

height_entry = tk.Entry(root, width=20)
height_entry.pack(pady=5)

# Button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="center")
result_label.pack(pady=10)

# Button to clear the result
clear_button = tk.Button(root, text="Clear", command=clear)
clear_button.pack(pady=5)

# Main loop
root.mainloop()