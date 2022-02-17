from flask import Flask, render_template, make_response, request
#from flask import request
from random import randint
import os
import sys

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')

#urls = '''
#1.jpg
#2.jpg
#3.png
#4.jpg
#'''
#mylist = [x for x in urls.splitlines() if x]

urls = os.listdir('web/static')

mylist = [x for x in urls if x]

def randimg():
    pic_num = randint(1,len(mylist))
    randimg = mylist[pic_num-1]
    print(randimg)
    return randimg

#@app.route('/client')
#def client():
#    ip_addr = request.environ['REMOTE_ADDR']
#    return '<h1> Your IP address is:' + ip_addr



@app.route("/")
def hellopage():
    APP_RUNNER_ENV_VAR_01 = os.getenv('APP_RUNNER_ENV_VAR_01', 'none')
    #ip_addr = request.environ['REMOTE_ADDR']
    html = f"""
<html><br>
<center>
<h1><br>hello Cats!</h1></html>
<img src="{randimg()}" width height="50%" >
<center>
deploy version: {APP_RUNNER_ENV_VAR_01}<br>

</html>
"""
    return html



@app.route("/help")
def helppage():
    return render_template('help.html')


if sys.argv[1:]:
    port = sys.argv[1]
else:
    port = 5000

if __name__ == '__main__':
   app.run(debug=False, host="0.0.0.0", port=port)
