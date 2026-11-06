Этот проект отображает имя приложения и айпи адресс
APP_NAME это имя приложения
API_KEY это секретный ключ для доступа к API
чтобы устоновить его нужно для начала нужно его склонировать: git clone https://github.com/oldm36532/first-githib.git
потом создаём виртуальное окружение с помощью данных команд:
python -m venv .venv
.venv\Scripts\Activate
для windows
python3 -m venv .venv
source .venv/bin/activate
для macOS/Linux
Устанавливаем зависимости: pip install -r requirements.txt
Cкопируйте файл .env.example в новый файл .env:cp .env.example .env
В файле .env можете заполнить значения по своему усмотрению,после этого запускаем код
python main.py
Если всё сработает правильно то должно вывестись
APP name is:"Имя приложения"
API key:True
