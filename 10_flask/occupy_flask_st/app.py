##[Lonely Devos] Michelle Lo, Rayat Roy, Theodore Fahey
##SoftDev
##K10 -- Putting Little Pieces Together/Creating our first webpage
##2021-10-05

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "you can see this, yeah?"
app.run()
