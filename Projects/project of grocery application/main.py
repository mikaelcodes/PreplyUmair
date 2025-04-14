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
windows.title("Grocery Application")
windows.geometry("400x400")


Label_title = tk.Label(windows, text="Grocery Application", font=("Arial", 14, "bold"))
Label_title.config(bg="lightblue", fg="black")

Label_title.pack(pady=20)


