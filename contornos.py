import cv2
import numpy as np
from tkinter import Tk, filedialog, Button, Label
from PIL import Image, ImageTk

# Función para seleccionar imagen y calcular nivel de llenado
def seleccionar_imagen():
    # Abrir el cuadro de diálogo para seleccionar una imagen
    ruta_imagen = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    
    if ruta_imagen:
        # Cargar y procesar la imagen
        calcular_nivel(ruta_imagen)

def calcular_nivel(image_path):
    # Cargar la imagen
    image = cv2.imread(image_path)
    image = cv2.resize(image, (600, 400))

    # Convertir la imagen a escala de grises y aplicar suavizado
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detectar bordes con Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Crear una máscara para definir la región de interés (ROI)
    height, width = edges.shape
    roi = edges[int(height*0.3):int(height*0.9), :]

    # Detectar contornos en la región de interés
    contours, _ = cv2.findContours(roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calcular el área total de la ROI y el área ocupada por el fluido
    total_area = roi.shape[0] * roi.shape[1]
    fluid_area = sum(cv2.contourArea(contour) for contour in contours)
    fill_percentage = (fluid_area / total_area) * 100

    # Mostrar el porcentaje de llenado en la interfaz
    resultado_label.config(text=f"Porcentaje de llenado estimado: {fill_percentage:.2f}%")

    # Dibujar los contornos y mostrar la imagen en la interfaz
    output = image.copy()
    cv2.drawContours(output[int(height*0.3):int(height*0.9), :], contours, -1, (0, 255, 0), 2)
    mostrar_imagen(output)

def mostrar_imagen(output):
    # Convertir la imagen de OpenCV a un formato compatible con Tkinter
    output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(output_rgb)
    img_tk = ImageTk.PhotoImage(img_pil)

    # Mostrar la imagen en la etiqueta de la interfaz
    imagen_label.config(image=img_tk)
    imagen_label.image = img_tk

# Configuración de la ventana principal de Tkinter
ventana = Tk()
ventana.title("Detección de Nivel de Fluido")
ventana.geometry("800x600")

# Botón para seleccionar imagen
boton_cargar = Button(ventana, text="Cargar Imagen", command=seleccionar_imagen)
boton_cargar.pack(pady=10)

# Etiqueta para mostrar el porcentaje de llenado
resultado_label = Label(ventana, text="Porcentaje de llenado estimado: ")
resultado_label.pack(pady=10)

# Etiqueta para mostrar la imagen procesada
imagen_label = Label(ventana)
imagen_label.pack()

# Iniciar el loop de la interfaz gráfica
ventana.mainloop()
