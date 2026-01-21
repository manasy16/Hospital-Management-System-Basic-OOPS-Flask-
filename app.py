from flask import Flask, render_template, request
from services.hospital_service import HospitalServices

app = Flask(__name__)
hospital = HospitalServices()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_patient", methods=["POST"])
def add_patient():
    patient = hospital.add_patient(
        int(request.form["patient_id"]),
        request.form["name"],
        int(request.form["age"]),
        request.form["gender"],
        request.form["contact"],
        request.form["disease"]
    )
    return render_template("result.html", message=str(patient))


@app.route("/add_doctor", methods=["POST"])
def add_doctor():
    doctor = hospital.add_doctor(
        int(request.form["doctor_id"]),
        request.form["name"],
        request.form["specialization"],
        request.form["contact"]
    )
    return render_template("result.html", message=str(doctor))


@app.route("/book_appointment", methods=["POST"])
def book_appointment():
    appointment = hospital.book_appointment(
        int(request.form["appointment_id"]),
        int(request.form["patient_id"]),
        int(request.form["doctor_id"]),
        request.form["date"],
        request.form["time"]
    )
    return render_template("result.html", message=str(appointment))


@app.route("/generate_bill", methods=["POST"])
def generate_bill():
    bill = hospital.generate_bill(
        int(request.form["bill_id"]),
        int(request.form["appointment_id"]),
        float(request.form["consultation_fee"]),
        float(request.form["medicine_cost"])
    )
    return render_template("result.html", message=str(bill))


if __name__ == "__main__":
    app.run(debug=True)
