import tkinter as tk
from tkinter import filedialog, messagebox
import os
import re

carpeta = ""  # Definimos la variable carpeta a nivel global

def seleccionar_carpeta():
    global carpeta
    carpeta = filedialog.askdirectory()
    actualizar_info_carpeta()

def actualizar_info_carpeta():
    if carpeta:
        archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
        num_archivos = len(archivos)
        extensiones = set(os.path.splitext(f)[1] for f in archivos)
        etiqueta_carpeta.config(text=f"{carpeta}")
        etiqueta_info.config(text=f"Archivos a modificar: {num_archivos}\nExtensiones: {', '.join(extensiones)}")
    else:
        etiqueta_carpeta.config(text="")
        etiqueta_info.config(text="Archivos a modificar: 0\nExtensiones: Ninguna")

def ejecutar_renombrado():
    if not carpeta:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una carpeta.")
        return

    if messagebox.askokcancel("Confirmación", "¿Estás seguro de que quieres renombrar todos los archivos en esta carpeta?"):
        palabras_clave = entrada_texto.get('1.0', 'end-1c').split(';')
        palabras_clave_limpias = []
        for palabra in palabras_clave:
            # Remover caracteres no permitidos y espacios extra
            palabra_limpia = re.sub(r'[<>:"/\\|?*\n\r\t]', '', palabra).strip()
            palabras_clave_limpias.append(palabra_limpia)
        renombrar_archivos(palabras_clave_limpias)
        messagebox.showinfo("Éxito", "Archivos renombrados correctamente.")

def renombrar_archivos(palabras_clave):
    for indice, archivo in enumerate(os.listdir(carpeta)):
        if os.path.isfile(os.path.join(carpeta, archivo)):
            extension = os.path.splitext(archivo)[1]
            nuevo_nombre = "_".join(palabras_clave) + f"_{indice + 1}{extension}"
            os.rename(os.path.join(carpeta, archivo), os.path.join(carpeta, nuevo_nombre))


# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Renombrador de Archivos")
ventana.geometry("400x280")

# Marco para la entrada de palabras clave
marco_palabras = tk.Frame(ventana, pady=10)
marco_palabras.pack(fill="x")
etiqueta_palabras = tk.Label(marco_palabras, text="Palabras Clave (separadas por ';'):")
etiqueta_palabras.pack(anchor="w")
entrada_texto = tk.Text(marco_palabras, height=6)  # 'height' controla el número de líneas
entrada_texto.pack(fill="x", padx=10)

# Marco para seleccionar carpeta y mostrar información
marco_carpeta = tk.Frame(ventana, pady=10)
marco_carpeta.pack(fill="x")
boton_carpeta = tk.Button(marco_carpeta, text="Seleccionar Carpeta", command=seleccionar_carpeta)
boton_carpeta.pack(side="left", padx=10)
etiqueta_carpeta = tk.Label(marco_carpeta, text="", anchor="w")
etiqueta_carpeta.pack(side="left", expand=True)

# Etiqueta de información
etiqueta_info = tk.Label(ventana, text="Archivos a modificar: 0\nExtensiones: Ninguna", pady=10)
etiqueta_info.pack(fill="x")

# Botón para ejecutar el renombrado
boton_ejecutar = tk.Button(ventana, text="Ejecutar", command=ejecutar_renombrado)
boton_ejecutar.pack(fill="x", padx=10, pady=10)  # Ajustado para llenar el espacio horizontal

ventana.mainloop()