from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/hello") 
def hello_world():
    return "Hello World!"

@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def type1(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def type2(value):
    print(value + 1)
    return "correct"

@app.route("/path/<path:value>")
def type3(value):
    print(value)
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name)
    else:
        return "Not Found", 404 

if __name__ == "__main__":
    app.run(debug=True) 
