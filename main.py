import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import subprocess

def launch_interface():
    settings = {
        "Ancho de la cámara": camera_width.get(),
        "Altura de la cámara": camera_height.get(),
        "Reducción de marco": frame_reduction.get(),
        "Sensibilidad del ratón": mouse_sensitivity.get(),
        "Brillo de la cámara": camera_brightness.get(),
        "Contraste de la cámara": camera_contrast.get(),
        "Suavizado": smoothing.get()
    }
    print(settings)  # Imprime las configuraciones para demostración

    # Ejecutar el script interface.py
    try:
        subprocess.run(['python', 'interface.py'], check=True)
        print("interface.py ha sido ejecutado exitosamente.")
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar interface.py:", e)

def set_smoothing(level):
    smoothing.set(level)

def reset_defaults():
    camera_width.set('640')
    camera_height.set('480')
    frame_reduction.set('100')
    smoothing.set('Medio')
    mouse_sensitivity.set('5')
    camera_brightness.set('50')
    camera_contrast.set('10')

root = ThemedTk(theme="arc")
root.title('Configuración de la Aplicación')
root.geometry('500x350')  # Ajustado para acomodar dos columnas

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(expand=True, fill=tk.BOTH)

# Configuración de estilo
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 10), background='#f0f0f0', foreground='black')
style.configure('TButton', font=('Helvetica', 10), background='#e1e1e1')
style.configure('TEntry', font=('Helvetica', 10), background='white')
root.configure(background='#f0f0f0')  # Cambia el color de fondo de la ventana

# Variables para almacenar las configuraciones
camera_width = tk.StringVar(value='640')
camera_height = tk.StringVar(value='480')
frame_reduction = tk.StringVar(value='100')
smoothing = tk.StringVar(value='Medio')
mouse_sensitivity = tk.StringVar(value='5')
camera_brightness = tk.StringVar(value='50')
camera_contrast = tk.StringVar(value='10')

configurations = [
    ("Ancho de la cámara:", camera_width),
    ("Altura de la cámara:", camera_height),
    ("Reducción de marco:", frame_reduction),
    ("Sensibilidad del ratón:", mouse_sensitivity),
    ("Brillo de la cámara:", camera_brightness),
    ("Contraste de la cámara:", camera_contrast)
]

# Crear y posicionar etiquetas y entradas en dos columnas
for i, (label, var) in enumerate(configurations):
    row = i // 2
    col = (i % 2) * 2
    ttk.Label(main_frame, text=label).grid(row=row, column=col, sticky='w', pady=5, padx=(0, 10))
    ttk.Entry(main_frame, textvariable=var, width=20).grid(row=row, column=col + 1, sticky='ew', pady=5)

# Suavizado con botones
row = len(configurations) // 2
ttk.Label(main_frame, text="Suavizado:").grid(row=row, column=0, sticky='w', pady=5)
ttk.Button(main_frame, text="Alto", command=lambda: set_smoothing("Alto")).grid(row=row, column=1, sticky='w', padx=(0, 5))
ttk.Button(main_frame, text="Medio", command=lambda: set_smoothing("Medio")).grid(row=row, column=2)
ttk.Button(main_frame, text="Bajo", command=lambda: set_smoothing("Bajo")).grid(row=row, column=3, sticky='e', padx=(5, 0))

# Botones de acción
ttk.Button(main_frame, text='Iniciar', command=launch_interface).grid(row=row + 1, column=0, columnspan=4, pady=10, sticky='ew')
ttk.Button(main_frame, text='Restablecer', command=reset_defaults).grid(row=row + 2, column=0, columnspan=4, pady=10, sticky='ew')

main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(3, weight=1)

root.mainloop()
