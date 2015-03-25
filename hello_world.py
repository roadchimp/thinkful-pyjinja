from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World!"

@app.route("/hello/<name>")
def template_hello(name):
  return render_template('hello.html', my_name= name)

@app.route("/jedi/<firstname>/<lastname>")
def jedi_name(firstname, lastname):
  return render_template('jedi.html', jedi = lastname[:3] + firstname[:2])  

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)