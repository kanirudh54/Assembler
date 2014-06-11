import os
from gi.repository import Gtk

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

    def on_button1_clicked(self, widget):
        file1 = 'input.txt'
        os.system("python convert.py " +file1)
        os.system("python pass1.py " +file1+ "_8085")
        os.system("python pass2.py " +file1+ "_8085")

    def on_button2_clicked(self, widget):
        file1 = 'input.txt'
        link_files=[]
        string1=""
        tempname=file1+"_8085_ass_sym"
        link_files.append(tempname)
        string1=string1+" "+tempname
        os.system("python linker.py " + string1 )

    def on_button3_clicked(self, widget):
        number_of_files = 1
        link_files=[]
        string1=""
        file1 = 'input.txt'
        for x in range (0,int(number_of_files)):
            tempname=file1+"_8085_ass_sym_lin"
            tempname2=raw_input(''+str(x)+' address :')
            link_files.append(tempname)
            link_files.append(tempname2)
            string1=string1+" "+tempname + " " +tempname2
        os.system("python loader.py " + string1 )

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
