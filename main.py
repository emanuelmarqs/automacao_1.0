#instalar a biblioteca pip install pyautogui

#importar a biblioteca 
import pyautogui as auto
import time

auto.PAUSE = 0.5 #faz abrir depois de 5segundos/OPCIONAL

#abre o menu iniciar
auto.press("win")

#abre o chrome
auto.write("chrome")
auto.press("enter")

#maximizar tela
auto.hotkey("alt", "space")
auto.press("enter")

#abre o github
auto.write("github.com")
auto.press("enter")

# #abre o classroom, em uma nova guia
time.sleep(3) #abre a proxima aba depois de 3 segundos.
auto.hotkey("ctrl","t")
auto.write("classroom.google.com")
auto.press("enter")


#GERAR ARQUIVO EXECUTAVEL EM PYTHON
#instala a biblioteca cx_Freeze
"""cxfreeze main.py --target-dir nome-da-pasta"""


