from tkinter import *
import pandas as pd
from user_log import log_user
from tkinter import messagebox
from functionalitati import afisare_raspuns, random_ro, data_coloana
import json
import time

user_name = log_user()
messagebox.showinfo(message=f'Bun venit \n{user_name.capitalize()}')
BACKGROUND_COLOR = "#B1DDC6"
cuvant1 = None
cuvant2 = None
cerinta = None
scor = 0
data_check = pd.read_csv('./data/Frequency list-en-ro.csv')
COUNT = 20
timer = None
font_size = 1


# Raspuns artistic
def raspuns_artistic(count: int, valoare_bool: bool):
    global timer
    global cerinta
    global font_size
    canvas.itemconfig(inseamna, text='')
    font_art = ('Ariel', font_size, 'bold')
    if valoare_bool:
        raspuns = 'CORECT!'
    else:
        raspuns = 'INCORECT!'
    canvas.itemconfig(artistic, text=f'{raspuns}', font=font_art)
    font_size += 2
    if count > 0:
        timer = window.after(10, raspuns_artistic, count - 1, cerinta)
    elif count == 0:
        time.sleep(1)
        canvas.itemconfig(artistic, text='')
        font_size = 1
        canvas.itemconfig(inseamna, text='inseamna')
        # window.after_cancel(timer)

# Definirea butoanelor
def right_fun():
    """Functie buton corect"""

    global scor
    global cerinta
    verificare1 = data_check[data_check.en == cuvant1[0]]
    verificare2 = data_check[data_check.ro == cuvant2]
    verificare1 = ''.join(verificare1.en).lower()
    verificare2 = ''.join(verificare2.en).lower()
    if verificare1 == verificare2:
        scor += 1
        cerinta = True
        raspuns_artistic(COUNT, cerinta)

    else:
        cerinta = False
        raspuns_artistic(COUNT, cerinta)
    jocul_fata()


def wrong_fun():
    """Functie buton incorect"""
    global scor
    global cerinta
    verificare1 = data_check[data_check.en == cuvant1[0]]
    verificare2 = data_check[data_check.ro == cuvant2]
    verificare1 = ''.join(verificare1.en).lower()
    verificare2 = ''.join(verificare2.en).lower()
    if verificare1 != verificare2:
        scor += 1
        cerinta = True
        raspuns_artistic(COUNT, cerinta)
    else:
        cerinta = False
        raspuns_artistic(COUNT, cerinta)
    jocul_fata()


# Front_end, interfata
window = Tk()
window.title(string='Flasy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
photo_front = PhotoImage(file='./images/card_front.png')
photo_back = PhotoImage(file='./images/card_back.png')
photo_right = PhotoImage(file='./images/right.png')
photo_wrong = PhotoImage(file='./images/wrong.png')

canvas = Canvas(width=800, height=526, highlightthickness=0)
imaginea = canvas.create_image((400, 263), image=photo_front)
canvas.config(bg=BACKGROUND_COLOR)
primul_cuvant = canvas.create_text((400, 150), text='', font=('Ariel', 40, 'italic'))
inseamna = canvas.create_text((400, 263), text='inseamna', font=('Ariel', 20, 'italic'))
second_cuvant = canvas.create_text((400, 363), text='', font=('Ariel', 60, 'bold'))
artistic = canvas.create_text((400, 263), text='', font=('Ariel', 10, 'bold'), fill='red')
afisare_scor = canvas.create_text((100, 50), text='', fill='blue')
canvas.grid(column=0, row=0, columnspan=2)

unknwon_button = Button(image=photo_wrong, highlightthickness=0, command=wrong_fun)
unknwon_button.grid(column=0, row=1)

right_button = Button(image=photo_right, highlightthickness=0, command=right_fun)
right_button.grid(column=1, row=1)



# Rularea jocului cu functionalitati
def jocul_spate(rol=True):
    global cuvant2
    cuvant2 = random_ro(cuvant1[0], cuvant1[1])
    canvas.itemconfig(imaginea, image=photo_back)
    canvas.itemconfig(second_cuvant, text=f'{cuvant2.capitalize()}?')


def jocul_fata():
    global timer
    global scor
    global cuvant1
    cuvant1 = afisare_raspuns()
    if scor > 0:
        canvas.itemconfig(afisare_scor, text=f'User: {user_name.capitalize()}\nScor: {scor}\nIntrebari ramase: {len(data_coloana)}')
    canvas.itemconfig(inseamna, text='inseamna')
    canvas.itemconfig(imaginea, image=photo_front)
    canvas.itemconfig(primul_cuvant, text=f'{cuvant1[0].capitalize()}')
    canvas.itemconfig(second_cuvant, text=f'{cuvant1[1].capitalize()}')
    window.after(3000, jocul_spate, True)


jocul_fata()

window.mainloop()

# try:
#     file = open('./data/scor_useri.json')
#     file.close()
# except FileNotFoundError:
#
#     with open('./data/scor_useri.json', 'w') as file:
#         json.
