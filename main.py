from flask import Flask, render_template, request
from random import randint
import os
import sys

# === ИСПРАВЛЕНИЕ 1: url_quote больше НЕ НУЖЕН ===
# Если где-то в будущем понадобится — используй urllib.parse.quote
# from urllib.parse import quote as url_quote

app = Flask(
    __name__,
    static_url_path='',
    static_folder='web/static',
    template_folder='web/templates'
)

# === ИСПРАВЛЕНИЕ 2: Безопасное чтение файлов ===
try:
    urls = os.listdir('web/static')
    mylist = [x for x in urls if x and not x.startswith('.')]  # игнорируем скрытые
except FileNotFoundError:
    print("ОШИБКА: Папка 'web/static' не найдена! Заполни её картинками.")
    mylist = ["placeholder.jpg"]  # fallback

def randimg():
    if not mylist:
        return "static/no-cat.jpg"  # если папка пуста
    pic_num = randint(0, len(mylist) - 1)  # randint(a, b) — включая b
    randimg_path = mylist[pic_num]
    print(f"Случайная картинка: {randimg_path}")
    return randimg_path  # возвращаем только имя файла

@app.route("/")
def hellopage():
    APP_RUNNER_ENV_VAR_01 = os.getenv('APP_RUNNER_ENV_VAR_01', 'local-dev')
    
    html = f"""
    <html>
    <head><title>Cat Generator</title></head>
    <body>
    <center>
    <h1>🐱 hello Cats! 🐱</h1>
    <img src="/static/{randimg()}" style="max-width:50%; height:auto;" alt="Random cat">
    <br><br>
    <small>deploy version: {APP_RUNNER_ENV_VAR_01}</small>
    </center>
    </body>
    </html>
    """
    return html

@app.route("/index")
def helppagef():
    return render_template('index.html')

@app.route("/ping")
def route_ping():
    return "pong", 200

@app.route("/help")
def helppage():
    return render_template('help.html')

# === ИСПРАВЛЕНИЕ 3: Безопасный порт ===
if __name__ == '__main__':
    port = 5000
    if sys.argv[1:]:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Порт должен быть числом. Использую 5000.")
            port = 5000
    
    app.run(host="0.0.0.0", port=port, debug=False)
