from tkinter import*
from tkinter.ttk import*
from time import strftime


tela=Tk()


tela.title("Relogio")

def Horas():
    HorasEscritas=strftime('%H:%M:%S %b  %p')
    Relogio.config(text=HorasEscritas)
    Relogio.after(1000,Horas)



Relogio=Label(tela,font=("Arial",120), background="Green"  , foreground="blue") 
Relogio.pack(anchor='center')

Horas()

mainloop()
