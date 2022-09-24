from flask import Flask,request,render_template

app=Flask(__name__)
@app.route("/greet/<name>")
@app.route("/")#decorator itll call the fuction below it there should be no space
def index(name="world"):
    return render_template("index.html",name=name)

@app.route("/about")#called URL Routing
def about():
    return "About us page"# &nbsp for space giving inside</h1>

@app.route("/add")
def add():
    a=request.args.get('a')
    b=request.args.get('b')
    x=int(a)
    y=int(b)
    return f"sum={x+y}"







app.run(debug=True)







