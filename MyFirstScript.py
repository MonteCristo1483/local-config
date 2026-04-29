import datetime  # Библиотека для работы со временем
import socket    # Библиотека для работы с сетью

# 1. Узнаем время
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2. Узнаем IP-адрес
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# 3. Выводим результат
print(f"Текущее время: {current_time}")
print(f"IP-адрес сервера: {ip_address}")