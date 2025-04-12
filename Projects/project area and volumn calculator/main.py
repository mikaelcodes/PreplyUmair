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



label_volume_length = tk.Label(frame_right, text="Volume Length:")
label_volume_length.pack(pady=5)
ent_volume_length= tk.Entry(frame_right, width=20)
ent_volume_length.pack(pady=5)
lable_volume_width = tk.Label(frame_right, text="Volume Width:")
lable_volume_width.pack(pady=5)
ent_volume_width = tk.Entry(frame_right, width=20)
ent_volume_width.pack(pady=5)
lable_volume_depth = tk.Label(frame_right, text="Volume Depth:")
lable_volume_depth.pack(pady=5)
ent_volume_depth = tk.Entry(frame_right, width=20)
ent_volume_depth.pack(pady=5)

def calculate_volume(length_entry, width_entry):
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        depth = float(ent_volume_depth.get())
        volume = length * width * depth  # Assuming a fixed height of 10 for volume calculation
        lable_result_volume.config(text=f"Volume: {volume}")
    except ValueError:
        lable_result_volume.config(text="Invalid input!")

button_volume = tk.Button(frame_right, text="Calculate Volume", command=lambda: calculate_volume(ent_volume_length, ent_volume_width))
button_volume.pack(pady=10)
lable_result_volume = tk.Label(frame_right, text="Volume:")
lable_result_volume.pack(pady=5)





tk.mainloop()




