from netmiko import ConnectHandler

# Especificaciones del dispositivo router
device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.91",  # IP de nuestra maquina router
    "username": "cisco",
    "password": "cisco123!",
}

# Comandos a ejecutar en el dispositivo router
commands = [
    "show ip interface brief",  # revisamos las interfaces de nuestro router 
    "show running-config",  # revisamos la configuración que se encuentra dentro de nuestro router 
    "show version",  # mostramos la versión del IOS del router en cuestion
]

# Conexión al router 
with ConnectHandler(**device) as net_connect:
    print(f"Conexión exitosa al router CSR1000v {device['ip']}\n")
    
    # Ejecución de los comandos y obtención de los resultados
    for command in commands:
        output = net_connect.send_command_timing(command)
        print(f"Resultado del comando '{command}':")
        print(output)
        print("-" * 50)

print("final del script")
