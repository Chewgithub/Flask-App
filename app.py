from flask import Flask, render_template, request

app = Flask(__name__)

class SampleClass:

    def __init__(self,f,s,t,num4):
        self.first=f
        self.second=s
        self.third=t
        self.fourth=num4


@app.route("/", methods=["GET", "POST"])
def render_data_stuctures():
    if request.method=="POST":
        pass
    movies=["John Wick 1","John Wick 2","John Wick 3",]

    cars={"brand":"Tesla",
          "model":"Roadster",
          "year":"2020"}
    moons=SampleClass("one","two","three","four")

    kwargs={
        "movies":movies,
        "car":cars,
        "moons":moons
    }
    return render_template("home.html", **kwargs)
