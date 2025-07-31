import tkinter as tk
root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")

for row in range(3):
    for col in range(3):
        btn1 = tk.Button(root, text="0")
        btn1.grid(row=0, column=0)
        
        btn2 = tk.Button(root, text="1")
        btn2.grid(row=0, column=1)

        btn3 = tk.Button(root, text="2")
        btn3.grid(row=0, column = 2)

        btn4 = tk.Button(root, text="=")
        btn4.grid(row=1, column=0)
root.mainloop()