from Tkinter import *

root = Tk()
class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
class radioButt():
    value = IntVar()
    def __init__(self,butts=["I","Cant","Set","My","Constructor","Variables"]):
        i = 0;
        for iButt in butts:
            print(iButt)
            Radiobutton(root, text=butts[i], variable=self.value, value=i).pack(anchor=W)
            i = i+1
    def get(self):
        return self.value.get()
    def set(self,setto="put in variable here"): #for dums who set radioboxes in code for some stupid reason
        return self.value.set(setto)


f=radioButt()



def callback():
    print "called the callback!"
    print(f.get());
    test.set("LELELELELELELELELE")


test=StatusBar(root);
test.set("LEL");
test.pack(side=TOP, fill=X)
test.set("Markshairdirt")


# create a menu
menu = Menu(root)
root.config(menu=menu)

autoLabel = Label(root, text="Autonomous")
autoLabel.pack()

filemenu = Menu(menu)
menu.add_cascade(label="Mark", menu=filemenu)
filemenu.add_command(label="Hair dirt", command=callback)
filemenu.add_command(label="A dumb", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Is kill", command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

toolbar = Frame(root)

b = Button(toolbar, text="new", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text="open", width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

t = Message(root, text="this is a message",anchor = W,aspect=150)
t.pack()

var = IntVar()

c = Checkbutton(root, text="Expand", variable=var)
c.pack()

v = IntVar()

Radiobutton(root, text="Two", variable=v, value=2).pack(anchor=W)


mainloop()
