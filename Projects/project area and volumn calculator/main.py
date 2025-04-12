import tkinter as tk

windows = tk.Tk()
windows.title("Project Area and Volume Calculator")
windows.geometry("400x400")

Label_title = tk.Label(windows, text="Project Area and Volume Calculator", font=("Arial", 14, "bold"))
Label_title.config(bg="lightblue", fg="black")
Label_title.pack(pady=20)


frame_left = tk.Frame(windows)
frame_left.pack(side=tk.LEFT, padx=20)

frame_right = tk.Frame(windows)
frame_right.pack(side=tk.RIGHT, padx=20)


label_area_length = tk.Label(frame_left, text="Area Length:")
label_area_length.pack(pady=5)
ent_area_length = tk.Entry(frame_left, width=20)
ent_area_length.pack(pady=5)

label_area_width = tk.Label(frame_left, text="Area Width:")
label_area_width.pack(pady=5)
ent_area_width = tk.Entry(frame_left, width=20)
ent_area_width.pack(pady=5)

def calculate_area(length_entry, width_entry):
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        area = length * width
        label_result_area.config(text=f"Area: {area}")
    except ValueError:
        label_result_area.config(text="Invalid input!")

button_area = tk.Button(frame_left, text="Calculate Area", command=lambda: calculate_area(ent_area_length, ent_area_width))
button_area.pack(pady=10)

label_result_area = tk.Label(frame_left, text="Area:")
label_result_area.pack(pady=5)









tk.mainloop()




