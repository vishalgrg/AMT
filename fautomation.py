from Tkinter import *
import tkFileDialog
import sys
import os
import tkMessageBox
import ttk


#owner:----VISHAL GARG--------

MACHINE_ = "machine:"
BATCH_FILE_PATH_ = "command:"
USES = "IDLE is Python's Tkinter-based Integrated DeveLopment+'\n'+Environment IDLE emphasizes a lightweight,clean design+'\n'+with a simple user interface.Although it is suitable for beginners, even advanced users will find that"


class Fautomation:
    def __init__(self,root):
        path = ""
        machinename = ""
        batchpath = ""

        self.flag=False

        self.makeMenu(root)
        
        label_0 = Label(root, text="Autosys Job Migration",width=20,font=("bold", 20))
        label_0.place(x=150,y=53)
        
        self.pathselectBtn = Button(root, text="Select JIL File Path",width=20,font=("bold", 10),
                               command=lambda: self.openDir(root))
        self.pathselectBtn.place(x=80,y=130)
        self.pathLabel = Label(root)
        self.pathLabel.place(x=260,y=130)

        self.machinelabel = Label(root, text="Enter new machine name ",width=20,font=("bold", 10))
        self.machinelabel.place(x=80,y=180)
        self.entry_machine = Entry(root)
        self.entry_machine.place(x=240,y=180)
        
        self.batchPathlabel = Label(root, text="Enter new new batch path",width=20,font=("bold", 10))
        self.batchPathlabel.place(x=80,y=230)
        self.entry_batchPath = Entry(root)
        self.entry_batchPath.place(x=245,y=230)
        self.startMigBtn = Button(root,text = "Start Migration", width =20,font=("bold", 10),bg='brown',fg='white',
                               command=lambda: self.updateMachine())
        self.startMigBtn.place(x=180,y=380)
        ttk.Separator(root).place(x=0, y=430, relwidth=1)
        self.versionLabel = Label(root,text="v 1.1.0",width=20,font=("bold", 8))
        self.versionLabel.place(x=500,y=432)

    def openDir(self,root):
        try:
            root.directory = tkFileDialog.askdirectory()
            self.pathLabel.config(text=root.directory)
            self.path = root.directory
            self.flag=True
            print (root.directory)

        except Exception as e:
                print("error %s" % str(e))

    def updateMachine(self):
         try:
             nM = self.entry_machine.get()
             print "-----------aasddfff------"+nM
             if nM == '':
                 self.showDialog("Field can not be empty")
                 return
             if not self.path:
                self.showDialog("Please select JIL files path")
                return
                 
             print nM
             for root, dirs, files in os.walk(self.path):
                 for file in files:
                     print file
                     if file.endswith(".txt"):
                         
                         fileN = os.path.join(root,file)
                         with open(fileN) as nfile:
                             for line in nfile:
                                 if MACHINE_ in line:
                                     self.inplace_change(fileN,line,MACHINE_+nM+'\n')
                           
         except Exception as e:
                print("error %s" % str(e))
         pass

    def updateBatchpath(self):
        pass
        
    def showDialog(self,msg):
        tkMessageBox.showinfo("Alert", msg)

        
    def inplace_change(self,filename, old_string, new_string):
    # Safely read the input filename using 'with'
        with open(filename) as f:
            s = f.read()
            if old_string not in s:
                print('"{old_string}" not found in {filename}.'.format(**locals()))
                return

    # Safely write the changed content, if found in the file
        with open(filename, 'w') as f:
            print('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
            s = s.replace(old_string, new_string)
            f.write(s)
            
    def menuListner(self):
        childwin = Toplevel(root,bg = '#585858')
        childwin.geometry('600x600')
        childwin.title("About AMT v1.1.0")
        labelHead = Label(childwin,text = "AMT Tool version 1.1.0",font=("Helvetica", 15),fg = 'white',bg = '#585858')
        labelHead.place(x=20,y=10)
        
        labelDesc = Label(childwin,text = "Autosys Migration Tool version 1.1.0",font=("Times", 10),fg = 'white',bg = '#585858')
        labelDesc.place(x=20,y=40)
        labeluses = Label(childwin,text = USES,font=("Times", 10),fg = 'white',bg = '#585858')
        labeluses.place(x=20,y=60)

        
        #button = Button(childwin, text="Do nothing button")
        #button.pack()
        
    def makeMenu(self,root):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New")
        #filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index",command = self.menuListner)
        helpmenu.add_command(label="About...",command = self.menuListner)
        menubar.add_cascade(label="Help", menu=helpmenu)

        root.config(menu=menubar)

    


        

root = Tk()
root.geometry('600x450')
root.title("Autosys Job Migration Tool v 1.1.0")
f= Fautomation(root)
root.mainloop()
