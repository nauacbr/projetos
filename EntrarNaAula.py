import pyautogui as gui
import time

gui.moveTo(381, 721)
time.sleep(1.5)
gui.moveTo(378, 656)
gui.click()
time.sleep(3)
gui.hotkey('Ctrl', 't')
gui.moveTo(430, 52)
gui.click()
gui.write('https://meet.google.com/opb-dbvb-uta')
gui.press('enter')
time.sleep(12)
gui.moveTo(499, 545)
gui.click()
time.sleep(0.5)
gui.moveTo(565, 546)
gui.click()
time.sleep(0.5)
gui.moveTo(905, 440)
gui.click()
