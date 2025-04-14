"""
This is the main file for the grocery application. First we will make 
a list of grocery items and their prices. Then we will create a function
to calculate the total price of the items in the list. Finally, we will 
create a GUI using tkinter to display the grocery list and the total price.
We will also add a button to calculate the total price and display it in
the GUI.

"""

import tkinter as tk

database = {
    'Apple': 1.2,
    'Banana': 0.5,
    'Orange': 0.8,
    'Grapes': 2.5,
    'Mango': 1.5,
    'Pineapple': 3.0,
    'Strawberry': 2.0,
    'Blueberry': 2.5,
    'Watermelon': 4.0,
    'Peach': 1.8,
    'Cherry': 2.2,
    'Kiwi': 1.0,
    'Papaya': 1.5,
    
}



fruits = list(database.keys())
prices = list(database.values())

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


selected_fruits = {}

def add_fruit():
    selected_fruit = fruits_var.get()
    if selected_fruit == 'select a fruit':
        label_result.config(text="Please select a fruit!")
        return
    if selected_fruit in fruits:
        label_result.config(text=f"{selected_fruit} is already in the list!")
    else:
        fruits.append(selected_fruit)
        prices.append(database[selected_fruit])
        label_result.config(text=f"{selected_fruit} added to the list!")
    fruits_var.set('select a fruit')  # reset the dropdown to default value
    selected_fruits[selected_fruit] = database[selected_fruit]  # Add the selected fruit to the dictionary

button_add = tk.Button(windows, text="Add Fruit", command=add_fruit)
button_add.pack(pady=10)





# make a button to calculate the total price
def calculate_total_price():
    total = 0
    for fruit, price in selected_fruits.items():
        try:
            quantity = int(ent_quantity.get())
            total += price * quantity
        except ValueError:
            label_result.config(text="Invalid quantity!")
            return
    label_result.config(text=f"Total Price: ${total:.2f}")

 

button_calculate = tk.Button(windows, text="Calculate Total Price", command=calculate_total_price)
button_calculate.pack(pady=10)

label_result = tk.Label(windows, text="Total Price:")
label_result.pack(pady=5)






tk.mainloop()
