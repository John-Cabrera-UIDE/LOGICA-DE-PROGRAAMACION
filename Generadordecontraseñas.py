import tkinter as tk
from tkinter import messagebox
import string
import secrets


# -------- FUNCIÓN PARA GENERAR CONTRASEÑAS --------
def generar_passwords():
    resultado_text.delete("1.0", tk.END)

    try:
        longitud = int(entry_longitud.get())
        cantidad = int(entry_cantidad.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa números válidos.")
        return

    usar_simbolos = var_simbolos.get()

    if longitud < 3:
        messagebox.showerror("Error", "La longitud debe ser al menos 3.")
        return

    for _ in range(cantidad):
        password = []

        # --- Caracteres obligatorios ---
        password.append(secrets.choice(string.ascii_uppercase))  # 1 mayúscula
        password.append(secrets.choice(string.digits))           # 1 número

        if usar_simbolos:
            password.append(secrets.choice(string.punctuation))  # 1 símbolo

        # --- Caracteres base ---
        caracteres = string.ascii_letters + string.digits
        if usar_simbolos:
            caracteres += string.punctuation

        # --- Completar el resto ---
        while len(password) < longitud:
            password.append(secrets.choice(caracteres))

        # Mezclar la contraseña para que no siga patrón fijo
        secrets.SystemRandom().shuffle(password)

        # Convertir lista a string
        password_final = ''.join(password)

        resultado_text.insert(tk.END, password_final + "\n")

# -------- INTERFAZ GRÁFICA --------
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x400")

# Longitud
tk.Label(ventana, text="Longitud de la contraseña:").pack()
entry_longitud = tk.Entry(ventana)
entry_longitud.pack()

# Cantidad
tk.Label(ventana, text="Cantidad de contraseñas:").pack()
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack()

# Checkbox símbolos
var_simbolos = tk.BooleanVar()
check_simbolos = tk.Checkbutton(
    ventana,
    text="Incluir símbolos",
    variable=var_simbolos
)
check_simbolos.pack()

# Botón generar
btn_generar = tk.Button(
    ventana,
    text="Generar",
    command=generar_passwords
)
btn_generar.pack(pady=10)

# Área de resultado
resultado_text = tk.Text(ventana, height=10)
resultado_text.pack()

ventana.mainloop()
