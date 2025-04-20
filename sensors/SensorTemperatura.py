import socket
import time
import random

IP = "127.0.0.1"
PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    temp = round(random.uniform(22.0, 30.0), 2)
    message = f"TEMP:{temp}"
    sock.sendto(message.encode(), (IP, PORT))
    print(f"[Sensor] Enviou: {message}")
    time.sleep(3)
