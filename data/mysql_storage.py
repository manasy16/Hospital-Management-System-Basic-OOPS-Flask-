from data.db_connection import get_connection
from models.patient import Patient
from models.doctors import Doctor
from models.appointment import Appointment
from models.billing import Billing

class MySQLStorage:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
    
    def add_patient(self,patient):
        # check if patient already exists
        self.cursor.execute(
            "SELECT patient_id FROM patients WHERE patient_id=%s",(patient.patient_id,)
       )

        if self.cursor.fetchone():
            raise ValueError("Patient with this ID already exists")
        query = """
        INSERT INTO patients VALUES(%s,%s,%s,%s,%s,%s)
"""

        self.cursor.execute(query,(
            patient.patient_id,
            patient.name,
            patient.age,
            patient.gender,
            patient.contact,
            patient.disease
            ))
        self.conn.commit()

    def get_patient(self,patient_id):
        self.cursor.execute(
            "SELECT * FROM patients WHERE patient_id=%s",(patient_id,)
        )
        row = self.cursor.fetchone()
        if row:
            return Patient(*row)
        return None
    
    def add_doctor(self,doctor):
        self.cursor.execute(
            "INSERT INTO doctors VALUES(%s,%s,%s,%s)",
            (doctor.doctor_id,doctor.name,doctor.specialization,doctor.contact))
        
        self.conn.commit()


    def get_doctor(self,doctor_id):
        self.cursor.execute(
            "SELECT * FROM doctors WHERE doctor_id =%s",(doctor_id,)
        )
        row = self.cursor.fetchone()
        if row:
            return Doctor(*row)
        return None
    

    def add_appointment(self,appointment):
        self.cursor.execute(
            "INSERT INTO appointments VALUES (%s,%s,%s,%s,%s)",
            (
                appointment.appointment_id,
                appointment.patient.patient_id,
                appointment.doctor.doctor_id,
                appointment.date,
                appointment.time
            )

        )
        self.conn.commit()
    
    def get_appointment(self,appointment_id):
        self.cursor.execute(
            "SELECT * FROM appointments WHERE appointment_id = %s",(appointment_id,)
        )
        row = self.cursor.fetchone()
        if row:
            _,pid,did,date,time=row
            patient=self.get_patient(pid)
            doctor = self.get_doctor(did)
            return Appointment(appointment_id,patient,doctor,date,time)
        return None

    def add_bill(self,bill):
        self.cursor.execute(
            "INSERT INTO bills VALUES(%s,%s,%s)",
            (bill.bill_id,bill.appointment.appointment_id,bill.total_amount)
        )
        self.conn.commit()

    
        