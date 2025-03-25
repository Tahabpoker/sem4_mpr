import FreeSimpleGUI as sg
import time

# Global variables
grid = [[0] * 9 for _ in range(9)]
speed = 0.05  # Default animation speed

# Function to create the GUI
def create_gui():
    sg.theme('LightGrey3')
    grid_layout = []

    # Create the Sudoku grid
    for box_row in range(3):
        row_layout = []
        for box_col in range(3):
            sub_grid = []
            for i in range(3):
                sub_row = []
                for j in range(3):
                    cell_key = f'cell_{box_row*3+i}_{box_col*3+j}'
                    cell = sg.Input('', size=(3, 1), font=('Arial', 16, 'bold'),
                                    justification='center', pad=(1, 1), key=cell_key,
                                    background_color='white', text_color='black', border_width=1)
                    sub_row.append(cell)
                sub_grid.append(sub_row)
            sub_frame = sg.Frame('', sub_grid, border_width=2, relief='solid', pad=(2, 2))
            row_layout.append(sub_frame)
        grid_layout.append(row_layout)

    # Add controls
    control_layout = [
        [sg.Text('Animation Speed:', font=('Arial', 12)), 
         sg.Slider(range=(0.01, 0.2), default_value=0.05, resolution=0.01, orientation='h', 
                   size=(20, 15), key='-SPEED-', enable_events=True)],
        [sg.Button('Solve', font=('Arial', 12), button_color=('white', '#4CAF50'), pad=(10, 10)),
         sg.Button('Clear', font=('Arial', 12), button_color=('white', '#f44336'), pad=(10, 10)),
         sg.Button('Load Sample', font=('Arial', 12), button_color=('white', '#2196F3'), pad=(10, 10))]
    ]

    layout = [
        [sg.Frame('Sudoku Grid', grid_layout, border_width=2, relief='groove', background_color='#d9d9d9')],
        [sg.Column(control_layout, justification='center')]
    ]

    return sg.Window('Sudoku Solver', layout, finalize=True, margins=(20, 20))

# Function to get the grid values
def get_grid(window):
    for i in range(9):
        for j in range(9):
            val = window[f'cell_{i}_{j}'].get()
            grid[i][j] = int(val) if val.isdigit() else 0

# Function to clear the grid
def clear_grid(window):
    for i in range(9):
        for j in range(9):
            window[f'cell_{i}_{j}'].update('', background_color='white')
            grid[i][j] = 0

# Function to load a sample puzzle
def load_sample(window):
    sample = [
        [1, 3, 0, 0, 5, 0, 0, 0, 9],
        [0, 0, 2, 1, 0, 0, 0, 4, 0],
        [0, 0, 0, 3, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [4, 0, 7, 0, 0, 3, 0, 6, 1],
        [0, 5, 6, 0, 0, 0, 0, 0, 2],
        [3, 0, 0, 5, 0, 4, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 3]
    ]
    clear_grid(window)
    for i in range(9):
        for j in range(9):
            if sample[i][j] != 0:
                window[f'cell_{i}_{j}'].update(str(sample[i][j]), background_color='#e6f3ff')
                grid[i][j] = sample[i][j]

# Function to find the next empty cell
def find_empty():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

# Function to check if a number is valid
def is_valid(num, row, col):
    # Check row
    if num in grid[row]:
        return False
    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False
    # Check 3x3 box
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    return True

# Function to solve the puzzle
def solve(window):
    empty = find_empty()
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(num, row, col):
            grid[row][col] = num
            window[f'cell_{row}_{col}'].update(str(num), background_color='#ccffcc')
            time.sleep(speed)
            window.refresh()

            if solve(window):
                return True

            grid[row][col] = 0
            window[f'cell_{row}_{col}'].update('', background_color='white')
            window.refresh()
            time.sleep(speed)

    return False

# Main program loop
window = create_gui()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Solve':
        get_grid(window)
        if solve(window):
            sg.popup('Sudoku Solved!', font=('Arial', 12))
        else:
            sg.popup('No Solution Exists!', font=('Arial', 12))
    elif event == 'Clear':
        clear_grid(window)
    elif event == 'Load Sample':
        load_sample(window)
    elif event == '-SPEED-':
        speed = float(values['-SPEED-'])

window.close()
