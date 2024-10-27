# Procesamiento de Imagenes - Screen Capture for Fluid Measurement
Este proyecto captura la pantalla en intervalos de 10 segundos y guarda cada imagen en un directorio. Posteriormente, las imágenes se pueden procesar con OpenCV para medir el porcentaje de espacio utilizado por un fluido en un recipiente horizontal.

## Requisitos
1. **Python 3** - Puedes descargarlo desde [python.org:] (https://www.python.org/downloads/)
2. **Paquetes necesarios** - Ejecuta el siguiente comando en la terminal para instalar las bibliotecas necesarias (Pillow y OpenCV):

   ```
   pip install pillow opencv-python
   ```

## Instrucciones de Descarga 
1. Ve a la sección de "Code" de la página. 
2. Click a "Download ZIP" 
3. Extrae la carpeta dentro del achivo .Zip (que será la carpeta que debes abrir con VSCode).

## Instrucciones de Ejecución
### Opción 1: Usar Visual Studio Code (VSCode)

1. Abre Visual Studio Code.
2. Abre la carpeta del proyecto en VSCode: ve a Archivo > Abrir carpeta... y selecciona la carpeta del proyecto.
3. Abre una terminal dentro de VSCode: selecciona Terminal > Nueva terminal (CTRL + Ñ).
4. Escribe el siguiente comando para ejecutar el script:
    ```
    python nombre_del_archivo.py
    ```
**Nota:** Es necesario tener instaladas las extensiones en VSCode (CTRL + SHIFT + X) de Python.

### Opción 2: Usar la Consola de Windows

1. Navega a la carpeta del proyecto en la consola de Windows usando el comando cd:
   ```
    cd ruta\a\la\carpeta
   ```
2. Ejecuta el script de Python:
   ```
    python "nombre_del_archivo.py"
   ```

¡Listo! El programa capturará la pantalla cada 10 segundos y guardará las imágenes en la carpeta captured_images.

## Detalles del Proyecto
Este programa realiza una captura de pantalla cada 10 segundos y guarda cada imagen en una carpeta llamada captured_images. Las imágenes están en formato PNG y están listas para análisis posterior con OpenCV.

## Notas
Asegúrate de tener permisos de escritura en el directorio donde se guardarán las capturas.
Para detener el script, simplemente cierra la terminal o usa Ctrl + C en la consola para interrumpir el proceso.
