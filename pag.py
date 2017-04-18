#coding:utf-8
from Tkinter import *

def calcular():
	print "VALORES"
	
	lb["text"] = "VALORES"


tela = Tk()

lb = Label(tela, text="Bem Vindo!") # Isso é um componente
lb.place(x=120, y=150) #Gerenciador é o place. ()

bt = Button(tela, width=20, text="CALCULAR", command=calcular)
bt.place(x=50, y=180)

lb = Label(tela, text="") # Isso é um componente
lb.place(x=120, y=220) #Gerenciador é o place. ()

tela.title("Calculadora")
tela.geometry("300x400+200+100") #dimensões, espaços para iniciar direita,top

#tela.wm_iconbitmap('calculadora.ico')

tela["bg"] = "purple" #background

tela.mainloop()
