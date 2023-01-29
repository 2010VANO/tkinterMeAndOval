from tkinter import *


def move_by_keys(event):
    if event.keysym == 'Up':
        canvas.move(rect, 0, -20)
    elif event.keysym == 'Down':
        canvas.move(rect, 0, 20)
    elif event.keysym == 'Left':
        canvas.move(rect, -20, 0)
    elif event.keysym == 'Right':
        canvas.move(rect, 20, 0)


win = Tk()
label = Label(win, text='Побег из игры')
label.pack()
canvas = Canvas(win, bg='#fff', width=700, height=700)
rect = canvas.create_rectangle((50, 650), (150, 550), fill='red')
oval = canvas.create_oval((330, 330), (400, 400), fill='purple')
canvas.pack()
win.bind("<KeyPress>", move_by_keys)
def rect_and_oval(d, s):
    if d == s:
        win.destroy()

rect_and_oval(rect, oval)

win.mainloop()
















