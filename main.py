from flask import Flask, render_template, request
from random import randint
import os
import sys

app = Flask(
    __name__,
    static_url_path='',
    static_folder='web/static',
    template_folder='web/templates'
)

# Безопасное чтение картинок
try:
    urls = os.listdir('web/static')
    mylist = [x for x in urls if x and not x.startswith('.')]
except FileNotFoundError:
    print("Папка 'web/static' не найдена!")
    mylist = ["no-cat.jpg"]

def randimg():
    if not mylist:
        return "no-cat.jpg"
    return mylist[randint(0, len(mylist) - 1)]

@app.route("/")
def hellopage():
    version = os.getenv('APP_RUNNER_ENV_VAR_01', 'dev')
    return f"""
    <html>
    <center>
    <h1>🐱 hello Cats! 🐱</h1>
    <img src="/static/{randimg()}" style="max-width:50%">
    <br><small>version: {version}</small>
    </center>
    </html>
    """

@app.route("/ping")
def ping():
    return "pong", 200

# Остальные роуты — по желанию
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/help")
def help_page():
    return render_template('help.html')

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host="0.0.0.0", port=port, debug=False)
