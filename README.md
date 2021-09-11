# [Codiation]('https://www.coditation.com/') - Assignment Overiew

Imagine an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two
possible states, live or dead. Every cell interacts with its eight neighbors, which are the cells that are
directly horizontally, vertically, or diagonally adjacent.
At each step in time (tick), the following transitions occur:
1. Any live cell with fewer than two live neighbors dies, as if by loneliness.
2. Any live cell with more than three live neighbors dies, as if by overcrowding.
3. Any live cell with two or three live neighbors lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbors comes to life.

The initial pattern constitutes the 'seed' (randomly placed 500 cells) of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths happen simultaneously, and the discrete moment at which this happens is called a tick. (In other words, each generation is a pure function of the one before.)

<b> Write a program in the language(s) of your choice with following guidelines:</b>
1. Accept a user input of new cells (max 100 at every step/tick) to be placed; each cell should have a
unique name which is to be accepted by the user. This input can be accepted through a CLI or
HTML element or any other form of user interface
2. Acceptance of the user input represents a tick and program is expected to calculate the state of
every cell
3. The program should output the state of the cells and changes - representation (UI/CLI et al.) of
the state of the cells can be decided by the developer
4. The program should provide a way to search by the name of the cell and show the current state of
the cell
5. The program should end on termination through appropriate OS specific signals
The program will be evaluated on the basis of the following criterion:
1. Object-oriented design. Hint: Grid, Cell et al. areclasses (python, java et al.) or struct (Golang)
2. Well-designed user interface - whether CLI or HTML/Desktop/Mobile app
3. Clear instructions and documentation on building/running the program
4. Naming convention 


## Requirements

- The program is written on Ubuntu(Linux) operating system but can be run on any device with Python 3 installed on it.
- Python Tkinter library is used to create the GUI
- install numpy
```pip install numpy```

## FAQs
- Getting error related to Tkinter not found or Tkinter module not found.
- This means that tkinter is not installed and you need to install it manually. Follow the below steps to fix it:
- [windows users]('https://stackoverflow.com/a/50027385/11211289')
- [Mac users]('https://stackoverflow.com/a/67465667/11211289')
- [Linux Users]('https://stackoverflow.com/a/27673103/11211289')

## Instructions
For MAC and Linux users:  
1. install numpy ```pip install numpy```
2. ```git clone https://github.com/tech-vin/Codiation.git ```
3. ```cd Codiation ```
4. ```python3 main.py ```


For windows users:   
1. install numpy ```pip install numpy```
2. ```git clone https://github.com/tech-vin/Codiation.git ```
3. ```cd Codiation ```
4. ```python main.py ```

