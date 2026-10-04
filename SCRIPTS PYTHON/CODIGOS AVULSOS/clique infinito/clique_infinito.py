import pyautogui
import time

try:
    print("Pressione Ctrl+C para parar ou encerre o script.")
    while True:
        pyautogui.click(x,y)  # Clica no pixel (x, y)
        time.sleep(0.1)  # Intervalo de 0,1 segundos entre os cliques (ajuste conforme necessário)
except KeyboardInterrupt:
    print("\nScript encerrado pelo usuário.")
