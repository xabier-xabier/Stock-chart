import PySimpleGUI as psg
from class_ import Stock, Time


#set the theme for the screen/window
psg.theme('kayak')
#psg.theme('DarkAmber')

#define layout
layout=[[psg.Text('Choose time period for the stock values',size=(40, 1), font='Lucida',justification='left')],
        [psg.Combo(['Daily','Weekly','Monthly'],default_value='Weekly',key='type')],
        [psg.Text('Choose the company whose shares you want to check',size=(40, 2), font='Lucida',justification='left')],
        [psg.Combo(['IBM','Amazon','Tesla', 'Apple','Microsoft','Alphabet','Nvidia','Meta platforms','Berkshire Hathaway','Eli Lilly','Visa',
                    'United Health', 'JP Morgan Chase', 'Walmart', 'Exxon Mobil', 'Broadcom', 'Mastercard','Johnson & Johnson'],default_value="IBM",key='company')],
        [psg.Button('SEARCH', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]

#Define Window
win =psg.Window('Choose the period and company for the stock value',layout)

while True:  # Event Loop
    event, values = win.read()
    if event in (psg.WIN_CLOSED, 'CANCEL'):         # If Cancel or close window, the program will end
        break
        
    else:
        if values['type']=="Daily":
            number_days=240
            code=Stock.check_code(values['company'])
            company_data=Stock.daily(code)
            today=str(Time.current_date())
            new_date=Stock.new_date(today,number_days)
            get_values=Stock.check_date(company_data,new_date)
            ma=Stock.MA_calculus(get_values[1])
            grafico=Stock.plot_graph1(get_values[0],get_values[1],get_values[2],get_values[3],get_values[5],ma,values['company'])
            volume_ma=Stock.MA_calculus(get_values[4])
            grafico1=Stock.plot_volume(grafico,get_values[4],volume_ma,values['company'])
            grafico_total=Stock.plot_all(get_values[0],get_values[1],get_values[2],get_values[3],get_values[5],ma,get_values[4],volume_ma,values['company'])

        elif values['type']=="Weekly":
            number_days=1500
            code=Stock.check_code(values['company'])
            company_data=Stock.weekly(code)
            today=str(Time.current_date())
            new_date=Stock.new_date(today,number_days)
            get_values=Stock.check_date_weekly(company_data,new_date)
            ma=Stock.MA_calculus(get_values[1])
            grafico=Stock.plot_graph1(get_values[0],get_values[1],get_values[2],get_values[3],get_values[5],ma,values['company'])
            volume_ma=Stock.MA_calculus(get_values[4])
            grafico1=Stock.plot_volume(grafico,get_values[4],volume_ma,values['company'])
            grafico_total=Stock.plot_all(get_values[0],get_values[1],get_values[2],get_values[3],get_values[5],ma,get_values[4],volume_ma,values['company'])

        else:
            number_days=6000
            code=Stock.check_code(values['company'])
            company_data=Stock.monthly(code)
            today=str(Time.current_date())
            new_date=Stock.new_date(today,number_days)
            get_values=Stock.check_date_monthly(company_data,new_date)
            ma=Stock.MA_calculus(get_values[1])
            grafico=Stock.plot_graph1(get_values[0],get_values[1],get_values[2],get_values[3],get_values[5],ma,values['company'])
            volume_ma=Stock.MA_calculus(get_values[4])
            grafico1=Stock.plot_volume(grafico,get_values[4],volume_ma,values['company'])
            grafico_total=Stock.plot_all(get_values[0],get_values[1],get_values[2],get_values[3],get_values[5],ma,get_values[4],volume_ma,values['company'])

win.close()


 
   

