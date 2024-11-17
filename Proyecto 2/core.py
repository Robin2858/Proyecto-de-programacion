import json
import os

def checkFile(filename):
    return os.path.isfile(filename)

def LoadInfo(filename):
     with open(filename, 'r') as file:
         return json.load(file)

def crearInfo(filename, data):
     with open(filename, 'w') as file:
         json.dump(data, file, indent=4)
         
DATA_FILE = 'usuarios.json'

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False  # El usuario ya existe
    users[username] = {'password': password, 'creditos': 0}
    save_users(users)
    return True

def login_user(username, password):
    users = load_users()
    if username in users and users[username]['password'] == password:
        return True
    return False

def get_user_credits(username):
    users = load_users()
    if username in users:
        return users[username]['creditos']
    return None

def update_user_credits(username, credits):
    users = load_users()
    if username in users:
        users[username]['creditos'] += credits
        save_users(users)
def login():  # Definición de la función login
    global current_user
    while True:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        
        if login_user(username, password):  # Llama a la función login_user directamente
            current_user = username
            print(f"Bienvenido {current_user}!")
            break
        else:
            print("Usuario o contraseña incorrectos. Intente nuevamente.")
