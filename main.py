from tkinter.constants import LEFT
from grid import Grid
import tkinter as tk
from tkinter import messagebox
import time


class Screen(tk.Canvas):
    def __init__(self):
        self.window_side_length = 800
        self.window_shape_length = 300
        tk.Canvas.__init__(
            self, 
            root, 
            height=self.window_side_length, 
            width=self.window_side_length
            )
        self.board = Grid()
        self.board.new_pattern('glider')
        self.ticks = 0
        self.factors_of_300 = [x for x in range(1, 151) if self.window_side_length%x == 0 and x < 151]
        self.action_state = 0 
        self.separation_length = 0
        self.moving_x = 0
        self.moving_y = 0
        self.slider = None
        self.play_pause = None
        self.patternlist = tk.StringVar()
        self.patternlist.set('clear')
        self.ticks_count = 0
        self.msg = tk.Label(root, text=None)
        self.msg.place(x=600, y=10)

        if self.action_state:
                self.tick()
                

    def todo(self, *action): 
        if self.action_state:
            self.action_state = 0
            self.play_pause.config(text='Play')
        else:
            self.action_state = 1 
            self.play_pause.config(text='Pause')

    def place_squares(self):
        self.delete('all')
        self.create_rectangle(
            0, 0, 
            self.window_side_length, 
            self.window_side_length, 
            fill='black'
            )

        if self.window_side_length % self.slider.get() != 0:  
            closest = sorted(
                self.factors_of_300, 
                key=lambda x: abs(x - self.slider.get())
                )
            self.separation_length = self.window_shape_length / closest[0]

        else:
            self.separation_length = self.window_shape_length / self.slider.get()
        m = (self.board.position2 * self.separation_length) - 15 
        x = self.moving_x
        y = self.moving_y-m
        x2 = self.separation_length+self.moving_x
        y2 = self.separation_length+self.moving_y-m
        cube_array = self.board.current_grid 
        for row in cube_array:
            for block in row:
                if block:
                    self.create_rectangle(x-m, y, x2-m, y2, fill='white')

                if not block:
                    pass
                x += self.separation_length
                x2 += self.separation_length
            x = self.moving_x
            x2 = self.separation_length+self.moving_x
            y += self.separation_length
            y2 += self.separation_length

        if self.action_state:
            self.tick()
        self.after(10, self.place_squares)

    def tick(self):
            if self.ticks != 100:
                #time.sleep(0.5)   uncomment for the delayed preview
                self.msg.config(text='')
                self.ticks += 1
                self.board.tick()
            else:
                self.action_state = 1
                self.msg.config(text='100 ticks completed!')
                
        

    def reverse_tick(self):
        self.board.tick_reverse()

    def start_over(self):
        self.ticks = 0
        self.board.start_over()

    def home(self):
        self.moving_x = 0
        self.moving_y = 0

        self.slider.set(25)

    def move(self, action):
        if action.keycode == 37:
            self.moving_x += 10
        elif action.keycode == 38:
            self.moving_y += 10
        elif action.keycode == 39:
            self.moving_x -= 10
        elif action.keycode == 40:
            self.moving_y -= 10

    def set_pattern(self):
        self.board.new_pattern(self.patternlist.get())


def main():
    canv = Screen()
    canv.grid(column=2)
    tk.Button(
        root, 
        text='<', 
        command=canv.reverse_tick).grid(column=2, row=1, sticky=tk.W)

    btn_frame = tk.Frame(root)
    btn_frame.grid(column=2, row=1)

    play_pause = tk.Button(
        btn_frame, 
        text='Play', 
        command=canv.todo
        )
    play_pause.pack(side=LEFT, expand=True)

    tk.Button(
        btn_frame, 
        text='Start Over', 
        command=canv.start_over
        ).pack(side=LEFT, expand=True)

    tk.Button(
        root, 
        text='>', 
        command=canv.tick
        ).grid(column=2, row=1, sticky=tk.E)

    frame = tk.LabelFrame(
        root, 
        text='Operations'
        )
    frame.grid(column=2)

    tk.Label(
        frame, 
        text='Zoom'
        ).grid(row=0, column=0)

    slider = tk.Scale(frame, from_=1, to=150, orient=tk.HORIZONTAL)
    slider.grid(row=0, column=1)
    slider.set(25)

    tk.Label(
        frame, 
        text='Select Pattern'
        ).grid(row=1, column=0)

    options = tk.OptionMenu(
        frame, 
        canv.patternlist, 
        'clear', 'glider', 'glider 2', 'glider gun', 'random'
        )
    options.grid(row=1, column=1)

    tk.Button(
        frame, 
        text='Go', 
        command=canv.set_pattern).grid(row=1, column=2)

    canv.play_pause = play_pause
    canv.slider = slider
    canv.place_squares()
    frame2 = tk.LabelFrame(frame)
    frame2.grid(row=2, columnspan=3, pady=20)
  
    root.bind('<Down>', canv.move)
    root.bind('<Left>', canv.move)
    root.bind('<Right>', canv.move)
    root.bind('<Up>', canv.move)
    root.bind('<space>', canv.todo)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('CODIATION')
    main()
    root.mainloop()
