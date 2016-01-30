from Tkinter import * # Import all of the >3.0 version of Tkiner's functions

root = Tk() # Create the main window

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
    def callback(self):
        print(self.get())
        #self.set(not self.get())
        #self.set(not self.get())
    def __init__(self,butts=["I","Cant","Set","My","Constructor","Variables"],row=0,col=0):
        self.value = IntVar()#5 initialize the variualbe inside the constructor as to not make it the same variable amongst all of this clas
        i = 0; #1 - mimick a c-style for loop counter
        for iButt in butts: #iterate thru the butts table
            print(str(iButt) + " a "+str(col+i)) #debug
            Radiobutton(root, text=butts[i], variable=self.value, value=i,command=self.callback).grid(row=row,column=col+i)
            #^ creates a radiobutton for screen root, with the text in the current button the for loop is on. After that, it goes onto the screen and is left/west-oriented.
            i = i+1 #1
    def get(self):
        return self.value.get() #3 - return the value of the value that the radiobutton uses
    def set(self,setto="put in variable here"): # for dums who set radioboxes in code for some stupid reason
        return self.value.set(setto) #4 same as get but sets

class label():
    def __init__(self,text="I cant set my text",row=0,col=0):
        Label(root, text=text).grid(row=row,column=col) # create a new label on screen root, with the text specified
class checkbox():
    def __init__(self,text="lel",row=0,col=0):
        self.value = IntVar()# See RadioButt - 5
        Checkbutton(root, text=text, variable=self.value).grid(row=row,column=col)
        #Create a new chekbox, on the screen root, with the text text, and the variable delcared above, an anchor to left/west. After that, put it on the screen.
    def get(self):
        return self.value.get() #See RadioButt, in get - 3
    def set(self,setto):
        return self.value.set(setto) # See RadioButt, in set - 4
class updown():
    def __init__(self,max=30,row=0,col=0):
        self.value = IntVar()# See RadioButt - 5
        Spinbox(from_=0,to=max,width=5).grid(row=row,column=col)
        #Create a new chekbox, on the screen root, with the text text, and the variable delcared above, an anchor to left/west. After that, put it on the screen.
    def get(self):
        return self.value.get() #See RadioButt, in get - 3
    def set(self,setto):
        return self.value.set(setto) # See RadioButt, in set - 4

isRed = checkbox("Is red?",0,0)

label("Autonomous",1,0)
label("Crossed",3,0)


sallyCrossed = checkbox("Sallydoors",4,0)
drawCrossed = checkbox("Drawbridge",4,1)
roughCrossed = checkbox("Rough Terrain",4,2)
stoneCrossed = checkbox("Stone Wall",4,3)
moatCrossed = checkbox("Moat",4,4)
sawCrossed = checkbox("Seasaw",4,5)
lowCrossed = checkbox("Lowbar",4,6)
rampCrossed = checkbox("Ramparts",4,7)
gateCrossed = checkbox("Gate",4,8)

label("",5,0)
pickedBall = checkbox("Picked up a ball",6,0)
startedBall = checkbox("Started with a ball",6,1)

label("",12,0)
label("Shot a ball onto...",13,0)
shotBall = radioButt(["High","Low","Didn't"],14,0)

label("",15,0)
label("Teleop",16,0)
label("Crossed",17,0)
label("Sallydoors",18,0);label("Drawbridge",18,1);label("Rought Terrain",18,2);label("Stone Wall",18,3);label("Moat",18,4);label("Seasaw",18,5);label("Lowbar",18,6);label("Ramparts",18,7);label("Gate",18,8)
teleCSally = updown(10,19,0);teleCDraw = updown(10,19,1);teleCRough=updown(10,19,2);teleCStone=updown(10,19,3);teleCMoat=updown(10,19,4);teleCSaw=updown(10,19,5)
teleCLow = updown(10,19,6);teleCRamp=updown(10,19,7);teleCGate=updown(10,19,8)
label("Balls picked up",21,0)
ballsPicked = updown(15,22,0)
label("Balls scored: Low",21,1)
lowScored = updown(15,22,1)
label("Balls scored: High",21,2)
highScored = updown(15,22,2)
label("Strategy",26,0)
strategy = radioButt(["Spy", "Defense", "Attack", "Defense" "Destroyer", "Multipurpose", "Other"],26,1)
gaveBall = checkbox("Gave a ball to a teammate",27,0)
recBall = checkbox("Got a ball from a teammate",27,1)



gotStuck = checkbox("Got stuck",31,0)
label("",32,0)
label("General",33,0)
label("Durability(1=Paperweight",34,0); label("5 = solid)",34,1)
durability = radioButt(["1","2","3","4","5"],35,0)



def callback():
    print "called the callback!"
    print(f.get());
    test.set("LELELELELELELELELE")



# create a menu - like the thing at the top of the screen with the apple logo, not inside the window
menu = Menu(root)
root.config(menu=menu)
'''

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Reset Current Fields", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Reset ALL data", command=callback)

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

'''
mainloop()
