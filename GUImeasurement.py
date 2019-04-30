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

#==================== Função que fecha a janela da GUI ======================
def iExit():
    root.destroy()
    return

#========= Função que limpa as variáveis de níveis de entrada e saída =======
    
# ARRUMAR ISSO AQUI URGENTEMENTE!!!!

def clearvars():
    varInMin_1.set("0")
    varInMax_1.set("0")
    varInMin_2.set("0")
    varInMax_2.set("0")
    varInMin_3.set("0")
    varInMax_3.set("0")
    varInMin_4.set("0")
    varInMax_4.set("0")
    varOutMin.set("0")
    varOutMax.set("0")

#=================== Condicionando sinais de entrada ========================
def inChannels():
    inputs=[var1.get(), var2.get(), var3.get(), var4.get()]
    return inputs



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
var1=tk.BooleanVar()
var2=tk.BooleanVar()
var3=tk.BooleanVar()
var4=tk.BooleanVar()
var5=tk.IntVar()
var6=tk.IntVar()
var7=tk.IntVar()
var8=tk.IntVar()
var9=tk.IntVar()
var10=tk.IntVar()
var11=tk.IntVar()
var12=tk.IntVar()
var13=tk.IntVar()
varInMin_1 = tk.StringVar()
varInMax_1 = tk.StringVar()
varInMin_2 = tk.StringVar()
varInMax_2 = tk.StringVar()
varInMin_3 = tk.StringVar()
varInMax_3 = tk.StringVar()
varInMin_4 = tk.StringVar()
varInMax_4 = tk.StringVar()
varOutMin = tk.StringVar() 
varOutMax = tk.StringVar()


#%% Setando variáveis
varInMin_1.set("-10")
varInMin_1.set("0")
varInMax_1.set("0")
varInMin_2.set("0")
varInMax_2.set("0")
varInMin_3.set("0")
varInMax_3.set("0")
varInMin_4.set("0")
varInMax_4.set("0")
varOutMin.set("0")
varOutMax.set("0")




#%% Canais de entrada
# Frame pai - Inf
lblInput = tk.Label(Inf, font=('arial', 15, 'italic'), bg='black', fg='white',
                 text="Input channels", bd = 4, width=23).grid(row=0, column=0)

In1 = tk.Checkbutton(Inf, text="1 - Binaural E", variable=var1, onvalue=True, offvalue=False,
                    font=('arial', 20, 'bold')). grid(row=1, sticky=tk.W)
In2 = tk.Checkbutton(Inf, text="2 - Binaural D", variable=var2,  onvalue=True, offvalue=False,
                    font=('arial', 20, 'bold')). grid(row=2, sticky=tk.W)
In3 = tk.Checkbutton(Inf, text="3 - Mic. 1", variable=var3, onvalue=True, offvalue=False,
                    font=('arial', 20, 'bold')). grid(row=3, sticky=tk.W)
In4 = tk.Checkbutton(Inf, text="4 - Mic. 2", variable=var4, onvalue=True, offvalue=False,
                    font=('arial', 20, 'bold')). grid(row=4, sticky=tk.W)




#%% Canais de saída
# Frame Pai - Outf
lblOutput = tk.Label(Outf, font=('arial', 15, 'italic'), bg='black', fg='white',
                 text="Output channels", bd = 4, width=23).grid(row=0, column=0)

Out1 = tk.Checkbutton(Outf, text="1 - OmniSource 1", variable=var5, onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command = AtivaDodec1).grid(row=1, sticky=tk.W)
Out2 = tk.Checkbutton(Outf, text="2 - OmniSource 2", variable=var6,  onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command = AtivaDodec2).grid(row=2, sticky=tk.W)
Out3 = tk.Checkbutton(Outf, text="3 - P.A", variable=var7, onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command = AtivaPA).grid(row=3, sticky=tk.W)



#%% Sinais de excitação
# Frame pai - Sigsf
lblOutput = tk.Label(Sigsf, font=('arial', 15, 'italic'), bg='black', fg='white',
                 text="Excitation signal", bd = 4, width=23).grid(row=0, column=0)

Signal1 = tk.Checkbutton(Sigsf, text="Exponential Sweep", variable=var8, onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command=AtivaSweep). grid(row=1, sticky=tk.W)
Signal2 = tk.Checkbutton(Sigsf, text="Speech", variable=var9, onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command=AtivaFala). grid(row=3, sticky=tk.W)
Signal3 = tk.Checkbutton(Sigsf, text="Music", variable=var10,  onvalue=1, offvalue=0, \
                    font=('arial', 20, 'bold'), command=AtivaMusica). grid(row=2, sticky=tk.W)



