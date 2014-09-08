__author__ = 'Роман'

import os
from computer import computer
from computers import ComputerVector
from processors import ProcessorVector
from processor import processor
from pickle import dump, load
from tkinter import *
from tkinter import messagebox
import tkinter.ttk

Computers = ComputerVector()
Processors = ProcessorVector()
Computers_filename = "Computers.dat"
Processors_filename = "Processors.dat"

if os.path.exists(Computers_filename):
        file = open(Computers_filename, "rb")
        Computers = load(file)

if os.path.exists(Processors_filename):
        file = open(Processors_filename, "rb")
        Processors = load(file)

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=10)

        self.create_widgets()
        self.tablename = "computers"

    def create_widgets(self):
        self.Create_Computers_TreeView()
        self.button_computers = Button(self, text="Computers", relief=SUNKEN, command=self.Button_Computers_click)
        self.button_computers.grid(column=0, row=0,padx=5, pady=5, sticky="nsew")
        self.button_processors = Button(self, text="Processors", command=self.Button_Processors_click)
        self.button_processors.grid(column=0, row=1,padx=5, pady=5, sticky="nsew")
        self.button_add = Button(self, text="Add", command=self.button_add_mouse_click)
        self.button_add.grid(column=1, row=7, sticky="nsew")
        self.button_remove = Button(self,text="Remove", command=lambda: self.remove_mouse_click(self))
        self.button_remove.grid(column=2, row=7, sticky="nsew")
        self.button_edit = Button(self,text="Edit", command=self.edit_mouse_click)
        self.button_edit.grid(column=3, row=7, sticky="nsew")
        self.button_search = Button(self,text="Search", command=self.search_mouse_click)
        self.button_search.grid(column=4, row=7, sticky="nsew")
        self.button_save = Button(self,text="Save", command=self.button_save_mouse_click)
        self.button_save.grid(column=5, row=7, sticky="nsew")

    def Button_Computers_click(self):
        self.tablename = "computers"
        self.button_computers.config(relief=SUNKEN)
        self.button_processors.config(relief=RAISED)
        if self.tree:
            self.tree.destroy()
        self.Create_Computers_TreeView()

    def Button_Processors_click(self):
        self.tablename = "processors"
        self.button_computers.config(relief=RAISED)
        self.button_processors.config(relief=SUNKEN)
        if self.tree:
            self.tree.destroy()
        self.Create_Processors_TreeView()

    def check_computer_with_proc_id_exist(self, proc_number):
        for i in range(Computers.get_len()):
            if int (Computers.computers[i].ProcessorId) == int (Processors.processors[proc_number].id):
                return True
        return False

    def remove_mouse_click(self, master):
        selected_item = self.tree.selection()
        if selected_item:
            number = self.tree.index(selected_item)
            if self.tablename == "computers":
                Computers.remove(Computers.computers[number])
                self.tree.delete(selected_item)
            else:
                if not self.check_computer_with_proc_id_exist(number):
                    Processors.remove(Processors.processors[number])
                    self.tree.delete(selected_item)
                else:
                    messagebox.showwarning("Warning!","You try to remove processor which is built-in existing computer!", parent=master)

    def Create_Computers_TreeView(self):
        self.element_header=['#1','#2', '#3', '#4', '#5', '#6']
        self.tree = tkinter.ttk.Treeview(self,height=50, columns= self.element_header, show="headings")
        self.tree.heading("#1", text="Id")
        self.tree.heading("#2", text="Name")
        self.tree.heading("#3", text="Height")
        self.tree.heading("#4", text="Width")
        self.tree.heading("#5", text="Weight")
        self.tree.heading("#6", text="ProcessorId")
        self.tree.column("#1", minwidth=50, width=100)
        self.tree.column("#2", minwidth=100, width=150)
        self.tree.column("#3", minwidth=80, width=150)
        self.tree.column("#4", minwidth=80, width=150)
        self.tree.column("#5", minwidth=80, width=150)
        self.tree.column("#6", minwidth=80, width=150)
        self.vsb = Scrollbar(orient="vertical", command=self.tree.yview)
        self.hsb = Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        for i in range(Computers.get_len()):
            self.tree.insert("", i, values=(Computers.computers[i].id,Computers.computers[i].Name,
                                            Computers.computers[i].Height,Computers.computers[i].Width
            ,Computers.computers[i].Weight, Computers.computers[i].ProcessorId))

        #self.tree.columnconfigure(1,minsize=50, weight=1)
        self.tree.grid(column=1, row=0, columnspan=5, rowspan=6, sticky='nsew')
        self.vsb.grid(column=6, row=0, sticky='ns')
        #self.hsb.grid(column=1, row=7, sticky='ew')

    def Create_Processors_TreeView(self):
        self.element_header=['#1','#2', '#3']
        self.tree = tkinter.ttk.Treeview(self,height=50, columns= self.element_header, show="headings")
        self.tree.heading("#1", text="Id")
        self.tree.heading("#2", text="Name")
        self.tree.heading("#3", text="Speed")
        self.tree.column("#1", minwidth=50, width=150)
        self.tree.column("#2",minwidth=100, width=300)
        self.tree.column("#3",minwidth=100, width=300)
        self.vsb = Scrollbar(orient="vertical", command=self.tree.yview)
        self.hsb = Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        for i in range(Processors.get_len()):
            self.tree.insert("", i, values=(Processors.processors[i].id,Processors.processors[i].Name,
                                            Processors.processors[i].Speed))
        self.tree.grid(column=1, row=0, columnspan=5, rowspan=6, sticky='nsew')
        self.vsb.grid(column=6, row=0, sticky='ns')
        #self.hsb.grid(column=1, row=7, columnspan=5, sticky='ew')

    def search_mouse_click(self):
        if self.tablename == "computers":
            self.computer_search_menu()
        else:
            self.processor_search_menu()

    def computer_search_menu(self):
        self.search_comp_menu = Toplevel(self)
        self.search_comp_menu.geometry("200x200")
        #self.wait_window(self.add_menu)
        name = self.generate_entry_widget(self.search_comp_menu, "Name", 0)
        height = self.generate_entry_widget(self.search_comp_menu, "Height", 1)
        width = self.generate_entry_widget(self.search_comp_menu, "Width", 2)
        weight = self.generate_entry_widget(self.search_comp_menu, "Weight", 3)
        processorId = self.generate_entry_widget(self.search_comp_menu, "ProcessorId", 4)

        button_find = Button(self.search_comp_menu, text="Find", command=lambda: self.find_computer(self.search_comp_menu, name, height, width, weight, processorId))
        button_find.grid(column=2,row=5, padx=5, pady=5, sticky="nsew")

        self.search_comp_menu.grid()
        self.search_comp_menu.mainloop()

    def find_computer(self, master, name, height, width, weight, processorId):
        selected_item = self.tree.selection()
        self.tree.selection_remove(selected_item)
        list = self.tree.get_children()
        for curr in list:
            values=self.tree.set(curr)
            if values["#2"] == name.get() or name.get() == NONE:
                if values["#3"] == height.get() or height.get() == NONE:
                    if values["#4"] == width.get() or width.get() == NONE:
                        if values["#5"] == weight.get() or weight.get() == NONE:
                            if values["#6"] == processorId.get() or processorId.get() == NONE:
                                self.tree.selection_add(curr)
                                self.tree.see(curr)
        master.destroy()


    def find_processor(self, master, name, speed):
        selected_item = self.tree.selection()
        self.tree.selection_remove(selected_item)
        list = self.tree.get_children()
        for curr in list:
            values=self.tree.set(curr)
            if values["#2"] == name.get() or name.get() == NONE:
                if values["#3"] == speed.get() or speed.get() == NONE:
                    self.tree.selection_add(curr)
                    self.tree.see(curr)
        master.destroy()

    def processor_search_menu(self):
        self.search_proc_menu = Toplevel(self)
        self.search_proc_menu.geometry("200x100")
        #self.wait_window(self.add_menu)
        name = self.generate_entry_widget(self.search_proc_menu, "Name", 0)
        speed = self.generate_entry_widget(self.search_proc_menu, "Speed", 1)
        button_find = Button(self.search_proc_menu, text="Find", command=lambda: self.find_processor(self.search_proc_menu, name, speed))
        button_find.grid(column=2,row=5, padx=5, pady=5, sticky="nsew")
        self.search_proc_menu.grid()
        self.search_proc_menu.mainloop()

    def edit_mouse_click(self):
        if self.tablename == "computers":
            self.computer_edit_menu()
        else:
            self.processor_edit_menu()

    def processor_edit_menu(self):
        selected_item = self.tree.selection()
        if selected_item:
            number = self.tree.index(selected_item)
            self.edit_menu = Toplevel(self)
            self.edit_menu.geometry("200x100")
            name = self.generate_entry_widget(self.edit_menu, "Name", 0, Processors.processors[number].Name)
            speed = self.generate_entry_widget(self.edit_menu, "Speed", 1, Processors.processors[number].Speed)
            button_ok = Button(self.edit_menu, text="Ok", command=lambda: self.save_edit_processor(self.edit_menu, name, speed, number, selected_item))
            button_ok.grid(column=2,row=3, padx=5, pady=5, sticky="nsew")

    def save_edit_processor(self, master, name, speed, number, item):
        Processors.processors[number].Name = name.get()
        Processors.processors[number].Speed = speed.get()
        self.tree.set(item, 1, value=name.get())
        self.tree.set(item, 2, value=speed.get())
        master.destroy()

    def computer_edit_menu(self):
        selected_item = self.tree.selection()
        if selected_item:
            number = self.tree.index(selected_item)
            self.edit_menu = Toplevel(self)
            self.edit_menu.geometry("200x200")
            #self.wait_window(self.add_menu)
            name = self.generate_entry_widget(self.edit_menu, "Name", 0, Computers.computers[number].Name)
            height = self.generate_entry_widget(self.edit_menu, "Height", 1, Computers.computers[number].Height)
            width = self.generate_entry_widget(self.edit_menu, "Width", 2, Computers.computers[number].Width)
            weight = self.generate_entry_widget(self.edit_menu, "Weight", 3, Computers.computers[number].Weight)
            processorId = self.generate_entry_widget(self.edit_menu, "ProcessorId", 4, Computers.computers[number].ProcessorId)
            button_ok = Button(self.edit_menu, text="Ok", command=lambda: self.save_edit_computer(self.edit_menu, name, height, width, weight, processorId, number, selected_item))
            button_ok.grid(column=2,row=5, padx=5, pady=5, sticky="nsew")

    def save_edit_computer(self, master, name, height, width, weight, processorId, number, item):
        if self.check_processorId_exist(processorId.get()):
            Computers.computers[number].Name = name.get()
            Computers.computers[number].Height = height.get()
            Computers.computers[number].Width = width.get()
            Computers.computers[number].Weight = weight.get()
            Computers.computers[number].ProcessorId = processorId.get()
            self.tree.set(item, 1, value=name.get())
            self.tree.set(item, 2, value=height.get())
            self.tree.set(item, 3, value=width.get())
            self.tree.set(item, 4, value=weight.get())
            self.tree.set(item, 5, value=processorId.get())
            master.destroy()
        else:
            messagebox.showwarning("Warning!","Processor with such ID is missing", parent=master)

    def computer_add_menu(self):
        self.add_menu = Toplevel(self)
        self.add_menu.geometry("200x200")
        #self.wait_window(self.add_menu)
        name = self.generate_entry_widget(self.add_menu, "Name", 0)
        height = self.generate_entry_widget(self.add_menu, "Height", 1)
        width = self.generate_entry_widget(self.add_menu, "Width", 2)
        weight = self.generate_entry_widget(self.add_menu, "Weight", 3)
        processorId = self.generate_entry_widget(self.add_menu, "ProcessorId", 4)

        button_ok = Button(self.add_menu, text="Ok", command=lambda: self.save_computer(self.add_menu, name, height, width, weight, processorId))
        button_ok.grid(column=2,row=5, padx=5, pady=5, sticky="nsew")

        self.add_menu.grid()
        self.add_menu.mainloop()

    def save_processor(self, master, name, speed):
        procid = self.generate_processor_id()
        proc = processor(procid, name.get(), speed.get())
        Processors.add_processor(proc)
        self.tree.insert("", Processors.get_len()-1, values=(Processors.processors[Processors.get_len()-1].id,Processors.processors[Processors.get_len()-1].Name,
                                            Processors.processors[Processors.get_len()-1].Speed))
        master.destroy()

    def processor_add_menu(self):
        self.add_menu = Toplevel(self)
        self.add_menu.geometry("200x100")
        name = self.generate_entry_widget(self.add_menu, "Name", 0)
        speed = self.generate_entry_widget(self.add_menu, "Speed", 1)
        self.add_menu.bind_all("<Key>", self.key_enter_press)
        button_ok = Button(self.add_menu, text="Ok", command=lambda: self.save_processor(self.add_menu, name, speed))
        button_ok.grid(column=2,row=3, padx=5, pady=5, sticky="nsew")

    def button_add_mouse_click(self):
        if self.tablename == "computers":
            self.computer_add_menu()
        else:
            self.processor_add_menu()

    def generate_entry_widget(self, master, label, row, text=NONE):
        self.label = Label(master, text=label)
        self.label.grid(column=1, row=row, padx=5, pady=5, sticky="nsew")
        self.entry = Entry(master)
        self.entry.insert(0, text)
        self.entry.grid(column=2, columnspan=2, row=row, padx=5, pady=5, sticky="nsew")
        return self.entry

    def check_processorId_exist(self, id):
        for i in range(Processors.get_len()):
            if Processors.processors[i].id == int(id):
                return True
        return False

    def save_computer(self, master, name, height, width, weight, processorId):
        compid = self.generate_computer_id()
        if self.check_processorId_exist(processorId.get()):
            comp = computer(compid, name.get(), height.get(), width.get(), weight.get(), processorId.get())
            Computers.add_computer(comp)
            self.tree.insert("", Computers.get_len()-1, values=(Computers.computers[Computers.get_len()-1].id,Computers.computers[Computers.get_len()-1].Name,
                                                Computers.computers[Computers.get_len()-1].Height,Computers.computers[Computers.get_len()-1].Width
                ,Computers.computers[Computers.get_len()-1].Weight, Computers.computers[Computers.get_len()-1].ProcessorId))
            master.destroy()
        else:
            messagebox.showwarning("Warning!","Processor with such ID is missing", parent=master)


    def generate_computer_id(self):
        c_id = 0
        if Computers.computers:
            length = Computers.get_len()
            for i in range(length):
                curr = Computers.computers[i]
                if curr.id >= c_id:
                    c_id = curr.id + 1
        return c_id

    def generate_processor_id(self):
        p_id = 0
        if Processors.processors:
            length = Processors.get_len()
            for i in range(length):
                curr = Processors.processors[i]
                if curr.id >= p_id:
                    p_id = curr.id + 1
        return p_id

    def button_save_mouse_click(self):
        dump(Computers, open(Computers_filename, "wb"))
        dump(Processors, open(Processors_filename, "wb"))

root = Tk()
root.geometry("950x480")
root.wm_maxsize(950, 950)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = App(root)
root.mainloop()