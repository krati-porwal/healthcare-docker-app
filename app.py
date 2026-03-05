from flask import Flask, render_template, request, redirect

app = Flask(__name__)

patients = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=["GET","POST"])
def add_patient():

    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        disease = request.form["disease"]
        doctor = request.form["doctor"]

        patients.append({
            "name": name,
            "age": age,
            "disease": disease,
            "doctor": doctor
        })

        return redirect("/patients")

    return render_template("add_patient.html")

@app.route("/patients")
def patients_list():
    return render_template("patients.html", patients=patients)

if __name__ == "__main__":
    app.run(debug=True)