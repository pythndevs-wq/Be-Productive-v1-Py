import customtkinter as ctk
import tkinter as tk
import todo


def main_dash():
    dash_root = ctk.CTk()
    dash_root.geometry("1000x700")
    dash_root._set_appearance_mode("light")

    dash_root.mainloop()

if __name__ == "__main__":
    main_dash()