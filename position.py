##Point(x=882, y=472)

import pyautogui
import time


print("Movimente o mouse para obter a posição.")
time.sleep(2)  # Dá tempo para o usuário mover o mouse
print("Posição do cursor:", pyautogui.position())  # Exibe a posição do mouse
