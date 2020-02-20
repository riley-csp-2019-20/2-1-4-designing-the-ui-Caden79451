import tkinter as tk

root = tk.Tk()
root.wm_geometry("200x200")
root.grid()

Blue = tk.Canvas(height = 100, width = 100, background= "Blue")
Blue.grid(row= 0, column= 0)

Green = tk.Canvas(height = 100, width=100, background= "Green")
Green.grid(row= 0,column= 1)

Red = tk.Canvas(height = 100, width=100, background= "Red")
Red.grid(row= 1,column= 0)

Yellow = tk.Canvas(height = 100, width=100, background= "Yellow")
Yellow.grid(row= 1,column= 1)
root.mainloop()