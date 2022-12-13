from tkinter import *
from cell import Cell
import settings
import funkcje as f
import time
from functools import partial



root = Tk()

root.geometry(f'{settings.WIDTH}x{settings.HEIGTH}')
root.title('sAGHper')
root.resizable(False,False)
root.configure(bg='black', cursor='pirate')

top_frame = Frame(
    root,
    bg='pink',
    width = f.percentage_width(100),
    height = f.percentage_heigth(10)

)
top_frame.place(x = 0 ,y = 0)

buttons = Frame(
    top_frame,
    bg='blue',
    width = f.percentage_width(50),
    height = f.percentage_heigth(8)

)
buttons.place(x = f.percentage_width(38) ,y = 20)

#left_frame = Frame(
  #  root,
 #   width = f.percentage_width(20),
  #  height = f.percentage_heigth(75),
  #  bg = 'black'
#)
#left_frame.place(x = 0, y=f.percentage_heigth(25))

center_frame = Frame(
    root,
    bg='blue',
    width = f.percentage_width(100),
    height = f.percentage_heigth(85)
)
center_frame.place(
    x = f.percentage_width(25),
    y = f.percentage_heigth(15)
)

komorki = []
for x in range(settings.GRID_SIZE):
    wsp_x = []
    for y in range(settings.GRID_SIZE):
        c1 = Cell(x,y)
        c1.create_button_object(center_frame)
        c1.cell_btn_object.grid(
            column=x, row=y
        )
        wsp_x.append(c1)
    komorki.append(wsp_x)

# Create a label with the text "Hello, World!"
label = Label(root, text=f"Generation: {settings.generation}", font=('Verdana', 30))

# Pack the label (i.e. show it on the screen)
label.pack(
    side=RIGHT

)
b_start = Button(buttons,
                 activebackground='green',
                 text='start game',
                 width=12,
                 height=3,
                 command=partial(f.start_game,root, komorki,label)
                 )
b_start.pack(side = LEFT)
b_stop = Button(buttons,activebackground='red',
                width=12,
                height=3,
               # padx=5,
                text='stop game',
                command=f.stop_game
                )
b_stop.pack(side= LEFT)
b_random = Button(buttons,
                  text='losuj komorki',
                  width=12,
                  height=3,
                  command=partial(f.randomize_grid, komorki))
b_random.pack()
root.mainloop()

