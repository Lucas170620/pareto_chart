from tkinter.filedialog import askopenfilename
from back.pareto import show_pareto_graphic
from tkinter import *
from tkinter.messagebox import showerror
import tkinter.colorchooser
from tkinter import messagebox
class GUI:
    def __init__(self):
        self.filename =None
        self.color_bar = None
        self.color_line = None
        self.root = Tk()
        self.root.title("Pareto")
        p1 = PhotoImage(file='../pareto/front/icons/pareto.png')
        self.root.iconphoto(False, p1)
        self.root.geometry("500x250")
        self.root.resizable(height = None, width = None)
        self.root.configure(background='black')
        self.widget1 = Frame()
        self.widget1.pack()
        self.crie_seu_pareto = Label(self.widget1, text="CRIE SUA PARETO",font=("Arial",25), fg='#FF4500',bg='black')
        self.crie_seu_pareto.pack()
        self.widget2 = Frame(background='black')
        self.widget2.pack()
        self.widget2.columnconfigure(1, weight=1)
        self.widget2.rowconfigure(1, weight=1)
        self.bar_text = Label(self.widget2, text="Escolha a cor da barra", font=("Arial", 20), fg='#FF4500', bg='black')
        self.bar_text.grid(row=0,column=0)
        self.bar_sub = Button(self.widget2,width=20,height=1,text="SELECIONAR",command=self.getColor_bar)
        self.bar_sub.grid(row=0, column=1)
        self.line_text = Label(self.widget2, text="Escolha a cor da linha", font=("Arial", 20), fg='#FF4500',
                                bg='black')
        self.line_text.grid(row=1, column=0)
        self.line_sub = Button(self.widget2, width=20, height=1,text="SELECIONAR",command=self.getColor_line)
        self.line_sub.grid(row=1, column=1)
        self.search_file_text = Label(self.widget2, text="Escolha o arquivo Xml", font=("Arial", 20), fg='#FF4500',
                                bg='black')
        self.search_file_text.grid(row=2,column=0)
        self.search_file_button = Button(self.widget2,command=self.search, width=20, height=1,text="Procurar")
        self.search_file_button.grid(row=2, column=1)
        self.submit = Button(self.widget2,command=self.sub, width=20, height=1,text="CRIAR")
        self.close = Button(self.widget2, command=self.root.destroy, width=20, height=1, text="FECHA")
        self.show_info = Button(self.widget2, command=self.show_info, width=20, height=1, text="Mostrar Exemplo de Arquivo .XML")

        self.show_info.grid(row=3, column=0, columnspan=2, sticky=W+E)
        self.submit.grid(row=4, column=0,columnspan=2,sticky=W+E)
        self.close.grid(row=5, column=0,columnspan=2,sticky=W+E)

        self.root.mainloop()
    def show_info(self):
        messagebox.showinfo("Exemple", '''
        <?xml version="1.0" encoding = "ISO-8859-1"?>
            <data>
                <cd>
                    <name>exemplo</name>
                    <number>20</number>
                </cd>
                <cd>
                    <name>exemplo2</name>
                    <number>30</number>
                </cd>
                <cd>
                    <name>exemplo3</name>
                    <number>60</number>
                </cd>
            </data>
        ''')
    def sub(self):
        if self.color_bar == None or self.color_line ==None:
            Tk().withdraw()
            showerror("color error","not exist this color")
        elif self.filename == None:
            Tk().withdraw()
            showerror("File Error", "please submit xml file")
        else:
            show_pareto_graphic(self.filename,self.color_bar,self.color_line)

    def search(self):
        filename = askopenfilename()
        if filename[len(filename) - 4:len(filename)] == '.xml':
            self.filename = filename
        else:
            self.filename = None
            Tk().withdraw()
            showerror(title='File Error', message="That file isn't .xml")
    def getColor_bar(self):
        self.color_bar = tkinter.colorchooser.askcolor()[1]
    def getColor_line(self):
        self.color_line = tkinter.colorchooser.askcolor()[1]