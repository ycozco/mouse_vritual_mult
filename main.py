import tkinter as tk
from tkinter import ttk, messagebox
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
        messagebox.showinfo("Éxito", "interface.py ha sido ejecutado exitosamente.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error al ejecutar interface.py: {e}")

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

# Usar ThemedTk para aplicar un tema
root = ThemedTk(theme="radiance")
root.title('Configuración de la Aplicación')
root.geometry('600x400')  # Ajustado para acomodar dos columnas

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(expand=True, fill=tk.BOTH)

# Configuración de estilo
style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12), background='#f0f0f0', foreground='black')
style.configure('TButton', font=('Helvetica', 12), background='#4caf50', foreground='white')
style.configure('TEntry', font=('Helvetica', 12), background='white')
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
    ("Ancho de la cámara:", camera_width, '#ff9999'),
    ("Altura de la cámara:", camera_height, '#ffcc99'),
    ("Reducción de marco:", frame_reduction, '#ffff99'),
    ("Sensibilidad del ratón:", mouse_sensitivity, '#ccff99'),
    ("Brillo de la cámara:", camera_brightness, '#99ff99'),
    ("Contraste de la cámara:", camera_contrast, '#99ffcc')
]

# Crear y posicionar etiquetas y entradas en dos columnas
for i, (label, var, color) in enumerate(configurations):
    row = i // 2
    col = (i % 2) * 2
    ttk.Label(main_frame, text=label, background=color).grid(row=row, column=col, sticky='w', pady=5, padx=(0, 10))
    entry = ttk.Entry(main_frame, textvariable=var, width=20)
    entry.grid(row=row, column=col + 1, sticky='ew', pady=5)
    entry.configure(background=color)  # Cambiar el color de fondo de la entrada

# Suavizado con botones
row = len(configurations) // 2
ttk.Label(main_frame, text="Suavizado:", background='#99ccff').grid(row=row, column=0, sticky='w', pady=5)
ttk.Button(main_frame, text="Alto", command=lambda: set_smoothing("Alto"), style='W.TButton').grid(row=row, column=1, sticky='w', padx=(0, 5))
ttk.Button(main_frame, text="Medio", command=lambda: set_smoothing("Medio"), style='W.TButton').grid(row=row, column=2)
ttk.Button(main_frame, text="Bajo", command=lambda: set_smoothing("Bajo"), style='W.TButton').grid(row=row, column=3, sticky='e', padx=(5, 0))

# Botones de acción
ttk.Button(main_frame, text='Iniciar', command=launch_interface, style='W.TButton').grid(row=row + 1, column=0, columnspan=4, pady=10, sticky='ew')
ttk.Button(main_frame, text='Restablecer', command=reset_defaults, style='W.TButton').grid(row=row + 2, column=0, columnspan=4, pady=10, sticky='ew')

# Ajustar configuración de estilo para botones
style.configure('W.TButton', font=('Helvetica', 12), background='#000', foreground='black')
style.map('W.TButton', background=[('active', '#07F720')], foreground=[('active', 'black')])

main_frame.columnconfigure(1, weight=1)
main_frame.columnconfigure(3, weight=1)

root.mainloop()
