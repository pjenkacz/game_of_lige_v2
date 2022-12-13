from tkinter import Button
class Cell:
    def __init__(self,x,y, is_mine = False):
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.state = 'dead'
        self.bg = 'red'

    def create_button_object(self, location):
        btn = Button(
            location,
           # text = 'OOO',
            width=2,
            height=1,
            bg = 'red',
           # text = f"{self.x},{self.y}"
        )
        self.cell_btn_object = btn
        btn.bind("<Button-1>", func = self.left_click_action)
        btn.bind("<Button-3>", func = self.right_click_action)
        btn.bind("<Button-3>", func=self.right_click_action)

    def left_click_action(self, event):
        print(self.x, self.y)
        self.state = "alive"
        print(self.state)
        self.cell_btn_object.configure(bg= 'green', fg='white')

    def right_click_action(self,event):
        print('i am right')
        self.state = "dead"
        print(self.state)
        self.cell_btn_object.configure(bg='red', fg='white')
    def print_values(self):
        print(self.x, self.y, self.state)

    def update_button(self):
        if self.state == 'dead':
            self.cell_btn_object.configure(bg = 'red')
        elif self.state == 'alive':
            self.cell_btn_object.configure(bg = 'green')


