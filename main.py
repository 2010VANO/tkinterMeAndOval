import tkinter
import random
from tkinter import PhotoImage

def prepare_and_start():
    global player
    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step,
                    random.randint(1, N_Y - 1) * step)
    oval_pos = (random.randint(0, N_X - 1) * step,
                random.randint(0, N_Y - 1) * step)

    player = canvas.create_image(
        (player_pos[0], player_pos[1]),
        image=player_pic, anchor='nw')
    label.config(text="Найди выход!")
    master.bind("<KeyPress>", key_pressed)


def move_warp(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    print(xy)
    if xy[0] <= 0:
        canvas.move(obj, WIDTH, 0)
    if xy[0] >= 0:
        canvas.move(obj, -WIDTH, 0)
    if xy[1] <= 0:
        canvas.move(obj, 0, HEIGHT)
    if xy[1] >= 0:
        canvas.move(obj, 0, -HEIGHT)

def key_pressed(event):
    if event.keysym == 'Up':
        move_warp(player, 0, -step)
    if event.keysym == 'Down':
        move_warp(player, 0, step)
    if event.keysym == 'Right':
        move_warp(player, step, 0)
    if event.keysym == 'Left':
        move_warp(player, -step, 0)


master = tkinter.Tk()

step = 10
N_X = 50
N_Y = 50
WIDTH = step * N_X
HEIGHT = step * N_Y
a = False
player_pic = tkinter.PhotoImage(file="player.png")
canvas = tkinter.Canvas(master, bg='gray',
                            width=600, height=600)
canvas.create_oval(300, 300, )


player_pos = (random.randint(0, N_X - 1) * step,
                random.randint(0, N_Y - 1) * step)
oval_pos = (random.randint(0, N_X - 1) * step,
            random.randint(0, N_Y - 1) * step)

print(oval_pos)
print(player_pos)

label = tkinter.Label(master, text="Не попадись!")
restart = tkinter.Button(master, text="Начать заново", command=prepare_and_start)

restart.pack()
label.pack()
canvas.pack()
prepare_and_start()
master.bind("<KeyPress>", key_pressed)
master.mainloop()















