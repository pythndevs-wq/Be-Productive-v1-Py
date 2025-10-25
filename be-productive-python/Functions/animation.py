import customtkinter as ctk
import tkinter as tk

# you can change this 
global my_y, my_x


def slide_animate(from_x, from_y, to_x, to_y):
    global my_y, my_x

    my_y = 600/2 + from_y
    my_x = 500/2 + from_x
    