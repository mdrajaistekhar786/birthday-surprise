from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# LOGIN PAGE
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "Sona" and password == "Ladoo":
            return redirect(url_for("celebrate"))
        else:
            return render_template("login.html", error="Wrong details 💔")

    return render_template("login.html")


# CELEBRATION PAGE
@app.route("/celebrate")
def celebrate():
    return render_template("celebrate.html")


# MESSAGE PAGE
@app.route("/message")
def message():
    return render_template("message.html")


# IMAGE 1 PAGE  ✅ ONLY ONCE
@app.route("/image1")
def image1():
    return render_template("image1.html")

@app.route("/image2")
def image2():
    return render_template("image2.html")
@app.route("/video1")
def video1():
    return render_template("video1.html")
@app.route("/video2")
def video2():
    return render_template("video2.html")
@app.route("/final")
def final():
    return render_template("final.html")



if __name__ == "__main__":
    app.run(debug=True)
