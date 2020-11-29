from flask import Flask ,render_template, request
import Image_Recognition
import os
import os, re, os.path
mypath = "C:\\Users\\---folder---\\enrollment\\static\\"
for root, dirs, files in os.walk(mypath):
    for file in files:
        os.remove(os.path.join(root, file))

app = Flask(__name__)

@app.route("/")
@app.route("/index" )
def index():
    return render_template("index.html")

@app.route("/url", methods=["GET","POST"])
def url():
    f=request.files["file"]
    f_path=mypath+f.filename
    f.save(f_path)
    ans=Image_Recognition.solution(f_path)
    return render_template("success.html",name=ans,url=f.filename)

