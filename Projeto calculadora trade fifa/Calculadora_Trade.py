from webbrowser import BackgroundBrowser
import PySimpleGUI as sg

sg.theme('Dark Grey 13')

btn_layout=[[sg.Button('Calcular', size=(10,0))]
]

calculadora=[
             [sg.Text('Calculadora Trade',font=50,text_color='White')],
             [sg.Text('Valor pago pelo jogador:',size=(19,0)),sg.Input(size=(7,0),key='pago',background_color='White',text_color='Black',do_not_clear= False)],
             [sg.Text('Valor de venda do jogador:',size=(19,0)),sg.Input(size=(7,0),key='venda',background_color='White',text_color='Black',do_not_clear= False)],
             [sg.Text('TAXA EA: 5% ', size=(12,0),text_color='White',background_color='Red')],
             [sg.Column(btn_layout)],
             
                       
]

window = sg.Window('Calculadora Trade', calculadora, icon=(r'C:\CursoPython\Projeto calculadora trade fifa\Icone\588283.ico'))
while True:
    event, values = window.read()
    if event in (None,'Cancelar'):   
        break
    if event in ('Calcular'):
        try:
            Qpago= int(values['pago'])
            Qvenda=int(values['venda'])
            Qtaxa=0.95
            Qcalc=int(Qvenda * Qtaxa)
            Qtotal=(Qcalc - Qpago)
            if (Qvenda > Qpago):
                sg.popup ('Vale apena voce vender o jogador!',
                '+'+ str(Qtotal)+' de coins',font=15,text_color='Black',background_color='green',button_color='Black', 
                icon=(r'C:\CursoPython\Projeto calculadora trade fifa\Icone\588283.ico'))
            else:
                sg.popup ('Voce vai perder com este jogador!!',
                str(Qtotal)+' coins!!',font=15,text_color='Black',background_color='red',button_color='Black',
                icon=(r'C:\CursoPython\Projeto calculadora trade fifa\Icone\588283.ico'))
        except:
                sg.popup ('Preencha todos os campos com numeros',font=15,text_color='Black',background_color='White',button_color='black',
                icon=(r'C:\CursoPython\Projeto calculadora trade fifa\Icone\588283.ico'))
    

window.close()

"""
valor_pago = int(input('valor pago pelo jogador? '))
valor_venda = int(input('Qual valor de venda do jogador? '))
taxa_ea = 0.95
calculo = (valor_venda * taxa_ea)
vale_apena = valor_venda > valor_pago
#n_vale_apena = valor_venda < valor_pago

if vale_apena:
    print('Vale apena voc?? vender o jogador')
else:
    print('Voc?? vai perder coins se vender esse jogador')

"""

 
