import time
import cv2
import numpy as np
from PIL import ImageGrab

def capture_screen(interval=10, save_path="captured_images"):
    # Crear directorio si no existe
    import os
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    # Contador de capturas
    count = 0
    
    while True:
        # Capturar pantalla
        screenshot = ImageGrab.grab()
        # Convertir a formato numpy array
        img_np = np.array(screenshot)
        # Convertir de RGB a BGR para OpenCV
        frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
        
        # Guardar imagen
        image_path = os.path.join(save_path, f"capture_{count}.png")
        cv2.imwrite(image_path, frame)
        print(f"Imagen capturada y guardada en: {image_path}")
        
        # Esperar el intervalo
        time.sleep(interval)
        count += 1

# Ejecutar captura de pantalla
capture_screen(interval=10)
