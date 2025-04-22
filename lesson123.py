import tkinter as tk
root = tk.Tk()
root.title("Пример Tkinter")
root.geometry("400x300")
label = tk.Label(root, text="Привет мир!", font=("Arial", 20))
label.pack(pady=50)

def cahnge_text():
    label.config(text = "Вы нажали кнопку!")
new_button = tk.Button(root, text="Нажми на меня", command=cahnge_text
command = cahnge_text_again)
new_button.pack()

def change_text_again():
    label.config(text = "Trolololo")
button = tk.Button(root, text="Нажми на меня", command=change_text)
button.pack()
button2 = tk.Button(root, text="Закрыть", command=root.quit)
button2.pack()
root.mainloop()