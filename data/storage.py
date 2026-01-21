class Storage:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}
        self.bills = {}
    
    def add_patient(self, patient):
        if patient.patient_id in self.patients:
            raise ValueError("Patient ID already exists.")
        self.patients[patient.patient_id] = patient

    def get_patient(self,patient_id):
        return self.patients.get(patient_id)
    
    def add_doctor(self, doctor):
        if doctor.doctor_id in self.doctors:
            raise ValueError("Doctor ID already exists.")
        self.doctors[doctor.doctor_id] = doctor

    def get_doctor(self, doctor_id):
        return self.doctors.get(doctor_id)
    

    def add_appointment(self, appointment):
        if appointment.appointment_id in self.appointments:
            raise ValueError("Appointment ID already exists.")
        self.appointments[appointment.appointment_id] = appointment

    def get_appointment(self, appointment_id):
        return self.appointments.get(appointment_id)

    def add_bill(self, bill):
        if bill.bill_id in self.bills:
            raise ValueError("Bill ID already exists.")
        self.bills[bill.bill_id] = bill
    def get_bill(self, bill_id):
        return self.bills.get(bill_id)