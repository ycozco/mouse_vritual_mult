import tkinter as tk
from tkinter import ttk
import IaVirtualMouseProject as vmp

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Parámetros")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Cámara
        ttk.Label(self.root, text="Resolución de Cámara").grid(column=0, row=0, padx=10, pady=10)
        
        self.wCam = tk.IntVar(value=vmp.wCam)
        self.hCam = tk.IntVar(value=vmp.hCam)
        ttk.Entry(self.root, textvariable=self.wCam).grid(column=1, row=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.hCam).grid(column=2, row=0, padx=10, pady=10)
        
        # Frame Reduction
        ttk.Label(self.root, text="Reducción del Marco").grid(column=0, row=1, padx=10, pady=10)
        
        self.frameR = tk.IntVar(value=vmp.frameR)
        ttk.Entry(self.root, textvariable=self.frameR).grid(column=1, row=1, padx=10, pady=10)
        
        # Suavizado
        ttk.Label(self.root, text="Suavizado").grid(column=0, row=2, padx=10, pady=10)
        
        self.smoothening = tk.IntVar(value=vmp.smoothening)
        ttk.Entry(self.root, textvariable=self.smoothening).grid(column=1, row=2, padx=10, pady=10)
        
        # Parámetros de HandDetector
        ttk.Label(self.root, text="Parámetros de HandDetector").grid(column=0, row=3, padx=10, pady=10, columnspan=3)
        
        self.maxHands = tk.IntVar(value=vmp.detector.maxHands)
        self.detectionCon = tk.DoubleVar(value=vmp.detector.detectionCon)
        self.trackCon = tk.DoubleVar(value=vmp.detector.trackCon)
        
        ttk.Label(self.root, text="maxHands").grid(column=0, row=4, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.maxHands).grid(column=1, row=4, padx=10, pady=10)
        
        ttk.Label(self.root, text="detectionCon").grid(column=0, row=5, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.detectionCon).grid(column=1, row=5, padx=10, pady=10)
        
        ttk.Label(self.root, text="trackCon").grid(column=0, row=6, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.trackCon).grid(column=1, row=6, padx=10, pady=10)
        
        # Botón para aplicar los cambios
        ttk.Button(self.root, text="Aplicar", command=self.apply_changes).grid(column=0, row=7, padx=10, pady=10, columnspan=3)
    
    def apply_changes(self):
        # Actualizar los parámetros en el módulo
        vmp.wCam = self.wCam.get()
        vmp.hCam = self.hCam.get()
        vmp.frameR = self.frameR.get()
        vmp.smoothening = self.smoothening.get()
        
        vmp.detector.maxHands = self.maxHands.get()
        vmp.detector.detectionCon = self.detectionCon.get()
        vmp.detector.trackCon = self.trackCon.get()
        
        print("Parámetros actualizados")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
