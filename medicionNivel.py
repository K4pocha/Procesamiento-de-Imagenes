import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab, Image, ImageTk
import os
import time
import threading
import cv2
import numpy as np

# Crear la carpeta donde se guardarán las capturas de pantalla
if not os.path.exists("captured_images"):
    os.makedirs("captured_images")

# Crear el archivo de historial
history_file_path = "historico_niveles.txt"
if not os.path.exists(history_file_path):
    with open(history_file_path, "w") as f:
        f.write("Historial de niveles de líquido:\n")

class ScreenCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Captura de Pantalla y Análisis de Nivel")
        
        # Variables para el intervalo de captura y el estado del ciclo
        self.capture_interval = tk.IntVar(value=10)
        self.capturing = False
        self.history = []

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

        # Etiqueta de estado y nivel actual
        self.status_label = tk.Label(self.root, text="Estado: Inactivo")
        self.status_label.pack(pady=10)

        self.level_label = tk.Label(self.root, text="Nivel Actual: N/A")
        self.level_label.pack(pady=5)

        # Historial de niveles
        self.history_label = tk.Label(self.root, text="Historial de Niveles:")
        self.history_label.pack(pady=5)

        self.history_text = tk.Text(self.root, height=5, width=30)
        self.history_text.pack(pady=5)
        self.history_text.config(state=tk.DISABLED)

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
            screenshot_path = f"captured_images/capture_{timestamp}.png"
            screenshot.save(screenshot_path)
            
            # Procesar la imagen para determinar el nivel de líquido
            level_percentage, level_status = self.process_image(screenshot_path)
            
            # Mostrar el nivel en la interfaz
            self.update_level(level_percentage, level_status)
            
            # Guardar el nivel en el historial
            self.save_to_history(level_percentage, level_status)

            # Esperar el tiempo de intervalo antes de la siguiente captura
            time.sleep(self.capture_interval.get())

        # Actualizar interfaz cuando se detiene la captura
        self.stop_capture()

    def process_image(self, image_path):
        # Leer la imagen
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Aplicar un umbral para separar el líquido del fondo (ajusta el valor según el color del líquido)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        # Detectar contornos para calcular el área ocupada por el líquido
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Obtener el área total del recipiente y el área ocupada por el líquido
            container_area = image.shape[0] * image.shape[1]
            liquid_area = sum(cv2.contourArea(contour) for contour in contours)

            # Calcular el porcentaje de llenado
            level_percentage = (liquid_area / container_area) * 100

            # Determinar el estado del nivel
            if level_percentage < 10:
                level_status = "Vacío"
            elif level_percentage > 90:
                level_status = "Completo"
            else:
                level_status = "Parcialmente Ocupado"

            return level_percentage, level_status
        else:
            # Si no se detectan contornos, se asume que está vacío
            return 0, "Vacío"

    def update_level(self, level_percentage, level_status):
        # Actualizar la etiqueta de nivel actual
        self.level_label.config(text=f"Nivel Actual: {level_status} ({level_percentage:.2f}%)")

    def save_to_history(self, level_percentage, level_status):
        # Guardar en el historial de la ventana
        if len(self.history) >= 5:
            self.history.pop(0)  # Mantener solo los últimos 5 registros
        self.history.append(f"{level_status} ({level_percentage:.2f}%)")

        # Actualizar el texto en la interfaz
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        for entry in self.history:
            self.history_text.insert(tk.END, entry + "\n")
        self.history_text.config(state=tk.DISABLED)

        # Guardar en el archivo de historial
        with open(history_file_path, "a") as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {level_status} ({level_percentage:.2f}%)\n")

# Crear la ventana principal y ejecutar la aplicación
root = tk.Tk()
app = ScreenCaptureApp(root)
root.mainloop()
