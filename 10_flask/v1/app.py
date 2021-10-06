# Lonely Devos: Michelle Lo, Rayat Roy, Theodore Fahey
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

#We predict that this file will run identically to v0 as the print statement in v0 was never run.
#Our predictions were correct! Hurray!
