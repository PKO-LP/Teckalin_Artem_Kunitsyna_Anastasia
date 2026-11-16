import tkinter as tk
Windowes = tk.Tk()
Windowes.title ("регистрация")
Windowes.geometry("500x500")
from tkinter import messagebox
def save_to_file():
    text1 = entry1.get()
    text2 = entry2.get()

    with open("data.txt", "w", encoding="utf-8") as file:
        file.write(f"Логин: {text1}\n")
        file.write(f"Пароль: {text2}\n")

        messagebox.showinfo("Данные сохранены в файл data.txt")
tk.Label(Windowes, text="Логин: ").pack(pady=(10, 2))
entry1 = tk.Entry(Windowes, width=30)
entry1.pack()
tk.Label(Windowes, text="Пароль: ").pack(pady=(10, 2))
entry2 = tk.Entry(Windowes, width=30)
entry2.pack()

btn = tk.Button(Windowes, text="Сохранить в файл", comman=save_to_file)
btn.pack(pady=15)

Windowes.mainloop()