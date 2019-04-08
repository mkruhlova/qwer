import tkinter as tk
from idlelib import window
from tkinter import *
from tkinter import Menu


class Main (Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("MagazynPro")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
        magMenu = Menu(menubar)
        magmenu2 = Menu(magMenu, tearoff=0)
        slowMenu = Menu(menubar)
        winMenu = Menu (menubar)

        #submenu = Menu(fileMenu)

        menubar.add_cascade(label="Dokumenty", underline=0, menu=fileMenu)

        fileMenu.add_cascade(label='Dokumenty przychodowe')
        fileMenu.add_cascade(label='Dokumenty rozchodowe')
        fileMenu.add_cascade(label='Dokumenty inwentaryzacyjne')
        fileMenu.add_cascade(label='Zamkniecie miesiaca')



        menubar.add_cascade(label="Magazyny", underline=0, menu=magMenu)

        magMenu.add_cascade(label='Kartoteki magazynowe')
        magMenu.add_cascade(label='Bilans otwarcia')
        magMenu.add_cascade(label='Inwentaryzacja')
        magMenu.add_cascade(label='Dokumenty magazynowe', menu=magmenu2)

        magmenu2.add_command(label='wg dokumentow')
        magmenu2.add_command(label='wg indeksow')
        magmenu2.add_command(label='wg grup materialowych i indeksow')


        menubar.add_cascade(label="Slowniki", underline=0, menu=slowMenu)

        slowMenu.add_cascade(label='Indeksy materialowe')
        slowMenu.add_cascade(label='Kartoteka kontrahentow')
        slowMenu.add_cascade(label='Jdnostki firmy')
        slowMenu.add_cascade(label='Jednostki miary')
        slowMenu.add_cascade(label='Magazyny')
        slowMenu.add_cascade(label='Dokumenty magazynowe')



        menubar.add_cascade(label="Pomoc", underline=0, menu=winMenu)
        winMenu.add_cascade(label='O programie')
        winMenu.add_cascade(label='Instrukcja obsugi')

        fileMenu.add_separator()
        fileMenu.add_command(label="Wyjscie", underline=0, command=self.onExit)

    def onExit(self):
        self.quit()

    def login(self):
        text = Label(text='Wpisz login i Haslo: ')
        text_log = Label(text="Wpisz login")
        login = Entry()
        text_pass = Label(text="Wpisz Haslo: ")
        passw = Entry(show="*")
        button_login = Button(text="Log in")
        text.pack()
        text_log.pack()
        login.pack()
        text_pass.pack()
        passw.pack()
        button_login.pack()





def main():
    root = Tk()
    root.geometry("650x450+300+200")
    app = Main(root)
    root.mainloop()




if __name__ == '__main__':
    main()