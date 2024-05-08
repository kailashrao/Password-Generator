from flask import Flask, render_template, request
import random
import passgen

application = Flask(__name__)

# Password Generator
@application.route("/", methods=["GET", "POST"])
def passgen1():
    if request.method == "POST":
        ml = request.form["ml"]
        u1 = request.form["u1"]
        l1 = request.form["l1"]
        n1 = request.form["n1"]
        s1 = request.form["s1"]
        e1 = request.form["e1"]
        list1 = [ml, u1, l1, n1, s1, e1]
        if "" in list1:
            return render_template("passgen3.html")
        else:
            passgen.main(ml, u1, l1, n1, s1, e1)
    return render_template("passgen1.html")

@application.route("/Passwords", methods=["GET", "POST"])
def passgen2():
    if request.method == "POST":
        ml = request.form["ml"]
        u1 = request.form["u1"]
        l1 = request.form["l1"]
        n1 = request.form["n1"]
        s1 = request.form["s1"]
        e1 = request.form["e1"]
        list1 = [ml, u1, l1, n1, s1, e1]
        if "" in list1:
            return render_template("passgen3.html")
        else:
            t = int(u1) + int(l1) + int(n1) + int(s1) + int(e1)
            passgen.main(ml, u1, l1, n1, s1, e1)
    with open("passgen.txt", "r") as file:
        return render_template("passgen2.html", result=file.read(), upper=u1, lower=l1, number=n1, special=s1, extra=e1, numpass=ml, total=t)

if __name__ == "__main__":
    application.run(debug=True)