#%% Templates da medição
# Frame Pai Tempf
lblTemplate = tk.Label(Tempf, font=('arial', 15, 'italic'), bg='black', fg='white',
                 text="Measurement type", bd = 4, width=23).grid(row=0, column=0)


Template1 = tk.Checkbutton(Tempf, text="Calibration", font=('arial', 20, 'bold'), variable = var11, \
                        onvalue=1, offvalue=0, command = AtivaCalibracao). grid(row=1, sticky=tk.W)
Template2 = tk.Checkbutton(Tempf, text="Noise floor", font=('arial', 20, 'bold'), variable = var12, \
                        onvalue=1, offvalue=0, command = AtivaRuidoDeFundo). grid(row=2, sticky=tk.W)
Template3 = tk.Checkbutton(Tempf, text="Room response", font=('arial', 20, 'bold'), variable = var13, \
                        onvalue=1, offvalue=0, command = AtivaRoomResponse). grid(row=3, sticky=tk.W)


#%% Menu da medição
# Frame Pai Menuf

# =========================   Botões fundamentais   ===========================
Run  =     tk.Button(Menuf, text="    Run     ", font=('arial', 20, 'bold'), bg='green').place(x=1000, y=30)
Checkout = tk.Button(Menuf, text="Checkout", font=('arial', 20, 'bold'), bg='purple').place(x=1000, y=130)
Save =     tk.Button(Menuf, text="    Save    ", font=('arial', 20, 'bold'), bg='blue').place(x=1000, y=220)
Exit =     tk.Button(Menuf, text="     Exit     ", font=('arial', 20, 'bold'), bg='red', command=iExit).place(x=1000, y=320)

# ================   Checagem de níveis de entradas e saídas   ================

# Canais de entrada
lblInCh = tk.Label(Menuf, font=('arial', 17, 'bold'), text="Input Channels").place(x=55,y=30)
lblInCh_min = tk.Label(Menuf, font=('arial', 14, 'italic'), text="Min. (dB)").place(x=45,y=70)
lblInCh_max = tk.Label(Menuf, font=('arial', 14, 'italic'), text="Max. (dB)").place(x=145,y=70)
lblInCh_1 = tk.Label(Menuf, font=('arial', 17, 'bold'), text="1").place(x=10,y=110)
lblInCh_2 = tk.Label(Menuf, font=('arial', 17, 'bold'), text="2").place(x=10,y=150)
lblInCh_3 = tk.Label(Menuf, font=('arial', 17, 'bold'), text="3").place(x=10,y=190)
lblInCh_4 = tk.Label(Menuf, font=('arial', 17, 'bold'), text="4").place(x=10,y=230)
InMin_1 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varInMin_1, state=tk.DISABLED).place(x=50,y=110)
InMax_1 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varInMax_1, state=tk.DISABLED).place(x=150,y=110)
InMin_2 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varInMin_2, state=tk.DISABLED).place(x=50,y=150)
InMax_2 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varInMax_2, state=tk.DISABLED).place(x=150,y=150)
InMin_3 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varInMin_3, state=tk.DISABLED).place(x=50,y=190)
InMax_3 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varInMax_3, state=tk.DISABLED).place(x=150,y=190)
InMin_4 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varInMin_4, state=tk.DISABLED).place(x=50,y=230)
InMax_4 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varInMax_4, state=tk.DISABLED).place(x=150,y=230)

#Canais de saída
lblOutCh= tk.Label(Menuf, font=('arial', 17, 'bold'), text="Output Channels").place(x=350,y=30)
lblOutCh_min = tk.Label(Menuf, font=('arial', 14, 'italic'), text="Min. (dB)").place(x=355,y=70)
lblOutCh_max = tk.Label(Menuf, font=('arial', 14, 'italic'), text="Max. (dB)").place(x=455,y=70)
OutMin_1 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varOutMin, state=tk.DISABLED).place(x=360,y=110)
OutMax_1 = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varOutMin, state=tk.DISABLED).place(x=460,y=110)

#Botão de Limpar as variáveis de níveis
Clear =     tk.Button(Menuf, text="     Clear     ", font=('arial', 17, 'bold'), bg='white', command=clearvars).place(x=225, y=300)










#print(inChannels())
#Sedex10 = main(inChannels(), outChannels(),...)

root.mainloop()