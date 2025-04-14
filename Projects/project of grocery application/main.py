"""
This is the main file for the grocery application. First we will make 
a list of grocery items and their prices. Then we will create a function
to calculate the total price of the items in the list. Finally, we will 
create a GUI using tkinter to display the grocery list and the total price.
We will also add a button to calculate the total price and display it in
the GUI.

"""

import tkinter as tk

fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Mango', 'Pineapple', 'Strawberry', 'Blueberry', 'Watermelon', 'Peach']
prices = [1.2, 0.5, 0.8, 2.5, 1.5, 3.0, 2.0, 2.5, 4.0, 1.8]

windows = tk.Tk()
windows.title("Mikaels Grocery Application")
windows.geometry("400x400")


Label_title = tk.Label(windows, text="Grocery Application", font=("Arial", 14, "bold"))
Label_title.config(bg="lightblue", fg="black")
Label_title.pack(pady=20)


# make a dropdown list of fruits
label_fruits = tk.Label(windows, text="Select a fruit:")
label_fruits.pack(pady=5)   

fruits_var = tk.StringVar()
fruits_var.set('select a fruit')  # set the default value to the first fruit

fruits_dropdown = tk.OptionMenu(windows, fruits_var, *fruits)
fruits_dropdown.pack(pady=5)



# entry to choose quantity
label_quantity = tk.Label(windows, text="Enter quantity:")
label_quantity.pack(pady=5)

ent_quantity = tk.Entry(windows, width=20)
ent_quantity.pack(pady=5)


# make a button to calculate the total price
def calculate_total_price():
    try:
        selected_fruit = fruits_var.get()
        selected_price = prices[fruits.index(selected_fruit)]  # Get the price based on the selected fruit
        quantity = int(ent_quantity.get())
        if selected_fruit == 'select a fruit' or selected_price == 'choose price':
            label_result.config(text="Please select a fruit and price!")
            return
        if quantity <= 0:
            label_result.config(text="Please enter a valid quantity!")
            return
        total_price = selected_price * quantity  # Assuming quantity is 1 for simplicity
        label_result.config(text=f"Total Price: ${total_price:.2f}")
    except ValueError:
        label_result.config(text="Invalid input!")


button_calculate = tk.Button(windows, text="Calculate Total Price", command=calculate_total_price)
button_calculate.pack(pady=10)

label_result = tk.Label(windows, text="Total Price:")
label_result.pack(pady=5)






tk.mainloop()
