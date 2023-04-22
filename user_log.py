import sys
from tkinter import *
from tkinter import messagebox

user = ''


def log_user():
    global user
    screen = Tk()
    screen.title('Innregistrare')
    screen.config(pady=20, padx=20)
    canvas = Canvas()
    canvas.config(height=200, width=200)
    canvas.grid(rowspan=5)

    mesaj_text = Label(text='Innregistrare user:')
    mesaj_text.grid(row=1, column=0)
    mesaj_box = Entry(width=20)
    mesaj_box.grid(row=2, column=0)

    def but_inn():
        global user
        char_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a',
                     's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v',
                     'b', 'n', 'm']
        if len(mesaj_box.get()) <= 2:
            messagebox.showerror(title='Eroare!', message='Continutul trebuie sa aibe mai mult de 2 caractere')
        else:
            user_proba = ''
            for char in mesaj_box.get().lower():
                if char in char_list:
                    user_proba += char
                    if len(user_proba) >= 2:
                        user = mesaj_box.get()
                        try:
                            screen.destroy()
                        except TclError:
                            pass
                        break
                elif char == mesaj_box.get().lower()[-1] and char not in char_list:
                    messagebox.showerror(title='Eroare!', message='Username-ul trebuie sa contina cel putin 2 litere')
                    break

    but_innregistrare = Button(text='Innregistrare', width=20, command=but_inn)
    but_innregistrare.grid(row=3, column=0, rowspan=1)
    screen.mainloop()
    if len(user) < 2:
        sys.exit()
    else:
        try:
            screen.destroy()
        except TclError:
            pass
        return user
