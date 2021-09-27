import tkinter


class ButtonEntry():
    def __init__(self, root):
        self.entry_var=""

        startLabel =tkinter.Label(root,text="Enter Star: ")
        self.startEntry=tkinter.Entry(root)

        startLabel.pack()
        self.startEntry.pack()
        self.startEntry.focus_set()

        plotButton= tkinter.Button(root,text="plot",
                           command=self.hi).pack()

    def hi(self):
        self.entry_var=self.startEntry.get()
        print("inside class", self.entry_var)

if __name__ == "__main__":
    root=tkinter.Tk()
    BE=ButtonEntry(root)
    root.mainloop()

    print("\nBack in __main__")
    print(BE.entry_var)
