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

app.run()


#Predictions: It would only print No hablo queso.
#Results: Our predictions were correct. Discovery made: the print statements actually go to terminal and do not disappear magically.
