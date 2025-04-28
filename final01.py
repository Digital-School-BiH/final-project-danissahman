import tkinter as tk
from tkinter import messagebox, simpledialog
import requests
import pyjokes
import threading
from translate import Translator




root = tk.Tk()
root.title("projekt")
root.geometry("500x500")
root.config(bg="#1e1e1e")

main_frame = tk.Frame(root, bg="#1e1e1e")
main_frame.pack(fill="both", expand=True)

screens = {}

def show_screen(screen_key):
    for scr in screens.values():
        scr.pack_forget()
    screens[screen_key].pack(fill="both", expand=True)


odgovori = {
    1: "Pariz",
    2: "7",
    3: "Vilijam Šekspir",
    4: "56",
    5: "H2O",
    6: "Sunce"
}


def create_main_menu():
    main_menu = tk.Frame(main_frame, bg="#1e1e1e")
    
    tk.Label(main_menu, text="Dobrodošao u Danisov projekat", fg="white", bg="#1e1e1e", font=("Helvetica", 16)).pack(pady=20)
    tk.Label(main_menu, text="Izaberi pitanje:", fg="white", bg="#1e1e1e", font=("Helvetica", 14)).pack(pady=10)

    for i in range(1, 7):
        btn = tk.Button(main_menu, text=f"Pitanje {i}", font=("Helvetica", 14), width=25,
                        command=lambda i=i: show_screen(f"pitanje_{i}"))
        btn.pack(pady=5)

    

    screens["main_menu"] = main_menu


def create_question_screen(q_number, question_text):
    frame = tk.Frame(main_frame, bg="#1e1e1e")
    
    tk.Label(frame, text=f"Pitanje {q_number}", fg="white", bg="#1e1e1e", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(frame, text=question_text, fg="white", bg="#1e1e1e", font=("Helvetica", 12), wraplength=400).pack(pady=10)

    entry = tk.Entry(frame, font=("Helvetica", 12), width=40)
    entry.pack(pady=10)

    def finish_question():
        odgovor = entry.get().strip().lower()
        tacan_odgovor = odgovori[q_number].strip().lower()

        if odgovor == tacan_odgovor:
            messagebox.showinfo("Tačno!", "Bravo! Odgovor je tačan.")
        else:
            messagebox.showinfo("Netačno", f"Nije tačno. Tačan odgovor je: {odgovori[q_number]}")
        
        show_screen("main_menu")

    tk.Button(frame, text="Završi", font=("Helvetica", 12), command=finish_question).pack(pady=20)

    screens[f"pitanje_{q_number}"] = frame


pitanja = {
    1: "Koji je glavni grad Francuske?",
    2: "Koliko kontinenata ima svet?",
    3: "Ko je napisao 'Romeo i Julija'?",
    4: "Koliko je 7 * 8?",
    5: "Koji je hemijski simbol za vodu?",
    6: "Kako se zove najbliža zvezda Zemlji?"
}

create_main_menu()
for i in range(1, 7):
    create_question_screen(i, pitanja[i])

show_screen("main_menu")
root.mainloop()

