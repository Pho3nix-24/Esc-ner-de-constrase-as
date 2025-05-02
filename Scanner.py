import re


# Definir la función para verificar la contraseña
def verificar_passwd(password):
    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"[0-9]", password):
        return False

    if not re.search(r"[\W_]", password):
        return False
    return True


# Leer el archivo de las contraseñas
def verificar_contraseñas(archivo):
    with open(archivo, "r") as f:
        contraseñas = f.readlines()

    for contraseña in contraseñas:
        contraseña = contraseña.strip()
        if verificar_passwd(contraseña):
            print(f"La contraseña '{contraseña}' es segura.")
        else:
            print(f"La contraseña '{contraseña}' no es segura.")

verificar_contraseñas("passwd.txt")
