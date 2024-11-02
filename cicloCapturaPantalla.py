import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab
import os
import time
import threading

# Crear la carpeta donde se guardarán las capturas de pantalla
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

class ScreenCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Captura de Pantalla")
        
        # Variables para el intervalo de captura y el estado del ciclo
        self.capture_interval = tk.IntVar(value=10)
        self.capturing = False

        # Configurar interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y menú desplegable para seleccionar el intervalo
        interval_label = tk.Label(self.root, text="Intervalo de captura (segundos):")
        interval_label.pack(pady=5)

        interval_menu = ttk.Combobox(self.root, textvariable=self.capture_interval, values=[1, 5, 10, 15, 20])
        interval_menu.pack(pady=5)

        # Botones de iniciar y detener captura
        self.start_button = tk.Button(self.root, text="Iniciar Captura", command=self.start_capture)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Detener Captura", command=self.stop_capture, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # Mensaje de estado
        self.status_label = tk.Label(self.root, text="Estado: Inactivo")
        self.status_label.pack(pady=10)

    def start_capture(self):
        if not self.capturing:
            self.capturing = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.config(text="Estado: Capturando")
            
            # Iniciar hilo para la captura de pantalla
            self.capture_thread = threading.Thread(target=self.capture_loop)
            self.capture_thread.start()

    def stop_capture(self):
        self.capturing = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Estado: Inactivo")

    def capture_loop(self):
        while self.capturing:
            # Capturar pantalla y guardar la imagen con una marca de tiempo
            timestamp = int(time.time())
            screenshot = ImageGrab.grab()
            screenshot.save(f"captured_images/capture_{timestamp}.png")
            
            # Esperar el tiempo de intervalo antes de la siguiente captura
            time.sleep(self.capture_interval.get())

        # Actualizar interfaz cuando se detiene la captura
        self.stop_capture()

# Crear la ventana principal y ejecutar la aplicación
root = tk.Tk()
app = ScreenCaptureApp(root)
root.mainloop()
