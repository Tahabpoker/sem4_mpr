from tkinter import *

root = Tk()
root.title("Sudoku Solver")
root.geometry("324x550")

label = Label(root, text = "fill in teh number and click slove ").grid(row=0, column=1,columnspan=10)

errLabel = Label(root, text="",fg="red")
errLabel.grid(row=15,column=1,columnspan=10,pady=5)
solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row = 15,column=1,columnspan=10,pady=5)

cells = {}

def validateNumber(p):
    out = ( p.isdigit() or p=="" ) and len(p)<2
    return out

reg = root.register(validateNumber)


def draw3x3(row,column,bgclo):
    for i in range(3):
        for j in range(3):
            e = Entry(root,width=5, bg=bgclo,justify="center",validate="key",validatecommand=(reg,"%p"))
            e.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells[(row+i+1, column+j+1)] = e 

def draw9x9Grid():
    color1, color2 = "#B0B0B0", "#ffffff"
    for row in range(1, 10, 3):
        for col in range(0, 9, 3):
            draw3x3(row, col, color1)
            color1, color2 = color2, color1

         
         
def clearValue():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell = cells[(row,col)]
            cell.delete(0,"end")

def getValues():
    board = []
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cells[(row,col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)


Button(root, command=getValues, text="Solve", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=10, relief=RAISED, bd=3).grid(row=20, column=1, columnspan=5, pady=20)
Button(root, command=clearValue, text="Clear", font=("Arial", 12, "bold"), bg="#F44336", fg="white", width=10, relief=RAISED, bd=3).grid(row=20, column=5, columnspan=5, pady=20)

draw9x9Grid()
root.mainloop()