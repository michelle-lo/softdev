# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

# DEMO
# basics of /static folder

from flask import Flask
import urllib.request, json
app = Flask(__name__)

@app.route("/")
def hello_world():
    x = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=w3dlvp3pigesf9dslufCffVjJUJAoglsX64cF5lK")
    # http = urllib.PoolManager()
    # r = http.request('GET', 'https://api.nasa.gov/planetary/apod?api_key=w3dlvp3pigesf9dslufCffVjJUJAoglsX64cF5lK')
    #print(x.read())
    dict = json.loads(x.read())
    print(dict)
    
    return ""

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
