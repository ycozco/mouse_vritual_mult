import cv2
import numpy as np
import HandTrackingModule as htm
import pyautogui
import tkinter as tk
from tkinter import ttk

# Variables globales que se pueden modificar
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7

# Función para iniciar el seguimiento de manos
def start_hand_tracking():
    global wCam, hCam, frameR, smoothening

    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)

    detector = htm.HandDetector(maxHands=1)

    plocX, plocY = 0, 0
    clocX, clocY = 0, 0

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            fingers = [1 if lmList[i][2] < lmList[i-2][2] else 0 for i in [8, 12, 16, 20]]
            
            if fingers[0] == 1 and fingers[1] == 0:  # Solo el dedo índice levantado
                x3 = np.interp(x1, (frameR, wCam-frameR), (0, pyautogui.size().width))
                y3 = np.interp(y1, (frameR, hCam-frameR), (0, pyautogui.size().height))

                clocX = plocX + (x3 - plocX) / smoothening
                clocY = plocY + (y3 - plocY) / smoothening

                pyautogui.moveTo(clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

        cv2.imshow("Image", img)
        cv2.waitKey(1)

# Función para mostrar la ventana de configuración
def show_config_window():
    def apply_changes():
        global wCam, hCam, frameR, smoothening
        wCam = int(wCam_var.get())
        hCam = int(hCam_var.get())
        frameR = int(frameR_var.get())
        smoothening = int(smoothening_var.get())
        root.destroy()
        start_hand_tracking()

    root = tk.Tk()
    root.title("Configuración de Parámetros")

    ttk.Label(root, text="Resolución de Cámara").grid(column=0, row=0, padx=10, pady=10)
    wCam_var = tk.IntVar(value=wCam)
    hCam_var = tk.IntVar(value=hCam)
    ttk.Entry(root, textvariable=wCam_var).grid(column=1, row=0, padx=10, pady=10)
    ttk.Entry(root, textvariable=hCam_var).grid(column=2, row=0, padx=10, pady=10)

    ttk.Label(root, text="Reducción del Marco").grid(column=0, row=1, padx=10, pady=10)
    frameR_var = tk.IntVar(value=frameR)
    ttk.Entry(root, textvariable=frameR_var).grid(column=1, row=1, padx=10, pady=10)

    ttk.Label(root, text="Suavizado").grid(column=0, row=2, padx=10, pady=10)
    smoothening_var = tk.IntVar(value=smoothening)
    ttk.Entry(root, textvariable=smoothening_var).grid(column=1, row=2, padx=10, pady=10)

    ttk.Button(root, text="Aplicar", command=apply_changes).grid(column=0, row=3, padx=10, pady=10, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    show_config_window()
