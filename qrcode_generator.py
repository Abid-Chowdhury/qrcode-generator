from qrcode import make
from tkinter import Tk, Label, Button, Entry

BLACK = '#242222'
window = Tk()
window.title('QR Code Generator')
window.config(background=BLACK)
window.resizable(False, False)

label_title = Label(window, text='QR Code Generator', font='Helvetica 20 bold', fg='white', bg=BLACK)
label_title.grid(row=0, column=0)

entry_url = Entry(window, width=25, font='Helvetica 15', justify='center')
entry_url.grid(row=1, column=0)

button_submit = Button(window, text='Generate', font='Helvetica 15', command=lambda: generate_qrcode(entry_url.get()))
button_submit.grid(row=2, column=0)

def generate_qrcode(url):
    img = make(url)
    img.save('qrcode.png')

window.mainloop()