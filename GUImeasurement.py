# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:51:58 2019

@author: leona
"""

import tkinter as tk
#import main
#import measureClass

root = tk.Tk()
root.geometry("1200x700+0+0")
root.title("Measure Class")
root.configure(background = 'black')

#%% Frames primarios

#   Frame com nome style da medição (Name frame - Namef)
Namef = tk.Frame(root, width=1200, height=50, bd=5, relief='raise')
Namef.place(x=0, y=0)

#   Frame de entradas (In frame- Inf)
Inf = tk.Frame(root, width=300, height=230, bd=8, relief='raise')
Inf.place(x=0,y=50)

#   Frame de saídas (Out frame- Outf)
Outf = tk.Frame(root, width=300, height=230, bd=8, relief='raise')
Outf.place(x=300,y=50)

#   Frame de sinais de excitação (Signals frame - Sigsf)
Sigsf = tk.Frame(root, width=300, height=230, bd=8, relief='raise')
Sigsf.place(x=600,y=50)

#   Frame de Templates de medição (Template frame - Tempf)
Tempf = tk.Frame(root, width=300, height=230, bd=8, relief='raise')
Tempf.place(x=900,y=50)

#   Frame de menu (Menu frame - Menuf)
Menuf = tk.Frame(root, width=1200, height=420, bd=8, relief='raise')
Menuf.place(x=0,y=280)


#%% Nome da medição
# Frame pai - Namef
lblNmae = tk.Label(Namef, font=('arial', 25, 'italic'), bg='black', fg='green',
                text="Keep Calm and Measure With Class", bd = 4, width=62).grid(row=0, column=0)


#%% SETUP DA MEDIÇÃO

#%%ARRUMAR ISSO
#========= Condicionando sinais de entrada ==============   RESOLVER ISSO
def SignalsIn():
    channelStatus=[var1.get(), var2.get(), var3.get(), var4.get()]
    for i in range(len(channelStatus)):
        if channelStatus[i]==1:
            channelStatus[i]=True
        else:
             channelStatus[i]=False
    return channelStatus


#%%
#========= Condicionando Checkbutton dos Sinais =========
def AtivaDodec1():
    if var5.get()==1:
        print("Dodecaedro 1 ligado")
        if var6.get()==1:
            var6.set(0)
            Out2.deselect()
            print("Dodecaedro 2 desligado")
        if var7.get()==1:
            var7.set(0)
            Out3.deselect()
            print("P.A desligado")
            
def AtivaDodec2():
    if var6.get()==1:
        print("Dodecaedro 2 ligado")
        if var5.get()==1:
            var5.set(0)
            Out1.deselect()
            print("Dodecaedro 1 desligado")
        if var7.get()==1:
            var7.set(0)
            Out3.deselect()
            print("P.A desligado")
            
def AtivaPA():
    if var7.get()==1:
        print("P.A ligado")
        if var5.get()==1:
            var5.set(0)
            Out1.deselect()
            print("Dodecaedro 1 desligado")
        if var6.get()==1:
            var6.set(0)
            Out2.deselect()
            print("Dodecaedro 2 desligado")

#========= Condicionando Checkbutton dos Sinais =========
def AtivaSweep():
    if var8.get()==1:
        print("Sinal de fala seleciondo")
        if var9.get()==1:
            var9.set(0)
            Signal2.deselect()
            print("Ruído de desativada")
        if var10.get()==1:
            var10.set(0)
            Signal3.deselect()
            print("Room Response desativada")
            
def AtivaFala():
    if var9.get()==1:
        print("Ruído de fundo ativada")
        if var8.get()==1:
            var8.set(0)
            Signal1.deselect()
            print("Calibração desativada")
        if var10.get()==1:
            var10.set(0)
            Signal3.deselect()
            print("Room response desativada")
            
def AtivaMusica():
    if var10.get()==1:
        print("Room response ativada")
        if var8.get()==1:
            var8.set(0)
            Signal1.deselect()
            print("Calibração desativada")
        if var9.get()==1:
            var9.set(0)
            Signal2.deselect()
            print("Ruído de fundo desativada")


#========= Condicionando Checkbutton dos templates =========
def AtivaCalibracao():
#    var5.set(0);    Out1.deselect()
#    var6.set(0);    Out2.deselect()
#    var7.set(0);    Out3.deselect()
#    var8.set(0);    Signal1.deselect()
#    var9.set(0);    Signal2.deselect()
#    var10.set(0);   Signal3.deselect()
    if var11.get()==1:
        print("Calibração ativada")
        if var12.get()==1:
            var12.set(0)
            Template2.deselect()
            print("Ruído de desativada")
        if var13.get()==1:
            var13.set(0)
            Template3.deselect()
        print("Room Response desativada")
     
def AtivaRuidoDeFundo():
#    var5.set(0);    Out1.deselect()
#    var6.set(0);    Out2.deselect()
#    var7.set(0);    Out3.deselect()
#    var8.set(0);    Signal1.deselect()
#    var9.set(0);    Signal2.deselect()
#    var10.set(0);   Signal3.deselect()
    if var12.get()==1:
        print("Ruído de fundo ativada")
        if var11.get()==1:
            var11.set(0)
            Template1.deselect()
            print("Calibração desativada")
        if var13.get()==1:
            var13.set(0)
            Template3.deselect()
            print("Room response desativada")

def AtivaRoomResponse():
    if var13.get()==1:
        print("Room response ativada")
        if var11.get()==1:
            var11.set(0)
            Template1.deselect()
            print("Calibração desativada")
        if var12.get()==1:
            var12.set(0)
            Template2.deselect()
            print("Ruído de fundo desativada")
def MSG():
    print(var1.get(), var2.get(), var3.get(), var4.get())



#%% Declarando variáveis
var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
var4=tk.IntVar()
var5=tk.IntVar()
var6=tk.IntVar()
var7=tk.IntVar()
var8=tk.IntVar()
var9=tk.IntVar()
var10=tk.IntVar()
var11=tk.IntVar()
var12=tk.IntVar()
var13=tk.IntVar()


#%% Canais de entrada
# Frame pai - Inf
lblInput = tk.Label(Inf, font=('arial', 15, 'italic'), bg='black', fg='white',
                 text="Canais de entrada", bd = 4, width=23).grid(row=0, column=0)

#In1 = Checkbutton(Inf, text="1 - Binaural E", variable=channelStatus[0], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=1, column=0)
#In2 = Checkbutton(Inf, text="2 - Binaural D", variable=channelStatus[1], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=2, column=0)
#In3 = Checkbutton(Inf, text="3 - Mic. 1", variable=channelStatus[2], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=3, column=0)
#In4 = Checkbutton(Inf, text="4 - Mic. 2", variable=channelStatus[3], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=4, column=0)

In1 = tk.Checkbutton(Inf, text="1 - Binaural E", variable=var1, onvalue=1, offvalue=0,
                    font=('arial', 20, 'bold'), command = SignalsIn). grid(row=1, sticky=tk.W)
In2 = tk.Checkbutton(Inf, text="2 - Binaural D", variable=var2,  onvalue=1, offvalue=0,
                    font=('arial', 20, 'bold'), command = SignalsIn). grid(row=2, sticky=tk.W)
In3 = tk.Checkbutton(Inf, text="3 - Mic. 1", variable=var3, onvalue=1, offvalue=0,
                    font=('arial', 20, 'bold'), command = SignalsIn). grid(row=3, sticky=tk.W)
In4 = tk.Checkbutton(Inf, text="4 - Mic. 2", variable=var4, onvalue=1, offvalue=0,
                    font=('arial', 20, 'bold'), command = SignalsIn). grid(row=4, sticky=tk.W)




#%% Canais de saída
# Frame Pai - Outf
lblOutput = tk.Label(Outf, font=('arial', 15, 'italic'), bg='black', fg='white',
                 text="Canais de saída", bd = 4, width=23).grid(row=0, column=0)

#Out1 = Checkbutton(Outf, text="1- Dodecaedro 1", variable=channelStatus[0], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=1, column=0)
#Out2 = Checkbutton(Outf, text="2 - Dodecaedro 2", variable=channelStatus[1], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=2, column=0)
#Out3 = Checkbutton(Outf, text="3 - P.A", variable=channelStatus[2], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=3, column=0)

Out1 = tk.Checkbutton(Outf, text="1- Dodecaedro 1", variable=var5, onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command = AtivaDodec1).grid(row=1, sticky=tk.W)
Out2 = tk.Checkbutton(Outf, text="2 - Dodecaedro 2", variable=var6,  onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command = AtivaDodec2).grid(row=2, sticky=tk.W)
Out3 = tk.Checkbutton(Outf, text="3 - P.A", variable=var7, onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command = AtivaPA).grid(row=3, sticky=tk.W)



#%% Sinais de excitação
# Frame pai - Sigsf
lblOutput = tk.Label(Sigsf, font=('arial', 15, 'italic'), bg='black', fg='white',
                 text="Sinal de excitação", bd = 4, width=23).grid(row=0, column=0)

#Signal1 = Checkbutton(Sigsf, text="Sweep exponencial", variable=channelStatus[0], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=1, column=0)
#Signal2 = Checkbutton(Sigsf, text="Música", variable=channelStatus[1], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=2, column=0)
#Signal3 = Checkbutton(Sigsf, text="Fala", variable=channelStatus[2], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=3, column=0)

Signal1 = tk.Checkbutton(Sigsf, text="Sweep exponencial", variable=var8, onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command=AtivaSweep). grid(row=1, sticky=tk.W)
Signal2 = tk.Checkbutton(Sigsf, text="Fala", variable=var9, onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command=AtivaFala). grid(row=3, sticky=tk.W)
Signal3 = tk.Checkbutton(Sigsf, text="Música", variable=var10,  onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command=AtivaMusica). grid(row=2, sticky=tk.W)



#%% Templates da medição
# Frame Pai Tempf
lblTemplate = tk.Label(Tempf, font=('arial', 15, 'italic'), bg='black', fg='white',
                 text="Measurement type", bd = 4, width=23).grid(row=0, column=0)

#Signal1 = Checkbutton(Sigsf, text="Sweep exponencial", variable=channelStatus[0], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=1, column=0)
#Signal2 = Checkbutton(Sigsf, text="Música", variable=channelStatus[1], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=2, column=0)
#Signal3 = Checkbutton(Sigsf, text="Fala", variable=channelStatus[2], onvalue=True, offvalue=False,
#                    font=('arial', 10, 'bold')). grid(row=3, column=0)

Template1 = tk.Checkbutton(Tempf, text="Calibração", font=('arial', 20, 'bold'), variable = var11, \
                        onvalue=1, offvalue=0, command = AtivaCalibracao). grid(row=1, sticky=tk.W)
Template2 = tk.Checkbutton(Tempf, text="Ruído de fundo", font=('arial', 20, 'bold'), variable = var12, \
                        onvalue=1, offvalue=0, command = AtivaRuidoDeFundo). grid(row=2, sticky=tk.W)
Template3 = tk.Checkbutton(Tempf, text="Room response", font=('arial', 20, 'bold'), variable = var13, \
                        onvalue=1, offvalue=0, command = AtivaRoomResponse). grid(row=3, sticky=tk.W)






root.mainloop()