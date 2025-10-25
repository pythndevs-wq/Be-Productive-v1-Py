import customtkinter as ctk
from tkinter import messagebox
import login
import dashboard

main = ctk.CTk()
main.title("Be Productive")
main.geometry("500x600")
main._set_appearance_mode('light')


artical_text = """"""

def shift():
    main.destroy()
    login.login_main()


def header():
    head_frame = ctk.CTkFrame(master=main, fg_color='#f7f7f7', corner_radius=0)
    head_frame.place()


    GetStarted_btn = ctk.CTkButton(master=head_frame, text="Get Started", corner_radius=32, fg_color="#007bff", text_color="#ffffff", hover_color="#599ee8",border_width=1, command=shift)
    GetStarted_btn.place(x=500/2, y=600/2)

def body():
    pass

def footer():
    pass

if __name__ == "__main__":
    body()
main.mainloop()