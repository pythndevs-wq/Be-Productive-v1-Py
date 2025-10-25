import customtkinter as ctk
from tkinter import messagebox
import json
from PIL import Image
import dashboard

root = ctk.CTk()
root.geometry("800x600")
root.title("Get Started!")
root._set_appearance_mode("light")
root.maxsize(800, 600)
root.minsize(800, 600)

global my_x1, my_x2, my_x3
my_x1 = 500/2 + 350
my_x2 = 500/2 - 550
my_x3 = 500/2 + 400

def animate_login_btn():
    global my_x1
    my_x1 -= 5
    if my_x1 >=80:
        login_btn.place(x = my_x1, y = 400)
        root.after(4, animate_login_btn)


def animate_pass_entry():
    global my_x2
    my_x2 += 5
    if my_x2 <= 80:
        password_entry.place(x=my_x2, y=300)
        root.after(4, animate_pass_entry)

def animate_user_entry():
    global my_x3
    my_x3 -= 5
    if my_x3 >=80:
        username_entry.place(x=my_x3, y=200)
        root.after(4, animate_user_entry)




def login():
    global username, password
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror(title="Program",message='User name and password is Required!')
    

    else:
        messagebox.showinfo(title="Program",message=f"Welcome Back, {username_entry.get()}")
        root.destroy()
        dashboard.main_dash()


def check_login_data():
    pass


def login_main():

    login_frame = ctk.CTkFrame(master=root, width=300, height=600, fg_color='#f7f7f7', corner_radius=0)
    login_frame.place(x=500, y=0)
    global username_entry, password_entry, login_btn


    username_label = ctk.CTkLabel(master=login_frame, text="Username: ", font=("Arial", 24), text_color="#333333")
    username_label.place(x=30, y=150)

    username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Enter Username", fg_color="#ffffff", border_color="#dddddd", text_color="#333333")
    username_entry.place(x=150, y=200)
    animate_user_entry()


    password_label = ctk.CTkLabel(master=login_frame, text="Password: ", font=("Arial", 24), text_color="#333333")
    password_label.place(x=30, y=250)

    password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Enter Password", fg_color="#ffffff", border_color="#dddddd", text_color="#333333")
    password_entry.place(x=150, y=300)
    animate_pass_entry()


    login_btn = ctk.CTkButton(master=login_frame, text="Login", corner_radius=32, fg_color="#007bff", text_color="#ffffff", hover_color="#007bff",border_width=1, command=login)
    login_btn.place(x = my_x1, y = 400)
    animate_login_btn()


    head_frame = ctk.CTkFrame(master=root, width=800, height=50)
    head_frame.place(x=0, y=0)
    login_text = ctk.CTkLabel(head_frame, text='Login', font=("Arial", 34), text_color="#ffffff")
    login_text.place(x= 350 , y = 5)
    

    
    root.mainloop()

if __name__ == "__main__":
    login_main()


