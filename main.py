from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os
import foldermanager
import readpdf


foldermanager.Create_dirfile()


def select_destination():

    destination_dir = filedialog.askdirectory(title = 'Selecione local de destino')

    if destination_dir:

        foldermanager.Define_diretory(destination_dir)

def Runfile(folder):

    pdfs = os.listdir(folder)

    for i in pdfs:

        file = f'{folder}/{i}'
        print(file)

        if not os.path.isdir(file) and readpdf.Ispdf(file):

            pdf_data = readpdf.extractContent(file)
            costumer_data = readpdf.FilterCostumerData(pdf_data)
            
            foldermanager.MoveFile(file, costumer_data)

def Select_nfe_dir():

    destination = foldermanager.Destination()

    if destination == '':

        messagebox.showwarning('Atenção','O destino das NFs ainda não foi definido')

    else:
        folder_dir = filedialog.askdirectory(title = 'Selecione a pasta com NFs')

        if folder_dir:

            Runfile(folder = folder_dir)

root = Tk()
frame = ttk.Frame(root, padding= 100)
frame.grid()

ttk.Label(frame, text="Selecione pasta com notas fiscais: ").grid(column= 0, row= 0)
ttk.Button(frame, text="Selecionar", command = Select_nfe_dir).grid(column= 1, row = 0)

ttk.Label(frame, text="Selecione o destino das NFs: ").grid(column= 0, row= 1)
ttk.Button(frame, text="Selecionar", command = select_destination).grid(column= 1, row = 1)

root.mainloop()