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
        url = i[0]
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
            game_week = dd[0]['gameweek']
        except:
            game_week=''
        try:
            game_name = dd[0]['home_display_name']+  ' ('+str(dd[0]['game']['HomeGoals']) + ' - '+str(dd[0]['game']['AwayGoals']) +') '+ dd[0]['away_display_name']
        except:
            game_name=''
        try:
            total_s = dd[0]['stats']['SO5Score']
        except:
            total_s=''
        try:
            all_round = dd[0]['stats']['AllAroundScore']
        except:
            all_round =''
        try:
            decisive = dd[0]['stats']['LevelFD']
        except:
            decisive= ''
        try:
            game_week1 = dd[1]['gameweek']
        except:
            game_week1=''
        try:
            game_name1 = dd[1]['home_display_name']+  ' ('+str(dd[1]['game']['HomeGoals']) + ' - '+str(dd[1]['game']['AwayGoals']) +' '+ dd[1]['away_display_name']
        except:
            game_name1=''
        try:
            total_s1 = dd[1]['stats']['SO5Score']
        except:
            total_s1=''
        try:
            all_round1 = dd[1]['stats']['AllAroundScore']
        except:
            all_round1 =''
        try:
            decisive1 = dd[1]['stats']['LevelFD']
        except:
            decisive1= ''


        record_data.append({
            'url' : url
            ,'game_week' : game_week
            ,'game_name' : game_name
            ,'decisive' : decisive
            ,'all_round' : all_round
            ,'total_s' : total_s
            ,'game_week1' : game_week1
            ,'game_name1' : game_name1
            ,'decisive1' : decisive1
            ,'all_round1' : all_round1
            ,'total_s1' : total_s1

        })
except:
    pass

df = pd.DataFrame(record_data)
df.to_csv('data_py_stats.csv',index=False,sep=';')



# body
# pyautogui.click(x = 501,  y = 441,  clicks = 1,  interval = 2, button = 'left')