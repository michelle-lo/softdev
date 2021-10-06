# Lonely Devos: Michelle Lo, Rayat Roy, Theodore Fahey
# SoftDev
# Oct 2021


from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()

#Predictions: the print statements will print to the terminal and the website will feature "No hablo queso!". app.debug will switch Debug Mode: on (results of this are still unclear). 
#Results: Same results on the website. However, in the terminal, we are informed that the Debug mode is on and are given a "Debugger PIN". What does this do?

#Preguntas: What is Debugger mode and what is a Debugger Pin?

