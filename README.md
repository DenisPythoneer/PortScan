### 🐍 Port Scanner - Инструмент для сканирования портов

![Скриншот интерфейса main.py](https://raw.githubusercontent.com/DenisPythoneer/PortScan/main/image/screenshotOne.png)

### 🍀 Лёгкий и мощный инструмент для сканирования портов, который помогает выявлять открытые порты и запущенные сервисы на целевых хостах.

Возможности:

    Быстрое сканирование TCP-портов с настраиваемым таймаутом

    Предустановленные распространённые порты с названиями сервисов (настраивается в config.py)

    Кросс-платформенность - работает на Windows, Linux и macOS

    Сохранение результатов в файл на рабочем столе (Windows) или в папке logs (Linux/macOS)

    Красивый интерфейс с ASCII-баннерами и цветным выводом

### 📦  Установка

Клонируйте репозиторий:

    bash

    git clone https://github.com/DenisPythoneer/PortScan.git
   
    cd port-scanner

Установите зависимости:

    bash

    pip install -r requirements.txt

### 🚀 Использование

Запустите скрипт:

    bash

    python main.py

    Введите IP-адрес или доменное имя для сканирования.

![Пример использования](https://raw.githubusercontent.com/DenisPythoneer/PortScan/main/image/ScreenshotTwo.png)

### ⚙️ Настройка

Вы можете редактировать список портов в файле config.py:
    
    python

    ports_dict = {
        20: "FTP-DATA",
        21: "FTP",
        22: "SSH",
        # ... и другие порты
    }

### 📌 Спасибо за внимание!
