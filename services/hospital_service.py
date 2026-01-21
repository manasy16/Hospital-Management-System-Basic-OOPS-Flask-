from models.patient import Patient
from models.appointment import Appointment
from models.doctors import Doctor
from data.mysql_storage import MySQLStorage
from models.billing import Billing
class HospitalServices:
    def __init__(self):
        self.storage= MySQLStorage()


    def add_patient(self,patient_id,name,age,gender,contact,disease):
        
        
        patient = Patient(patient_id,name,age,gender,contact,disease)
        self.storage.add_patient(patient)
        return patient
    
    def add_doctor(self,doctor_id,name,specialization,contact):
        
        
        doctor = Doctor(doctor_id,name,specialization,contact)
        self.storage.add_doctor(doctor)
        return doctor

    def book_appointment(self,appointment_id,patient_id,doctor_id,date,time):
        
        patient = self.storage.get_patient(patient_id)
        if patient is None:
            raise ValueError("Patient does not exist")

    # 2️⃣ Check doctor existence
        doctor = self.storage.get_doctor(doctor_id)
        if doctor is None:
            raise ValueError("Doctor does not exist")

        appointment = Appointment(
            appointment_id,
            self.storage.get_patient(patient_id),
            self.storage.get_doctor(doctor_id),
            date,
            time
        )
        
        self.storage.add_appointment(appointment)
        return appointment
    
    def generate_bill(self, bill_id, appointment_id, consultation_fee, medicine_cost):

        appointment = self.storage.get_appointment(appointment_id)
        if appointment is None:
            raise ValueError("Appointment does not exist")

        bill = Billing(
            bill_id,
            appointment,
            consultation_fee,
            medicine_cost
        )

        self.storage.add_bill(bill)
        return bill