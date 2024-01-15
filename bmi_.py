import tkinter as tk

def calculate_bmi(weight, height):
    # BMI formula
    return weight / (height ** 2)

def classify_bmi(bmi):
    # Classify BMI based on predefined ranges
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def calculate_button_clicked():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Invalid input. Weight and height must be positive.")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError as e:
        result_label.config(text=f"Error: {e}")

# Create the main window
window = tk.Tk()
window.title("BMI Calculator")

# Create and place widgets
weight_label = tk.Label(window, text="Weight (kg):")
weight_label.pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

height_label = tk.Label(window, text="Height (m):")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()

calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_button_clicked)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Run the Tkinter event loop
window.mainloop()
