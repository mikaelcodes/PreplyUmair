'# making a simple calculaotr'
import math
import tkinter as tk
# change display size

window = tk.Tk()
window.geometry("400x400")


my_entry = tk.Entry()
my_entry.pack()
my_entry2 = tk.Entry()
my_entry2.pack()



my_label = tk.Label(text = "result:")
my_label.pack()

def mikalel():
    try:
        x = float(my_entry.get())
        y = float(my_entry2.get())
    
        z = x + y
        w = x - y
        h = x * y
        i = x / y
        aa = math.sqrt(x-y)
        my_label.config(text = f"sum:{z}\n diff:{w}\nmulti:{h}\nratio:{i}\nsqrt{aa}  " ) 
    except:
        my_label.config(text = f"error" )

button = tk.Button(text = "calculate", command = mikalel )
button.pack()


## make new label
# make new entry 
## make new button
# when you will write temperature in celsius it will convert to fahrenheit

mylable2 = tk.Label(text = "Write temperature in C:")
my_entry3 = tk.Entry()
mylable2.pack()
my_entry3.pack()

def mikalel2():
    try:
        x = float(my_entry3.get())
        y = x * 9/5 + 32
        mylable2.config(text = f"fahrenheit:{y}  " ) 
    except:
        mylable2.config(text = f"error" )   

button2 = tk.Button(text = "calculate tem in F", command = mikalel2 )    

button2.pack()


tk.mainloop()

