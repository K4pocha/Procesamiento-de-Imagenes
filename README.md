# Procesamiento de Imágenes

Este repositorio contiene varios scripts en Python para el procesamiento de imágenes, enfocados en capturar imágenes de pantalla y medir el nivel de un líquido en un recipiente horizontal.

## Contenido

- [Requisitos](#requisitos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso](#uso)
  - [Programa de Captura de Pantalla (screenshots)](#programa-de-captura-de-pantalla)
  - [Programa de Captura y Medición de Nivel (screenshot+medicion de nivel)](#programa-de-captura-y-medicion-de-nivel)
  - [Programa de Detección de Contornos (contornos)](#programa-de-detección-de-contornos)
- [Contribuciones](#contribuciones)

## Requisitos

Para ejecutar estos programas, necesitas instalar los siguientes paquetes de Python:

```
pip install opencv-python numpy pillow
```

## Estructura del Proyecto
- *screenshots.py:* Captura de pantalla en intervalos definidos.
- *screenshot_medicion.py:* Captura de pantalla y cálculo del porcentaje de llenado de un líquido en un recipiente horizontal.
- *contornos.py:* Detección de contornos en imágenes capturadas.

## Uso
### Programa de Captura de Pantalla
Este script captura la pantalla en intervalos de tiempo definidos y guarda las imágenes en una carpeta local para su procesamiento posterior.

1. Ejecuta *screenshots.py:*
```
python screenshots.py
```
2. Configura el intervalo de captura (actualmente configurado predeterminado en 10 segundos).

## Programa de Captura y Medición de Nivel
Este programa captura la pantalla, identifica un recipiente horizontal en la imagen y calcula el porcentaje de llenado.

1. Ejecuta *screenshot_medicion.py:*
```
python screenshot_medicion.py
```

2. Coloca el recipiente en el área de captura de pantalla para obtener mediciones precisas del nivel del líquido.

## Programa de Detección de Contornos
Este script detecta contornos en una imagen. Es útil para resaltar los bordes de objetos en la captura de pantalla.

1. Ejecuta *contornos.py:*
```
python contornos.py
```

## Contribuciones
Este es un proyecto en desarrollo. Las contribuciones son bienvenidas para mejorar los algoritmos de detección y análisis de imágenes. Puedes proponer cambios a través de un Pull Request.

**¡Gracias por usar este repositorio!**