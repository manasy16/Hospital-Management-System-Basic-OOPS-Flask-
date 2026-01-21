class Appointment:
    def __init__(self,appointment_id,patient,doctor,date,time):
        self.appointment_id=appointment_id
        self.patient  = patient
        self.doctor =doctor #here patient and doctor are object
        self.date =date
        self.time=time

    def get_details(self):
        return{
            "Appointment ID":self.appointment_id,
            "Patient":self.patient,
            "Doctor":self.doctor,
            "Date":self.date,
            "Time":self.time

        }
    
    def __str__(self):
        return(
            f"Appointment[{self.appointment_id}]"
            f"{self.patient.name}-> Dr. {self.doctor.name}"
            f"on {self.date} at {self.time}"
        )