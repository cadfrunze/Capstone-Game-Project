from tkinter import *
from user_log import log_user
from tkinter import messagebox
from functionalitati import alegere
import sys

# user_name = log_user()
# messagebox.showinfo(message=f'Bun venit \n{user_name.capitalize()}')
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title(string='Flasy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

photo_front = PhotoImage(file='./images/card_front.png')
photo_back = PhotoImage(file='./images/card_back.png')
photo_right = PhotoImage(file='./images/right.png')
photo_wrong = PhotoImage(file='./images/wrong.png')

canvas_front = Canvas(width=800, height=526, highlightthickness=0)
canvas_front.create_image((400, 263), image=photo_front)
canvas_front.config(bg=BACKGROUND_COLOR)
canvas_front.create_text((400, 150), text='Title', font=('Ariel', 40, 'italic'))
canvas_front.create_text((400, 263), text='inseamna', font=('Ariel', 40, 'italic'))
canvas_front.create_text((400, 363), text='word', font=('Ariel', 60, 'bold'))
canvas_front.grid(column=0, row=0, columnspan=2)

unknwon_button = Button(image=photo_wrong, highlightthickness=0)
unknwon_button.grid(column=0, row=1)

right_button = Button(image=photo_right, highlightthickness=0)
right_button.grid(column=1, row=1,)






window.mainloop()
