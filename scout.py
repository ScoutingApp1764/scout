#!/usr/bin/python
from Tkinter import * # Import all of the >3.0 version of Tkiner's functions
import sqlite3 as sq


#We use the serial number as the file name so that no 2 computer's file names are alike
#########################################################
import objc
from Foundation import NSBundle

IOKit_bundle = NSBundle.bundleWithIdentifier_('com.apple.framework.IOKit')

functions = [("IOServiceGetMatchingService", b"II@"),
                     ("IOServiceMatching", b"@*"),
                                  ("IORegistryEntryCreateCFProperty", b"@I@@I"),
                                              ]

objc.loadBundleFunctions(IOKit_bundle, globals(), functions)

def io_key(keyname):
    return IORegistryEntryCreateCFProperty(IOServiceGetMatchingService(0, IOServiceMatching("IOPlatformExpertDevice")), keyname, None, 0)
def get_hardware_serial():
    return io_key("IOPlatformSerialNumber")
######################################################### SRC: https://gist.github.com/pudquick/c7dd1262bd81a32663f0
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
    def __init__(self,butts=["I","Cant","Set","My","Constructor","Variables"],row=0,col=0):
        print("\"radio\";")
        self.value = IntVar()#5 initialize the variualbe inside the constructor as to not make it the same variable amongst all of this clas
        i = 0; #1 - mimick a c-style for loop counter
        for iButt in butts: #iterate thru the butts table
            #print(str(iButt) + " a "+str(col+i)) #debug
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
        print("\"check\";")
        self.value = IntVar()# See RadioButt - 5
        Checkbutton(root, text=text, variable=self.value).grid(row=row,column=col)
        #Create a new chekbox, on the screen root, with the text text, and the variable delcared above, an anchor to left/west. After that, put it on the screen.
    def get(self):
        return self.value.get() #See RadioButt, in get - 3
    def set(self,setto):
        return self.value.set(setto) # See RadioButt, in set - 4
class updown():
    def callback(self):
        print(self.get())
    def __init__(self,max=30,row=0,col=0):
        print("\"updown\";")
        self.value = StringVar()# See RadioButt - 5
        Spinbox(from_=0,to=max,width=5,command=self.callback,textvariable=self.value).grid(row=row,column=col)
        #Create a new chekbox, on the screen root, with the text text, and the variable delcared above, an anchor to left/west. After that, put it on the screen.
    def get(self):
        return int(self.value.get()) #See RadioButt, in get - 3
    def set(self,setto):
        return self.value.set(str(setto)) # See RadioButt, in set - 4

label("Round Number:",0,0);roundNum=updown(100000,0,1)
label("Team Number:",1,0);teamNum = updown(100000,1,1)
posi = radioButt(["Red 1","Red 2","Red 3","Blue 1","Blue 2","Blue 3"],0,2)

label("!!!AUTONOMOUS!!!",3,0)
label("Crossed",4,0)


sallyCrossed = checkbox("Sallydoors",5,0)
drawCrossed = checkbox("Drawbridge",5,1)
roughCrossed = checkbox("Rough Terrain",5,2)
stoneCrossed = checkbox("Stone Wall",5,3)
moatCrossed = checkbox("Moat",5,4)
sawCrossed = checkbox("Seasaw",5,5)
lowCrossed = checkbox("Lowbar",5,6)
rampCrossed = checkbox("Ramparts",5,7)
gateCrossed = checkbox("Gate",5,8)

label("",5,0)
pickedBall = checkbox("Picked up a ball",6,0)
startedBall = checkbox("Started with a ball",6,1)

label("",12,0)
label("Shot a ball onto...",13,0)
shotBall = radioButt(["High","Low","Didn't"],14,0)

label("",15,0)
label("!!!TELEOP!!!",16,0)
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
gotStuck = checkbox("Got stuck",28,0)





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
#mainloop()
#;       ;;;;;   ;
#;       ;   ;   ;
#;       ;   ;   ;
#;       ;   ;   ;
#;       ;   ;   ;
#;;;;;   ;;;;;   ;;;;

letable = [
    ["roundNum",roundNum],["teamNum",teamNum],["posi",posi],["sallyScrossed",sallyCrossed],["drawCrossed",drawCrossed],["roughCrossed",roughCrossed],["stoneCrossed",stoneCrossed],["moatCrossed",moatCrossed],["sawCrossed",sawCrossed],["lowCrossed",lowCrossed],["rampCrossed",rampCrossed],["gateCrossed",gateCrossed],["pickedBall",pickedBall],["startedBall",startedBall],["shotBall",shotBall],["teleCSally",teleCSally],["teleCRough",teleCRough],["teleCStone",teleCStone],["teleCMoat",teleCMoat],["teleCSaw",teleCSaw],["teleCLow",teleCLow],["teleCRamp",teleCRamp],["teleCGate",teleCGate],["ballsPicked",ballsPicked],["lowScored",lowScored],["highScored",highScored],["strategy",strategy],["gaveBall",gaveBall],["recBall",recBall],["gotStuck",gotStuck]
]
class _database():
    def __init__(self):
        self.s = sq.connect("THEDATABASE_"+get_hardware_serial()) #This will make a unique file for every computer that makes a database
        self.m = self.s.cursor()

        strTable = ""
        for _list in letable:
            strTable = strTable+_list[0]+" INT,"
        print(strTable[0:-1])
        #self.m.executescript("CREATE TABLE Data("+strTable[0:-1]+");")
    def t1(self):
        self.m.execute("SELECT SQLITE_VERSION()")
        print(self.m.fetchone())
    def t2(self):
        #`self.m.execute("INSERT INTO data VALUES(2)")
        self.m.execute("SELECT * FROM data")
        print(self.m.fetchone())
        print("^^^")
    def setLeVars(self):
        strTable = ""
        for _list in letable:
            strTable = strTable + str(_list[1].get()) + ","
        self.m.execute("INSERT INTO Data VALUES("+strTable[0:-1]+")")
        print("~~STRTable"+strTable)
    def commit(self):
        self.s.commit()
    def fin(self):
        self.s.commit()
        self.s.close()


data = _database()


def buttcallback():
    print "click!"
    data.setLeVars()
    data.commit()
    for _tab in letable:
        _tab[1].set(0)
        print("reset "+_tab[0])


butt = Button(root, text="Submit", command=buttcallback)
butt.grid(row=30,column=0)



mainloop()
#data.setLeVars()
#data.t2()
print("VVV")
print(get_hardware_serial())
print(roundNum.get())
data.fin()
