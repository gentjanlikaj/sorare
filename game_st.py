from turtle import right
import pyautogui
from time import sleep
import win32clipboard
import json
import pandas as pd
import csv
sleep(5)
def get_links():

    with open('links.csv', newline='') as f:
        reader = csv.reader(f)
        zips = list(reader)
    zips_code =[]   
    for l in zips:
        zips_code.append(l)
    return zips_code

al = get_links()
record_data = []
pyautogui.click(x = 145,  y = 33,  clicks = 1,  interval = 1, button = 'left')
# left tab
try :
    for i in al :
        url = 'https://www.soraredata.com/api/players/stats/78042859911154029513388193307818671269994012057057865007193797215504460478869'
        pyautogui.click(x = 329,  y = 82,  clicks = 1,  interval = 2, button = 'left')
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(url)
        win32clipboard.CloseClipboard()
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        sleep(1.5)
        pyautogui.click(x = 329,  y = 402,  clicks = 1,  interval = 1, button = 'left')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')


        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.EmptyClipboard()
        win32clipboard.CloseClipboard()
        try:
            dd = json.loads(data)
        except:
            dd = ''

        try:
            p_id = dd['player']['PlayerId']
        except:
            p_id =''
        url = 'https://www.soraredata.com/player/'+p_id
        try:    
            name = dd['player']['FullName']
        except:
            name =''
        try:    
            d_name = dd['player']['DisplayName']
        except:
            d_name =''
        try:    
            position = dd['player']['Position']
        except:
            position =''
        try:    
            age = dd['player']['Age']
        except:
            age =''
        try:    
            birth_date = dd['player']['BirthDate']
        except:
            birth_date =''
        try:    
            legue = dd['team']['League']
        except:
            legue =''
        try:    
            l5 = dd['averages']['avg_5']
        except:
            l5 =''
        try:    
            l15 = dd['averages']['avg_15']
        except:
            l15 =''
        try:    
            l40 = dd['averages']['avg_40']
        except:
            l40 =''
        try:    
            limit_cnt  = dd['supply_and_averages'][0]['card_supply']['count']
        except:
            limit_cnt  =''
        try:    
            rare_cnt = dd['supply_and_averages'][1]['card_supply']['count']
        except:
            rare_cnt =''
        try:    
            s_rare_cnt = dd['supply_and_averages'][2]['card_supply']['count']
        except:
            s_rare_cnt =''
        try:    
            unique_cnt = dd['supply_and_averages'][3]['card_supply']['count']
        except:
            unique_cnt =''
        try:    
            avg_limit_3d = dd['valuations']['LIMITED']['Average']
        except:
            avg_limit_3d =''
        try:    
            price_limit_3d = dd['valuations']['LIMITED']['EurAverage']
        except:
            price_limit_3d =''
        try:    
            avg_RARE_7d = dd['valuations']['RARE']['Average']
        except:
            avg_RARE_7d =''
        try:    
            price_RARE_7d = dd['valuations']['RARE']['EurAverage']
        except:
            price_RARE_7d =''
        try:    
            avg_S_RARE_7d = dd['valuations']['SUPER RARE']['Average']
        except:
            avg_S_RARE_7d =''
        try:    
            price_S_RARE_7d = dd['valuations']['SUPER RARE']['EurAverage']
        except:
            price_S_RARE_7d =''
        try:    
            avg_S_RARE_7d = dd['valuations']['COMMON']['Average']
        except:
            avg_S_RARE_7d =''
        try:    
            price_S_RARE_7d = dd['valuations']['COMMON']['EurAverage']
        except:
            price_S_RARE_7d =''
        try:    
            d3_avg_lmt = dd['supply_and_averages'][0]['average'][0]['Average']
        except:
            d3_avg_lmt =''
        try:    
            d7_avg_lmt = dd['supply_and_averages'][0]['average'][1]['Average']
        except:
            d7_avg_lmt =''
        try:    
            d14_avg_lmt = dd['supply_and_averages'][0]['average'][2]['Average']
        except:
            d14_avg_lmt =''
        try:    
            d30_avg_lmt = dd['supply_and_averages'][0]['average'][3]['Average']
        except:
            d30_avg_lmt =''

        try:    
            d3_avg_rare = dd['supply_and_averages'][1]['average'][0]['Average']
        except:
            d3_avg_rare =''
        try:    
            d7_avg_rare = dd['supply_and_averages'][1]['average'][1]['Average']
        except:
            d7_avg_rare =''
        try:    
            d14_avg_rare = dd['supply_and_averages'][1]['average'][2]['Average']
        except:
            d14_avg_rare =''
        try:    
            d30_avg_rare = dd['supply_and_averages'][1]['average'][3]['Average']
        except:
            d30_avg_rare =''

        try:    
            d3_avg_s_rare = dd['supply_and_averages'][2]['average'][0]['Average']
        except:
            d3_avg_s_rare =''
        try:    
            d7_avg_s_rare = dd['supply_and_averages'][2]['average'][1]['Average']
        except:
            d7_avg_s_rare =''
        try:    
            d14_avg_s_rare= dd['supply_and_averages'][2]['average'][2]['Average']
        except:
            d14_avg_s_rare=''
        try:    
            d30_avg_s_rare= dd['supply_and_averages'][2]['average'][3]['Average']
        except:
            d30_avg_s_rare=''

        try:    
            d3_avg_unique  = dd['supply_and_averages'][3]['average'][0]['Average']
        except:
            d3_avg_unique  =''
        try:    
            d7_avg_unique  = dd['supply_and_averages'][3]['average'][1]['Average']
        except:
            d7_avg_unique  =''
        try:    
            d14_avg_unique = dd['supply_and_averages'][3]['average'][2]['Average']
        except:
            d14_avg_unique =''
        try:    
            d30_avg_unique = dd['supply_and_averages'][3]['average'][3]['Average']
        except:
            d30_avg_unique =''

        record_data.append({
            'url' : url
            ,'name' : name
            ,'d_name' : d_name
            ,'position' : position
            ,'age' : age
            ,'birth_date' : birth_date
            ,'legue' : legue
            ,'l5' : l5
            ,'l15' : l15
            ,'l40' : l40
            ,'limit_cnt ' : limit_cnt 
            ,'rare_cnt' : rare_cnt
            ,'s_rare_cnt' : s_rare_cnt
            ,'unique_cnt' : unique_cnt
            ,'avg_limit_3d' : avg_limit_3d
            ,'price_limit_3d' : price_limit_3d
            ,'avg_RARE_7d' : avg_RARE_7d
            ,'price_RARE_7d' : price_RARE_7d
            ,'avg_S_RARE_7d' : avg_S_RARE_7d
            ,'price_S_RARE_7d' : price_S_RARE_7d
            ,'avg_S_RARE_7d' : avg_S_RARE_7d
            ,'price_S_RARE_7d' : price_S_RARE_7d
            ,'d3_avg_lmt' : d3_avg_lmt
            ,'d7_avg_lmt' : d7_avg_lmt
            ,'d14_avg_lmt' : d14_avg_lmt
            ,'d30_avg_lmt' : d30_avg_lmt

            ,'d3_avg_rare' : d3_avg_rare
            ,'d7_avg_rare' : d7_avg_rare
            ,'d14_avg_rare' : d14_avg_rare
            ,'d30_avg_rare' : d30_avg_rare

            ,'d3_avg_s_rare' : d3_avg_s_rare
            ,'d7_avg_s_rare' : d7_avg_s_rare
            ,'d14_avg_s_rar' : d14_avg_s_rare
            ,'d30_avg_s_rar' : d30_avg_s_rare

            ,'d3_avg_unique ' : d3_avg_unique 
            ,'d7_avg_unique ' : d7_avg_unique 
            ,'d14_avg_unique' : d14_avg_unique
            ,'d30_avg_unique' : d30_avg_unique
        })
except:
    pass

df = pd.DataFrame(record_data)
df.to_csv('data_py_game.csv',index=False,sep=';')



# body
# pyautogui.click(x = 501,  y = 441,  clicks = 1,  interval = 2, button = 'left')