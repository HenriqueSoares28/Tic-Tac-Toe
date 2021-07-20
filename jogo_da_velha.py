import random
from tkinter import *
from time import sleep


janela = Tk()
janela2 = Tk()
tentativas = 0

if tentativas == 5:
    janela.destroy()

def botopc():
    while True:
        if tentativas == 5:
            break
        else:
            r = random.randint(1,10)
            if r == 1:
                if bt1['text'] == '':
                    bt1['text'] = 'O'
                    break
                 
            if r == 2:
                if bt2['text'] == '': 
                    bt2['text'] = 'O'
                    break
                
            if r == 3:
                if bt3['text'] == '':
                    bt3['text'] = 'O'
                    break
                
            if r == 4:
                if bt4['text'] == '':
                   
                    bt4['text'] = 'O'
                    break
                
            if r == 5:
                if bt5['text'] == '':
                    bt5['text'] = 'O'
                    break
                
            if r == 6:
                if bt6['text'] == '':
                    bt6['text'] = 'O'
                    break
                
            if r == 7:
                if bt7['text'] == '':
                    bt7['text'] = 'O'
                    break
                
            if r == 8:
                if bt8['text'] == '':
                    bt8['text'] = 'O'
                    break
                
            if r == 9:
                if bt9['text'] == '':
    
                    bt9['text'] = 'O'
                    break
                
    


def opc1(l='X'):
    if bt1['text'] == '':
        bt1['text'] = l
        global tentativas 
        tentativas += 1
        print(tentativas)
        botopc()
    else:
        print('Lugar ja ocupado')
    
def opc2(l='X'):
    if bt2['text'] == '':
        bt2['text'] = l
        global tentativas 
        tentativas += 1
        print(tentativas)
        botopc()
    else:
        print('Lugar ja ocupado')
    
def opc3(l='X'):
    if bt3['text'] == '':
        bt3['text'] = l
        global tentativas 
        tentativas += 1
        print(tentativas)
        botopc()
    else:
        print('Lugar ja ocupado')
    
def opc4(l='X'):
    if bt4['text'] == '':
        bt4['text'] = l
        global tentativas 
        tentativas += 1
        print(tentativas)
        botopc()
    else:
        print('Lugar ja ocupado')
    
def opc5(l='X'):
    if bt5['text'] == '':
        bt5['text'] = l
        global tentativas 
        tentativas += 1
        print(tentativas)
        botopc()
    else:
        print('Lugar ja ocupado')
    
def opc6(l='X'):
    if bt6['text'] == '':
        bt6['text'] = l
        global tentativas 
        tentativas += 1
        print(tentativas)
        botopc()
    else:
        print('Lugar ja ocupado')
    
def opc7(l='X'):
    if bt7['text'] == '':
        bt7['text'] = l
        global tentativas 
        tentativas += 1
        print(tentativas)
        botopc()
    else:
        print('Lugar ja ocupado')
    
def opc8(l='X'):
    if bt8['text'] == '':
        bt8['text'] = l
        global tentativas 
        tentativas += 1
        print(tentativas)
        botopc()
    else:
        print('Lugar ja ocupado')
    
def opc9(l='X'):
    if bt9['text'] == '':
        bt9['text'] = l
        global tentativas 
        tentativas += 1
        print(tentativas)
        botopc()
    else:
        print('Lugar ja ocupado')



        
if tentativas == 5:
    janela.quit()
    
    
janela2.geometry('345x303+100+100')
finalizar = Label(janela2,  width=15, height=6, text='Finalizar')
finalizar.grid(row=0, column=0)


        
    
    

bt1 = Button(janela,  width=15, height=6, text='', command=opc1)
bt2 = Button(janela,  width=15, height=6, text='', command=opc2)
bt3 = Button(janela,  width=15, height=6, text='', command=opc3)
bt4 = Button(janela,  width=15, height=6, text='', command=opc4)
bt5 = Button(janela,  width=15, height=6, text='', command=opc5)
bt6 = Button(janela,  width=15, height=6, text='', command=opc6)
bt7 = Button(janela,  width=15, height=6, text='', command=opc7)
bt8 = Button(janela,  width=15, height=6, text='', command=opc8)
bt9 = Button(janela,  width=15, height=6, text='', command=opc9)
bt10 = Button(janela, width=15, height=6, text='',)

#while tentativas != 5:
bt1.grid(row=0,column=0)
bt2.grid(row=0,column=1)
bt3.grid(row=0,column=2)
bt4.grid(row=1,column=0)
bt5.grid(row=1,column=1)
bt6.grid(row=1,column=2)
bt7.grid(row=2,column=0)
bt8.grid(row=2,column=1)
bt9.grid(row=2,column=2)
#bt10.grid(row=0,column=0)

botoes = (bt1, bt2, bt3, bt4, bt5, bt7, bt7, bt8, bt9)




janela.geometry('345x303+100+100')
janela.mainloop()   



    
    
