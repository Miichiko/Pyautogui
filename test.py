import pyautogui


while True:
    try:
        teste = pyautogui.locateOnScreen(
            './teste/pokemon.png', confidence=0.8)
        if (teste != None):
            pyautogui.click(teste, duration=1)
            texto = pyautogui.locateOnScreen(
                './teste/texto.png', confidence=0.8)
            if (texto != None):
                pyautogui.click(texto, duration=1)
            break
        else:
            print("não achei")

    except:
        print('não achei!!!')
