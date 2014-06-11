import os
import subprocess
from gi.repository import Gtk
global name
#File Chooser
class FileChooserWindow(Gtk.Window):

    def __init__(self,parent):
        Gtk.Window.__init__(self, title="FileChooser Example")
        box1 = Gtk.Box(spacing=6)
        self.add(box1)

        button5 = Gtk.Button("Choose File")
        button5.connect("clicked", self.on_file_clicked)
        box1.add(button5)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        dialog.set_select_multiple(self)
        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            #print("File selected: " + dialog.get_filenames())
            test= (dialog.get_filenames())
            print test
            global name
            name =[] 
            for i in test:
                sda = i.split('/')
                name.append(sda[len(sda)-1])
            print name
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

############################
class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Assembler")
        self.set_size_request(200, 100)
        self.set_border_width(30)
        self.box = Gtk.Box(spacing=20)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Assemble")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Link")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)
        
        self.button3 = Gtk.Button(label="Load")
        self.button3.connect("clicked", self.on_button3_clicked)
        self.box.pack_start(self.button3, True, True, 0)

        self.button4 = Gtk.Button(label="Add file")
        self.button4.connect("clicked", self.on_button4_clicked)
        self.box.pack_start(self.button4, True, True, 0)


    def on_button1_clicked(self, widget):
        file1 = name[len(name)-1]
        os.system("python convert.py " +file1)
        os.system("python pass1.py " +file1+ "_8085")
        os.system("python pass2.py " +file1+ "_8085")

    def on_button2_clicked(self, widget):
        link_files=[]
        string1=""
        for x in name:
            tempname=x
            link_files.append(tempname)
            string1=string1+" "+tempname
        print string1
        os.system("python linker.py " + string1 )

    def on_button3_clicked(self, widget):
        link_files=[]
        string1=""
        for x in name:
            tempname=x
            tempname2=raw_input(''+str(x)+' address :')
            link_files.append(tempname)
            link_files.append(tempname2)
            string1=string1+" "+tempname + " " +tempname2
        os.system("python loader.py " + string1 )

    def on_button4_clicked(self, widget):
        win1 = FileChooserWindow(self)
        win1.show_all()        
       


win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
