from flask import Flask, render_template
app = Flask(＿_name＿_)

@app.route('/')
def index():
    return render_template("index.html")
  
@app.route('/blog/')
def blog():
    return render_template("blog.html")
  
@app.route('/contacts/')
def contacts():
    return render_template("contacts.html")
  
if ＿name＿ == '＿main＿'
    app.run()