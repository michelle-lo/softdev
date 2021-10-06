# Lonely Devos: Michelle Lo, Rayat Roy, Theodore Fahey
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
    
 #Predictions: We predict that this file will run exactly as version 3 because the If statement is true. Debug mode will also be on.
#Results:
#The if statement makes it so that every time that we reload the page, the print statement runs again. So we think that every time the page detects it being opened it will print to the terminal. 
