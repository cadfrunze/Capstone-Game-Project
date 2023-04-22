from tkinter import *
from user_log import log_user
from tkinter import messagebox
import sys
user_name = log_user()
messagebox.showinfo(message=f'Bun venit \n{user_name.capitalize()}')
window = Tk()
window.title(string='Flasy')
window.config(height=600, width=600)






window.mainloop()
