import socket
from datetime import datetime
from pystyle import Colors
from colorama import Fore, init
import os
import platform
from pathlib import Path
from datetime import datetime

from config import ports_dict


Success = Colors.green + "[+]" + Colors.reset
Error = Colors.red + "[-]" + Colors.reset
Info = Colors.blue + "[*]" + Colors.reset


init(autoreset=True)


def get_desktop_path():
    home = Path.home()
    if platform.system() == "Windows":
        return home / "Desktop"
    else:
        pass


def save_results(host, open_ports):
    if platform.system() == "Windows":
        try:
            desktop = get_desktop_path()
            filename = desktop / f"portscan.txt"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"Результаты сканирования {host}\n\n")
                f.write(f"Время начала: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(f"Всего проверено портов: {len(ports_dict)}\n")
                f.write(f"Найдено открытых портов: {len(open_ports)}\n\n")
                if open_ports:
                    f.write("Открытые порты:\n")
                    for port, service in open_ports:
                        f.write(f"{port}/TCP - {service}\n")
                else:
                    f.write("Открытых портов не обнаружено!")
                print(f"\n{Success} Файл 'portscan.txt' сохранен на рабочий стол!")

        except Exception as e:
            print(f"{Error} Ошибка при сохранении файла: {e}")
    
    else:
        try:
            LOG_FILE = os.path.join('logs', 'app.log')
            log_dir = os.path.dirname(LOG_FILE)

            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)
        
            with open(LOG_FILE, 'w', encoding='utf-8') as f:
                f.write(f"Результаты сканирования {host}\n\n")
                f.write(f"Время начала: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(f"Всего проверено портов: {len(ports_dict)}\n")
                f.write(f"Найдено открытых портов: {len(open_ports)}\n\n")
                
                if open_ports:
                    f.write("Открытые порты:\n")
                    for port, service in open_ports:
                        f.write(f"{port}/TCP - {service}\n")
                else:
                    f.write("Открытых портов не обнаружено!")

            print(f"\n{Success} Логи сохранены в файл: {LOG_FILE}")

        except PermissionError:
            print(f"{Error} Ошибка доступа: нет прав для записи в файл {LOG_FILE}")
        except Exception as e:
            print(f"{Error} Ошибка при сохранении логов: {str(e)}")


def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False


def scan_ports(host, ports_dict):
    print(f"\nНачато сканирование хоста: {host}")
    print(f"Время начала: {datetime.now().hour}:{datetime.now().minute}\n")
    
    open_ports = []
    
    for port, service in ports_dict.items():
        if scan_port(host, port):
            open_ports.append((port, service))
            print(f"{Success} Порт {port} ({service}) - открыт" + Colors.reset)
        else:
            print(f"{Error} Порт {port} - закрыт", end="\r")
    
    print("\n\nРезультаты сканирования:")
    print(f" - Всего проверено портов: {len(ports_dict)}")
    print(f"{Success} - Открытых портов: {len(open_ports)}")
    
    if open_ports:
        print("\nСписок открытых портов:")
        for port, service in open_ports:
            print(f"{Success} • {port}/TCP - {service}")
    else:
        print(f"\n{Error} Открытых портов не обнаружено")
    
    print(f"\nВремя завершения: {datetime.now().hour}:{datetime.now().minute}")

    save_results(host, open_ports)
    return open_ports


def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.CYAN + f"""
     ███████████                      █████     █████████                               
    ░░███░░░░░███                    ░░███     ███░░░░░███                              
    ░███    ░███  ██████  ████████  ███████  ░███    ░░░   ██████   ██████   ████████  
    ░██████████  ███░░███░░███░░███░░░███░   ░░█████████  ███░░███ ░░░░░███ ░░███░░███ 
    ░███░░░░░░  ░███ ░███ ░███ ░░░   ░███     ░░░░░░░░███░███ ░░░   ███████  ░███ ░███ 
    ░███        ░███ ░███ ░███       ░███ ███ ███    ░███░███  ███ ███░░███  ░███ ░███ 
    █████       ░░██████  █████      ░░█████ ░░█████████ ░░██████ ░░████████ ████ █████
    ░░░░░         ░░░░░░  ░░░░░        ░░░░░   ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ 
                                                                                    
                            [https://github.com/DenisPythoneer]
                                        {Fore.RED + 'FSOCIETY'}                                                                                   
    """)
    

def host_input():
    display_banner()
    
    host = input(f"\n{Info} Введите IP-адресс или домен: ")
    try:
        if socket.gethostbyname(host):  
            scan_ports(host, ports_dict)
    except socket.gaierror:
        print(f"\n{Error} Ошибка: некорректный IP или домен!" + Colors.reset)


def main():
    host_input()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.green + "\nДо свидания!" + Colors.reset)