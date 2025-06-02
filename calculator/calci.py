import tkinter as tk
import math 
# --- Calculator Logic ---

current_expression = ""
MAX_DIGITS = 12 # Define the maximum number of digits allowed in the display

def button_click(char):
    global current_expression
    current_text = entry.get()

    # Check if the character is a digit or a decimal point
    # and if the current length is less than MAX_DIGITS
    if str(char).isdigit() or str(char) == '.':
        if len(current_text) >= MAX_DIGITS:
            # If max digits reached, do not append the character
            return
    
    # Append the character
    entry.delete(0, tk.END) # Clear current content
    entry.insert(0, current_text + str(char)) # Insert updated content

def clear_click():
    """Clears the display."""
    global current_expression
    entry.delete(0, tk.END)
    current_expression = ""

def backspace_click():
    """Removes the last character from the display."""
    global current_expression
    current_text = entry.get()
    if current_text:
        new_text = current_text[:-1]
        entry.delete(0, tk.END)
        entry.insert(0, new_text)
        current_expression = new_text

def sqrt_operation():
    try:
        num_str = entry.get()
        if not num_str or num_str == '.':
            raise ValueError("Invalid input for square root.")
        num = float(num_str)
        if num < 0:
            raise ValueError("Cannot take square root of a negative number.")
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        global current_expression
        current_expression = str(result)
    except ValueError as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        print(f"Square Root Error: {e}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        print(f"General Square Root Error: {e}")

def calculate():
    """Evaluates the expression in the display."""
    global current_expression
    try:
        expression = entry.get()
        # Using eval() for full expression evaluation.
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        current_expression = str(result)
    except (SyntaxError, ZeroDivisionError, NameError) as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        print(f"Calculation Error: {e}")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        print(f"General Error during calculation: {e}")


# --- GUI Setup ---
window = tk.Tk()
window.title("Advanced Calculator")
window.geometry("350x500") # Adjusted height for new layout
window.resizable(False, False)

# Entry widget (display)
entry = tk.Entry(window, width=20, font=("Arial", 20), borderwidth=2, relief="groove", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Define button dimensions and font
btn_width = 6
btn_height = 2
btn_font = ("Arial", 14)

# Create buttons (numbers and basic operators)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3) # C and + are now here
]

for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(window, text=text, command=clear_click, width=btn_width, height=btn_height, font=btn_font, bg="lightcoral")
    else:
        button = tk.Button(window, text=text, command=lambda t=text: button_click(t), width=btn_width, height=btn_height, font=btn_font)
    button.grid(row=row, column=col, padx=5, pady=5)

# Add DEL button
button_del = tk.Button(window, text="DEL", command=backspace_click, width=btn_width, height=btn_height, font=btn_font, bg="orange")
button_del.grid(row=5, column=0, padx=5, pady=5)

# Add advanced operation buttons (parentheses, exponent)
button_open_paren = tk.Button(window, text="(", command=lambda: button_click('('), width=btn_width, height=btn_height, font=btn_font)
button_open_paren.grid(row=5, column=1, padx=5, pady=5)

button_close_paren = tk.Button(window, text=")", command=lambda: button_click(')'), width=btn_width, height=btn_height, font=btn_font)
button_close_paren.grid(row=5, column=2, padx=5, pady=5)

button_exponent = tk.Button(window, text="^", command=lambda: button_click('**'), width=btn_width, height=btn_height, font=btn_font)
button_exponent.grid(row=5, column=3, padx=5, pady=5)

# Add sqrt button
button_sqrt = tk.Button(window, text="sqrt", command=sqrt_operation, width=btn_width, height=btn_height, font=btn_font)
button_sqrt.grid(row=6, column=0, padx=5, pady=5)

# Equals button (now on row 6, spanning 3 columns)
equals_button = tk.Button(window, text="=", command=calculate, width=btn_width * 3 + 2, height=btn_height, font=btn_font, bg="lightgreen")
equals_button.grid(row=6, column=1, columnspan=3, padx=5, pady=5) # Spanning the remaining 3 columns

# Run the main loop
window.mainloop()
