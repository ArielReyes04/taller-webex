import requests
import json
import time
import threading
import os

def obtener_mi_nombre(token):
    """Obtiene el nombre del usuario dueño del token (Basado en authentication.py)."""
    url = 'https://webexapis.com/v1/people/me'
    headers = {'Authorization': f'Bearer {token}'}
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json().get("displayName")
    except Exception:
        return None
    return None

def enviar_mensaje(token, room_id, texto):
    """Envía un mensaje a la sala (Basado en creat-markdown-message.py)."""
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {'roomId': room_id, 'text': texto}
    requests.post(url, headers=headers, json=payload)

def escuchar_mensajes(token, room_id):
    """Consulta la API continuamente en segundo plano para traer mensajes nuevos."""
    url = 'https://webexapis.com/v1/messages'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'roomId': room_id, 'max': 10} # Trae los últimos 10 mensajes
    
    mensajes_vistos = set()
    primera_carga = True

    while True:
        try:
            res = requests.get(url, headers=headers, params=params)
            if res.status_code == 200:
                items = res.json().get("items", [])
                
                # Las APIs de Webex devuelven los mensajes del más nuevo al más viejo,
                # les damos la vuelta para leerlos en orden cronológico.
                items.reverse() 
                
                for msg in items:
                    msg_id = msg.get("id")
                    if msg_id not in mensajes_vistos:
                        mensajes_vistos.add(msg_id)
                        
                        # Si es la primera vez que corre, guarda los viejos silenciosamente
                        if not primera_carga:
                            quien = msg.get("personEmail")
                            texto = msg.get("text")
                            print(f"\n[{quien}]: {texto}")
                            print("Tú: ", end="", flush=True) # Mantiene el prompt de escritura limpio
                
                primera_carga = False
        except Exception as e:
            pass
        
        time.sleep(2) # Espera 2 segundos antes de volver a preguntar a la API

# --- FLUJO PRINCIPAL DE LA APLICACIÓN ---
print("=== BIENVENIDO AL CHAT CONSOLA DE WEBEX ===")
room_id = input("Introduce el room_id de la sala: ").strip()

# Configuración del usuario actual
token_actual = input("Introduce tu Token de Acceso Webex: ").strip()
nombre_usuario = obtener_mi_nombre(token_actual)

if not nombre_usuario:
    print("❌ Token inválido o expirado. No se pudo iniciar sesión.")
    exit()

print(f"\n✅ Sesión iniciada como: {nombre_usuario}")
print("Conectando al canal de mensajes en tiempo real...\n")
print("-" * 50)

# Iniciamos el hilo de segundo plano para recibir mensajes en tiempo real
hilo_recibir = threading.Thread(target=escuchar_mensajes, args=(token_actual, room_id), daemon=True)
hilo_recibir.start()

# Bucle principal en primer plano para ENVIAR mensajes
while True:
    texto_a_enviar = input("Tú: ")
    if texto_a_enviar.lower() == '/salir':
        print("Saliendo de la aplicación...")
        break
    if texto_a_enviar.strip():
        enviar_mensaje(token_actual, room_id, texto_a_enviar)