import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def button_callback():
   label.configure(text=button.cget('text'))

root = customtkinter.CTk()
root.geometry("400x150")

root.title('Tkinter.com - Custom Tkinter Buttons')
#root.iconbitmap('images/codemy.ico')
root.geometry('600x350')

button = customtkinter.CTkButton(
    root, text="HELLO WORLD!!!", 
    command=button_callback,
    height=100,
    width=200,
    font=("Helvetica",24),
    text_color='black',
    fg_color="red",
    hover_color="green",
    corner_radius=50,
    bg_color='white',
    border_width=10,
    border_color='yellow',
    state="normal")

button.pack(pady=80)

label= customtkinter.CTkLabel(root, text='')
label.pack(pady=20)
root.mainloop()