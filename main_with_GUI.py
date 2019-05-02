#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:42:38 2019

@author: mtslazarin
"""

#%% Importando bibliotecas
import tkinter as tk

#%% Classe da janela de tomadas da medição
class takeWindow(object):
    
    def __init__(self,root):
        self.root = root
        # Frames primarios        
        #   Frame com nome style da medição (Name frame - Namef)
        self.nameF = tk.Frame(root, width=1200, height=50, bd=5, relief='raise')
        self.nameF.place(x=0, y=0)
        self.lblName = tk.Label(self.nameF, font=('arial', 25, 'italic'), bg='black', fg='green',
                        text="Keep Calm and Measure With Class", bd = 4, width=62).grid(row=0, column=0)
        
        #   Frame de seleção dos canais de entrada (In frame- Inf)
        self.inF = tk.Frame(root, width=300, height=230, bd=8, relief='raise')
        self.inF.place(x=0,y=50)
        self.lblInput = tk.Label(self.inF, font=('arial', 15, 'italic'), bg='black', fg='white',
                         text="Input channels", bd = 4, width=23).grid(row=0, column=0)
        self.var1=tk.BooleanVar()
        self.in1 = tk.Checkbutton(self.inF, text="1 - Binaural E", variable=self.var1, onvalue=True, offvalue=False,
                            font=('arial', 20, 'bold')). grid(row=1, sticky=tk.W)
        self.var2=tk.BooleanVar()
        self.in2 = tk.Checkbutton(self.inF, text="2 - Binaural D", variable=self.var2,  onvalue=True, offvalue=False,
                            font=('arial', 20, 'bold')). grid(row=2, sticky=tk.W)
        self.var3=tk.BooleanVar()
        self.in3 = tk.Checkbutton(self.inF, text="3 - Mic. 1", variable=self.var3, onvalue=True, offvalue=False,
                            font=('arial', 20, 'bold')). grid(row=3, sticky=tk.W)
        self.var4=tk.BooleanVar()
        self.in4 = tk.Checkbutton(self.inF, text="4 - Mic. 2", variable=self.var4, onvalue=True, offvalue=False,
                            font=('arial', 20, 'bold')). grid(row=4, sticky=tk.W)
        
        #   Frame de seleção da fonte (Out frame- Outf)
        self.outF = tk.Frame(root, width=300, height=230, bd=8, relief='raise')
        self.outF.place(x=300,y=50)
        self.lblOutput = tk.Label(self.outF, font=('arial', 15, 'italic'), bg='black', fg='white',
                         text="Output channels", bd = 4, width=23).grid(row=0, column=0)
        self.var5=tk.BooleanVar()
        self.out1 = tk.Checkbutton(self.outF, text="1 - OmniSource 1", variable=self.var5, onvalue=True, offvalue=False, \
                            font=('arial', 20, 'bold'), command = self.AtivaDodec1).grid(row=1, sticky=tk.W)
        self.var6=tk.BooleanVar()
        self.out2 = tk.Checkbutton(self.outF, text="2 - OmniSource 2", variable=self.var6,  onvalue=True, offvalue=False, \
                            font=('arial', 20, 'bold'), command = self.AtivaDodec2).grid(row=2, sticky=tk.W)
        self.var7=tk.BooleanVar()
        self.out3 = tk.Checkbutton(self.outF, text="3 - P.A", variable=self.var7, onvalue=True, offvalue=False, \
                            font=('arial', 20, 'bold'), command = self.AtivaPA).grid(row=3, sticky=tk.W)
        
        #   Frame de seleção do sinal de excitação (Signals frame - Sigsf)
        self.sigsF = tk.Frame(root, width=300, height=230, bd=8, relief='raise')
        self.sigsF.place(x=600,y=50)
        self.lblOutput = tk.Label(self.sigsF, font=('arial', 15, 'italic'), bg='black', fg='white',
                         text="Excitation signal", bd = 4, width=23).grid(row=0, column=0)
        self.var8=tk.BooleanVar()
        self.signal1 = tk.Checkbutton(self.sigsF, text="Exponential Sweep", variable=self.var8, onvalue=True, offvalue=False, \
                            font=('arial', 20, 'bold'), command=self.AtivaSweep). grid(row=1, sticky=tk.W)
        self.var9=tk.BooleanVar()
        self.signal2 = tk.Checkbutton(self.sigsF, text="Speech", variable=self.var9, onvalue=True, offvalue=False, \
                            font=('arial', 20, 'bold'), command=self.AtivaFala). grid(row=3, sticky=tk.W)
        self.var10=tk.BooleanVar()
        self.signal3 = tk.Checkbutton(self.sigsF, text="Music", variable=self.var10,  onvalue=True, offvalue=False, \
                            font=('arial', 20, 'bold'), command=self.AtivaMusica). grid(row=2, sticky=tk.W)
        
        #   Frame de seleção do tipo (template) de tomada da medição (Template frame - Tempf)
        self.tempF = tk.Frame(root, width=300, height=230, bd=8, relief='raise')
        self.tempF.place(x=900,y=50)
        self.lblTemplate = tk.Label(self.tempF, font=('arial', 15, 'italic'), bg='black', fg='white',
                         text="Measurement type", bd = 4, width=23).grid(row=0, column=0)
        self.var11=tk.IntVar()
        self.template1 = tk.Checkbutton(self.tempF, text="Calibration", font=('arial', 20, 'bold'), variable = self.var11, \
                                onvalue=True, offvalue=False, command = self.AtivaCalibracao). grid(row=1, sticky=tk.W)
        self.var12=tk.IntVar()
        self.template2 = tk.Checkbutton(self.tempF, text="Noise floor", font=('arial', 20, 'bold'), variable = self.var12, \
                                onvalue=True, offvalue=False, command = self.AtivaRuidoDeFundo). grid(row=2, sticky=tk.W)
        self.var13=tk.IntVar()
        self.template3 = tk.Checkbutton(self.tempF, text="Room response", font=('arial', 20, 'bold'), variable = self.var13, \
                                onvalue=True, offvalue=False, command = self.AtivaRoomResponse). grid(row=3, sticky=tk.W)
        
        #   Frame de menu (Menu frame - Menuf)
        self.menuF = tk.Frame(root, width=1200, height=420, bd=8, relief='raise')
        self.menuF.place(x=0,y=280)
        # =========================   Botões fundamentais   ===========================
        self.takeRun  = tk.Button(self.menuF, text="Take Run", font=('arial', 20, 'bold'), bg='green').place(x=1000, y=10)
        self.takeCheck = tk.Button(self.menuF, text="Take Check", font=('arial', 20, 'bold'), bg='green').place(x=1000, y=60)
        self.takeSave = tk.Button(self.menuF, text="Take Save", font=('arial', 20, 'bold'), bg='green').place(x=1000, y=110)
        self.medStatus = tk.Button(self.menuF, text="Med Status", font=('arial', 20, 'bold'), bg='red').place(x=1000, y=160)
        self.medSave = tk.Button(self.menuF, text="Med Save", font=('arial', 20, 'bold'), bg='red').place(x=1000, y=210)
        self.medLoad = tk.Button(self.menuF, text="Med Load", font=('arial', 20, 'bold'), bg='red').place(x=1000, y=260)
        # ================   Checagem de níveis de entradas e saídas   ================        
        # Canais de entrada
        self.lblInCh = tk.Label(self.menuF, font=('arial', 17, 'bold'), text="Input Channels").place(x=55,y=30)
        self.lblInCh_min = tk.Label(self.menuF, font=('arial', 14, 'italic'), text="Min. (dB)").place(x=45,y=70)
        self.lblInCh_max = tk.Label(self.menuF, font=('arial', 14, 'italic'), text="Max. (dB)").place(x=145,y=70)
        self.lblInCh_1 = tk.Label(self.menuF, font=('arial', 17, 'bold'), text="1").place(x=10,y=110)
        self.lblInCh_2 = tk.Label(self.menuF, font=('arial', 17, 'bold'), text="2").place(x=10,y=150)
        self.lblInCh_3 = tk.Label(self.menuF, font=('arial', 17, 'bold'), text="3").place(x=10,y=190)
        self.lblInCh_4 = tk.Label(self.menuF, font=('arial', 17, 'bold'), text="4").place(x=10,y=230)
        self.varInMin_1 = tk.StringVar()
        self.varInMin_1.set("0")
        self.InMin_1 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varInMin_1, state=tk.DISABLED).place(x=50,y=110)
        self.varInMax_1 = tk.StringVar()
        self.varInMax_1.set("0")
        self.InMax_1 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varInMax_1, state=tk.DISABLED).place(x=150,y=110)
        self.varInMin_2 = tk.StringVar()
        self.varInMin_2.set("0")
        self.InMin_2 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varInMin_2, state=tk.DISABLED).place(x=50,y=150)
        self.varInMax_2 = tk.StringVar()
        self.varInMax_2.set("0")
        self.InMax_2 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varInMax_2, state=tk.DISABLED).place(x=150,y=150)
        self.varInMin_3 = tk.StringVar()
        self.varInMin_3.set("0")
        self.InMin_3 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varInMin_3, state=tk.DISABLED).place(x=50,y=190)
        self.varInMax_3 = tk.StringVar()
        self.varInMax_3.set("0")
        self.InMax_3 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varInMax_3, state=tk.DISABLED).place(x=150,y=190)
        self.varInMin_4 = tk.StringVar()
        self.varInMin_4.set("0")
        self.InMin_4 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varInMin_4, state=tk.DISABLED).place(x=50,y=230)
        self.varInMax_4 = tk.StringVar()
        self.varInMax_4.set("0")
        self.InMax_4 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varInMax_4, state=tk.DISABLED).place(x=150,y=230)
        
        #Canais de saída
        self.lblOutCh= tk.Label(self.menuF, font=('arial', 17, 'bold'), text="Output Channels").place(x=290,y=30)
        self.lblOutCh_min = tk.Label(self.menuF, font=('arial', 14, 'italic'), text="Min. (dB)").place(x=295,y=70)
        self.lblOutCh_max = tk.Label(self.menuF, font=('arial', 14, 'italic'), text="Max. (dB)").place(x=395,y=70)
        self.varOutMin = tk.StringVar()
        self.OutMin_1 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varOutMin, state=tk.DISABLED).place(x=300,y=110)
        self.varOutMin.set("0")
        self.varOutMax = tk.StringVar()
        self.varOutMax.set("0")
        self.OutMax_1 = tk.Entry(self.menuF, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=self.varOutMin, state=tk.DISABLED).place(x=400,y=110)
        
        #Botão de Limpar as variáveis de níveis
        self.clear =     tk.Button(self.menuF, text="     Clear     ", font=('arial', 17, 'bold'), bg='white', command=self.clearvars).place(x=175, y=300)
        
        #Nova medição
        self.var14=tk.BooleanVar()
        self.newmeasurement = tk.Checkbutton(self.menuF, text=" New Measurment", font=('arial', 20, 'bold'), variable = self.var14, \
                                onvalue=True, offvalue=False, command = self.AtivaCalibracao).place(x=550, y=30)
#        if newmeasurement:
#            newmeasurement_name = tk.Entry(Menuf, font=('arial', 17, 'bold'), bd=1, width=5, textvariable=varOutMin, state=tk.DISABLED).place(x=400,y=110)

    def iExit(self):
        self.root.destroy()
        return

    #========= Função que limpa as variáveis de níveis de entrada e saída =======
    def clearvars(self):
        self.varInMin_1.set("0")
        self.varInMax_1.set("0")
        self.varInMin_2.set("0")
        self.varInMax_2.set("0")
        self.varInMin_3.set("0")
        self.varInMax_3.set("0")
        self.varInMin_4.set("0")
        self.varInMax_4.set("0")
        self.varOutMin.set("0")
        self.varOutMax.set("0")
    
    #=================== Condicionando sinais de entrada ========================
    def GetChannelStatus(self):
        channelStatus = [self.var1.get(), self.var2.get(), self.var3.get(), self.var4.get()]
        return channelStatus
    
    #===================== Condicionando Fonte selecionada ======================
    def GetSource(self):
        if self.var5.get():
            source = 'S1'
        if self.var6.get():
            source = 'S2'
        if self.var7.get():
            source = 'S3'
        return source
    
    #==================== Condicionando sinais de saída =========================
    def GetExcitation(self):
        if self.var8.get():
            excitation = 'varredura'
        if self.var9.get():
            excitation = 'fala'
        if self.var10.get():
            excitation = 'musica'
        return excitation

    #==================== Condicionando sinais de saída =========================    
    def GetKind(self):
        if self.var11.get():
            Kind = 'calibration'
        if self.var12.get():
            Kind = 'noisefloor'
        if self.var13.get():
            Kind = 'newpoint'
        return Kind
    
    #========= Condicionando Checkbutton das Fontes =========
    def AtivaDodec1(self):
        if self.var11.get() or self.var12.get():
            self.var5.set(False)
        else:
            if self.var5.get():
                if self.var6.get():
                    self.var6.set(False)
    #                Dodecaedro 2 desligado
                if self.var7.get():
                    self.var7.set(False)
    #                P.A desligado
                
    def AtivaDodec2(self):
        if self.var11.get() or self.var12.get():
            self.var6.set(False)
        else:
            if self.var6.get():
                if self.var5.get():
                    self.var5.set(False)
                if self.var7.get():
                    self.var7.set(False)
                
    def AtivaPA(self):
        if self.var11.get() or self.var12.get():
            self.var7.set(False)
        else:
            if self.var7.get():
                if self.var5.get():
                    self.var5.set(False)
                if self.var6.get():
                    self.var6.set(False)

    #========= Condicionando Checkbutton dos Sinais =========
    def AtivaSweep(self):
        if self.var11.get() or self.var12.get():
            self.var8.set(False)
        else:
            if self.var8.get():
                if self.var9.get():
                    self.var9.set(False)
    #                Ruído de desativada
                if self.var10.get():
                    self.var10.set(False)
    #                Room Response desativada
                
    def AtivaFala(self):
        if self.var11.get() or self.var12.get():
            self.var9.set(False)
        else:
            if self.var9.get():
                if self.var8.get():
                    self.var8.set(False)
    #                Calibração desativada
                if self.var10.get():
                    self.var10.set(False)
    #                Room response desativada
                
    def AtivaMusica(self):
        if self.var11.get() or self.var12.get():
            self.var10.set(False)
        else:
            if self.var10.get():
                if self.var8.get():
                    self.var8.set(False)
                if self.var9.get():
                    self.var9.set(False)
    
    
    #========= Condicionando Checkbutton dos tipos de medição (template) =========
    def AtivaCalibracao(self):
        self.var5.set(False)
        self.var6.set(False)
        self.var7.set(False)
        self.var8.set(False)
        self.var9.set(False)
        self.var10.set(False)
        if self.var11.get():
            if self.var12.get():
                self.var12.set(False)
#                Noise floor de desativada
            if self.var13.get():
                self.var13.set(False)
#                Room response desativada
         
    def AtivaRuidoDeFundo(self):
        self.var5.set(False)
        self.var6.set(False)
        self.var7.set(False)
        self.var8.set(False)
        self.var9.set(False)
        self.var10.set(False)
        if self.var12.get():
            if self.var11.get():
                self.var11.set(False)
            if self.var13.get():
                self.var13.set(False)
    
    def AtivaRoomResponse(self):
        if self.var13.get():
            if self.var11.get():
                self.var11.set(False)
            if self.var12.get():
                self.var12.set(False)
        
 #%% Instanciando janela
root = tk.Tk()
root.geometry("1200x700+0+0")
root.title("Measure Class")
root.configure(background = 'black')
#%% Criando instância do takeWindow
takeWindow(root)
#%% Abrindo janela
root.mainloop()