#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import tkinter
from tkinter import *
from tkinter import filedialog
import os
import datetime
import crop
from tkinter import messagebox

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Scan to Crop')
        self.minsize(300,200)
        self.createWidgets()

    def createWidgets(self):
        self.grid()
        tPrefixe = Label(self, text='Prefix')
        tPrefixe.grid(row=0, column=0)
        
        entryText = StringVar()
        entryText.set('Scrop_')        
        Prefixe = Entry(self, textvariable=entryText)
        Prefixe.grid(row=0, column=1)

        quitButton = Button(self, text = "Exit", 
                                 command = self.quit)
        quitButton.grid(row=1, column=0)
        submitButton = Button(self, text = "Scan & Crop", 
                                 command = lambda: self.submitCrop(Prefixe.get()))
        submitButton.grid(row=1, column=1)
        return()

    def submitCrop(self,Prefix):
        Directory = tkinter.filedialog.askdirectory( initialdir='~/Images/',  title='Backup Directory')
        self.WindowCleaning()
        while True:
            DestinationFile = Directory + '/' + Prefix + datetime.datetime.now().strftime("%y%m%d%H%M%S") + '.jpg'
            self.waitMessage()
            # OsCommand = 'hp-scan --device=\'escl:http://192.168.1.13:8080\' --mode=\'color\' --file=\'' + DestinationFile + '\''
            # OsCommand = 'hp-scan --device=\'hpaio:/net/envy_5640_series?ip=192.168.1.13&queue=false\' --mode=\'color\' --file=\'' + DestinationFile + '\''
            OsCommand = 'hp-scan --device=\'airscan:e0:HP ENVY 5640 series [E2C1E6]\' --mode=\'color\' --file=\'' + DestinationFile + '\''
            returnCode = os.popen(OsCommand).read()
            if not os.path.exists(DestinationFile) or not returnCode:
                messagebox.showerror(title=None,message='Scan error')
                exit()
            ReturnCode = crop.crop(DestinationFile)
            Next = messagebox.askyesno(title='Stop-Again', message='Another One ?')
            if not Next:
                exit()
        exit()
    
    def waitMessage(self):
        root = Tk()
        root.withdraw()
        timeout=30000
        try:
            root.after(timeout, root.destroy)
            messagebox.showinfo('Scanning...', 'Please wait', master=root)
        except:
            pass

    def WindowCleaning(self):
        #---------- cleaning window
        for Widget in self.winfo_children():
            Widget.destroy()
        return()

app = Application()
app.mainloop()