import tkinter as tk


root = tk.Tk()
root.title("Simple Form")
root.geometry("450x500")
root.config(bg="lightyellow")


name_var = tk.StringVar()
number_var = tk.StringVar()
gender_var = tk.StringVar(value="")  # Default empty
hobby_reading = tk.IntVar()
hobby_sports = tk.IntVar()
hobby_music = tk.IntVar()


def submit():
    name = name_var.get()
    number = number_var.get()
    gender = gender_var.get()
    hobbies = []

    if hobby_reading.get():
        hobbies.append("Reading")
    if hobby_sports.get():
        hobbies.append("Sports")
    if hobby_music.get():
        hobbies.append("Music")

    
    output_text.delete(1.0, tk.END)

    
    output_text.insert(tk.END, f"Name: {name}\n")
    output_text.insert(tk.END, f"Phone Number: {number}\n")
    output_text.insert(tk.END, f"Gender: {gender}\n")
    output_text.insert(tk.END, f"Hobbies: {', '.join(hobbies) if hobbies else 'None'}\n")


tk.Label(root, text="Name:", bg="lightyellow", font=("Arial", 12)).place(x=50, y=30)
tk.Entry(root, textvariable=name_var, width=30).place(x=180, y=30)

tk.Label(root, text="Phone Number:", bg="lightyellow", font=("Arial", 12)).place(x=50, y=80)
tk.Entry(root, textvariable=number_var, width=30).place(x=180, y=80)

tk.Label(root, text="Gender:", bg="lightyellow", font=("Arial", 12)).place(x=50, y=130)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="lightyellow").place(x=180, y=130)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="lightyellow").place(x=250, y=130)

tk.Label(root, text="Hobbies:", bg="lightyellow", font=("Arial", 12)).place(x=50, y=180)
tk.Checkbutton(root, text="Reading", variable=hobby_reading, bg="lightyellow").place(x=180, y=180)
tk.Checkbutton(root, text="Sports", variable=hobby_sports, bg="lightyellow").place(x=180, y=210)
tk.Checkbutton(root, text="Music", variable=hobby_music, bg="lightyellow").place(x=180, y=240)


tk.Button(root, text="Submit", command=submit, bg="green", fg="white", font=("Arial", 12)).place(x=180, y=290)


output_text = tk.Text(root, height=7, width=40, font=("Arial", 12))
output_text.place(x=50, y=350)


root.mainloop()
