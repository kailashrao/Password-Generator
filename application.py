from flask import Flask, render_template, request
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
        inputs = [ml, u1, l1, n1, s1, e1]

        for i in range(len(inputs)):
            if inputs[i] == "": inputs[i] = 0
            else: inputs[i] = int(inputs[i])

        passgen.generatePasswords(inputs)
    return render_template("passgen.html")

@application.route("/Passwords", methods=["GET", "POST"])
def passgen2():
    if request.method == "POST":
        ml = request.form["ml"]
        u1 = request.form["u1"]
        l1 = request.form["l1"]
        n1 = request.form["n1"]
        s1 = request.form["s1"]
        e1 = request.form["e1"]
        inputs = [ml, u1, l1, n1, s1, e1]

        for i in range(len(inputs)):
            if inputs[i] == "": inputs[i] = 0
            else: inputs[i] = int(inputs[i])

        t = sum(inputs) - inputs[0]
        passgen.generatePasswords(inputs)
    with open("passgen.txt", "r") as file:
        return render_template("passgen.html", result=file.read(), upper=u1, lower=l1, number=n1, special=s1, extra=e1, numpass=ml, total=t)

if __name__ == "__main__":
    application.run(debug=True)