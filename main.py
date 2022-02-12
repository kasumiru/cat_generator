from flask import Flask, render_template, make_response
from random import randint
import os

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

@app.route("/")
def hellopage():
    html = f"""
<html><br>
<center>
<h1><br>hello Cats!</h1></html>
<img src="{randimg()}" width height="50%" >
</html>
"""
    return html



@app.route("/help")
def helppage():
    return render_template('help.html')


if __name__ == '__main__':
   app.run(debug=False)
