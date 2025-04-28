import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import random
import requests
import pyjokes
import threading

root = tk.Tk()
root.title("Devine Asistant")
root.geometry("500x500")
root.config(bg = "#1e1e1e")


main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill="both", expand=True)
screens = {}
#prebacivanje ekrana
def show_screen(name):
    for scr in screens.values():
        scr.pack_forget()
    screens[name].pack(fill="both", expand=True)

#main menu

def create_main_menu():
    main_menu = tk.Frame(main_frame, bg="#1e1e1e")

    tk.Label(main_menu, text="Izaberi pitanje:", fg="white", bg="#1e1e1e"


    for 1 in range(1, 7):
        btn = tk.Button(main_menu, text="Pitanje {i}", width=20, command=lambda i=1: show_screen("Pitanje_{1}"))
        btn.pack(pady=5)
    screens["main_menu"] = main_menu

    
def create_question_screen(q_number, question_text)