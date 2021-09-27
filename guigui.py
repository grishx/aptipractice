import tkinter as tk

root = tk.Tk()
HEIGHT= 512
WIDTH = 379

def gamemode():
    frame1=tk.Canvas(root,bg="black")
    frame1.place(relwidth=1, relheight= 1)


canvas= tk.Canvas(root, height= HEIGHT , width = WIDTH, bg = "#333333")
canvas.pack()

start_frame=tk.Canvas(root,bg="black")
start_frame.place(relwidth=1, relheight= 1)

start_button = tk.Button(start_frame, text = "Start!",bg= "#55a13a" ,fg = "white", command= gamemode)
start_button.place(relx=0.5, rely=0.5, anchor="c", relheight= 0.2, relwidth= 0.4)




root.mainloop()
